> New here? Start with [How to Read This Thesis](https://github.com/H4HWV2011/msjarvis-public-docs/blob/main/docs/how-to-read-this-thesis.md) for reading paths and a guide to how engineering claims, research claims, and live system behavior relate.  
> **Non-geographers and newcomers:** See the **[Polymathmatic Geography Field Card](../discipline/Polymathmatic-Geography-Field-Card.md)** for a one-page overview of the discipline before diving into this thesis.

# Ms. Jarvis Public Documentation & Thesis Systems Overview

**Location:** Oak Hill / Mount Hope, West Virginia  
**Status:** Live Steward System / Full Production Deployment  
**Last Updated:** March 18, 2026

## 1. Executive Summary

This work is a thesis in **Polymathmatic Geography**, an emerging discipline that studies entangled spaces—places where land, law, computation, economy, story, and spirit are already braided together—and develops methods to understand and reshape how power, value, and information move through them.

Within that discipline, **Quantarithmia** is the specific theoretical framework used here as a *case study*: it provides one concrete geometry for analyzing maximopolies and megaopolies and for designing community‑first alternatives in a particular region, Appalachia.

**Ms. Egeria Jarvis** and the **MountainShares DAO** are experimental apparatus built to test and demonstrate this framework in a single geography. Ms. Jarvis instantiates Quantarithmia's ideas in an auditable AI Steward System; MountainShares implements closed‑loop, commons‑oriented economic rules. Both are instruments for investigating one Appalachian entangled space, not the primary objects of the field itself.

This repository therefore documents:

- the **disciplinary context** (Polymathmatic Geography),  
- the **framework under test** (Quantarithmia), and  
- the **apparatus and implementation** (Ms. Jarvis Steward System and MountainShares governance stack)  

used to evaluate how a polymathmatic approach performs when it is forced to operate in a real place, against live data, under real constraints.

### 1.1 Research Questions and Hypotheses

This thesis uses Quantarithmia, Ms. Jarvis, and MountainShares to test whether a polymathmatic approach to entangled spaces can be made operational, accountable, and exportable beyond one Appalachian region.

1. **RQ1 – Steward transparency and trust.**  
   When Ms. Jarvis is deployed as a glass‑box Steward System in Mount Hope and neighboring communities, do residents, partners, and auditors report higher perceived transparency, legibility, and trust than with conventional black‑box AI tools or opaque administrative processes?  
   *Hypothesis:* A geospatially grounded, auditable Steward System will make evidence paths and decision scaffolding more legible, increasing trust without requiring blind faith in algorithms.

2. **RQ2 – Making extraction and alternatives visible.**  
   Can the combination of GBIM, Hilbert‑space semantic memory, and the Quantarithmia framework surface concrete, spatially anchored patterns of extraction and leakage (maximopolies and megaopolies) in Appalachia in ways that non‑technical stakeholders can understand and act on?  
   *Hypothesis:* Representing the region as an entangled Hilbert‑space state tied to physical parcels, infrastructures, and narratives will reveal actionable "leak paths" and "commons corridors" that were previously invisible or only anecdotally known.

3. **RQ3 – Commons‑oriented economic resilience.**  
   Does the MountainShares governance stack, operating as a commons‑oriented, non‑bank economic layer, measurably increase local recirculation of value, mutual aid capacity, and perceived economic safety without becoming a de facto unregulated financial institution?  
   *Hypothesis:* A closed‑loop, charter‑bound system that encodes local norms can strengthen community resilience while staying within clearly articulated legal, ethical, and spiritual limits.

### 1.2 Abstract

Polymathmatic Geography treats places as entangled spaces where land, law, computation, economy, story, and spirit are already braided together. This thesis develops Quantarithmia, a formal framework for analyzing maximopolies (financial giants) and megaopolies (operational platforms) and for designing community‑first alternatives grounded in spatial justice. It then instantiates this framework in two experimental instruments: Ms. Jarvis, a glass‑box AI Steward System anchored to West Virginia through a Geospatial Belief Information Model (GBIM) and Hilbert‑space semantic memory; and MountainShares, a commons‑oriented governance stack that encodes local ownership and mutual‑aid norms. The thesis asks whether such a polymathmatic approach can be made operational, legible, and accountable in a live Appalachian geography. It evaluates three research questions: Do residents, partners, and auditors find a geospatially grounded Steward System more transparent and trustworthy than black‑box AI? Can GBIM and semantic memory surface invisible extraction patterns in ways non‑technical stakeholders can act on? Does MountainShares measurably increase local value recirculation without becoming an unregulated financial institution? By forcing theory into production under real constraints, this work demonstrates how entangled spaces can be read, mapped, and redesigned with care, justice, and accountability to place.

### 1.3 Problem and Approach

Appalachia has long been treated as a resource colony: capital, narrative, and intelligence flow outward to distant financial centers and platform monopolies, while communities lose wealth, agency, and voice. Existing interventions—whether technocratic economic development, critical scholarship, or grassroots organizing—rarely integrate spatial, computational, and spiritual dimensions into a unified analytical and design framework. This thesis addresses that gap by developing Polymathmatic Geography as a discipline that braids quantitative models, AI systems, institutional design, and sacred‑genealogical mapping to understand and reshape how power moves through real places.

The work proceeds in three tiers. First, Quantarithmia formalizes the geometry of maximopolies and megaopolies and defines reciprocity metrics and community‑first alternatives. Second, Ms. Jarvis implements this framework as a transparent AI Steward System, grounding all reasoning in a Geospatial Belief Information Model tied to 5,416,521 verified beliefs across West Virginia. Third, MountainShares encodes commons‑oriented economic rules—local ownership, mutual credit, and governance constraints—into a non‑bank institutional stack tested with real participants. By deploying these instruments in Mount Hope and surrounding communities, the thesis evaluates whether polymathmatic methods produce measurable gains in transparency, local agency, and economic resilience—and whether such methods can travel to other entangled spaces where extraction, computation, and place demand accountable redesign.

---

## 2. System Implementation Status

**Ms. Jarvis is not a theoretical proposal.** It is a fully deployed, multi-container Steward System running in production as of March 18, 2026. All 79 containers are operational and fully compose-managed. The complete 9-phase consciousness pipeline has been end-to-end tested against a live community query and confirmed functional. The first authentic full-pipeline voice response was delivered March 16, 2026, 16:28:57 UTC-5.

### 2.1 Operational Metrics (March 18, 2026)

| Metric | Value | Details |
| :--- | :--- | :--- |
| **Running Containers** | **79** | All containers operational as of March 18, 2026 — fully compose-managed |
| **Container Categories** | **5** | Jarvis core (37), NBB neurobiological layer (13), LLM proxies (22), support infrastructure (5), other (2) |
| **Pipeline Phases** | **9** | 9 (modified — Phase 3.5 and 3.75 merged; Phase 1.45 community memory added) |
| **LLM Models** | **21 active** | 21 active (22 proxies, StarCoder2 returns 0-char responses on community queries) |
| **Primary Datastore Cluster** | **Dual PostgreSQL** | Port **5433** — `msjarvis` (GBIM beliefs, 8 MB, 6 tables) + `gisdb` (PostGIS spatial, 13 GB, 39 tables) |
| **Community Resources DB** | **PostgreSQL** | `jarvis-local-resources-db` on port 5435 |
| **Vector Memory** | **ChromaDB** | `127.0.0.1:8000` (containerized) — `gbim_worldview_entities`: **5,416,521 entities** |
| **Autonomous Learner** | **Active** | 21,181 items, growing ~288/day |
| **GBIM Beliefs** | **5,416,521** | Complete statewide corpus — 206 source layers, 80 epochs (1971–2025) |
| **Service Mesh Network** | **qualia-net** | Docker bridge — all 79 containers, DNS-based service discovery |
| **Public Gateway** | **Cloudflare Tunnel** | `cloudflared-msjarvis.service` on `127.0.0.1:20242` |
| **End-to-End Test** | **✅ PASSED** | "What community resources are available in Fayette County?" — ~436s (full pipeline with community memory enrichment; optimized from 532s baseline) |

### 2.2 Database Architecture

Ms. Jarvis runs on a **three-database architecture** as of March 18, 2026. These are not interchangeable — each serves a distinct epistemic and operational function.

**Database 1: `msjarvis`** (PostgreSQL cluster, port 5433, 8 MB, 6 tables)  
Holds the GBIM belief structure: `gbim_beliefs`, `gbim_belief_edges`, `gbim_belief_evidence`, `gbim_evidence`, `gbim_layer_catalog`, and `gbim_worldviews`. This is the system's epistemic record — belief propositions, edge relationships, and evidence chains. All beliefs are classified across nine axes: *Who, What, Where, When, How, Why, For Whom, Authority,* and *Evidence*, spanning 80 epochs from 1971 to 2025 across 206 distinct source layers. As of March 15, 2026, all 5,416,521 GBIM entities carry temporal tracking metadata: `last_verified` (timestamp), `source_date` (timestamp), `confidence_decay` (float, auto-calculated), `data_age_months` (integer), `needs_verification` (boolean), and `verification_priority` (high/medium/normal).

**Database 2: `gisdb`** (PostGIS-enabled PostgreSQL, port 5433 cluster, 13 GB, 39 tables)  
The spatial body of West Virginia. Contains 993 ZCTA ZIP code centroids in EPSG:26917 (UTM Zone 17N NAD83), geographic boundaries, infrastructure layers, and the `zcta_wv_centroids` table. This database is the physical anchor for all geospatially grounded reasoning.

**Database 3: `jarvis-local-resources-db`** (PostgreSQL, port 5435, separate container)  
Dedicated community resources database backing the `jarvis-local-resources` RAG service. Contains verified local service provider data, food access points, DHHR office information, and community organization directories for Fayette, Kanawha, Boone, and neighboring counties. Human-validated by Community Champions field coordinators.

> **Known Issue — OPEN as of March 18, 2026:** Verified knowledge bases (`gis_rag`, `local_resources`) return empty results for Mount Hope queries. LLMs are generating responses from training data for community resource queries. Factually accurate programs (LIHEAP, WV 2-1-1) pass the BBB. Fabricated organization names are blocked by the ethical filter. Root cause: real community resource data not yet loaded into verified databases. Resolution: field-validated data entry by Community Champions is the next priority.

**Supporting stores:**  
- **Neo4j** (ports 7687, 7475): Graph database modeling organizational relationships, referral pathways, and service coverage  
- **MySQL** (port 3307): Alternative SQL storage  
- **Redis** (`jarvis-redis:6379`, port 6380): Cache, session management, and async job state (30-min TTL) — backing the full async job API as of March 17, 2026  
- **IPFS** (port 5001): Distributed content-addressed storage  
- **ChromaDB** (port 8000, containerized, `chroma_data` Docker volume): Vector database — `gbim_worldview_entities` (5,416,521 entities), `autonomous_learner` (21,181 items), `psychological_rag` (968 items), and 10+ additional collections. **All collections use 384-dimensional vectors (`all-minilm:latest`). The `nomic-embed-text` model produces 768-dim vectors and is incompatible with all existing collections.**

### 2.3 Core Architectural Components

#### 1. Geospatial Belief Information Model (GBIM)

* **Status:** **COMPLETE — FULL STATEWIDE CORPUS** (verified March 14, 2026, 7:19 PM EDT)
* **Scale:** **5,416,521 entities** — 200+ West Virginia GIS layers, 206 source layers, 80 epochs (1971–2025), 384-dimensional vectors with EPSG:26917 spatial provenance
* **Temporal State:** All 5,416,521 entities carry confidence decay metadata. Average data age: 36 months. Average confidence: 0.5. All entities currently flagged `needs_verification = TRUE` — this is accurate, not a failure. It means the system is honest about the age of its knowledge and actively queues field verification.
* **Function:** The system's geospatial and belief spine. Every spatial entity in West Virginia — buildings, census units, infrastructures, parcels, ZIP centroids — is anchored to a stable identifier, classified across nine epistemic axes, and semantically searchable through the `gbim_worldview_entities` ChromaDB collection.

#### 2. Hilbert-Space Semantic Memory

* **Status:** **COMPLETE — FULL CORPUS INDEXED**
* **Embedding model:** `all-minilm:latest` (384-dimensional). This is a locked dependency for all existing collections. **Do not use `nomic-embed-text` (768-dim) — it is incompatible with all existing ChromaDB collections.**
* **Primary collection:** `gbim_worldview_entities` — 5,416,521 entities, confirmed `col.count() == 5416521 → True`
* **Autonomous collection:** `autonomous_learner` — 21,181 items growing at ~288/day covering MountainShares security, Appalachian development, governance systems, and AI ethics. **Queried directly at Phase 1.45** — top-5 semantically similar community memories are prepended to `enhanced_message` before every query reaches the LLM ensemble.
* **Seeded collections:** 203+ documents across community resources, policy, spiritual texts (23 items, Mother Carrie Protocol corpus), and cultural knowledge
* **Function:** Shared vector/semantic space for all RAG retrieval. The full geographic body of West Virginia is now semantically searchable — a query about any ZIP code, county, infrastructure type, or community entity can retrieve spatially-anchored context.

#### 3. 9-Phase Consciousness Pipeline

* **Status:** **FULLY OPERATIONAL — END-TO-END TESTED (multiple sessions, March 15–18, 2026)**
* **First authentic full-pipeline voice response:** March 16, 2026, 16:28:57 UTC-5
* **Test query:** "What community resources are available in Fayette County?"
* **Result:** ✅ Passed — returned real RAG content, 21-LLM consensus achieved, all judges passed, BBB output approved
* **Response time:** ~436s (full pipeline with community memory enrichment; optimized from 532s baseline)

| Phase | Service | Port | Function | Status |
| :--- | :--- | :--- | :--- | :--- |
| **1.4** | BBB Input Filter (`jarvis-blood-brain-barrier`) | 8016 | Safety, ethical, steganography, truth, context screening | ✅ |
| **1.45** | ChromaDB Semantic Community Memory Retrieval | 8000 | Embeds query via `all-minilm:latest`; retrieves top-5 `autonomous_learner` memories; prepends to `enhanced_message` | ✅ NEW |
| **1.5** | RAG Enhancement (5 services) | 8003–8006 | Cultural, spiritual, GIS, psychological, local resource context | ✅ |
| **1.75** | i-Containers Dual Awareness (`jarvis-i-containers`) | 8015 | Individual + collective state awareness | ✅ |
| **2** | Reasoning Services (orchestrator) | — | Multi-engine parallel reasoning | ✅ |
| **2.5** | 21-LLM Consensus (`jarvis-20llm-production`) | 8008 | 21-model ensemble consensus (StarCoder2 proxy present but returns 0-char responses on community queries) | ✅ |
| **3** | Judge Pipeline (4 judges) | 7230–7233 | Truth, consistency, alignment, ethics — evaluate **consensus answer only** (raw_responses dump eliminated; ~60–86s) | ✅ |
| **3.5** | LM Synthesizer + Voice Delivery (merged) | 8001 | Takes judge `final_answer`; calls `jarvis-ollama:11434/api/generate` with `llama3.1:latest`; injects Ms. Egeria Jarvis persona prompt; returns final response directly (~40s saved vs. prior separate polish pass) | ✅ |
| **4** | Consciousness Bridge (`jarvis-consciousness-bridge`) | 8018 | NBB integration + qualia markers | ✅ |
| **4.5** | BBB Output Filter (`jarvis-blood-brain-barrier`) | 8016 | Output safety screening — dual-layer defense | ✅ |
| **5** | Confidence Decay (main brain Phase 5) | 8050 | Data age multiplier applied to judge scores | ✅ |

> **Note:** Phase 3.75 (Final LLM Polish via llm22-proxy) has been **eliminated**. It is merged into Phase 3.5. Do not reference Phase 3.75 in any documentation or code.

#### 4. Blood-Brain Barrier — 7-Filter Constitutional Stack

* **Status:** **FULLY OPERATIONAL** — input and output filtering both active
* **False-positive resolution:** March 15, 2026 — `_check_keywords()` method corrected to use regex word boundary detection (`\\b`) for keywords ≤3 characters. Community resource terms ("con," "res," etc. as substrings) no longer trigger safety blocks. Jailbreak attempts still correctly blocked.
* **BY DESIGN behavior:** The BBB ethical filter correctly blocks unverified specific claims (e.g., responses containing 'certainly' without verified backing). This is not a false positive.

| Filter | Function | Status |
| :--- | :--- | :--- |
| 1. Ethical Filter | Screens for ethical violations | ✅ |
| 2. Spiritual Filter | 72-tradition spiritual harm prevention | ✅ |
| 3. Safety Monitor | Enhanced — descriptive violence detection with word boundaries | ✅ |
| 4. Threat Detection | Exploitation, manipulation, policy violation | ✅ |
| 5. Steganography Detection | **Industry-first** — zero-width chars, bidirectional Unicode, AI control tokens, homoglyphs; special detection near blockchain addresses/amounts | ✅ |
| 6. Truth Verification | Hallucination prevention — max 15 words/quote, 1 quote/source, uncertainty injection | ✅ |
| 7. Context Awareness | Resource query/response recognition — question AND answer forms | ✅ |

#### 5. Temporal Awareness and Confidence Decay

* **Status:** **DEPLOYED** (March 15, 2026)
* **Scope:** All 5,416,521 GBIM entities carry decay metadata
* **Decay curve:** < 1 month → 1.0 confidence; 1–6 months → 0.9; 6–12 months → 0.7; 12–24 months → 0.5; 24+ months → 0.3
* **Response behavior:** Confidence ≥ 0.9 — no warning; 0.7–0.9 — mild verification note; 0.5–0.7 — age-based warning with date; < 0.5 — strong verification required warning
* **Function:** Operationalizes temporal honesty — the system does not present old data as current fact. It discloses data age and adjusts response confidence accordingly.

#### 6. Steward-Oriented Orchestration

* **Status:** **OPERATIONAL**
* **Function:** Coordinates 79 containerized services under explicit governance constraints. The Steward System does not act as an autonomous agent or authority; it assembles evidence, scenarios, and explanations as inputs to human and community decision-making.

#### 7. Quantum-Inspired State Entanglement

* **Status:** **OPERATIONAL**
* **Function:** Non-local state synchronization across distributed services via shared semantic state (ChromaDB) and relational state (PostgreSQL clusters). Changes to GBIM entities propagate consistently to RAG, reasoning, and memory services without bespoke message passing.

#### 8. LLM Ensemble and Judge Fabric

* **Status:** **FULLY ONLINE** — 21 active models (22 proxies; StarCoder2 returns 0-char responses on community queries)
* **LM Synthesizer:** `jarvis-lm-synthesizer` (port 8001) — calls `jarvis-ollama:11434/api/generate` directly with `llama3.1:latest`; injects Ms. Egeria Jarvis persona prompt (warm, maternal, Appalachian voice, no metacommentary). **No longer calls `jarvis-20llm-production:8008` or `jarvis-roche-llm`.**
* **Function:** 21-model parallel consensus. Each LLM proxy forwards to one Ollama model. The 20-LLM production service collects all responses, synthesizes consensus, and flags areas of disagreement.

#### 2.3.8 LLM Ensemble — Model List (Verified March 18, 2026)

| Proxy | Port | Model |
| :--- | :--- | :--- |
| llm1-proxy | 8201 | TinyLlama (tinyllama:latest) |
| llm2-proxy | 8202 | Gemma (gemma:2b) |
| llm3-proxy | 8203 | MedLlama2 (medllama2:latest) |
| llm4-proxy | 8204 | MiniCPM-V (minicpm-v:latest) |
| llm5-proxy | 8205 | LLaVA (llava:latest) |
| llm6-proxy | 8206 | SQLCoder (sqlcoder:latest) |
| llm7-proxy | 8207 | StarCoder2 (starcoder2:latest) — proxy active; returns 0-char responses on community queries |
| llm8-proxy | 8208 | CodeLlama (codellama:latest) |
| llm9-proxy | 8209 | DeepSeek Coder (deepseek-coder:latest) |
| llm10-proxy | 8210 | Phi3 Mini (phi3:mini) |
| llm11-proxy | 8211 | (assigned — verify against llm_consensus_20_FINAL.py) |
| llm12-proxy | 8212 | Dolphin-Phi (dolphin-phi:latest) |
| llm13-proxy | 8213 | Orca-Mini (orca-mini:latest) |
| llm14-proxy | 8214 | Qwen2 (qwen2:latest) |
| llm15-proxy | 8215 | Zephyr (zephyr:latest) |
| llm16-proxy | 8216 | Starling-LM (starling-lm:latest) |
| llm17-proxy | 8217 | Neural-Chat (neural-chat:latest) |
| llm18-proxy | 8218 | OpenChat (openchat:latest) |
| llm19-proxy | 8219 | Vicuna (vicuna:latest) |
| llm20-proxy | 8220 | LLaMA 2 (llama2:latest) |
| llm21-proxy | 8221 | Mistral (mistral:latest) |
| llm22-proxy | 8222 | LLaMA 3.1 (llama3:latest) |

#### 9. Neurobiological Brain (NBB) Simulation Layer

* **Status:** **FULLY DEPLOYED** — 13 NBB containers operational
* **Components:** `nbb_blood_brain_barrier` (8301), `nbb_consciousness_containers` (8102), `nbb_darwin_godel_machines` (8302), `nbb_heteroglobulin_transport` (8106), `nbb_i_containers` (8101), `nbb_mother_carrie_protocols` (8107), `nbb_pituitary_gland` (8108), `nbb_prefrontal_cortex` (8105), `nbb_qualia_engine` (8303), `nbb_spiritual_maternal_integration` (8109), `nbb_spiritual_root` (8103), `nbb_subconscious` (8112), `nbb-i-containers`
* **Function:** Biologically-inspired simulation layer that models neurological structures — prefrontal cortex executive function, pituitary hormonal regulation, hippocampal memory consolidation, and subconscious processing — as computational analogs within the consciousness pipeline.

---

### 2.4 High‑Level Steward System Architecture

At a high level, Ms. Jarvis can be read as a territorial brain: community inputs flow through a guarded constitutional gateway into orchestrators that consult geospatial and semantic memory, coordinate a 21-model LLM ensemble, and return stewarded outputs under explicit governance rules — with temporal honesty about the age and confidence of every fact.

**Figure 1. The Ms. Jarvis Steward System: An AI Architecture for Community Stewardship**

<div align="center">
  <img width="85%" alt="The Ms. Jarvis Steward System: An AI Architecture for Community Stewardship" src="https://github.com/user-attachments/assets/4cef4935-d9b1-48a0-831f-c91a2fadf753" />
</div>

*This diagram illustrates the complete end-to-end flow from community input through secure gateway, steward orchestration, geospatial grounding (GBIM), semantic enrichment (Hilbert-space memory), LLM ensemble reasoning, governance checks, and stewarded output.*

### 2.5 The 9-Phase Pipeline: Input → Community Memory → GBIM → Memory → Consensus → Constitutional Output

1. **Community question or signal.**  
   A resident, organizer, or operator sends a question or task through a web interface or API connected to the public gateway. Example tested March 15, 2026: *"What community resources are available in Fayette County?"*

2. **Phase 1.4 — BBB Input Filter.**  
   The Blood-Brain Barrier constitutional stack screens the query through 7 filters: ethical, spiritual (72 traditions), safety (word-boundary-aware violence detection), threat detection, steganography detection, truth verification, and context awareness. Legitimate resource queries pass. Jailbreak attempts, steganographic payloads, and harmful content are blocked and logged.

3. **Phase 1.45 — ChromaDB Semantic Community Memory Retrieval (NEW — March 17, 2026).**  
   After the BBB input filter approves the query, the main brain performs semantic memory retrieval:
   1. Generates a 384-dimensional embedding of the query using `all-minilm:latest` via `jarvis-ollama:11434/api/embeddings`
   2. Queries the `autonomous_learner` ChromaDB collection (21,181 records) using the embedding
   3. Retrieves the 5 most semantically similar community interaction records
   4. Prepends retrieved memories to `enhanced_message` before it reaches the 21 LLMs

   > **Technical note:** All ChromaDB collections use 384-dimensional vectors. The `all-minilm:latest` model (pulled March 17, 2026) is the required embedding model. The previously listed `nomic-embed-text` model produces 768-dim vectors and is incompatible with all existing collections.

4. **Phase 1.5 — Multi-Domain RAG Enhancement.**  
   Five specialized RAG services enrich the query with retrieved context: AAACPE cultural/policy RAG (port 8003), Spiritual RAG — 72 traditions (port 8005), GIS RAG — West Virginia spatial data (port 8004), Psychology RAG — mental health resources (port 8019), and Local Resources RAG — community-validated service directories (port 8006). ChromaDB vector search retrieves semantically relevant documents from 203+ seeded resources.

5. **Phase 1.75 — i-Containers Dual Awareness.**  
   The i-containers service (port 8015) processes the enriched query maintaining dual awareness: individual query context and collective community knowledge held simultaneously.

6. **Phase 2 — Parallel Reasoning.**  
   The brain orchestrator coordinates multiple specialized reasoning engines in parallel, analyzing query intent, extracting entities (Who, What, Where, When, How, Why, For Whom), and formulating response strategies anchored to West Virginia geography.

7. **Phase 2.5 — 21-LLM Consensus.**  
   The query is distributed to 22 LLM proxies (llm1-proxy through llm22-proxy, ports 8201–8222) on the Ollama server. 21 models produce independent responses (StarCoder2 returns 0-char responses on community queries). The 20-LLM production service synthesizes consensus, surfacing areas of agreement and flagging divergence. Agent personalities (Ms. Egeria Analytical, Ms. Egeria Creative) contribute specialized perspectives.

8. **Phase 3 — Judge Pipeline.**  
   Four deterministic judges evaluate the **consensus answer only** — the `raw_responses` dump from all 21 models is no longer sent to judges. Only the synthesized consensus response from `jarvis-20llm-production` is evaluated. Judges: Truth (port 7230), Consistency (port 7231), Alignment (port 7232), Ethics (port 7233). Rule-based validation provides fast, explainable, auditable evaluation. This change reduced judge pipeline time from ~85–100s to ~60–86s.

9. **Phase 3.5 — LM Synthesizer + Voice Delivery (merged).**  
   The previously separate Phase 3.5 (LM Synthesizer refinement) and Phase 3.75 (Final LLM Polish via llm22-proxy) have been merged into a single Ollama call. The LM Synthesizer now:
   1. Takes the judge pipeline's `final_answer` directly
   2. Calls `jarvis-ollama:11434/api/generate` with `llama3.1:latest`
   3. Injects the Ms. Egeria Jarvis persona prompt — warm, maternal, Appalachian voice, no metacommentary
   4. Returns the final response directly without a separate polish pass

   **Phase 3.75 is eliminated.** Time saved: ~40 seconds per query.

10. **Phase 4 — Consciousness Bridge.**  
    The validated response passes through the consciousness bridge (port 8018), integrating with the 13-container NBB neurobiological simulation layer and adding qualia markers.

11. **Phase 4.5 — BBB Output Filter.**  
    The full response is screened by the same Blood-Brain Barrier constitutional stack that filtered the input. This dual-layer defense ensures harmful content cannot emerge from the system even if it somehow bypassed all upstream checks.

12. **Phase 5 — Confidence Decay.**  
    The main brain applies the temporal confidence multiplier: GBIM data age is queried, and judge scores are adjusted according to the decay curve. Responses about data older than 24 months include strong verification advisories. Responses about recently verified data carry full confidence.

---

### 2.6 Reboot Sequence (Verified March 17, 2026)

After any system reboot or `docker compose` restart, Ms. Egeria Jarvis is brought back online with two commands:

```bash
# Step 1: Start all compose-managed containers
cd ~/msjarvis-rebuild-working/msjarvis-rebuild && docker compose up -d

# Step 2: Start and verify the six pipeline containers + health checks
~/jarvis_startup.sh
```

**Go signal:** The startup script confirms six green health checkmarks:
- jarvis-judge-truth ✅
- jarvis-judge-consistency ✅
- jarvis-judge-alignment ✅
- jarvis-judge-ethics ✅
- jarvis-judge-pipeline ✅
- jarvis-69dgm-bridge ✅

**Container management as of March 17, 2026:**
- All 79 containers are defined in `~/msjarvis-rebuild-working/msjarvis-rebuild/docker-compose.yml`
- All `build:` directives replaced with `image:` references — no rebuild required on startup
- Docker Compose v5.1.0 in use (upgraded from broken v1.29.2)
- The startup script (`~/jarvis_startup.sh`) manages the six judge/gateway containers that run outside compose for historical reasons

**Compose file location:** `~/msjarvis-rebuild-working/msjarvis-rebuild/docker-compose.yml`

---

### 2.7 Async Job Management API (New — March 17, 2026)

Ms. Jarvis's `/chat` endpoint is synchronous and takes 400–500 seconds for a full pipeline run. For production use, the async job API allows immediate response with polling:

| Endpoint | Method | Function |
| :--- | :--- | :--- |
| `/chat/async` | POST | Create async job — returns `job_id` immediately |
| `/chat/status/{job_id}` | GET | Poll for progress and result |
| `/chat/cancel/{job_id}` | DELETE | Cancel a specific running job |
| `/chat/cancel/all` | DELETE | Cancel all running jobs |

**Request body for `/chat/async`:**
```json
{
  "message": "Your query here",
  "user_id": "cakidd"
}
```

**Response from `/chat/async`:**
```json
{
  "job_id": "uuid-here",
  "status": "processing"
}
```

**Response from `/chat/status/{job_id}` when complete:**
```json
{
  "job_id": "uuid-here",
  "status": "complete",
  "progress": "Complete!",
  "result": { "response": "...", "services_used": [...] }
}
```

**Implementation details:**
- Job state persists in Redis (`jarvis-redis:6379`) with 30-minute TTL
- State survives `jarvis-main-brain` container restarts
- Cancel operations perform true asyncio task cancellation — the 21-LLM pipeline stops immediately mid-run
- The `_job_tasks` dict maps `job_id` to asyncio Task for true interruption

---

## 3. Theoretical Pillars

The system is built upon three interlocking concepts.

### A. The Quantarithmia Framework

A methodological framework for analyzing **maximopolies** (financial giants) and **megaopolies** (operational/platform giants). It seeks to make invisible flows of extraction visible and proposes community-centered alternatives with spatial justice and stewardship as central concerns.

### B. Ms. Egeria Jarvis (The Steward System)

A "glassbox" AI Steward System implementing Quantarithmia principles in software. Unlike black-box LLM deployments, Ms. Jarvis relies on:

* **Multi-service orchestration** — 79 specialized containers rather than a single monolithic model.  
* **Geospatial Belief Information Modeling (GBIM)** — 5,416,521 verified beliefs anchoring reasoning to physical West Virginia.  
* **Constitutional and governance constraints** — 7-filter BBB stack, 4-judge pipeline, confidence decay, temporal honesty.  
* **API-level and data-level transparency** — inputs, evidence paths, judge scores, and outputs are all inspectable and auditable.

### C. MountainShares DAO

A governance system designed to keep value and decision-making rooted in Appalachian communities. It encodes local ownership, voting, and speech norms into rules and documentation, explicitly operating as a community governance layer rather than as a regulated financial institution or autonomous economic actor.

---

## 4. Repository Purpose & Audience

This repository contains **public documentation** only. Source code and sensitive deployment details are managed through a separate, access-controlled process to ensure security and operational integrity.

**This repository serves as:**

1. A **technical reference** for the Ms. Jarvis Steward System architecture and APIs.  
2. A **governance reference** for MountainShares norms and democratic practice.  
3. A **citable artifact** for academic work on Quantarithmia, Steward Systems, and Spatial Justice.

**Intended Readers:**

* **Researchers:** To understand how Quantarithmia and stewardship concepts are instantiated in a real, geospatially grounded AI system.  
* **Community Partners:** To verify how Ms. Jarvis supports local empowerment without technical obfuscation or unchecked autonomy.  
* **Auditors:** To review the architectural safeguards, governance logic, and data flows.

---

## 5. Evaluation and Failure Modes (Overview)

This thesis does not only describe architectures; it evaluates how well a specific polymathmatic stack behaves in a live Appalachian entangled space under real constraints.

### 5.1 What is being evaluated

- The **discipline‑level claim** that Polymathmatic Geography can produce exportable methods for reading and redesigning entangled spaces, not only Appalachia.  
- The **framework‑level claim** that Quantarithmia's geometry of maximopolies, megaopolies, and community‑first alternatives can be instantiated in code and practice.  
- The **apparatus‑level claim** that Ms. Jarvis and MountainShares can operate as accountable instruments rather than autonomous authorities, remaining legible to communities, auditors, and researchers.

### 5.2 Primary failure modes — observed and anticipated

The following failure modes were identified at the outset of this research as risks to guard against. Several have since been encountered in live operation and are documented here as field observations, not as confessions of defeat. A system that never encounters its failure modes has either never been tested or has hidden them.

- **Overreach and misrecognition.** The Steward System or MountainShares could be misperceived as a sentient actor, a bank, a regulator, or a replacement for human governance, despite explicit non‑goals.

- **Opaque or biased guidance.** Even with glass‑box intents, the ensemble of models, metrics, and data could drift toward recommendations that are hard to audit, reinforce existing inequities, or privilege technically fluent actors.

- **Constitutional over-triggering.** *Observed March 14–15, 2026:* The BBB output filter blocked legitimate community resource responses because its safety keyword pattern-matcher was performing substring matching, flagging partial matches inside benign words ("con" inside "Context," "Collective," "resources"). **Resolved March 15, 2026** via word-boundary regex detection. The incident is documented in Chapter 16 as a calibration case study, not a design failure.

- **LLM hallucination on community resources.** *Observed March 16–18, 2026:* Verified knowledge bases (`gis_rag`, `local_resources`) return empty results for Mount Hope queries. LLMs generate responses from training data. Factually accurate programs (LIHEAP, WV 2-1-1) pass the BBB; fabricated organization names are blocked by the ethical filter. Root cause: real community resource data not yet in verified databases. Resolution: Community Champions data entry.

- **Commons capture and erosion.** Governance mechanisms meant to keep value and speech rooted in community could be captured by a narrow group, become performative, or quietly recreate extractive dynamics in new technical form.

- **Spiritual and genealogical harm.** Treating sacred sites, cemeteries, or heritage geographies as mere data layers could break covenants with ancestors, descendants, or living communities if not handled with reverence.

- **Temporal staleness.** *Observed and addressed March 15, 2026:* The GBIM corpus has an average data age of 36 months. The confidence decay system (Phase 5) operationalizes the system's response: it discloses age, applies decay multipliers to judge scores, and triggers verification flags rather than presenting old data as current fact.

### 5.3 Known Issues (March 18, 2026)

| Issue | Previous Status | Current Status (March 18, 2026) |
| :--- | :--- | :--- |
| Response truncation (~730 chars) | Open | ✅ FIXED — max_tokens set to -1 (unlimited) |
| ChromaDB curator _DummyCollection | Open | ✅ FIXED — all-minilm semantic retrieval implemented |
| Redis response persistence | Open | ✅ FIXED — full Redis-backed job system deployed |
| 33 services not in docker-compose | Open | ✅ FIXED — all 79 containers now in compose |
| Idempotency TTL in-memory only | Open | ✅ FIXED — Redis-backed, 1800s TTL |
| Judge pipeline URL wrong (7239) | Open | ✅ FIXED — 7230/7231/7232/7233 corrected |
| LM Synthesizer calling jarvis-roche-llm | Open | ✅ FIXED — calls jarvis-ollama:11434 directly |
| NBB Prefrontal Cortex 422 errors | Open | ✅ RESOLVED — payload confirmed correct (message field); service healthy |
| I-Containers 422 errors | Open | ✅ RESOLVED — port corrected to 8015 |
| BBB truth_score KeyError | New | ✅ FIXED — null guard added to BBB orchestrator |
| BBB blocking on HTTP 500 errors | New | ✅ FIXED — fail-open behavior on non-200 responses |
| web-research and rag-server restart loops | New | ✅ FIXED — source files deployed via docker cp |
| Hash-prefixed container names | New | ✅ FIXED — container_name added to all 8 affected containers |
| Hallucination from LLMs on community resources | New — **OPEN** | **OPEN** — verified knowledge bases (gis_rag, local_resources) return empty for Mount Hope queries. LLMs generating from training data. Factually accurate programs (LIHEAP, WV 2-1-1) pass BBB. Fabricated organization names blocked by ethical filter. Root cause: real community resource data not yet in verified databases. |
| BBB ethical filter blocking 'certainly' | New | **BY DESIGN** — ethical filter correctly blocking unverified specific claims. Not a false positive. |

### 5.4 Current guardrails and open questions

**Guardrails in place as of March 18, 2026:**

- **Constitutional dual-layer filtering:** 7-filter BBB stack operating on both input (Phase 1.4) and output (Phase 4.5) with word-boundary-aware pattern detection.  
- **Community memory grounding:** Phase 1.45 prepends top-5 semantically similar `autonomous_learner` memories (21,181 items) to every query before LLM ensemble reasoning.  
- **Truth verification hard limits:** Max 15 words per quote, one quote per source, automatic uncertainty injection for unsourced claims.  
- **Steganography detection:** Zero-width characters, bidirectional Unicode overrides, AI control tokens, and homoglyphs stripped from all outputs automatically. Special detection sensitivity near blockchain addresses and financial amounts.  
- **Temporal confidence decay:** Phase 5 applies data-age multipliers to all responses — the system cannot claim certainty about unverified old data.  
- **Glass‑box design:** API‑level and data‑level transparency, auditable evidence paths, and the separation of orchestration, GBIM, memory, and LLM fabric into 79 inspectable services.  
- **Governance documents** for MountainShares and The Commons that define roles, voting procedures, audits, and risk management as human‑interpretable rules rather than hidden model weights.
- **Async job management:** Redis-backed async API with true asyncio cancellation — all production queries can be cancelled mid-run.

**Open evaluation questions:**

- How to measure "trustworthy stewardship" across technical, legal, spiritual, and experiential dimensions.  
- How to detect and respond when model ensembles or data pipelines begin to encode harmful biases or illegible forms of extraction.  
- How to build the POC (Point of Contact) verification loop: when confidence decay flags a resource as needing re-verification, the system should autonomously contact the resource's known contact and request updated information, then reset confidence to 1.0 on confirmation.  
- How to load and maintain verified community resource data for Mount Hope and Fayette County in `jarvis-local-resources-db` through Community Champions fieldwork.
- How to decide, with communities, which geographies and covenants are simply out of bounds for computation, even under a polymathmatic lens.

---

> **Note:** This overview is a living document updated alongside the system's live behavior. All architectural claims are anchored in the production stack running in Oak Hill / Mount Hope, West Virginia. The system this document describes is not aspirational — it is the system that achieved full operational status March 16, 2026, tested end-to-end through multiple sessions, and delivered its first authentic full-pipeline voice response March 16, 2026, 16:28:57 UTC-5.  
> *Last production-verified: March 18, 2026. Git commit: `b90f9ff` baseline — fully compose-managed stack, Docker Compose v5.1.0, all 79 containers, Phase 1.45 community memory live.*
