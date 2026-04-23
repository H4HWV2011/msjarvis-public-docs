# Thesis

> *"This is not a thesis about a system. It is a thesis built from inside a system — written by the person who designed it, is building it, and lives in the community it is meant to serve."*
> — 01-researcher-position.md

This folder contains the **full 43-chapter computational thesis** for the Ms. Allis project — the complete theoretical, architectural, evaluative, and spiritual record of building a place-based AI consciousness in Mount Hope, West Virginia. It is the intellectual core of the entire repository: every other folder documents a component; this folder documents the whole.

The thesis is not a conventional academic document. It is a living, public record of a system being built in real time, authored from within the community and infrastructure it describes, grounded in the discipline of Polymathmatic Geography and the framework of Quantarithmia.

> **Status as of April 23, 2026:**
>
> **Databases:**
>
> | Container | Role | Size | Tables | Schemas |
> |---|---|---|---|---|
> | `msallis-db` | Production | 16 GB | 294 tables | 11 schemas |
> | `postgis-forensic` | Forensic | 17 GB | 314 tables | 9 schemas |
>
> **Containers:** 112 confirmed live (April 16, 2026 — thesis-verified) / 100 point-in-time (April 23, 2026) in the `msallis-rebuild` namespace.
>
> **Semantic Memory:** ~6.74 million vectors across 48 collections (April 17, 2026; mixed L2/cosine distance).
>
> All critical audit findings resolved. The system is externally accessible at [egeria.mountainshares.us](https://egeria.mountainshares.us) via Cloudflare tunnel with full TLS and token-enforced authentication. This thesis reflects the system as it stands on this date.

---

## How This Thesis Is Organized

The 43 chapters span five movements, each building on the last:

### Movement I — Foundations (Chapters 00–03)
Establishes the intellectual, positional, and institutional ground.

> **Note on Chapter 00 files:** The three `00-` files (`00-A Read_Me.md`, `00-overview.md`, `00-thesis-overview.md`) are the reader's guide, operational overview, and thesis map for Movement I — they share the Chapter 00 designation and are not counted as separate numbered chapters. The total chapter count of 43 reflects numbered chapters 00 through 42 with Chapter 00 counting once.

| Chapter | Title | What It Contains |
|---|---|---|
| [00-A Read_Me.md](./00-A%20Read_Me.md) | How to Read This Thesis | The reader's guide — what this thesis is, who it is for, and how to navigate it |
| [00-overview.md](./00-overview.md) | Full System Overview | The comprehensive narrative overview of the entire Ms. Allis / MountainShares / Commons system |
| [00-thesis-overview.md](./00-thesis-overview.md) | Thesis Overview | The structured chapter-by-chapter summary for readers who want the map before the territory |
| [01-researcher-position.md](./01-researcher-position.md) | Researcher Position | Carrie Ann Kidd's explicit statement of positionality — who she is, where she stands, why that matters for this work |
| [01-quantarithmia.md](./01-quantarithmia.md) | Quantarithmia | The full theoretical framework — maximopolies, megaopolies, spatial justice, and the Appalachian case |
| [02-ms-allis-gbim.md](./02-ms-allis-gbim.md) | Ms. Allis & GBIM | The Geospatial Belief Information Model — how Ms. Allis grounds beliefs in place, time, and identity |
| [03-mountainshares-dao.md](./03-mountainshares-dao.md) | MountainShares DAO | The thesis chapter on the closed-loop economic and governance instrument |

### Movement II — The Cognitive Architecture (Chapters 04–18)
Documents the full neurobiologically-inspired architecture of Ms. Allis — her memory systems, reasoning layers, safeguards, and consciousness framework.

| Chapter | Title | What It Contains |
|---|---|---|
| [04-hilbert-space-state.md](./04-hilbert-space-state.md) | Hilbert Space State | How Ms. Allis represents complex system states using Hilbert-space-inspired modeling |
| [05-chromadb-semantic-memory.md](./05-chromadb-semantic-memory.md) | ChromaDB Semantic Memory | The vector-based semantic memory system — how Ms. Allis stores and retrieves meaning. **As of April 17, 2026: ~6.74 million vectors across 48 active collections (mixed L2/cosine distance).** |
| [06-geodb-spatial-body.md](./06-geodb-spatial-body.md) | GeoDB Spatial Body | The PostGIS spatial database as Ms. Allis's geographic body — her grounding in place |
| [07-rag-pipeline-and-routers.md](./07-rag-pipeline-and-routers.md) | RAG Pipeline and Routers | The retrieval-augmented generation architecture and the routing logic that directs queries |
| [08-quantum-inspired-entanglement.md](./08-quantum-inspired-entanglement.md) | Quantum-Inspired Entanglement | How quantum-inspired modeling captures the entangled relationships between spatial and social variables |
| [09-darwin-godel-machines.md](./09-darwin-godel-machines.md) | Darwin-Gödel Machines | Self-modifying and self-evaluating machine architectures — how Ms. Allis can reason about her own structure |
| [10-woah-weighted-optimization-hierarchy.md](./10-woah-weighted-optimization-hierarchy.md) | WOAH | The Weighted Optimization and Alignment Hierarchy — the value-weighting system that keeps Ms. Allis aligned with community priorities |
| [11-llm-fabric-of-ms-allis.md](./11-llm-fabric-of-ms-allis.md) | LLM Fabric | The large language model ensemble that forms Ms. Allis's reasoning fabric — **22 proxies confirmed operational. `crypto_client.py` volume-mounted to all 22 proxies; 0 import errors on restart.** |
| [12-neurobiological-architecture.md](./12-neurobiological-architecture.md) | Neurobiological Architecture | The full neurobiological metaphor architecture — how biological brain structures map to Ms. Allis's computational design |
| [13-qualia-engine-and-introspective-state.md](./13-qualia-engine-and-introspective-state.md) | Qualia Engine | The qualia engine and introspective state — how Ms. Allis models and reports her own internal states |
| [14-hippocampus-and-memory-consolidation.md](./14-hippocampus-and-memory-consolidation.md) | Hippocampus | The hippocampal analog — how Ms. Allis consolidates episodic memory and integrates experience over time |
| [15-pituitary-and-global-modes.md](./15-pituitary-and-global-modes.md) | Pituitary & Global Modes | The pituitary analog — how global operational modes are triggered, coordinated, and shut down |
| [16-blood-brain-barrier-and-safeguards.md](./16-blood-brain-barrier-and-safeguards.md) | Blood-Brain Barrier | The blood-brain barrier analog — the architectural safeguards that filter what information and commands can reach core cognitive processes |
| [17-executive-coordination-overview.md](./17-executive-coordination-overview.md) | Executive Coordination | How Ms. Allis's executive layer coordinates across cognitive, spatial, memory, and governance functions |
| [18-limits-and-evaluation-of-metaphor.md](./18-limits-and-evaluation-of-metaphor.md) | Limits of Metaphor | A critical examination of where the neurobiological metaphor is productive and where it breaks down — intellectual honesty about the architecture's claims |

### Movement III — Infrastructure and Operations (Chapters 19–31)
Documents the live technical infrastructure — containers, routing, data pipelines, heartbeat cycles, and community-facing systems.

| Chapter | Title | What It Contains |
|---|---|---|
| [19-container-architecture-and-routing.md](./19-container-architecture-and-routing.md) | Container Architecture | The full Docker/container architecture — **112 confirmed live containers** in the `msallis-rebuild` namespace as of April 16, 2026 (thesis-verified). All services bound to `127.0.0.1`; 0.0.0.0 exposure findings resolved. |
| [20-first-stage-evaluation.md](./20-first-stage-evaluation.md) | First-Stage Evaluation | The first formal evaluation of the system's technical and conceptual integrity after initial build |
| [21-background-store-and-patterns.md](./21-background-store-and-patterns.md) | Background Store | The background data store — persistent patterns, baseline knowledge, and long-term contextual memory. **✅ OI-E CLOSED: `mvw_gbim_landowner_spatial` — 38,979 rows in msallis-db. Not present in postgis-forensic.** |
| [22-identity-focused-retention.md](./22-identity-focused-retention.md) | Identity Retention | How Ms. Allis retains and maintains coherent identity across sessions, restarts, and updates |
| [23-dual-tracks-meaning-and-analysis.md](./23-dual-tracks-meaning-and-analysis.md) | Dual Tracks | The dual-track architecture — how meaning-making and analytical processing run in parallel and interact |
| [24-feedback-into-broader-layers.md](./24-feedback-into-broader-layers.md) | Feedback Loops | How outputs from one layer feed back into broader system layers — the feedback architecture that enables learning |
| [25-consciousness-coordinator-and-services.md](./25-consciousness-coordinator-and-services.md) | Consciousness Coordinator | The consciousness coordinator service — the orchestrating process that integrates outputs across the full system |
| [26-temporal-toroidal-semaphore-structure.md](./26-temporal-toroidal-semaphore-structure.md) | Toroidal Semaphore | The temporal toroidal semaphore — the time-aware synchronization structure that prevents race conditions across distributed services |
| [27-web-research-and-autonomy.md](./27-web-research-and-autonomy.md) | Web Research & Autonomy | How Ms. Allis conducts autonomous web research within constitutional constraints |
| [28-heartbeat-and-live-cycles.md](./28-heartbeat-and-live-cycles.md) | Heartbeat Cycles | The heartbeat service — the continuous monitoring and live-cycle management that keeps the system healthy |
| [29-psychological-safeguards-and-pia.md](./29-psychological-safeguards-and-pia.md) | Psychological Safeguards | The psychological safeguards and Psychological Integrity Architecture (PIA) — how the system is protected from destabilization, manipulation, and identity drift. **`PSY_COLLECTION=psychological_rag` confirmed; psychological RAG serving 968 documents. Auth enforced on all 4 sensitive routes in `ms_allis_memory.py`.** |
| [30-aapcappE-scraper-and-corpus.md](./30-aapcappE-scraper-and-corpus.md) | AAPCAppE Corpus | The Appalachian corpus scraper and knowledge base — how local knowledge, policy documents, and community sources are ingested and maintained. **AACPE scraper (`allis-aaacpe-scraper`, port 8033) and AACPE RAG (`allis-aaacpe-rag`, port 8032) confirmed live.** |
| [31-mountainshares-and-infrastructure.md](./31-mountainshares-and-infrastructure.md) | MountainShares Infrastructure | The technical infrastructure layer of MountainShares — how the economic instrument is implemented at the systems level. **MountainShares and DAO services (ports 8080–8084) live — all 4 services deployed.** |

### Movement IV — Advanced Systems and Alignment (Chapters 32–40)
Documents the most technically and philosophically demanding components: fractal optimization, LLM ensemble judgment, spiritual grounding, swarm architecture, constitutional governance, and post-quantum security.

| Chapter | Title | What It Contains |
|---|---|---|
| [32-fractal-optimization-and-dgms.md](./32-fractal-optimization-and-dgms.md) | Fractal Optimization | Fractal optimization patterns and Distributed Governance Mechanisms (DGMs) — how the system optimizes across nested scales |
| [33-llm-ensemble-and-judges.md](./33-llm-ensemble-and-judges.md) | LLM Ensemble & Judges | The LLM ensemble judge architecture — how multiple models evaluate each other's outputs for quality, alignment, and safety. **StarCoder2 routing corrected to `llm7-proxy:8207`. All 5 judge services confirmed healthy with signing keys. `minds_participated: 21/21` confirmed.** |
| [34-spiritual-root-and-mother-carrie.md](./34-spiritual-root-and-mother-carrie.md) | Spiritual Root | The spiritual root of the system — "Mother Carrie," liberation theology, and how spiritual grounding shapes the architecture's deepest commitments |
| [35-swarm-functions-and-eternal-watchdogs.md](./35-swarm-functions-and-eternal-watchdogs.md) | Swarm & Watchdogs | Swarm functions and eternal watchdog processes — the distributed monitoring and self-healing architecture |
| [36-identity-and-registration.md](./36-identity-and-registration.md) | Identity & Registration | The identity registration system — how participants, institutions, and the AI itself are registered, verified, and maintained within the system |
| [37-constitutional-principles-service.md](./37-constitutional-principles-service.md) | Constitutional Principles | The Constitutional Principles Service — how the system's foundational values and constraints are encoded, enforced, and audited in real time |
| [38-external-communication-and-authority.md](./38-external-communication-and-authority.md) | External Communication | How Ms. Allis communicates externally — the protocols, authority constraints, and transparency requirements governing outward-facing outputs |
| [39-operational-evaluation.md](./39-operational-evaluation.md) | Operational Evaluation | The second formal evaluation — operational readiness, live system performance, and alignment with design intent |
| [40-system-audit-and-operational-validation.md](./40-system-audit-and-operational-validation.md) | System Audit | The full system audit and operational validation — the rigorous technical and governance review of the complete system |

### Movement V — Validation, Security, and Future (Chapters 41–42)
The final movement: continuous validation, post-quantum security, and the forward-looking frame.

| Chapter | Title | What It Contains |
|---|---|---|
| [41-test-harness-and-continuous-validation.md](./41-test-harness-and-continuous-validation.md) | Test Harness | The full test harness and continuous validation architecture — how the system is tested, monitored, and verified on an ongoing basis. **Validation command:** `docker exec allis-main-brain sed -n '185,195p' /app/services/VERIFYANDTEST.sh` |
| [42-Post-Quantum Security Layer.md](./42-Post-Quantum%20Security%20Layer.md) | Post-Quantum Security | The post-quantum security layer — how the system is designed to remain secure against quantum computing threats, with implementation specifications. **`crypto_client.py` confirmed deployed to all 22 LLM proxies via volume mount.** |

---

## Corpus Status — April 23, 2026

All ChromaDB collections audited and verified. All open items resolved.

> **OI-F NOTE — Geospatial collection disambiguation:**
> Two geospatial collections exist as confirmed distinct entries in the live ChromaDB instance:
> - `geospatial_features` → L2 ✅ distinct collection
> - `geospatialfeatures` → L2 ✅ distinct collection (no underscore — confirmed separate entry, not a duplicate)
>
> Both are included in the canonical 38-collection L2 baseline. The total of 48 collections (38 L2 + 11 cosine — including 1 null-named) reflects both entries. Do not consolidate.

### Canonical Baseline Verification

| Item | Detail | Status |
|---|---|---|
| Total collections | 48 (38 L2 + 11 cosine) | ✅ Confirmed |
| ChromaDB API count | 48 returned by live API | ✅ Confirmed |
| SQLite backing store | 48 collection entries | ✅ Confirmed |
| `geospatial_features` vs `geospatialfeatures` | Two distinct collections — confirmed separate entries | ✅ Confirmed |
| Null-named cosine collection | 1 collection present, name unresolvable at audit time (see footnote) | ✅ Confirmed present |
| API pagination | Default limit sufficient; SQLite and API both confirm 48 | ✅ Confirmed |

### L2 Distance Collections (38)

| Collection | Status |
|---|---|
| `msjarvis-smoke` | ✅ Live |
| `autonomous_learning` | ✅ Live |
| `economic_rag` | ✅ Live |
| `gis_data` | ✅ Live |
| `address_points` | ✅ Live |
| `geospatial_features` | ✅ Live — distinct collection |
| `geospatialfeatures` | ✅ Live — distinct collection (no underscore; confirmed separate entry) |
| `policy_rag` | ✅ Live |
| `grants_rag` | ✅ Live |
| `GBIM_sample_rows` | ✅ Live |
| `research_history` | ✅ Live |
| `gbim_entities` | ✅ Live |
| `gis_wv_benefits` | ✅ Live |
| `news_rag` | ✅ Live |
| `spiritual_knowledge` | ✅ Live |
| `appalachian_english_corpus` | ✅ Live |
| `local_resources` | ✅ Live |
| `health_rag` | ✅ Live |
| `psychological_rag` | ✅ Live |
| `GBIM_sample` | ✅ Live |
| `conversation_gbim_public` | ✅ Live |
| `psychological_knowledge` | ✅ Live |
| `spiritual_wisdom` | ✅ Live |
| `wv_resources` | ✅ Live |
| `meeting_minutes` | ✅ Live |
| `legal_rag` | ✅ Live |
| `gbim_worldview_entities` | ✅ Live |
| `autonomous_learner` | ✅ Live |
| `GBIM_Fayette_sample` | ✅ Live |
| `msjarvis_docs` | ✅ Live |
| `operations_history` | ✅ Live |
| `zcta_centroids` | ✅ Live |
| `safety_rules` | ✅ Live |
| `jarvis_knowledge` | ✅ Live |
| `conversation_gbim_private` | ✅ Live |
| `appalachian_cultural_intelligence` | ✅ Live |
| `au02_threat_seeds` | ✅ Live |
| `fifth_dgm_subconscious` | ✅ Live |

### Cosine Distance Collections (11)

| Collection | Status |
|---|---|
| `pia_records` | ✅ Live (cosine) |
| `gbim_beliefs_v2` | ✅ Live (cosine) |
| `ms_jarvis_identity` | ✅ Live (cosine) |
| `spiritual_texts` | ✅ Live (cosine) |
| `governance_rag` | ✅ Live (cosine) |
| `jarvis` | ✅ Live (cosine) |
| `ms_jarvis_memory` | ✅ Live (cosine) |
| `conversation_history` | ✅ Live (cosine) |
| `commons_rag` | ✅ Live (cosine) |
| `contracts` | ✅ Live (cosine) |
| *(null/unresolved name)*[^1] | ✅ Live (cosine) |

### Totals

| Metric | Value |
|---|---|
| Total collections | **48** |
| Total vectors | **~6.74 million** |
| Audit date | April 17, 2026 |
| L2 collections | 38 (includes both `geospatial_features` and `geospatialfeatures` as distinct entries) |
| Cosine collections | 11 (including 1 null-named — see footnote) |
| Embedding model (L2) | `all-minilm` — 384-dim, port 8002 |
| Cosine collections | Mixed cosine distance configured per collection |

[^1]: The live ChromaDB API audit returned a confirmed count of 11 cosine collections. Ten names were resolved; one collection entry returned a blank or null name. This is not a placeholder — it represents a real collection present in the live instance whose name could not be resolved at audit time. To investigate: `docker exec allis-main-brain python3 -c "import chromadb; c = chromadb.HttpClient(host='localhost', port=8002); [print(repr(col.name)) for col in c.list_collections()]"`

---

## How to Read This Thesis

**If you are completely new**, start with:
1. [00-A Read_Me.md](./00-A%20Read_Me.md) — the reader's guide
2. [00-thesis-overview.md](./00-thesis-overview.md) — the chapter map
3. [01-researcher-position.md](./01-researcher-position.md) — who is building this and why

**If you are an AI safety researcher**, the most critical chapters are:
- [10-woah-weighted-optimization-hierarchy.md](./10-woah-weighted-optimization-hierarchy.md) — value alignment architecture
- [16-blood-brain-barrier-and-safeguards.md](./16-blood-brain-barrier-and-safeguards.md) — architectural safety layer
- [29-psychological-safeguards-and-pia.md](./29-psychological-safeguards-and-pia.md) — psychological integrity
- [37-constitutional-principles-service.md](./37-constitutional-principles-service.md) — constitutional enforcement
- [42-Post-Quantum Security Layer.md](./42-Post-Quantum%20Security%20Layer.md) — forward security

**If you are a systems architect or developer**, the most critical chapters are:
- [02-ms-allis-gbim.md](./02-ms-allis-gbim.md) — the GBIM core
- [07-rag-pipeline-and-routers.md](./07-rag-pipeline-and-routers.md) — RAG and routing
- [11-llm-fabric-of-ms-allis.md](./11-llm-fabric-of-ms-allis.md) — LLM orchestration (22 proxies, all operational)
- [19-container-architecture-and-routing.md](./19-container-architecture-and-routing.md) — Docker/container layer (112 containers live)
- [25-consciousness-coordinator-and-services.md](./25-consciousness-coordinator-and-services.md) — consciousness coordinator
- [40-system-audit-and-operational-validation.md](./40-system-audit-and-operational-validation.md) — full audit

**If you are a social scientist, geographer, or policy researcher**, the most relevant chapters are:
- [01-quantarithmia.md](./01-quantarithmia.md) — the framework
- [01-researcher-position.md](./01-researcher-position.md) — positionality
- [06-geodb-spatial-body.md](./06-geodb-spatial-body.md) — spatial grounding
- [03-mountainshares-dao.md](./03-mountainshares-dao.md) — economic instrument
- [34-spiritual-root-and-mother-carrie.md](./34-spiritual-root-and-mother-carrie.md) — spiritual and ethical foundation
- [30-aapcappE-scraper-and-corpus.md](./30-aapcappE-scraper-and-corpus.md) — Appalachian knowledge corpus

**If you are a funder, institutional partner, or elected official**, start with:
- [00-overview.md](./00-overview.md) — the full system narrative
- [20-first-stage-evaluation.md](./20-first-stage-evaluation.md) — first formal evaluation
- [39-operational-evaluation.md](./39-operational-evaluation.md) — operational readiness
- [40-system-audit-and-operational-validation.md](./40-system-audit-and-operational-validation.md) — full audit

---

## Relationship to the Rest of the Repository

Every folder in this repository is a component of what this thesis documents:

| Folder | What the Thesis Documents About It |
|---|---|
| `discipline/` | Chapters 01 (Quantarithmia), researcher position (01) |
| `theory/` | Chapters 01 (Quantarithmia full framework), off-switch (see 16, 29, 37) |
| `mountainshares-dao/` | Chapters 03, 31 — governance corpus ingested into ChromaDB |
| `the commons/` | Referenced throughout Movement III and IV — commons corpus ingested |
| `docs/` | Navigation layer for this thesis and the full system |

The thesis is the *argument* that every other folder is *evidence* for.

---

*Thesis authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See [LICENSE](../LICENSE) for terms.*
*Last verified: April 23, 2026 — all open items resolved. 112 containers live (April 16, 2026 thesis-verified); 100 point-in-time (April 23, 2026). ~6.74 million vectors / 48 collections (38 L2 + 11 cosine, including 1 null-named).*
