# Chapter 00 — Thesis Overview
## Ms. Egeria Jarvis: A Chapter-by-Chapter Map of the Thesis

*Last updated: 2026-03-28 by Carrie Kidd (Mamma Kidd), Mount Hope WV*

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
| [01-quantarithmia.md](./01-quantarithmia.md) | Quantarithmia | The full theoretical framework — maximopolies, megaopolies, spatial justice, and the Appalachian case. This is the lens through which every architectural and governance decision is made. |
| [02-ms-jarvis-gbim.md](./02-ms-jarvis-gbim.md) | Ms. Jarvis & GBIM | The Geospatial Belief Information Model — the nine-axis epistemic framework through which Ms. Jarvis grounds beliefs in place, time, worldview, and identity. The GBIM corpus contains 5,416,521 verified beliefs as of March 28, 2026. |
| [03-mountainshares-dao.md](./03-mountainshares-dao.md) | MountainShares DAO | The thesis chapter on the closed-loop economic and governance instrument — how MountainShares encodes community ownership, contribution, and participation into a DAO structure with a live Appalachian-grounded corpus. Phase 0 beta launched March 26–27, 2026 on Arbitrum One mainnet (chain ID 42161). |

---

## Movement II — The Cognitive Architecture (Chapters 04–18)

Movement II documents the full neurobiologically-inspired cognitive architecture of Ms. Jarvis — her memory systems, reasoning layers, safeguards, and consciousness framework. This movement is where the metaphor of a neurobiological brain does the most work, and also where Chapter 18 critically examines where that metaphor breaks down. Systems architects should read this movement carefully; it is where the design decisions that matter most for performance, alignment, and safety are made.

| Chapter | Title | What It Contains |
|---|---|---|
| [04-hilbert-space-state.md](./04-hilbert-space-state.md) | Hilbert Space State | How Ms. Jarvis represents complex system states using Hilbert-space-inspired modeling — the mathematical substrate beneath the cognitive architecture |
| [05-chromadb-semantic-memory.md](./05-chromadb-semantic-memory.md) | ChromaDB Semantic Memory | The vector-based semantic memory system — how Ms. Jarvis stores and retrieves meaning. Production: ChromaDB port 8002, all-minilm:latest 384-dim embeddings, 100-word chunk constraint, cosine similarity. **6,675,442 verified vectors across 40 active collections as of March 28, 2026. 19,338 duplicate vectors removed from `spiritual_rag` during March 28 remediation. 7 orphaned empty collections confirmed — no active service queries them.** |
| [06-geodb-spatial-body.md](./06-geodb-spatial-body.md) | GeoDB Spatial Body | The PostGIS spatial database as Ms. Jarvis's geographic body — her grounding in place. Production: msjarvisgis (port 5432), 91 GB, 501 tables, 5,416,521 GBIM beliefs. |
| [07-rag-pipeline-and-routers.md](./07-rag-pipeline-and-routers.md) | RAG Pipeline and Routers | The retrieval-augmented generation architecture and the routing logic that directs queries across the full RAG surface — text, spatial, psychological, governance, commons, and landowner belief paths. |
| [08-quantum-inspired-entanglement.md](./08-quantum-inspired-entanglement.md) | Quantum-Inspired Entanglement | How quantum-inspired modeling captures the entangled relationships between spatial and social variables — the theoretical basis for non-linear belief interaction |
| [09-darwin-godel-machines.md](./09-darwin-godel-machines.md) | Darwin-Gödel Machines | Self-modifying and self-evaluating machine architectures — how Ms. Jarvis can reason about and revise her own structure within constitutional constraints |
| [10-woah-weighted-optimization-hierarchy.md](./10-woah-weighted-optimization-hierarchy.md) | WOAH | The Weighted Optimization and Alignment Hierarchy — the value-weighting system that keeps Ms. Jarvis aligned with community priorities. The primary alignment document for AI safety researchers. |
| [11-llm-fabric-of-ms-jarvis.md](./11-llm-fabric-of-ms-jarvis.md) | LLM Fabric | The large language model ensemble that forms Ms. Jarvis's reasoning fabric — **22 proxies confirmed operational (ports 8201–8222) as of March 28, 2026. `crypto_client.py` volume-mounted to all 22 proxy service definitions in `docker-compose.yml`; 0 `ModuleNotFoundError` on restart. StarCoder2 corrected to `llm7-proxy:8207`. `minds_participated: 21/21` confirmed on end-to-end test.** |
| [12-neurobiological-architecture.md](./12-neurobiological-architecture.md) | Neurobiological Architecture | The full neurobiological metaphor architecture — how biological brain structures (hippocampus, pituitary, blood-brain barrier, qualia engine) map to Ms. Jarvis's computational design |
| [13-qualia-engine-and-introspective-state.md](./13-qualia-engine-and-introspective-state.md) | Qualia Engine | The qualia engine and introspective state — how Ms. Jarvis models and reports her own internal states, and what claims are and are not being made about machine experience |
| [14-hippocampus-and-memory-consolidation.md](./14-hippocampus-and-memory-consolidation.md) | Hippocampus | The hippocampal analog — how Ms. Jarvis consolidates episodic memory and integrates experience over time through the autonomous learner cycle (21,181+ items, ~288/day) |
| [15-pituitary-and-global-modes.md](./15-pituitary-and-global-modes.md) | Pituitary & Global Modes | The pituitary analog — how global operational modes are triggered, coordinated, and shut down across the distributed stack |
| [16-blood-brain-barrier-and-safeguards.md](./16-blood-brain-barrier-and-safeguards.md) | Blood-Brain Barrier | The blood-brain barrier analog — the architectural safeguards that filter what information and commands can reach core cognitive processes. Production: port 8016, Phase 1.4 input blocking active, Phase 4.5 output in log+passthrough mode. |
| [17-executive-coordination-overview.md](./17-executive-coordination-overview.md) | Executive Coordination | How Ms. Jarvis's executive layer coordinates across cognitive, spatial, memory, and governance functions — the orchestration logic above the individual service level |
| [18-limits-and-evaluation-of-metaphor.md](./18-limits-and-evaluation-of-metaphor.md) | Limits of Metaphor | A critical examination of where the neurobiological metaphor is productive and where it breaks down — the intellectual honesty chapter that names what the architecture is not claiming |

---

## Movement III — Infrastructure and Operations (Chapters 19–31)

Movement III documents the live technical infrastructure — containers, routing, data pipelines, heartbeat cycles, and community-facing systems. This is where theory meets `docker ps`. Chapters in this movement are the most directly verifiable against the production system described in `00-overview.md`. The container architecture chapter (19) and the heartbeat chapter (28) in particular are living documents updated with each sprint.

| Chapter | Title | What It Contains |
|---|---|---|
| [19-container-architecture-and-routing.md](./19-container-architecture-and-routing.md) | Container Architecture | The full Docker/container architecture — **96 confirmed live containers** in the `msjarvis-rebuild` namespace as of March 28, 2026. All services now bound to `127.0.0.1` — `jarvis-i-containers` (8015) and `jarvis-memory` (8056) corrected from `0.0.0.0` during March 28 remediation. See §00.7 in `00-overview.md` for full service count history. |
| [20-first-stage-evaluation.md](./20-first-stage-evaluation.md) | First-Stage Evaluation | The first formal evaluation of the system's technical and conceptual integrity after initial build — criteria, methodology, and findings |
| [21-background-store-and-patterns.md](./21-background-store-and-patterns.md) | Background Store | The background data store — persistent patterns, baseline knowledge, and long-term contextual memory that persists across sessions. **⚠️ `mvw_gbim_landowner_spatial` materialized view remains at 0 rows — rebuild pending (Item 21, known backlog).** |
| [22-identity-focused-retention.md](./22-identity-focused-retention.md) | Identity Retention | How Ms. Jarvis retains and maintains coherent identity across sessions, restarts, and updates — the design decisions that prevent personality drift |
| [23-dual-tracks-meaning-and-analysis.md](./23-dual-tracks-meaning-and-analysis.md) | Dual Tracks | The dual-track architecture — how meaning-making and analytical processing run in parallel and interact without collapsing into each other |
| [24-feedback-into-broader-layers.md](./24-feedback-into-broader-layers.md) | Feedback Loops | How outputs from one layer feed back into broader system layers — the feedback architecture that enables genuine learning rather than static response generation |
| [25-consciousness-coordinator-and-services.md](./25-consciousness-coordinator-and-services.md) | Consciousness Coordinator | The consciousness coordinator service — the orchestrating process that integrates outputs across the full system. Production: confirmed ACTIVE March 25, 2026 with Appalachian-voice persona-consistent responses. |
| [26-temporal-toroidal-semaphore-structure.md](./26-temporal-toroidal-semaphore-structure.md) | Toroidal Semaphore | The temporal toroidal semaphore — the time-aware synchronization structure that prevents race conditions across 96 distributed services |
| [27-web-research-and-autonomy.md](./27-web-research-and-autonomy.md) | Web Research & Autonomy | How Ms. Jarvis conducts autonomous web research within constitutional constraints — the `web-research-gateway` (port 8007) and its authority boundaries |
| [28-heartbeat-and-live-cycles.md](./28-heartbeat-and-live-cycles.md) | Heartbeat Cycles | The EEG heartbeat architecture — the continuous monitoring and live-cycle management that keeps the system healthy. Production as of March 26, 2026: `eeg-delta` (30s cadence, 1 pulse confirmed), `eeg-theta` (60s cadence, 486 pulses confirmed), `eeg-beta` (5-min cadence, topic: Appalachian, 1 pulse confirmed). |
| [29-psychological-safeguards-and-pia.md](./29-psychological-safeguards-and-pia.md) | Psychological Safeguards | The psychological safeguards and Psychological Integrity Architecture (PIA) — how the system is protected from destabilization, manipulation, and identity drift at the service level. **March 28, 2026: `PSY_COLLECTION=psychological_rag` confirmed; `psychological_rag` restored to 968 documents. `_auth()` present and correctly called on all 4 sensitive routes in `ms_jarvis_memory.py`.** |
| [30-aapcappE-scraper-and-corpus.md](./30-aapcappE-scraper-and-corpus.md) | AAPCAppE Corpus | The Appalachian corpus scraper and knowledge base — how local policy documents, emergency protocols, and community sources are ingested and maintained. **★ Status: Active — March 27, 2026:** `jarvis-aaacpe-scraper` (port 8033) live, 39 sources, `total_runs: 1`, 65 documents in ChromaDB, RAG retrieval verified with emergency protocol and Fayette County utility examples. |
| [31-mountainshares-and-infrastructure.md](./31-mountainshares-and-infrastructure.md) | MountainShares Infrastructure | The technical infrastructure layer of MountainShares — how the economic instrument is implemented at the systems level. **★ Phase 0 beta launched March 26–27, 2026:** all five services (ports 8080–8084) deployed, five smart contracts live on Arbitrum One mainnet (chain ID 42161), `governance_rag` (643 chunks) and `commons_rag` (306 chunks) confirmed as live corpus backing. |

---

## Movement IV — Advanced Systems and Alignment (Chapters 32–40)

Movement IV documents the most technically and philosophically demanding components: fractal optimization, LLM ensemble judgment, spiritual grounding, swarm architecture, constitutional governance, and post-quantum security. This is where the thesis makes its most ambitious claims about what kind of system Ms. Jarvis is — and provides the most rigorous accounting for those claims. AI safety researchers and governance scholars should pay particular attention to Chapters 33, 37, and 39.

| Chapter | Title | What It Contains |
|---|---|---|
| [32-fractal-optimization-and-dgms.md](./32-fractal-optimization-and-dgms.md) | Fractal Optimization | Fractal optimization patterns and Distributed Governance Mechanisms (DGMs) — how the system optimizes across nested scales without collapsing into a single control point |
| [33-llm-ensemble-and-judges.md](./33-llm-ensemble-and-judges.md) | LLM Ensemble & Judges | The LLM ensemble judge architecture — how 22 models evaluate each other's outputs for quality, alignment, and safety before synthesis. **March 28, 2026: StarCoder2 endpoint corrected to `llm7-proxy:8207` in `llm_consensus_20_FINAL.py` line 260. All 5 judge services healthy with signing keys. `minds_participated: 21/21` on end-to-end test. `/chat` confirmed as production endpoint on port 8008.** |
| [34-spiritual-root-and-mother-carrie.md](./34-spiritual-root-and-mother-carrie.md) | Spiritual Root | The spiritual root of the system — "Mother Carrie," liberation theology, and how spiritual grounding shapes the architecture's deepest commitments. The `spiritual_rag` collection (deduplicated — 19,338 duplicate vectors removed March 28, 2026) is the operational expression of this chapter. |
| [35-swarm-functions-and-eternal-watchdogs.md](./35-swarm-functions-and-eternal-watchdogs.md) | Swarm & Watchdogs | Swarm functions and eternal watchdog processes — the distributed monitoring and self-healing architecture that keeps the system coherent across hardware failures and service restarts |
| [36-identity-and-registration.md](./36-identity-and-registration.md) | Identity & Registration | The identity registration system — how participants, institutions, and the AI itself are registered, verified, and maintained within the system's governance structure |
| [37-constitutional-principles-service.md](./37-constitutional-principles-service.md) | Constitutional Principles | The Constitutional Principles Service — how the system's foundational values and constraints are encoded, enforced, and audited in real time. Production: `governance_rag` contains 643 semantically indexed chunks including the full US Constitution (97 chunks, Project Gutenberg) and all MountainShares governance documents. |
| [38-external-communication-and-authority.md](./38-external-communication-and-authority.md) | External Communication | How Ms. Jarvis communicates externally — the protocols, authority constraints, and transparency requirements governing outward-facing outputs through the public URL (https://egeria.mountainshares.us) |
| [39-operational-evaluation.md](./39-operational-evaluation.md) | Operational Evaluation | The second formal evaluation — operational readiness, live system performance, and alignment with design intent. Funders and institutional partners should read this alongside Chapter 40. |
| [40-system-audit-and-operational-validation.md](./40-system-audit-and-operational-validation.md) | System Audit | The full system audit and operational validation — the rigorous technical and governance review of the complete system. **March 28, 2026: All 5 tracked audit items closed — CRIT-CRYPTO, REM-06 (confirmed false positive), REM-09 (full route inventory documented), REM-13, REM-16. `openapi.json` [OPEN] flags noted as misleading for manually-called auth — not FastAPI `Depends()` declarations.** |

---

## Movement V — Validation, Security, and Future (Chapters 41–42)

Movement V closes the thesis with two documents that face forward rather than backward: the continuous validation architecture that governs how the system is tested on an ongoing basis, and the post-quantum security layer that governs how the system will remain secure as the threat landscape evolves. The preflight gate (24 PASS 0 FAIL, verified March 25, 2026) documented in `00-overview.md` §00.8 is the operational expression of Chapter 41's test harness.

| Chapter | Title | What It Contains |
|---|---|---|
| [41-test-harness-and-continuous-validation.md](./41-test-harness-and-continuous-validation.md) | Test Harness | The full test harness and continuous validation architecture — how the system is tested, monitored, and verified on an ongoing basis. Passing checks: container count ✅, gateway health ✅, judge pipeline ✅, judge signing keys ✅, auth enforcement ✅, Cloudflare tunnel ✅. **⚠️ Open: `VERIFYANDTEST.sh` syntax error on line 190 — script does not complete regression baseline. `preflight_gate.sh` `fail`/`ok` command stubs not wired.** |
| [42-Post-Quantum Security Layer.md](./42-Post-Quantum%20Security%20Layer.md) | Post-Quantum Security | The post-quantum security layer — how the system is designed to remain secure against quantum computing threats, with implementation specifications and the cryptographic architecture backing `jarvis-crypto-policy`. **March 28, 2026: `crypto_client.py` confirmed deployed to all 22 LLM proxies via compose volume mount. 0 `ModuleNotFoundError` in logs since fix. `JARVIS_API_KEY` env var confirmed set in production — drives internal token bypass in `ms_jarvis_memory._auth()`.** |

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
- [02-ms-jarvis-gbim.md](./02-ms-jarvis-gbim.md) — the GBIM core
- [07-rag-pipeline-and-routers.md](./07-rag-pipeline-and-routers.md) — RAG and routing
- [11-llm-fabric-of-ms-jarvis.md](./11-llm-fabric-of-ms-jarvis.md) — LLM orchestration (22 proxies, all operational)
- [19-container-architecture-and-routing.md](./19-container-architecture-and-routing.md) — Docker/container layer (96 containers live, `msjarvis-rebuild` namespace)
- [25-consciousness-coordinator-and-services.md](./25-consciousness-coordinator-and-services.md) — consciousness coordinator
- [40-system-audit-and-operational-validation.md](./40-system-audit-and-operational-validation.md) — full audit

**If you are a social scientist, geographer, or policy researcher**, the most relevant chapters are:
- [01-quantarithmia.md](./01-quantarithmia.md) — the framework
- [01-researcher-position.md](./01-researcher-position.md) — positionality
- [06-geodb-spatial-body.md](./06-geodb-spatial-body.md) — spatial grounding
- [03-mountainshares-dao.md](./03-mountainshares-dao.md) — economic instrument
- [34-spiritual-root-and-mother-carrie.md](./34-spiritual-root-and-mother-carrie.md) — spiritual and ethical foundation
- [30-aapcappE-scraper-and-corpus.md](./30-aapcappE-scraper-and-corpus.md) — Appalachian knowledge corpus (★ Active March 27, 2026)

**If you are a funder, institutional partner, or elected official**, start with:
- [00-overview.md](./00-overview.md) — the full operational system reference
- [20-first-stage-evaluation.md](./20-first-stage-evaluation.md) — first formal evaluation
- [39-operational-evaluation.md](./39-operational-evaluation.md) — operational readiness
- [40-system-audit-and-operational-validation.md](./40-system-audit-and-operational-validation.md) — full audit

---

## Production Status Cross-Reference

The chapter map above reflects the system's state as of **March 28, 2026**. Key production facts relevant to thesis navigation:

| Fact | Value | Chapter |
|---|---|---|
| Live containers (`msjarvis-rebuild`) | **96** | Ch. 19 |
| GBIM beliefs in production | **5,416,521** | Ch. 02, 06 |
| Landowner beliefs (GBIM) | **20,593** | Ch. 02 |
| ChromaDB total vectors | **6,675,442 across 40 collections** | Ch. 05 |
| `spiritual_rag` | Deduplicated — 19,338 duplicates removed | Ch. 34 |
| `psychological_rag` | **968 documents — restored** | Ch. 29 |
| `msjarvis_docs` | **4,192 items** | Ch. 05 |
| LLM proxies | **22/22 operational — `crypto_client.py` mounted** | Ch. 11 |
| `minds_participated` | **21/21** | Ch. 33 |
| Port 0.0.0.0 exposures | **0 — all corrected to 127.0.0.1** | Ch. 19 |
| Preflight gate | **24 PASS 0 FAIL** | Ch. 41 |
| Consciousness pipeline | **ACTIVE** (March 25, 2026) | Ch. 25 |
| `governance_rag` | **643 chunks** | Ch. 37 |
| `commons_rag` | **306 chunks** | Ch. 31 |
| `aaacpe_corpus` | **65 docs, 39 sources ★** | Ch. 30 |
| MountainShares Phase 0 beta | **LIVE — Arbitrum One (42161) ★** | Ch. 03, 31 |
| EEG heartbeats | **delta / theta / beta — all LIVE** | Ch. 28 |
| Public URL | **https://egeria.mountainshares.us** | Ch. 38 |
| `mvw_gbim_landowner_spatial` | **⚠️ 0 rows — rebuild pending (Item 21)** | Ch. 21 |
| `VERIFYANDTEST.sh` line 190 | **⚠️ Syntax error — script infrastructure open** | Ch. 41 |

For the full service registry, sprint history, ChromaDB inventory, and pipeline flow diagram, see [00-overview.md](./00-overview.md).

---

*Thesis authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Jarvis is an original system designed and built by Carrie Ann Kidd.*
*See [LICENSE](../LICENSE) for terms.*
*Last verified: March 28, 2026 — 96 containers live, all critical audit findings resolved, MountainShares Phase 0 beta live, AAPCAppE corpus active.*
