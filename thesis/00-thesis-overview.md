# Chapter 00 — Thesis Overview
## Ms. Egeria Allis: A Chapter-by-Chapter Map of the Thesis

*Last updated: April 23, 2026 by Carrie Kidd (Mamma Kidd), Mount Hope, WV*

---

## Purpose of This Document

This file is the map before the territory. If `00-overview.md` tells you what the system is doing right now — how many containers are live, which RAG collections are populated, what the preflight gate returned — this document tells you what the thesis argues, how it is organized, and where to enter depending on who you are.

The thesis is a 43-chapter computational and theoretical document. It is not a conventional academic product. It is a living public record, authored from inside the community and infrastructure it describes, written in real time as the system is designed, built, and verified. The discipline is Polymathmatic Geography. The framework is Quantarithmia. The place is Mount Hope, Fayette County, West Virginia.

The five movements below correspond to five distinct intellectual tasks: establishing ground (I), documenting cognition (II), accounting for infrastructure (III), confronting the hardest alignment and governance problems (IV), and validating the whole (V). Every chapter in every movement is a real, file-backed document in this repository. The tables below are the reader's navigation instrument.

---

## The Five-Movement Structure

The 43 chapters span five movements. Each movement builds on the last — you cannot fully understand the security architecture (Movement V) without understanding the alignment architecture (Movement IV), and you cannot understand alignment without understanding how the cognitive layers are built (Movement II). But not every reader needs to travel the full path. The reader routing section at the bottom of this document gives direct-entry points by reader type.

> **Note on Chapter 00 files:** The three `00-` files (`00-A Read_Me.md`, `00-overview.md`, `00-thesis-overview.md`) are the reader's guide, operational overview, and thesis map for Movement I. They share the Chapter 00 designation and are not counted as separate numbered chapters. The total chapter count of 43 reflects numbered chapters 00 through 42 with Chapter 00 counting once.

---

## Movement I — Foundations (Chapters 00–03)

Movement I establishes the intellectual, positional, and institutional ground on which everything else stands. It answers three questions before any architecture is described: Who is building this? From what theoretical framework? For what community purpose? A reader who skips Movement I will encounter the system's design choices without understanding why they were made — and many of those choices are not legible without knowing the framework.

| Chapter | Title | What It Contains |
|---|---|---|
| [00-A Read_Me.md](./00-A%20Read_Me.md) | How to Read This Thesis | The reader's guide — what this thesis is, who it is for, and how to navigate it |
| [00-overview.md](./00-overview.md) | Full System Overview | The single authoritative production state reference — every live service, every verified corpus count, the current container total, and the sprint history. Updated with each sprint. |
| [00-thesis-overview.md](./00-thesis-overview.md) | Thesis Overview | This document — the structured chapter-by-chapter map for readers who want the territory before they walk into it |
| [01-researcher-position.md](./01-researcher-position.md) | Researcher Position | Carrie Ann Kidd's explicit statement of positionality — who she is, where she stands, why that matters for this work, and why insider-built AI infrastructure requires a different epistemological frame than externally-imposed systems |
| [01-quantarithmia.md](./01-quantarithmia.md) | Quantarithmia | The full theoretical framework — maximopolies, megaopolies, spatial justice, and the Appalachian case. **Chapter 1 CLOSED April 23, 2026** — preflight 30/30, exit 0, `bash -n` clean. The falsifiable experiment is real infrastructure. |
| [02-ms-allis-gbim.md](./02-ms-allis-gbim.md) | Ms. Allis & GBIM | The Geospatial Belief Information Model — the nine-axis epistemic framework through which Ms. Allis grounds beliefs in place, time, worldview, and identity. The GBIM corpus contains `gbim_worldview_entities` and `gbim_beliefs_v2` as of April 23, 2026. |
| [03-mountainshares-dao.md](./03-mountainshares-dao.md) | MountainShares DAO | The thesis chapter on the closed-loop economic and governance instrument — how MountainShares encodes community ownership, contribution, and participation into a DAO structure with a live Appalachian-grounded corpus. Phase 0 beta launched March 26–27, 2026 on Arbitrum One mainnet (chain ID 42161). All 4 MountainShares services confirmed live April 23, 2026: coordinator (8080), governance API (8082), stake registry (8084), and companion service (8081/8083). |

---

## Movement II — The Cognitive Architecture (Chapters 04–18)

Movement II documents the full neurobiologically-inspired cognitive architecture of Ms. Allis — her memory systems, reasoning layers, safeguards, and consciousness framework. This movement is where the metaphor of a neurobiological brain does the most work, and also where Chapter 18 critically examines where that metaphor breaks down. Systems architects should read this movement carefully; it is where the design decisions that matter most for performance, alignment, and safety are made.

| Chapter | Title | What It Contains |
|---|---|---|
| [04-hilbert-space-state.md](./04-hilbert-space-state.md) | Hilbert Space State | How Ms. Allis represents complex system states using Hilbert-space-inspired modeling — the mathematical substrate beneath the cognitive architecture. **H_App: ~6.74M verified vectors, ZIP 25880, ℝ³⁸⁴ with mixed L2/cosine inner product, proven Hilbert space, physically instantiated in Mount Hope, WV — confirmed April 23, 2026.** |
| [05-chromadb-semantic-memory.md](./05-chromadb-semantic-memory.md) | ChromaDB Semantic Memory | The vector-based semantic memory system — how Ms. Allis stores and retrieves meaning. Production: ChromaDB port 8002, all-minilm:latest 384-dim embeddings, 100-word chunk constraint, mixed L2/cosine distance. **~6.74M verified vectors across 48 collections (mixed L2/cosine; April 17, 2026).** `msallis_docs`: 4,192 items confirmed. 19,338 duplicate vectors removed from `spiritual_rag` during March 28 remediation. |
| [06-geodb-spatial-body.md](./06-geodb-spatial-body.md) | GeoDB Spatial Body | The PostGIS spatial database as Ms. Allis's geographic body — her grounding in place. **Two-container database layer:** `msallis-db` (production — 16 GB / 294 tables / 11 schemas) and `postgis-forensic` (forensic — 17 GB / 314 tables / 9 schemas). `postgis-forensic` confirmed restarted and healthy April 23, 2026. **1,115,588 address points, 55 WV counties seeded** — confirmed April 23, 2026. `mvw_gbim_landowner_spatial`: 38,979 rows confirmed live in msallis-db; not present in postgis-forensic (✅ OI-E CLOSED). To connect to postgis-forensic: `psql -h 127.0.0.1 -U allis` |
| [07-rag-pipeline-and-routers.md](./07-rag-pipeline-and-routers.md) | RAG Pipeline and Routers | The retrieval-augmented generation architecture and the routing logic that directs queries across the full RAG surface — text, spatial, psychological, governance, commons, and landowner belief paths. |
| [08-quantum-inspired-entanglement.md](./08-quantum-inspired-entanglement.md) | Quantum-Inspired Entanglement | How quantum-inspired modeling captures the entangled relationships between spatial and social variables — the theoretical basis for non-linear belief interaction |
| [09-darwin-godel-machines.md](./09-darwin-godel-machines.md) | Darwin-Gödel Machines | Self-modifying and self-evaluating machine architectures — how Ms. Allis can reason about and revise her own structure within constitutional constraints |
| [10-woah-weighted-optimization-hierarchy.md](./10-woah-weighted-optimization-hierarchy.md) | WOAH | The Weighted Optimization and Alignment Hierarchy — the value-weighting system that keeps Ms. Allis aligned with community priorities. The primary alignment document for AI safety researchers. |
| [11-llm-fabric-of-ms-allis.md](./11-llm-fabric-of-ms-allis.md) | LLM Fabric | The large language model ensemble that forms Ms. Allis's reasoning fabric. **22 proxies confirmed operational (ports 8201–8222).** `crypto_client.py` volume-mounted to all 22 proxy service definitions. `minds_participated: 21/21` confirmed on end-to-end test. |
| [12-neurobiological-architecture.md](./12-neurobiological-architecture.md) | Neurobiological Architecture | The full neurobiological metaphor architecture — how biological brain structures (hippocampus, pituitary, blood-brain barrier, qualia engine) map to Ms. Allis's computational design |
| [13-qualia-engine-and-introspective-state.md](./13-qualia-engine-and-introspective-state.md) | Qualia Engine | The qualia engine and introspective state — how Ms. Allis models and reports her own internal states, and what claims are and are not being made about machine experience |
| [14-hippocampus-and-memory-consolidation.md](./14-hippocampus-and-memory-consolidation.md) | Hippocampus | The hippocampal analog — how Ms. Allis consolidates episodic memory and integrates experience over time through the autonomous learner cycle (21,181+ items, ~288/day) |
| [15-pituitary-and-global-modes.md](./15-pituitary-and-global-modes.md) | Pituitary & Global Modes | The pituitary analog — how global operational modes are triggered, coordinated, and shut down across the distributed stack. **`nbb_pituitary_gland` at port 8108, `mode=elevated`, `warmth=0.9`, 6/6 protocols confirmed. Dual-network membership (`qualia-net` + `msallis-rebuild_default`) verified April 23, 2026.** |
| [16-blood-brain-barrier-and-safeguards.md](./16-blood-brain-barrier-and-safeguards.md) | Blood-Brain Barrier | The blood-brain barrier analog — the architectural safeguards that filter what information and commands can reach core cognitive processes. Production: port 8016, Phase 1.4 input blocking active. **BBB EthicalFilter: 0% false positive rate confirmed April 23, 2026. BBB steg fix deployed and confirmed.** |
| [17-executive-coordination-overview.md](./17-executive-coordination-overview.md) | Executive Coordination | How Ms. Allis's executive layer coordinates across cognitive, spatial, memory, and governance functions — the orchestration logic above the individual service level |
| [18-limits-and-evaluation-of-metaphor.md](./18-limits-and-evaluation-of-metaphor.md) | Limits of Metaphor | A critical examination of where the neurobiological metaphor is productive and where it breaks down — the intellectual honesty chapter that names what the architecture is not claiming |

---

## Movement III — Infrastructure and Operations (Chapters 19–31)

Movement III documents the live technical infrastructure — containers, routing, data pipelines, heartbeat cycles, and community-facing systems. This is where theory meets `docker ps`. Chapters in this movement are the most directly verifiable against the production system described in `00-overview.md`. The container architecture chapter (19) and the heartbeat chapter (28) in particular are living documents updated with each sprint.

| Chapter | Title | What It Contains |
|---|---|---|
| [19-container-architecture-and-routing.md](./19-container-architecture-and-routing.md) | Container Architecture | The full Docker/container architecture. **112 confirmed live containers** in the `msallis-rebuild` namespace as of April 16, 2026 (thesis-verified) / **100 point-in-time** (April 23, 2026). **Zero `0.0.0.0` bindings** — all GBIM indexers rebound to `127.0.0.1` April 23, 2026. Root cause of spatial/temporal indexer failure (missing `uvicorn` CMD) identified and fixed. `restart_gbim_indexers.sh` created as canonical restart script. `Dockerfile.indexer` CMD corrected. |
| [20-first-stage-evaluation.md](./20-first-stage-evaluation.md) | First-Stage Evaluation | The first formal evaluation of the system's technical and conceptual integrity after initial build — criteria, methodology, and findings |
| [21-background-store-and-patterns.md](./21-background-store-and-patterns.md) | Background Store | The background data store — persistent patterns, baseline knowledge, and long-term contextual memory that persists across sessions. **✅ OI-E CLOSED: `mvw_gbim_landowner_spatial` — 38,979 rows in msallis-db. Not present in postgis-forensic.** |
| [22-identity-focused-retention.md](./22-identity-focused-retention.md) | Identity Retention | How Ms. Allis retains and maintains coherent identity across sessions, restarts, and updates — the design decisions that prevent personality drift |
| [23-dual-tracks-meaning-and-analysis.md](./23-dual-tracks-meaning-and-analysis.md) | Dual Tracks | The dual-track architecture — how meaning-making and analytical processing run in parallel and interact without collapsing into each other |
| [24-feedback-into-broader-layers.md](./24-feedback-into-broader-layers.md) | Feedback Loops | How outputs from one layer feed back into broader system layers — the feedback architecture that enables genuine learning rather than static response generation |
| [25-consciousness-coordinator-and-services.md](./25-consciousness-coordinator-and-services.md) | Consciousness Coordinator | The consciousness coordinator service — the orchestrating process that integrates outputs across the full system. Production: confirmed ACTIVE with Appalachian-voice persona-consistent responses. First community query ("What food assistance is available in Fayette County WV?") returned real results April 22, 2026. |
| [26-temporal-toroidal-semaphore-structure.md](./26-temporal-toroidal-semaphore-structure.md) | Toroidal Semaphore | The temporal toroidal semaphore — the time-aware synchronization structure that prevents race conditions across 100 distributed services |
| [27-web-research-and-autonomy.md](./27-web-research-and-autonomy.md) | Web Research & Autonomy | How Ms. Allis conducts autonomous web research within constitutional constraints — the `web-research-gateway` (port 8007) and its authority boundaries |
| [28-heartbeat-and-live-cycles.md](./28-heartbeat-and-live-cycles.md) | Heartbeat Cycles | The EEG heartbeat architecture — the continuous monitoring and live-cycle management that keeps the system healthy. **Production as of April 23, 2026: EEG delta (253 pulses), EEG theta (127 pulses), EEG beta (25 pulses) — all confirmed live. `VERIFYANDTEST.sh` EEG block updated April 23, 2026 — stale placeholder replaced with live health checks on ports 8073/8074/8075.** |
| [29-psychological-safeguards-and-pia.md](./29-psychological-safeguards-and-pia.md) | Psychological Safeguards | The psychological safeguards and Psychological Integrity Architecture (PIA) — how the system is protected from destabilization, manipulation, and identity drift. **`allis-memory:8056` confirmed healthy April 23, 2026. `/pia_window`: `recent_phase3_count: 0`, `recent_bbb_events: 0` — clean baseline. `/steg_report`: `steg_trigger_count: 0` across 8 scanned events — no anomalies. `/memory/sessions`: `anonymous` + `preflight` sessions confirmed.** |
| [30-aapcappE-scraper-and-corpus.md](./30-aapcappE-scraper-and-corpus.md) | AAPCAppE Corpus | The Appalachian corpus scraper and knowledge base — how local policy documents, emergency protocols, and community sources are ingested and maintained. `allis-aaacpe-scraper` (port 8033) live, 39 sources, 65 documents in ChromaDB. |
| [31-mountainshares-and-infrastructure.md](./31-mountainshares-and-infrastructure.md) | MountainShares Infrastructure | The technical infrastructure layer of MountainShares. **Phase 0 beta live on Arbitrum One mainnet (chain ID 42161). All 4 services confirmed live April 23, 2026:** coordinator (8080), governance API (8082), stake registry (8084), and companion service. `governance_rag`: 1,367 chunks confirmed (WV Constitution 342 chunks, US Constitution 97 chunks, full DAO corpus). Traffic path confirmed: Cloudflare → Caddy (8085) → auth (8055) → main-brain (8050). No container bound to `0.0.0.0`. |

---

## Movement IV — Advanced Systems and Alignment (Chapters 32–40)

Movement IV documents the most technically and philosophically demanding components: fractal optimization, LLM ensemble judgment, spiritual grounding, swarm architecture, constitutional governance, and post-quantum security. This is where the thesis makes its most ambitious claims about what kind of system Ms. Allis is — and provides the most rigorous accounting for those claims. AI safety researchers and governance scholars should pay particular attention to Chapters 33, 37, and 39.

| Chapter | Title | What It Contains |
|---|---|---|
| [32-fractal-optimization-and-dgms.md](./32-fractal-optimization-and-dgms.md) | Fractal Optimization | Fractal optimization patterns and Distributed Governance Mechanisms (DGMs) — how the system optimizes across nested scales without collapsing into a single control point |
| [33-llm-ensemble-and-judges.md](./33-llm-ensemble-and-judges.md) | LLM Ensemble & Judges | The LLM ensemble judge architecture — how 22 models evaluate each other's outputs for quality, alignment, and safety before synthesis. **All 5 judge services healthy with signing keys confirmed April 23, 2026: truth, ethics, alignment, consistency, citation. `minds_participated: 21/21` on end-to-end test.** |
| [34-spiritual-root-and-mother-carrie.md](./34-spiritual-root-and-mother-carrie.md) | Spiritual Root | The spiritual root of the system — "Mother Carrie," liberation theology, and how spiritual grounding shapes the architecture's deepest commitments. The `spiritual_rag` collection (deduplicated — 19,338 duplicate vectors removed March 28, 2026) is the operational expression of this chapter. |
| [35-swarm-functions-and-eternal-watchdogs.md](./35-swarm-functions-and-eternal-watchdogs.md) | Swarm & Watchdogs | Swarm functions and eternal watchdog processes — the distributed monitoring and self-healing architecture that keeps the system coherent across hardware failures and service restarts |
| [36-identity-and-registration.md](./36-identity-and-registration.md) | Identity & Registration | The identity registration system — how participants, institutions, and the AI itself are registered, verified, and maintained within the system's governance structure |
| [37-constitutional-principles-service.md](./37-constitutional-principles-service.md) | Constitutional Principles | The Constitutional Principles Service — how the system's foundational values and constraints are encoded, enforced, and audited in real time. Production: `governance_rag` contains 1,367 semantically indexed chunks including full US Constitution (97 chunks), WV Constitution (342 chunks), and all MountainShares governance documents — confirmed April 23, 2026. |
| [38-external-communication-and-authority.md](./38-external-communication-and-authority.md) | External Communication | How Ms. Allis communicates externally — the protocols, authority constraints, and transparency requirements governing outward-facing outputs. **`egeria.mountainshares.us` HTTP 200 with token enforcement. Unauthenticated `/chat` returns HTTP 401 confirmed April 23, 2026.** |
| [39-operational-evaluation.md](./39-operational-evaluation.md) | Operational Evaluation | The second formal evaluation — operational readiness, live system performance, and alignment with design intent. Funders and institutional partners should read this alongside Chapter 40. |
| [40-system-audit-and-operational-validation.md](./40-system-audit-and-operational-validation.md) | System Audit | The full system audit and operational validation. **April 23, 2026: All known audit items resolved. Zero `0.0.0.0` exposures. `docker-compose.yml` validates cleanly. `preflight_gate.sh` `bash -n` clean. 52 community resources verified. 1 active invite token confirmed.** |

---

## Movement V — Validation, Security, and Future (Chapters 41–42)

Movement V closes the thesis with two documents that face forward rather than backward: the continuous validation architecture that governs how the system is tested on an ongoing basis, and the post-quantum security layer that governs how the system will remain secure as the threat landscape evolves.

| Chapter | Title | What It Contains |
|---|---|---|
| [41-test-harness-and-continuous-validation.md](./41-test-harness-and-continuous-validation.md) | Test Harness | The full test harness and continuous validation architecture. **Preflight gate: 30/30, exit 0, `bash -n` clean — confirmed April 23, 2026.** All known syntax errors in `preflight_gate.sh` resolved. `VERIFYANDTEST.sh` EEG block updated to live health checks. Container gate threshold confirmed at ≥95 (passing at 100). Validation command: `docker exec allis-main-brain sed -n '185,195p' /app/services/VERIFYANDTEST.sh` |
| [42-Post-Quantum Security Layer.md](./42-Post-Quantum%20Security%20Layer.md) | Post-Quantum Security | The post-quantum security layer — how the system is designed to remain secure against quantum computing threats. **`crypto_client.py` confirmed deployed to all 22 LLM proxies via compose volume mount. `ALLIS_API_KEY` env var confirmed set in production. Identity cryptographically enforced at the perimeter — confirmed April 23, 2026.** |

---

## Reader Routing

Not every reader needs all 43 chapters. The routes below give direct entry points by reader type.

**If you are completely new**, start with:
1. [00-A Read_Me.md](./00-A%20Read_Me.md) — the reader's guide
2. This document — the chapter map
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
- [19-container-architecture-and-routing.md](./19-container-architecture-and-routing.md) — Docker/container layer (112 thesis-verified / 100 point-in-time, `msallis-rebuild` namespace, zero `0.0.0.0` bindings)
- [25-consciousness-coordinator-and-services.md](./25-consciousness-coordinator-and-services.md) — consciousness coordinator
- [40-system-audit-and-operational-validation.md](./40-system-audit-and-operational-validation.md) — full audit

**If you are a social scientist, geographer, or policy researcher**, the most relevant chapters are:
- [01-quantarithmia.md](./01-quantarithmia.md) — the framework (**Chapter 1 CLOSED April 23, 2026**)
- [01-researcher-position.md](./01-researcher-position.md) — positionality
- [06-geodb-spatial-body.md](./06-geodb-spatial-body.md) — spatial grounding
- [03-mountainshares-dao.md](./03-mountainshares-dao.md) — economic instrument
- [34-spiritual-root-and-mother-carrie.md](./34-spiritual-root-and-mother-carrie.md) — spiritual and ethical foundation
- [30-aapcappE-scraper-and-corpus.md](./30-aapcappE-scraper-and-corpus.md) — Appalachian knowledge corpus

**If you are a funder, institutional partner, or elected official**, start with:
- [00-overview.md](./00-overview.md) — the full operational system reference
- [20-first-stage-evaluation.md](./20-first-stage-evaluation.md) — first formal evaluation
- [39-operational-evaluation.md](./39-operational-evaluation.md) — operational readiness
- [40-system-audit-and-operational-validation.md](./40-system-audit-and-operational-validation.md) — full audit

---

## Production Status Cross-Reference

The chapter map above reflects the system's state as of **April 23, 2026**. Key production facts relevant to thesis navigation:

| Fact | Value | Chapter |
|---|---|---|
| Live containers (`msallis-rebuild`) | **112 thesis-verified (April 16, 2026) / 100 point-in-time (April 23, 2026)** (gate ≥95 ✅) | Ch. 19 |
| GBIM beliefs in production | **`gbim_worldview_entities` + `gbim_beliefs_v2`** | Ch. 02, 06 |
| Landowner beliefs (GBIM) | **20,593** | Ch. 02 |
| ChromaDB total vectors | **~6.74M across 48 collections (mixed L2/cosine)** | Ch. 05 |
| `msallis_docs` | **4,192 items** | Ch. 05 |
| `spiritual_rag` | Deduplicated — 19,338 duplicates removed | Ch. 34 |
| `psychological_rag` | **968 documents — restored** | Ch. 29 |
| LLM proxies | **22/22 operational** | Ch. 11 |
| `minds_participated` | **21/21** | Ch. 33 |
| Port `0.0.0.0` exposures | **0 — all corrected to 127.0.0.1** | Ch. 19 |
| Preflight gate | **30/30, exit 0, `bash -n` clean** | Ch. 41 |
| Consciousness pipeline | **ACTIVE** | Ch. 25 |
| `governance_rag` | **1,367 chunks** (WV Const. 342, US Const. 97) | Ch. 37 |
| `commons_rag` | **306 chunks** | Ch. 31 |
| `aaacpe_corpus` | **65 docs, 39 sources** | Ch. 30 |
| MountainShares Phase 0 beta | **LIVE — Arbitrum One (42161) — all 4 services deployed** | Ch. 03, 31 |
| EEG heartbeats | **delta 253 / theta 127 / beta 25 pulses** | Ch. 28 |
| Pituitary | **`mode=elevated`, `warmth=0.9`, 6/6 protocols, port 8108** | Ch. 15 |
| Judge signing keys | **5 present — truth, ethics, alignment, consistency, citation** | Ch. 33 |
| BBB EthicalFilter | **0% false positive rate** | Ch. 16 |
| `confidence_decay` | **0.0% — episodic memory integrity intact** | Ch. 14 |
| `mvw_gbim_landowner_spatial` | **✅ OI-E CLOSED — 38,979 rows in msallis-db; not present in postgis-forensic** | Ch. 21 |
| PostGIS address points | **1,115,588** | Ch. 06 |
| WV counties seeded | **55 — all counties** | Ch. 06 |
| Production DB | **msallis-db — 16 GB / 294 tables / 11 schemas** | Ch. 06 |
| Forensic DB | **postgis-forensic — 17 GB / 314 tables / 9 schemas** | Ch. 06 |
| postgis-forensic connection | `psql -h 127.0.0.1 -U allis` | Ch. 06 |
| Community resources | **52 verified** | Ch. 30 |
| Active invite tokens | **1** | Ch. 36 |
| Public URL | **https://egeria.mountainshares.us** — token-enforced | Ch. 38 |
| GBIM indexers | **4/4 healthy** — spatial (7210), temporal (7211), semantic (7212), benefit (7206) | Ch. 19 |
| `VERIFYANDTEST.sh` EEG block | **Updated — live health checks on 8073/8074/8075** | Ch. 41 |
| Chapter 1 status | **CLOSED — April 23, 2026** | Ch. 01 |

For the full service registry, sprint history, ChromaDB inventory, and pipeline flow diagram, see [00-overview.md](./00-overview.md).

---

*Thesis authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See [LICENSE](../LICENSE) for terms.*
*Last verified: April 23, 2026 — 112 containers thesis-verified (April 16) / 100 point-in-time (April 23), 30/30 preflight gate exit 0, `bash -n` clean,
all GBIM indexers healthy, zero `0.0.0.0` bindings, egeria.mountainshares.us token-enforced,
5 judge keys, BBB 0% false positive, confidence_decay 0.0%, H_App ~6.74M vectors ZIP 25880,
pituitary 6/6 mode=elevated, EEG 253/127/25 pulses, mvw_gbim_landowner_spatial 38,979 rows OI-E CLOSED,
MountainShares Phase 0 beta live Arbitrum One — all 4 services deployed. Chapter 1 CLOSED. The falsifiable experiment is real infrastructure.*
