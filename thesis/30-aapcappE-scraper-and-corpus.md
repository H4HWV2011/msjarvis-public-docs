# 30. AAPCAppE Scraper and Appalachian English Corpus Integration

This chapter describes the scraper, seed corpus, and planned processing pipeline for bringing Appalachian English into the system as a first-class variety. The immediate implementation centers on a small, manually seeded corpus (`appalachian_english_corpus`) and a general-purpose AaaCPE scraper service, while the longer-term roadmap is to integrate the Audio-Aligned and Parsed Corpus of Appalachian English (AAPCAppE) as an authoritative source.

## 30.1 Purpose of the AAPCAppE Integration

The AAPCAppE integration is meant to move Appalachian English from ad hoc prompts and stereotypes into a documented, corpus-informed layer of the system.

- Authentic language modeling  
  - Provide empirically grounded examples of Appalachian English as it is actually used, supporting recognition and generation that respect its phonology, morphosyntax, and lexicon.  
  - Reduce reliance on generalized U.S. English assumptions by incorporating dialect-specific evidence into the linguistic layer.

- Contextual understanding  
  - Link dialect forms to locations, speakers, and interactional settings, improving interpretation of narratives, oral histories, and community discourse.  
  - Support analysis of how local forms encode stance, identity, and relationships across different Appalachian communities.

- Communication quality  
  - Avoid treating systematic dialect features (for example, a‑prefixing, double modals, negative concord) as “errors” to be corrected.  
  - Highlight where institutional or bureaucratic phrasing diverges from local norms, suggesting rephrasings or parallel explanations when appropriate.

These goals apply both to the current seed corpus and to the future, richer AAPCAppE-based integration.

## 30.2 Target Corpus: Current State vs Roadmap

The system distinguishes between the current seed implementation and the future AAPCAppE-backed integration.

- Current seed implementation  
  - A Chroma collection named `appalachian_english_corpus` holds a small, hand-curated set of Appalachian English material.  
  - Its contents include:
    - A short internal knowledge file (`AaaCPE_Appalachian_Dialect_Knowledge.txt`) tagged as `source: "AAPCAppE_seed"` and `variety: "Appalachian English"`.  
    - A single illustrative conversational chunk labeled `source: "AaaCPE_community_v1"` with features such as `a_prefixing` and `double_modals`, and metadata placeholders for `speaker_region`, `recording_year`, and `project`.  
    - A larger number of internal prompt and configuration lines tagged `source: "MsJarvis_internal"` that associate the label “Appalachian English” with various system prompts and documents.  
  - No records in this collection are currently fetched from live AAPCAppE endpoints; it functions as a bootstrap and test corpus.

- Future AAPCAppE integration  
  - The Audio-Aligned and Parsed Corpus of Appalachian English (AAPCAppE) is the intended primary external source: a roughly one-million-word corpus of time-aligned and syntactically parsed speech.  
  - In the target design, AAPCAppE-derived material will be ingested from documented APIs or export mechanisms, in accordance with the project’s user agreement and citation policies.  
  - The long-term aim is for AAPCAppE (and closely related, licensed subcorpora) to provide the main empirical backbone for Appalachian English usage, with the current seed corpus retained as a small, high-trust supplement.

## 30.3 Scraper Operation and Scheduling

At present, there is no dedicated AAPCAppE scraper in production; instead there is a general AaaCPE scraper service and manual seed loading.

- Current AaaCPE scraper  
  - The `aaacpe_scraper_service` is a FastAPI-based service that scrapes configured web sources and forwards content into a generic retrieval-augmented generation (RAG) server.  
  - Its configured sources include:
    - A MountainShares blog and other project-related websites.  
    - Regional news outlets and rural technology/news sites.  
    - AI research feeds (for example, recent arXiv lists).  
  - The scraper runs on a scheduled basis using an internal scheduler, but it is currently oriented toward general knowledge updates, not specifically toward dialect corpora or AAPCAppE.

- Seed loading  
  - The `appalachian_english_corpus` collection is populated via one-time or ad hoc loading scripts that:
    - Embed the `AaaCPE_Appalachian_Dialect_Knowledge.txt` seed file as multiple chunks.  
    - Insert a single test record from `test_local_aacpe.txt` labeled `AaaCPE_community_v1`, containing a conversational example with double modals and a‑prefixing.  
    - Add various internal prompt or configuration lines labeled as Appalachian English to tie system prompts into the dialect-aware layer.  
  - These operations are not currently scheduled; updates to the seed corpus are manual.

- Future AAPCAppE scraping and scheduling  
  - A dedicated AAPCAppE scraper will be introduced as a separate service or configuration profile, distinct from the general AaaCPE web scraper.  
  - This scraper will:
    - Poll AAPCAppE-provided endpoints or regularly updated export files on a fixed schedule compatible with licensing and load policies.  
    - Retrieve transcripts, time alignments, and parsed annotations, and pass them to the normalization layer.  
  - Each scraping run will log:
    - The specific AAPCAppE resources accessed.  
    - Counts of records added, updated, or skipped.  
    - Any access, parsing, or policy-related errors.  
  - This will allow maintainers to track how the internal Appalachian English corpus evolves over time and to audit any changes.

## 30.4 Normalization and Record Structure

The documentation distinguishes between the existing seed record format and the richer target schema for AAPCAppE-derived data.

- Current seed record format  
  - Seed entries in `appalachian_english_corpus` store text chunks with relatively simple metadata:
    - `source` (for example, `"AAPCAppE_seed"`, `"AaaCPE_community_v1"`, `"MsJarvis_internal"`).  
    - `file` (for example, `AaaCPE_Appalachian_Dialect_Knowledge.txt`, `test_local_aacpe.txt`, or internal service file paths).  
    - `variety: "Appalachian English"`.  
    - `chunk_index` (an integer indicating the chunk’s order within a file).  
  - The single conversational example extends this with:
    - `register` (for example, `"conversation"`).  
    - `features` (for example, `"a_prefixing,double_modals"`).  
    - `speaker_region`, `recording_year`, and `project`, currently populated with placeholder values (such as `TBD_region`).  
  - The seed schema suffices for basic retrieval tests and experimentation, but does not yet encode full corpus identifiers, alignment pointers, or detailed sociolinguistic metadata.

- Target AAPCAppE record schema  
  - When integrating real AAPCAppE data, each normalized record is expected to include:
    - Core fields:
      - An internal record ID.  
      - The original AAPCAppE token, sentence, or utterance ID as a reference back into the corpus.  
      - An Appalachian English text segment (token, sentence, or utterance).  
      - Retrieval and source-update timestamps.  
    - Annotation fields:
      - References to audio alignment data (for example, audio file path and start/end timecodes).  
      - Speaker metadata (pseudonymous speaker ID, subcorpus label, region, age or age group, recording period), consistent with AAPCAppE’s documentation.  
      - Linguistic annotations from the parsed corpus (part-of-speech tags, syntactic parses, and other available layers).  
      - Notes about recording conditions, genre, and interaction type when provided.  
    - Derived tags:
      - Region or subregion labels inferred from corpus metadata (for example, specific counties or communities).  
      - Interactional setting (for example, interview, casual conversation, storytelling).  
      - Document or discourse type (for example, narrative, discussion of work, church-related talk).
  - Existing seed records are treated as a subset of this schema and can later be backfilled or adjusted so that all dialect records share a coherent structure.

## 30.5 Integration with Memory, Spatial, and Belief Layers

Once normalized, dialect records are integrated with the broader memory and reasoning layers, with a clear distinction between the current seed state and the planned AAPCAppE-backed future.

- Current semantic memory state  
  - The Chroma collection `appalachian_english_corpus` is present and actively used in tests and development utilities.  
  - The collection currently contains:
    - A small number of seed knowledge chunks and one conversational AaaCPE example.  
    - A larger set of internal lines that mark prompts and documents as Appalachian English.  
  - This collection acts as a focused semantic memory node for dialect-aware retrieval, but does not yet reflect the breadth of a full corpus.

- Planned semantic memory integration for AAPCAppE  
  - A dedicated collection (for example, `appalachian_english_aapcappe`) will be introduced for embeddings derived directly from AAPCAppE.  
  - For each embedded record, metadata will include:
    - `corpus_origin = "AAPCAppE"`.  
    - Subcorpus identifiers corresponding to specific data sets within AAPCAppE.  
    - Region, register, and relevant linguistic attributes (for example, presence of a-prefixing, double modals, or other features).  
  - Retrieval components will be updated so that:
    - Queries mentioning Appalachian English or characteristic constructions can preferentially draw from AAPCAppE-backed examples.  
    - Existing tests that query `appalachian_english_corpus` can be redirected or extended to cover the new collection without breaking compatibility.

- Spatial backbone linkage  
  - In the seed state, spatial linkage is minimal; some records include a placeholder `speaker_region` but are not fully wired into the spatial backbone.  
  - With AAPCAppE integration:
    - Subcorpora and speaker location metadata will be mapped to geospatial entities such as counties, communities, and regions in Appalachia.  
    - This will support queries and reasoning that connect language usage to place (for example, patterns in specific valleys, towns, or regions).  
    - Spatial tags can also help in visualizing variation across the corpus.

- Belief and concept structures  
  - The seed corpus already introduces some concepts, such as typical expressions, values, and cultural frames, but in a limited way.  
  - AAPCAppE integration will allow:
    - Extraction of entities, relationships, and recurring themes in Appalachian English discourse (for example, work, church, family, local institutions).  
    - Connection of dialectal expressions to their referents in belief graphs, so that reasoning can account for local terminology and metaphor.  
    - Careful representation of how language indexes identity, stance, and social structure without reducing these patterns to stereotypes.

## 30.6 Use in Understanding and Generation

Both the seed corpus and the future AAPCAppE integration play roles in understanding and generation, but with different levels of authority and coverage.

- Current seed usage  
  - Retrieval tests (such as those that query “might could head up the holler”) verify that the system can surface clearly Appalachian phrases from `appalachian_english_corpus`.  
  - Feature tests check that constructions like double modals and a‑prefixing can be retrieved and recognized as features of Appalachian English, not as random noise.  
  - Internal prompts labeled as Appalachian English help ensure that system personas and evaluators do not frame these features as incorrect when the context calls for dialect authenticity.  
  - The small size and handcrafted nature of the seed corpus means it is treated as illustrative rather than statistically representative.

- Planned AAPCAppE-backed usage  
  - Understanding:
    - Retrieval pipelines will use AAPCAppE-based embeddings to disambiguate dialect-specific constructions and lexical items across a wide variety of naturally occurring contexts.  
    - Evaluators will incorporate distributional information from AAPCAppE (for example, where a feature is common, restricted, or rare) when interpreting user input or deciding how to flag forms.  
  - Generation:
    - In contexts where it is appropriate to respond in Appalachian English, generation modules will condition on AAPCAppE-informed patterns of syntax, collocation, and rhythm.  
    - The system will avoid overusing or mixing dialect features in ways that are not supported by the corpus, reducing the risk of caricature.  
    - For institutional or cross-community contexts, the system may generate parallel versions of a message: one in a more institutional register and one that leans more into Appalachian English norms, while clearly indicating the intended audience of each.  
  - Mediation with institutional language:
    - AAPCAppE-informed patterns can highlight where institutional or bureaucratic phrasing differs sharply from local norms in length, formality, or structure.  
    - Evaluators can then suggest or apply rephrasings that respect both the institutional requirements and the lived language of Appalachian communities.

## 30.7 Safeguards and Governance

Using any dialect-linked corpus requires explicit safeguards and ongoing governance to avoid misuse and stereotyping.

- Source and barrier treatment  
  - AAPCAppE and any related endpoints will be treated as policy-recognized sources with documented provenance, licensing, and usage constraints.  
  - Even when a source is high trust, content will still pass through privacy, safety, and appropriateness checks.  
  - Seed and AAPCAppE-derived records alike will be handled with attention to potential identifiability of speakers and communities, including redaction or exclusion rules where necessary.

- Documentation and transparency  
  - The role of the seed corpus and the AAPCAppE integration will be documented for collaborators, including:
    - What data is included and what is excluded.  
    - How it is normalized, stored, and tagged.  
    - How it can influence understanding and generation.  
  - Documentation will emphasize that Appalachian English is treated as a systematic variety with its own norms, not as an errorful deviation from another standard.

- Community engagement and feedback  
  - Summaries of how dialect patterns influence system behavior can be shared with community partners, linguists, and educators.  
  - Feedback channels will allow community stakeholders to:
    - Flag outputs that feel inauthentic, stigmatizing, or otherwise problematic.  
    - Request changes to how certain constructions are used in sensitive contexts.  
    - Suggest additional areas where Appalachian English should be foregrounded or, conversely, where a more neutral variety is preferable.  
  - As the AAPCAppE integration matures, governance practices will be revisited to ensure they align with project agreements and community expectations.

## 30.8 Summary

The AAPCAppE scraper and corpus integration are conceived as a two-stage process: an initial seed implementation centered on a small handcrafted corpus, and a future, higher-fidelity integration with the Audio-Aligned and Parsed Corpus of Appalachian English. By clearly separating current behavior from roadmap commitments, defining a richer normalization schema, and tying dialect records into semantic, spatial, and belief layers, the system positions Appalachian English as a systematic, respected variety in both understanding and communication. Safeguards, documentation, and ongoing community engagement are integral to ensuring that this integration supports Appalachian voices without exploitation or stereotype.
