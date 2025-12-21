## 30.2 Target Corpus: Current State vs Roadmap

The system distinguishes between the **current seed implementation** and the **future AAPCAppE-backed integration**.

- Current seed implementation:
  - A Chroma collection named `appalachian_english_corpus` contains a small, hand-curated seed set of Appalachian English material.
  - Its contents include:
    - A short internal knowledge file (`AaaCPE_Appalachian_Dialect_Knowledge.txt`) tagged as `source: "AAPCAppE_seed"` and `variety: "Appalachian English"`.
    - A single illustrative conversational chunk labeled `source: "AaaCPE_community_v1"` with features such as `a_prefixing` and `double_modals`.
    - Additional internal prompt and configuration lines tagged `source: "MsJarvis_internal"` to anchor usage of the label “Appalachian English.”
  - No records in this collection are currently fetched from live AAPCAppE endpoints.

- Future AAPCAppE integration:
  - The Audio-Aligned and Parsed Corpus of Appalachian English (AAPCAppE) is the planned primary source, a one-million-word corpus of time-aligned and parsed Appalachian English speech hosted at the AAPCAppE site.
  - When implemented, AAPCAppE-derived material will be ingested from documented APIs or export mechanisms under the project’s user agreement and citation requirements.
  - The long-term goal is to treat AAPCAppE and tightly related, licensed subcorpora as the authoritative backbone for Appalachian English usage, with the current seed corpus serving only as a bootstrap layer.

---

## 30.3 Scraper Operation and Scheduling

At present, there is **no dedicated AAPCAppE scraper in production**; instead there is a general AaaCPE scraper service and manual seed loading.

- Current AaaCPE scraper:
  - The `aaacpe_scraper_service` is a FastAPI-based service that scrapes configured web sources (such as community blogs and news outlets) and forwards content to a generic RAG server.
  - Its configuration currently lists sources like a MountainShares blog, regional news, and AI research feeds, not AAPCAppE endpoints.
  - The service is wired for scheduled scraping (via an internal scheduler) but does not yet target or label dialect corpora specifically.

- Seed loading:
  - The current `appalachian_english_corpus` collection is populated via one-time or ad hoc loading scripts that embed:
    - The `AaaCPE_Appalachian_Dialect_Knowledge.txt` seed file.
    - A small number of internal prompt lines referring to Appalachian English.
    - A single test record labeled `AaaCPE_community_v1` for feature-based retrieval tests.
  - No periodic job is yet responsible for refreshing or expanding this Appalachian corpus.

- Future AAPCAppE scraping and scheduling:
  - A dedicated AAPCAppE scraper will be introduced as a separate service or configuration profile:
    - It will poll AAPCAppE-provided endpoints or export files on a fixed schedule compatible with project policies.
    - It will retrieve transcripts, time alignments, and parsed annotations, and normalize them into the internal record format described below.
  - Each run will log contacted endpoints, items retrieved, and any errors, so that the growth of the Appalachian English collection can be monitored over time.

---

## 30.4 Normalization and Record Structure

The documentation distinguishes between the **existing seed record format** and the **richer target schema for AAPCAppE data**.

- Current seed record format:
  - Seed entries in `appalachian_english_corpus` store text chunks with minimal metadata:
    - `source` (for example, `"AAPCAppE_seed"`, `"AaaCPE_community_v1"`, `"MsJarvis_internal"`).
    - `file` (for example, `AaaCPE_Appalachian_Dialect_Knowledge.txt`, `test_local_aacpe.txt`).
    - `variety: "Appalachian English"`.
    - `chunk_index` (integer chunk ordering within a file).
  - One illustrative conversational record adds additional fields:
    - `register` (for example, `"conversation"`).
    - `features` (for example, `"a_prefixing,double_modals"`).
    - `speaker_region`, `recording_year`, and `project`, currently placeholders (`TBD_region`, `TBD_year`, `TBD_project_name`).
  - These fields are sufficient for feature-based tests, but do not yet encode full corpus identifiers, alignment, or speaker demographics.

- Target AAPCAppE record schema:
  - When integrating real AAPCAppE data, each normalized record is expected to include:
    - Core fields:
      - An internal record ID and the original AAPCAppE token or sentence identifier.
      - An Appalachian English text segment (token, sentence, or utterance).
      - Retrieval and source-update timestamps.
    - Annotation fields:
      - Pointers to AAPCAppE alignment data (timecodes, audio file references).
      - Speaker metadata (pseudonymous ID, subcorpus label, region, age or age group, recording period), consistent with AAPCAppE documentation.
      - Syntactic and morphological annotations from the parsed corpus.
    - Derived tags:
      - Region, conversational setting, and document type, inferred from subcorpus and metadata where permitted by licensing.
  - The existing seed records are considered a subset of this schema and will be migrated or backfilled as needed once the AAPCAppE pipeline is live.

---

## 30.5 Integration with Memory, Spatial, and Belief Layers

The integration plan again distinguishes between the current seed state and the intended AAPCAppE-backed future.

- Current semantic memory state:
  - The Chroma collection `appalachian_english_corpus` is already present and used by local tests to retrieve examples with Appalachian features such as “might could” and “holler.”
  - Most entries are tagged as `source: "MsJarvis_internal"` or `"AAPCAppE_seed"` and act as a small, high-trust seed set for dialect-aware prompts and experiments.
  - There is currently no separate collection explicitly named for AAPCAppE, and all dialect-related material is consolidated under this single collection.

- Planned semantic memory integration for AAPCAppE:
  - A dedicated collection (for example, `appalachian_english_aapcappe`) will store embeddings for AAPCAppE-derived records, with metadata fields including:
    - `corpus_origin = "AAPCAppE"`.
    - `subcorpus` (for example, specific recording projects within AAPCAppE).
    - `region`, `register`, and key linguistic attributes.
  - Retrieval pipelines will be updated so that:
    - Dialect-aware understanding and generation can explicitly favor AAPCAppE-backed examples when Appalachian English is relevant.
    - Tests that currently query `appalachian_english_corpus` can be redirected or extended to cover the richer collection.

- Spatial and belief-layer linkage:
  - Seed records may carry coarse regional tags (`speaker_region`) but these are currently placeholders and not wired into the spatial backbone.
  - AAPCAppE integration will:
    - Map subcorpora and documented locations to geospatial entities (counties, communities, institutions) where consistent with project policies.
    - Feed recurrent entities and relationships from AAPCAppE into belief graphs, emphasizing community life, institutions, and recurring themes in Appalachian English discourse.

---

## 30.6 Use in Understanding and Generation

Both the seed corpus and the future AAPCAppE integration play roles in understanding and generation, but with different levels of authority.

- Current seed usage:
  - Retrieval tests (for example, `test_aapcappe_retrieval.py` and `test_aacpe_features.py`) query `appalachian_english_corpus` to ensure that phrases like “might could” and “a‑going” can be surfaced and recognized as legitimate features of Appalachian English.
  - Internal prompts and configuration lines tagged as `Appalachian English` help guard against treating dialectal forms as errors in system personas and evaluators.
  - The single `AaaCPE_community_v1` example provides a concrete, conversational instance for early tuning and debugging, but is not treated as statistically representative of the dialect.

- Planned AAPCAppE-backed usage:
  - Understanding:
    - Retrieval will leverage AAPCAppE-derived embeddings to disambiguate dialect-specific constructions across a broader range of contexts, grounded in documented usage.
    - Evaluators will incorporate frequency and distributional patterns from AAPCAppE when deciding whether a form is dialectal, stylistic, or truly anomalous.
  - Generation:
    - When context and role permit, generation components will condition on AAPCAppE-informed patterns (for example, rhythm, preferred constructions) to produce Appalachian English that reflects attested usage rather than stereotypes.
    - Corpus-backed constraints will help avoid mixing features that do not co-occur in real speakers or overusing marked forms in sensitive contexts.
  - Mediation with institutional language:
    - As with the seed, AAPCAppE-based statistics will support detection of points where institutional or bureaucratic phrasing diverges markedly from local norms, suggesting parallel paraphrases or additional explanation.
