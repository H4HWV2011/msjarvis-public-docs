> **Why this matters for Polymathmatic Geography**
> This chapter formalizes how psychological and mental-health knowledge is integrated into Ms. Jarvis to guide interaction patterns, monitor interaction risks, and adapt system behavior over time, all grounded in three PostgreSQL databases (`msjarvis` port 5433: 5,416,521 verified GBIM beliefs; `gisdb` port 5433: 13 GB PostGIS; `jarvis-local-resources-db` port 5435: community resources). It supports:
> - **P1 – Every where is entangled** by ensuring that psychological safeguards are woven into the same retrieval, filtering, and memory infrastructure anchored to PostgreSQL that handles spatial and technical content, not isolated in a separate silo.
> - **P3 – Power has a geometry** by making psychological constraints visible as named services, tagged collections, PostgreSQL-validated rules, and explicit endpoints rather than hiding them in opaque model behavior.
> - **P5 – Design is a geographic act** by tailoring psychological guidance to populations and risk types specific to Appalachian communities grounded in PostgreSQL GBIM — rural grief, economic stress, identity disruption — rather than generic global corpora.
> - **P12 – Intelligence with a ZIP code** by grounding psychological RAG retrieval in collections that include place-specific and community-specific mental health materials validated against PostgreSQL West Virginia institutional knowledge.
> - **P16 – Power accountable to place** by logging PIA review cycle outputs, recording recommendations and observed patterns in PostgreSQL-auditable format, and making this material available for human oversight and community governance review.
>
> As such, this chapter belongs to the **Computational Instrument** tier: it specifies the psychological safeguard services, guidance corpus, and PIA review loop that protect interaction quality and mental-health alignment in Ms. Jarvis's operation, all anchored to the three-database PostgreSQL architecture. The `jarvis-psychology-services` (port 8019) and `psychological_rag_domain` (port 8006) services were deployed and confirmed operational March 15, 2026 (commit `b90f9ff`), contributing to the verified 349.87s end-to-end 9-phase pipeline benchmark.

```
┌─────────────────────────────────────────────────────────────┐
│   Psychological Safeguards Architecture                     │
│   (Production State: March 15, 2026, commit b90f9ff)        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  User Request → jarvis-main-brain (8050)                    │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Phase 1.4 — BBB 7-Filter Input Stack         │         │
│  │  (Always Active — port 8016)                  │         │
│  │  -  EthicalFilter                               │         │
│  │  -  SpiritualFilter                             │         │
│  │  -  SafetyMonitor (word-boundary regex,         │         │
│  │    fixed March 15 — no false-positives on      │         │
│  │    community resource terms)                   │         │
│  │  -  ThreatDetection                             │         │
│  │  -  SteganographyDetection (March 15)           │         │
│  │  -  TruthVerification (March 15)                │         │
│  │  -  ContextAwareness (March 15)                 │         │
│  │  -  TruthValidator (vs PostgreSQL msjarvis)     │         │
│  │    - correct_identity                          │         │
│  │    - correct_creator                           │         │
│  │    - relationship_clear                        │         │
│  │  -  normalize_identity                          │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Phase 3 — Psychology Pre-Assessment           │         │
│  │  (Deployed March 15, 2026 — Always Active)     │         │
│  │  ┌──────────────────────────────────────────┐  │         │
│  │  │  jarvis-psychology-services (8019)       │  │         │
│  │  │  /psychological_assessment               │  │         │
│  │  │  -  psychological_assessment              │  │         │
│  │  │  -  therapeutic_guidance                  │  │         │
│  │  │  -  emotional_support                     │  │         │
│  │  │  -  wellbeing_recommendations             │  │         │
│  │  │  -  evidence_based_approaches             │  │         │
│  │  │  Severity classification + crisis check  │  │         │
│  │  └──────────────────────────────────────────┘  │         │
│  │  ┌──────────────────────────────────────────┐  │         │
│  │  │  psychological_rag_domain (8006)         │  │         │
│  │  │  /search, /add_document                  │  │         │
│  │  │  ChromaDB psychological_rag collection   │  │         │
│  │  │  (port 8000, chroma_data volume)         │  │         │
│  │  │  968 items: therapy, mindfulness,        │  │         │
│  │  │  trauma, depression, anxiety, social     │  │         │
│  │  │  support (validated vs Postgres msjarvis)│  │         │
│  │  └──────────────────────────────────────────┘  │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  Response Processing                                        │
│  -  truthverdict (from BBB + PostgreSQL validation)          │
│  -  consciousnesslayers (psych assessment layer included)    │
│  -  background_rag_store → ms_jarvis_memory (ChromaDB)       │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  PIA Review Loop (Manual Process)             │         │
│  │  ────────────────────────────────────         │         │
│  │  Inputs (manually sampled):                    │         │
│  │  -  ms_jarvis_memory entries                    │         │
│  │  -  truthverdict fields                         │         │
│  │  -  BBB barrier_stats (PostgreSQL-auditable)    │         │
│  │  -  Psychology service outputs                  │         │
│  │                                                 │         │
│  │  Analysis:                                      │         │
│  │  -  Recurring truthverdict violations           │         │
│  │  -  BBB block-rate trends                       │         │
│  │  -  Identity-confusion patterns                 │         │
│  │  -  Underuse of psychological guidance          │         │
│  │                                                 │         │
│  │  Outputs (written recommendations):            │         │
│  │  -  BBB parameter adjustments                   │         │
│  │  -  Judge instruction updates                   │         │
│  │  -  Mode policy refinements                     │         │
│  │  -  Guidance corpus additions (PostgreSQL-      │         │
│  │    validated for WV community context)         │         │
│  │                                                 │         │
│  │  Operator Action Required for Implementation   │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  Accountability                                             │
│  -  PostgreSQL-auditable PIA records                         │
│  -  BBB barrier_stats logged                                 │
│  -  Community governance review                              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> **Figure 29.1.** Psychological safeguards architecture (March 15, 2026): BBB 7-filter pipeline (expanded from 4 filters to 7 as of March 15) and TruthValidator validated against PostgreSQL `msjarvis` provide primary safety gate on every request (Phase 1.4); psychological services (Phase 3, deployed March 15 — now active on every production request) offer severity classification, crisis indicator check, and evidence-based guidance; manual PIA review loop samples logs and produces written recommendations requiring operator action; all accountability records PostgreSQL-auditable for community governance review.

---

## Status as of March 15, 2026

| Category | Details |
|---|---|
| **Implemented and verified (March 15, 2026)** | `jarvis-psychology-services` confirmed running at **127.0.0.1:8019** (deployed March 15, commit `b90f9ff`). Exposes `/psychological_assessment` accepting a query and returning structured fields: `psychological_assessment`, `therapeutic_guidance`, `emotional_support`, `wellbeing_recommendations`, `evidence_based_approaches`. **Phase 3 psychology pre-assessment is now active on every production 9-phase pipeline request** (Chapter 17), including severity classification and crisis indicator check — confirmed in 349.87s end-to-end benchmark. `psychological_rag_domain` confirmed running at **127.0.0.1:8006** (port corrected from 9006 to 8006 as of March 15 containerized deployment). Exposes `/search` and `/add_document` for a curated psychological corpus (968 items: therapy, mindfulness, trauma, depression, anxiety, social support). ChromaDB `psychological_rag` collection confirmed present (port 8000, `chroma_data` Docker volume restored March 15 — previously unavailable due to missing volume mount). PostgreSQL `msjarvis` at **127.0.0.1:5433** (5,416,521 verified GBIM entities, 80 epochs, 206 source layers) as ground truth for validating psychological guidance against West Virginia community context. **BBB 7-filter pipeline** (expanded from 4 to 7 filters as of March 15): `EthicalFilter`, `SpiritualFilter`, `SafetyMonitor` (word-boundary regex fix March 15), `ThreatDetection`, `SteganographyDetection` (March 15), `TruthVerification` (March 15), `ContextAwareness` (March 15) at **0.0.0.0:8016** — functions as Phase 1.4 live gate on every request. `normalize_identity` and `TruthValidator` enforce prohibitions on anthropomorphic claims and identity confusion validated against PostgreSQL `msjarvis` GBIM on every `ultimatechat` response (Chapter 17, Chapter 22). `truthverdict` attached to every `UltimateResponse` with `correct_identity`, `correct_creator`, `relationship_clear` booleans. |
| **Partially implemented / scaffolded** | PIA review loop exists as a structured process that **manually samples logs and introspection outputs, producing written recommendations** — it does **not** auto-rewrite configuration, prompts, or filters. Integration of PIA recommendations back into barrier parameters, judge weights, or mode settings requires explicit operator action. Psychological-guidance-specific `consciousnesslayers` entries appear when `jarvis-psychology-services` is explicitly invoked; they are now consistently produced at Phase 3 of the 9-phase pipeline. Population- and risk-type-specific retrieval tagging (e.g. rural grief, adolescent caregivers) is partially implemented; differential retrieval tuning grounded in PostgreSQL GBIM West Virginia data is future work. |
| **Future work / design intent only** | Automated, scheduled PIA review cycle with machine-readable output format for direct configuration integration. Automated propagation of PIA recommendations into BBB penalty weights, judge instructions, and global mode policies without manual operator step. Persistent introspective log of PIA cycle inputs, analyses, and recommendations as a first-class ChromaDB collection with PostgreSQL audit trail. Population- and risk-type-specific retrieval tuning driving differential guidance validated against PostgreSQL GBIM West Virginia community data. |

> **Cross-reference:** The BBB 7-filter pipeline that enforces safety and ethical constraints validated against PostgreSQL is described in **Chapter 16**. Identity normalization and `TruthValidator` validated against PostgreSQL GBIM are described in **Chapter 22**. The psychological services' relationship to the meaning-oriented track is described in **Chapter 23**. For the canonical 9-phase `ultimatechat` execution sequence see **Chapter 17**.

---

# 29. Psychological Safeguards and the PIA Review Loop

This chapter formalizes how psychological and mental-health knowledge is integrated into Ms. Jarvis to guide interaction patterns, monitor interaction risks, and adapt system behavior over time. In the current deployment (March 15, 2026, commit `b90f9ff`), this is realized through two confirmed running services — `jarvis-psychology-services` (port **8019**, deployed March 15) and `psychological_rag_domain` (port **8006**, containerized March 15) — a curated psychological corpus in ChromaDB (968 items, `psychological_rag` collection, port 8000, `chroma_data` volume restored March 15), validation against PostgreSQL `msjarvis` (port 5433, 5,416,521 GBIM entities) for West Virginia community context, the BBB 7-filter pipeline at port **8016** as the primary live Phase 1.4 safety gate, and a manual PIA review process that produces recommendations rather than automated rewrites.

**Phase 3 psychology pre-assessment is now active on every production 9-phase pipeline request** (confirmed March 15, 2026, 349.87s end-to-end benchmark, all phases approved). Prior to March 15, `jarvis-psychology-services` was unavailable due to missing container builds and the missing ChromaDB `chroma_data` volume. Both services are now confirmed operational.

A critical constraint is that these mechanisms are designed for **supportive, psychoeducational guidance and risk awareness** validated against PostgreSQL community data, not for formal DSM-style diagnosis or clinical decision-making. Clinical constructs are used at a high level only; the system does not reproduce or implement DSM-5 in full and is not a substitute for professional care.

---

## 29.1 Role of Psychological Guidance

In the current deployment, psychological guidance grounded in PostgreSQL `msjarvis` is not treated as an auxiliary feature but as a core constraint on how the system interacts with people, now enforced at Phase 3 of every production 9-phase pipeline request. Its primary functions are threefold.

**Interaction quality.** `jarvis-psychology-services` (port **8019**) provides principled reference points for respectful, non-coercive, and supportive exchanges validated against PostgreSQL GBIM West Virginia community norms. Its `/psychological_assessment` endpoint runs on every production request and returns structured responses: `therapeutic_guidance`, `emotional_support`, `wellbeing_recommendations`, and `evidence_based_approaches`. `psychological_rag_domain` (port **8006**) provides retrieval of curated materials — therapy, mindfulness, trauma, depression, anxiety, and social-support content (968 items) — via `/search`, backed by the ChromaDB `psychological_rag` collection (port 8000, `chroma_data` volume). These materials are curated for high-level, evidence-informed guidance validated against PostgreSQL community context; they are not used to perform formal diagnosis.

**Risk awareness.** `TruthValidator` (applied on every response via `jarvis-main-brain`, port **8050**) encodes patterns known to be harmful — identity confusion, anthropomorphic overclaiming, misleading statements about agency and embodiment — validated against PostgreSQL `msjarvis` GBIM ground truth and returns `correct_identity`, `correct_creator`, and `relationship_clear` booleans. The BBB 7-filter Phase 1.4 stack at port **8016** screens for content violating ethical or community-safety constraints including high-risk mental-health content. The SafetyMonitor word-boundary regex fix deployed March 15 eliminates false-positives on community resource terms while maintaining protection for genuine risk patterns.

**Self-checking.** `normalize_identity` applied to every `ultimatechat` response rewrites outputs that deviate from allowed self-descriptions validated against PostgreSQL GBIM or blur human-machine boundaries, before the response is returned to the caller. Together with the BBB 7-filter pipeline, this prevents the system from presenting itself as a clinician, therapist, or human agent.

---

## 29.2 Organization of the Guidance Corpus

In the current deployment, psychological guidance materials are curated in the `psychological_rag` collection within ChromaDB (**127.0.0.1:8000**, `chroma_data` Docker volume, restored March 15) and served via `psychological_rag_domain` (**127.0.0.1:8006**, confirmed running March 15), with validation against PostgreSQL `msjarvis` for West Virginia community context.

**Corpus content (968 items, verified March 15).** `psychological_rag_domain` holds a curated corpus on topics including therapy, mindfulness, trauma, depression, anxiety, and social support, validated against PostgreSQL GBIM for appropriateness to Appalachian community contexts. `jarvis-psychology-services` uses this corpus to identify patterns such as anxiety, depression, stress, grief, and trauma, pulling evidence-based snippets via RAG to generate structured responses. The corpus is logically distinct from general reference and technical knowledge, making its normative and clinical role explicit and allowing it to be governed and updated separately with PostgreSQL validation. Community-validated resource data from `jarvis-local-resources-db` (port 5435) — including resources validated by Harmony for Hope Community Champions such as lead validator Crystal Colyer — is also eligible for inclusion in the psychological guidance corpus where relevant to Appalachian mental health support. Where DSM-style constructs appear, they do so at the level of paraphrased, high-level concepts rather than verbatim manual text.

**Tagging and retrieval.** The design intends that items will be tagged with theme (e.g. "trauma-informed care," "addictive dynamics"), population (e.g. adolescents, caregivers, rural Appalachian communities from PostgreSQL GBIM), and risk type (e.g. self-harm risk, identity confusion, dependency) to support targeted retrieval validated against PostgreSQL community data. In the current deployment, tagging is partially implemented; `/search` on `psychological_rag_domain` supports query-based retrieval against the 968-item corpus, and population- and risk-type-specific differential retrieval tuning grounded in PostgreSQL GBIM West Virginia data is identified as future work.

---

## 29.3 Use During Live Interactions — 9-Phase Pipeline Integration

In the current deployment (March 15, 2026), psychological safeguards validated against PostgreSQL `msjarvis` are active at multiple phases of the 9-phase production pipeline (Chapter 17).

**Phase 1.4 — BBB 7-filter input stack.** Before any content reaches the psychological assessment or LLM synthesis phases, the request passes through all 7 BBB filters (port 8016): `EthicalFilter`, `SpiritualFilter`, `SafetyMonitor` (word-boundary regex fixed March 15), `ThreatDetection`, `SteganographyDetection`, `TruthVerification`, and `ContextAwareness`. This is the primary live gate for psychologically sensitive content, validated against PostgreSQL `msjarvis` GBIM ground truth.

**Phase 3 — Psychology pre-assessment (deployed March 15, now always active).** Every production request passes through `jarvis-psychology-services` (port 8019) via `/psychological_assessment`. This service provides:
- Severity classification (mild / moderate / severe)
- Crisis indicator check (Boolean flag for immediate risk)
- `therapeutic_guidance`: evidence-based approaches relevant to detected patterns
- `emotional_support`: supportive language recommendations
- `wellbeing_recommendations`: actionable, non-diagnostic suggestions
- `evidence_based_approaches`: specific evidence-informed frameworks

Phase 3 output feeds the LM Synthesizer (Phase 3.5, port 8001), which incorporates psychological context alongside GBIM RAG, PostGIS spatial data, and community resource data before passing enriched context to the 22-model ensemble (Phase 2.5).

**Phase 4 — Psychological RAG context building.** `jarvis-spiritual-rag` (port 8005) queries `psychological_rag_domain` (port 8006) as one of its RAG sources during Phase 4 context building, retrieving relevant entries from the 968-item `psychological_rag` ChromaDB collection (port 8000). This psychological RAG context is combined with GBIM beliefs (PostgreSQL `msjarvis`, port 5433), PostGIS spatial data (`gisdb`, port 5433), and community resources (`jarvis-local-resources-db`, port 5435) into the unified context block.

**Phase 4.5 — BBB output guard.** After the 22-model ensemble and 69-DGM cascade, `apply_output_guards_async` passes the response through BBB `/filter` (port 8016, 8.0s timeout), applying psychological content filtering to the generated output before delivery.

**Post-processing — identity normalization.** `normalize_identity` ensures the final response speaks as Ms. Egeria Jarvis, not as a clinician or therapist. `TruthValidator` verifies `correct_identity`, `correct_creator`, and `relationship_clear` booleans validated against PostgreSQL `msjarvis` GBIM.

---

## 29.4 The PIA Review Loop

In the current deployment, the Psychology-Informed Alignment (PIA) review loop exists as a structured **manual process** that samples logs and introspection outputs validated against PostgreSQL `msjarvis`, producing written recommendations — **not auto-rewrites of configuration, prompts, or filters**.

**Inputs and scope.** PIA review operates by manually sampling:
- Recent interaction logs and `ms_jarvis_memory` entries (ChromaDB, confirmed written after every `/chat` call via `background_rag_store`; Chapter 17 §17.6)
- `truthverdict` fields from `UltimateResponse` (`correct_identity`, `correct_creator`, `relationship_clear`) validated against PostgreSQL `msjarvis` GBIM
- BBB `barrier_stats` counters (total_filtered, total_blocked, pass_rate) from the 7-filter pipeline
- Phase 3 outputs from `jarvis-psychology-services` (severity classifications, crisis flags)
- `psychological_rag_domain` `/search` usage patterns against the 968-item corpus
- `confidence_decay` values from GBIM temporal metadata (Phase 5) for entities underlying psychological resource recommendations

Automated, scheduled sampling is identified as future work.

**Analysis.** The PIA review examines recurring patterns in system behavior validated against PostgreSQL GBIM — recurring `truthverdict` violations, BBB 7-filter block-rate trends, identity-confusion patterns in `TruthValidator` outputs, underuse of psychological guidance in sensitive interaction categories, and crisis indicator detection rates from Phase 3. Some classification of patterns is still heuristic; fully automated pattern-detection is identified as future work. Clinical frameworks such as DSM-style nosology inform human reviewers' judgments at this stage but are not implemented as automatic diagnostic pipelines.

**Outputs and recommendations.** The PIA review loop produces structured **written recommendations** such as:
- "Tighten identity phrasing constraints validated against PostgreSQL in crisis-related dialogues"
- "Introduce explicit boundary statements for maternal metaphors"
- "Increase Phase 3 severity threshold for economic-stress queries common in Appalachian community contexts"
- "Add to `psychological_rag` corpus: rural grief resources validated against Fayette County community data from `jarvis-local-resources-db`"
- "Review `confidence_decay` for DHHR mental health service entities (currently `needs_verification=TRUE`)"

These are human-interpretable and require explicit operator action to implement — they do not automatically rewrite BBB parameters, judge instructions, or global mode policies. Machine-readable output format and automated propagation are identified as future work.

---

## 29.5 Integration with Barriers, Modes, and Judge Components

In the current deployment, PIA recommendations can be applied to several confirmed control surfaces validated against PostgreSQL `msjarvis`, but application requires explicit operator action.

**Barrier and filter adjustments.** BBB 7-filter pipeline at port **8016** exposes rule sets validated against PostgreSQL GBIM that can be updated in response to PIA findings. The SafetyMonitor word-boundary regex fix deployed March 15 is an example of a PIA-informed adjustment: eliminating false-positives on community resource terms (e.g. "crisis center," "domestic violence shelter") that were previously triggering the SafetyMonitor incorrectly. In the current deployment, updates to filter parameters validated against PostgreSQL remain manual.

**Global mode settings.** The design intends that PIA outputs will modify mode selection policies validated against PostgreSQL GBIM — for instance, enforcing more cautious orchestration modes for certain user cohorts or topics if recent behavior indicates elevated psychological risk. In the current deployment, mode settings are adjusted by operators following PIA review rather than by automated policy updates.

**Evaluator and judge behavior.** Judge services (7230–7233, confirmed running) can receive updated instructions reflecting refined psychological guidance validated against PostgreSQL — for example, stronger penalties for overconfident advice in clinical domains or for failure to recommend professional help when appropriate. In the current deployment, these updates are applied manually following PIA recommendations. The design intends that future configurations will give judges direct access to `psychological_rag_domain` outputs (968-item corpus) validated against PostgreSQL and PIA summaries as explicit scoring dimensions.

**69-DGM cascade integration.** The 69-DGM cascade (`jarvis-69dgm-bridge`, port 9000, 23 connectors × 3 stages) at Phase 7 provides an additional validation layer for psychologically sensitive responses. 69-DGM verdicts are architecturally authoritative and grounded in PostgreSQL `msjarvis` GBIM beliefs; future PIA recommendations may target specific DGM connector configurations relevant to psychological safety.

---

## 29.6 Recording, Memory, and Accountability

In the current deployment, psychological safeguards are recorded through several confirmed mechanisms with PostgreSQL-auditable trails.

**`ms_jarvis_memory` and interaction logs.** Every `/chat` response produces a `bg_<ISO8601>` entry in `ms_jarvis_memory` ChromaDB (port 8000, `chroma_data` volume; Chapter 17 §17.6), with `truthverdict` fields recording BBB 7-filter judgments validated against PostgreSQL GBIM including ethics violations and crisis flag triggers. These entries are the primary raw material for PIA sampling. BBB `barrier_stats` counters provide aggregate counts of filter interventions across all 7 filters, including those triggered by psychologically sensitive content.

**Phase 3 assessment records.** Every production request now generates a Phase 3 psychology pre-assessment record from `jarvis-psychology-services` (port 8019) — severity classification, crisis indicator Boolean, and five structured guidance fields. These records are included in `consciousnesslayers` of the `UltimateResponse` and are available for PIA sampling. The March 15 deployment means this is the first date from which a complete longitudinal Phase 3 assessment record exists.

**PIA review records.** Each manual PIA review cycle produces a written record of inputs sampled, patterns observed validated against PostgreSQL GBIM, and recommendations proposed. The design intends these records will be written into a dedicated ChromaDB collection as timestamped introspective artifacts tagged as psychological-alignment entries with PostgreSQL audit trail. In the current deployment, these records are maintained as manually produced documents rather than automatically ingested into ChromaDB.

**Human oversight and governance.** PIA review outputs are explicitly designed for inspection by human reviewers including domain experts, ethicists, and community governance bodies, with all validations traceable to PostgreSQL `msjarvis` GBIM ground truth. This material supports questions such as: "Has the system systematically improved in handling crisis-adjacent queries?", "Where have psychological safeguards validated against PostgreSQL been relaxed or tightened?", "Do the recorded mitigations align with declared community norms anchored in PostgreSQL GBIM?", and "Are DHHR and mental health service entities in `jarvis-local-resources-db` being confirmed through the POC verification loop promptly?" The design treats psychological risk as a first-class governance concern, on par with technical reliability and knowledge integrity. DSM-style frameworks inform human oversight here as reference points, but automated behavior remains conservative and non-diagnostic.

---

## 29.7 Summary

In the current deployment (March 15, 2026, commit `b90f9ff`), psychological safeguards are realized through two confirmed running services — `jarvis-psychology-services` (**127.0.0.1:8019**, deployed March 15) and `psychological_rag_domain` (**127.0.0.1:8006**, containerized March 15) — a curated psychological corpus in ChromaDB (**127.0.0.1:8000**, `chroma_data` volume, 968 items in `psychological_rag` collection), validation against PostgreSQL `msjarvis` (port 5433, 5,416,521 GBIM entities) for West Virginia community context, the BBB 7-filter pipeline at **0.0.0.0:8016** as the primary Phase 1.4 live safety gate, and `normalize_identity` plus `TruthValidator` validated against PostgreSQL applied to every `ultimatechat` response.

**Key operational facts as of March 15, 2026:**
- Phase 3 psychology pre-assessment is now **active on every production 9-phase pipeline request** (confirmed in 349.87s end-to-end benchmark)
- BBB has expanded from 4 filters to **7 filters** (SteganographyDetection, TruthVerification, ContextAwareness added March 15)
- SafetyMonitor word-boundary regex fixed March 15 — eliminates false-positives on community resource terms
- `psychological_rag_domain` port is **8006** (not 9006 — corrected in March 15 containerized deployment)
- ChromaDB `psychological_rag` collection previously unavailable; now accessible via `chroma_data` Docker volume

**Two important constraints** must be stated clearly: the PIA review loop **produces written recommendations through a manual sampling process validated against PostgreSQL**, not auto-rewrites; and propagation of PIA recommendations into BBB parameters, judge weights, or mode policies requires explicit operator action. The psychological guidance stack is explicitly **non-diagnostic**: it does not implement DSM-5 in full, and any DSM-style constructs are used only at a high-level, psychoeducational layer validated against PostgreSQL community data rather than as clinical criteria.

The design intends that future work will automate the PIA sampling cycle with PostgreSQL-auditable output, produce machine-readable recommendation outputs for direct configuration integration, persist PIA records as a first-class ChromaDB collection with PostgreSQL audit trail for ongoing governance review, and refine corpus curation and tagging so that place-specific and population-specific mental-health materials grounded in Appalachian contexts via PostgreSQL GBIM are more systematically retrieved while maintaining clear boundaries between supportive guidance and clinical diagnosis. For the BBB 7-filter pipeline that enforces safety constraints validated against PostgreSQL see **Chapter 16**. For the identity constraints enforced alongside psychological safeguards validated against PostgreSQL see **Chapter 22**. For the canonical 9-phase `ultimatechat` execution sequence see **Chapter 17**. For ChromaDB `psychological_rag` collection architecture see **Chapter 5**.

*Last updated: 2026-03-15 19:16 EDT by Carrie Kidd, Oak Hill WV*
