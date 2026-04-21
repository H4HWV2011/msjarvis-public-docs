# Chapter 30 — AAPCappE Scraper and Corpus

**Carrie Kidd (Mamma Kidd) · Mount Hope, WV**  
**Last updated: ★★★★ April 6, 2026 — FINAL REWRITE**

**105/105 containers Up (zero Restarting, zero Exited). AAPCappE scraper and corpus handling are documented as part of Ms. Allis’s data pipeline, with explicit constraints for ethical scraping, Appalachian focus, and survivor-safe content curation. 

---

## 30.1 Purpose of AAPCappE in Ms. Allis

The **AAPCappE scraper and corpus** are designed to:

- Collect public, ethically accessible data relevant to:
  - Appalachian communities,
  - Policy and governance,
  - Poverty, health, environment, and infrastructure,
- Provide Ms. Allis with:
  - Better context for answering questions,
  - Evidence for `rag_grounded_v2` and judge pipeline decisions,
  - Material for identifying structural patterns in Appalachian life.

AAPCappE is:

- **Not** a generic web crawler,
- **Not** a surveillance tool,
- A **focused, purpose-built pipeline** for Appalachian public content that is explicitly allowed for research and stewardship use.

---

## 30.2 Ethical Scraping Principles

AAPCappE follows these principles:

1. **Respect for robots.txt and site policies**:
   - Do not scrape sites that disallow bots or research use.
2. **No scraping behind logins or paywalls**:
   - Avoid personal data and gated content.
3. **Rate-limiting and politeness**:
   - Avoid harming site performance,
   - Use backoffs and maximum request limits.
4. **Transparency and traceability**:
   - Keep records of:
     - URLs scraped,
     - Timestamps,
     - Parsing decisions.
5. **Survivor safety and spiritual sensitivity**:
   - Avoid:
     - Personal trauma narratives that are not clearly intended for public analysis,
     - Content that could be used to re-identify or retraumatize individuals.

These constraints are encoded in:

- Scraper configuration,
- Corpus filters,
- Downstream RAG and GBIM ingestion rules.

---

## 30.3 Scraper Architecture

The AAPCappE scraper:

- Runs as a set of scripts and/or services that:

  - Accept:
    - URL lists,
    - Domain-focused configurations,
    - Query parameters.
  - Output:
    - Cleaned text,
    - Metadata (title, date, author when available),
    - Source tags (e.g., “policy report”, “news article”, “community story”).

- Integrates with Ms. Allis’s infrastructure via:

  - **RAG ingestion**:
    - Parsed content can be sent into:
      - ChromaDB collections,
      - Specific RAG services (`allis-gis-rag`, `allis-spiritual-rag`, others).
  - **GBIM ingestion**:
    - High-value structured insights (e.g., “this county has X% poverty”) may be converted into GBIM entities with `confidence_decay` metadata.

The scraper is designed to be:

- **Reproducible** — given the same config and URLs,
- **Auditable** — logs show what was scraped and when,
- **Safe** — respect for community and survivor boundaries.

---

## 30.4 Corpus Curation and Filtering

The AAPCappE corpus is not a raw dump. It is **curated**:

- Documents are:

  - Tagged by:
    - Geography (county, ZIP code where identifiable),
    - Topic (health, environment, economy, governance),
    - Source type (government, nonprofit, news, community narrative).
  - Filtered for:
    - Relevance to Appalachian communities,
    - Appropriateness for Ms. Allis’s roles (steward, not voyeur).

- Content that is:

  - Clearly personally identifying,
  - Sensitive in a way that is not intended for public analysis,
  - Potentially retraumatizing without strong public-interest justification,

  is either:

  - Excluded entirely, or
  - Abstracted into high-level GBIM statements without direct quotation.

Corpus management includes:

- Versioning:
  - Keep track of corpus versions over time,
  - Allow rollback and differential analysis.
- Documentation:
  - Describe what domains and topics are included,
  - Specify inclusion and exclusion criteria.

---

## 30.5 Integration with RAG and GBIM

AAPCappE corpus feeds into:

- **ChromaDB RAG collections**:

  - For example:
    - Policy RAG,
    - Infrastructure RAG,
    - Regional history RAG.
  - Exposed via:
    - `allis-gis-rag:8004` (where relevant to geography),
    - `allis-spiritual-rag:8005` (where spiritual or community values are involved),
    - Other domain-specific RAG endpoints.

- **GBIM entities in `msallis:5433`**:

  - Derived facts may be:
    - Stored as entities with `confidence_decay` metadata,
    - Linked to specific counties, ZIP codes, or institutions.

This integration allows Ms. Allis to:

- Use the AAPCappE corpus as **evidence** when responding,
- Provide more grounded answers for:
  - Local policy questions,
  - Infrastructure planning,
  - MountainShares and community economic topics.

---

## 30.6 Governance and Oversight

AAPCappE is governed by the same oversight structures as the rest of Ms. Allis:

- **Constitutional guardian**:
  - Ensures scraping and corpus use are consistent with:
    - Privacy protections,
    - Community sovereignty,
    - General welfare principles.
- **Spiritual root and survivor safety**:
  - SpiritualFilter and SafetyMonitor must be able to flag:
    - Corpus content that contradicts safety commitments,
    - Usage patterns that lean on harmful narratives.
- **Dynamic Governance Mechanisms (DGMs)**:
  - Used to:
    - Adjust scraping targets,
    - Tighten or relax filters,
    - Add or remove domains,
    - Respond to community feedback.

Community can:

- Provide feedback on:
  - Which sites/feeds are helpful,
  - Which ones feel extractive or unsafe.
- Request:
  - Exclusion of certain types of content,
  - Clearer documentation of corpus sources.

All such changes are:

- Logged,
- Tied to DGMs,
- Visible in system governance documents.

---

## 30.7 Status and Future Work

As of April 6, 2026:

- AAPCappE scraper:

  - Configured for a **limited set** of known, ethically appropriate sources,
  - Produces structured text and metadata,
  - Logs activity for auditing.

- Corpus:

  - Seeded with a curated set of Appalachian public documents,
  - Integrated with RAG and GBIM pipelines,
  - Documented in internal schemas and notebooks.

Future work includes:

- Expanding the corpus cautiously:
  - With explicit community and governance review,
  - Focusing on high-value, public-interest content.
- Building:

  - Better tools for:
    - Browsing the corpus,
    - Explaining to users what sources inform Ms. Allis’s answers.
  - More robust survivor-focused filters for:
    - Trauma-heavy content,
    - Historical violence narratives.

AAPCappE, as defined in this chapter, is a **tool for stewardship and truth**, not an engine for covert data extraction.

---

*Chapter 30 — AAPCappE Scraper and Corpus*  
*Ms. Egeria Allis Steward System — Harmony for Hope, Inc.*  
*Mount Hope, West Virginia*  
*SEALED: ★★★★ April 6, 2026 — FINAL REWRITE*  
