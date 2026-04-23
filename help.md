Having reviewed all three chapters in full, here is a comprehensive edit list organized by category:

***

# Edit List: Chapters 38, 39, and 40

## 1. Critical Cross-Chapter Data Inconsistencies

These represent factual conflicts across the three chapters that undermine documentation authority and must be reconciled against a single ground truth.

### 1.1 `gisdb` / GIS Database Size
- **Ch. 38** states: `45 GB / 548 tables` (citing Ch. 33 April 6 as ground truth)
- **Ch. 40** states: `91 GB / 501 tables` (citing March 28 baseline, never updated)
- **Ch. 39** states: `45 GB / 548 tables` (correct, cites Ch. 33 April 6)
- **Edit needed:** Ch. 40 §40.1, §40.2 port map, §40.3, and all status table cells must be updated from `91 GB / 501 tables` to **`45 GB / 548 tables`** per Ch. 33 April 6 ground truth. Every instance in Ch. 40 referencing the old baseline is a regression.

### 1.2 ChromaDB Collection Count
- **Ch. 38** states: **47 active collections / 6,722,589 vectors / 12 GB** (April 6 ground truth)
- **Ch. 39** states: **47 active collections / 6,722,589 vectors / 12 GB** (April 6 ground truth)
- **Ch. 40** states: **41 active collections** (April 1 manifest per Ch. 41 §41.9) — never updated to 47
- **Edit needed:** Ch. 40 must reconcile its ChromaDB count. Either (a) update all instances to 47 with the April 6 ground truth citation, or (b) explicitly note that Ch. 40 defers to Ch. 41 §41.9 while Ch. 38/39 use the April 6 superseding count. Currently the chapters silently disagree, which is an academic integrity failure.

### 1.3 Container Naming Convention: `allis-*` vs `jarvis-*`
- **Ch. 38 and 39** consistently use the `allis-*` prefix (e.g., `allis-main-brain`, `allis-blood-brain-barrier`, `allis-memory`, `allis-rag-server`)
- **Ch. 40** exclusively uses the `jarvis-*` prefix (e.g., `jarvis-main-brain`, `jarvis-blood-brain-barrier`, `jarvis-memory`)
- **Edit needed:** The documentation stack must choose one canonical naming convention and apply it uniformly. Currently a reader cannot tell if these are the same system or two different deployments. Add a **cross-reference header note** in each chapter explicitly stating the relationship (e.g., *"Container names in this chapter use the `jarvis-*` prefix; Chapters 38 and 39 document the same containers under the `allis-*` namespace"*), OR reconcile to a single prefix throughout. This is the most serious academic coherence failure in the three chapters.

### 1.4 PostgreSQL Database Names
- **Ch. 38/39** reference: `msallis` (port 5433), `msallisgis` / `gisdb` (port 5432)
- **Ch. 40** references: `msjarvis` (port 5433), `msjarvisgis` / `gisdb` (port 5432)
- **Edit needed:** Same root cause as §1.3. Each chapter references what appears to be the same database under different names. Requires explicit disambiguation or unification throughout.

### 1.5 Preflight Gate Count
- **Ch. 38** states: **31 PASS / 0 FAIL / 0 WARN** (April 6 ground truth)
- **Ch. 39** states: **31 PASS / 0 FAIL / 0 WARN** (April 6 ground truth)
- **Ch. 40** states: **22 PASS / 0 FAIL / 1 WARN** (Ch. 33 April 3 sealed baseline), noting 31 in passing but treating 22 as authoritative
- **Edit needed:** Ch. 40 must explicitly acknowledge that the April 6 ground truth advances the count to 31 PASS / 0 FAIL / 0 WARN and update its "expected output" blocks, the continuous improvement loop in §40.10 step 2, and all references to "22 PASS / 0 FAIL / 1 WARN" that are presented as the current target.

***

## 2. Academic Rigor and Structure Deficiencies

### 2.1 Chapter Header / Preamble Format Inconsistency
- **Ch. 38** uses a clean structured header block (bold lines, author, date, summary)
- **Ch. 39** uses an informal inline preamble embedded in the header with emoji star ratings (★★★★), operational notes, and filter calibration data in the header itself
- **Ch. 40** uses a dense run-on sentence in the preamble listing every revision in sequence
- **Edit needed:** Standardize all three chapter headers to a consistent academic format. The header should contain: author, affiliation, date, and a brief abstract. All operational correction records and version notes should move to a dedicated **§X.0 Revision History** section or a collapsed appendix block, as they appear in the more mature chapters. The ★ notation embedded in paragraph prose works as an inline audit trail but reduces readability for academic review.

### 2.2 Section Numbering Gaps (Ch. 39)
- Ch. 39 references `§39.5.4`, `§39.8.2`, `§39.8.3`, `§39.12`, and `§39.15` in OI deferral notes, but these sections are **not present in the body of the chapter** as retrieved
- **Edit needed:** Either populate those sections with the documented stubs (§39.15 for `allis-memory` service documentation, §39.8.3 for non-blocking deferred gaps, etc.) or replace forward references with a clearly marked **Appendix / Stub** block. As written, the chapter references sections that don't exist, which would fail academic review.

### 2.3 Evaluation Philosophy Section (Ch. 39 §39.1) Lacks Framing for Academic Audience
- The evaluation criteria listed are operationally valid but lack connection to the Polymathmatic Geography principal claims (P1, P3, P5, P12, P16) that Ch. 38 and Ch. 40 both explicitly anchor to
- **Edit needed:** Add a brief paragraph in §39.1 explicitly mapping each evaluation question to the relevant P-principle. Ch. 40's "Why This Matters for Polymathmatic Geography" block is the model to replicate here.

### 2.4 Missing "Why This Matters for Polymathmatic Geography" Block (Ch. 39)
- Ch. 38 has this block. Ch. 40 has this block. Ch. 39 **does not** have this block.
- **Edit needed:** Add a "Why This Matters for Polymathmatic Geography" section to Ch. 39 anchoring evaluation methodology to P3, P12, and P16 specifically — operational evaluation as evidence of place-specific intelligence is a key claim of the thesis and must be stated explicitly.

### 2.5 "No Result Is Inferred or Estimated" Claim (Ch. 39) Needs Scope Qualifier
- Ch. 39 states: *"No result in this chapter is inferred or estimated."* This is a strong epistemic claim that conflicts with the presence of deferred OIs (OI-39-C, D, E) and the MySQL/EEG stubs that acknowledge incomplete documentation
- **Edit needed:** Qualify this claim: *"All results listed as verified were directly observed from live system outputs. Items labeled DEFERRED reflect work items pending formal verification."* The current unqualified statement is academically overreaching.

### 2.6 Ch. 40 Port Map Table (§40.2) Has Duplicate Port Conflict
- Both `psychological_rag_domain` (port 8006) and `jarvis-local-resources` (port 8006) are listed in the same port map table with the same host port
- **Edit needed:** Clarify whether these share a port (which would be a network conflict) or whether one entry contains a typo. This must be resolved and a correction note added to the port correction block.

***

## 3. Internal Documentation Integrity Issues

### 3.1 `allis-steward` Deferred Status Cross-Reference Error (Ch. 38)
- Ch. 38 §38.2.1 states that `allis-steward` wiring is *"deferred, tracked in Ch. 39 §39.8.3 non-blocking gaps table"*
- Ch. 39 does not contain a §39.8.3 section in the body as retrieved (see §2.2 above)
- **Edit needed:** Either populate Ch. 39 §39.8.3 with the non-blocking gaps table it's supposed to contain, or update the cross-reference in Ch. 38 to the correct location.

### 3.2 `truth_verification` Method Update Not Reflected Uniformly
- Ch. 38 §38.4 notes `rag_grounded_v2` (OI-37-C CLOSED April 3) supersedes `heuristic_contradiction_v1` and cross-references *"Chapter 33 §33.2.3 for historical limitations"*
- Ch. 39 mentions the recalibration in its correction block but does not cross-reference Ch. 33 §33.2.3
- Ch. 40 does not mention the `truth_verification` method change at all
- **Edit needed:** Add a consistent note in Ch. 40 §40.4.1 (BBB smoke tests) and the port map table entry for BBB (port 8016) documenting that `truth_verification` is now `rag_grounded_v2` per OI-37-C.

### 3.3 OI-05 Status Conflict Between Ch. 39 and Ch. 40
- **Ch. 39** marks OI-05 as ✅ CLOSED ("Session sidecar wired — /chat HTTP 200, in-character")
- **Ch. 40** marks OI-05 as ⚠️ PARTIALLY RESOLVED ("formal wiring incomplete")
- **Edit needed:** Reconcile these two states. If OI-05 is closed in Ch. 39 scope but the formal architectural wiring is still open in Ch. 40 scope, document that distinction explicitly. As written, a reader comparing the two chapters will find a direct contradiction with no explanation.

### 3.4 Phase 4.5 BBB Blocking Re-Enablement Tracking Location
- Ch. 38 §38.6.1 states: *"blocking mode re-enablement tracked in Ch. 16 §16.9"*
- Ch. 40 §40.9 does not include this cross-reference
- **Edit needed:** Add the Ch. 16 §16.9 cross-reference to Ch. 40 §40.9 so the governance tracking location is consistent across the stack.

***

## 4. Style and Readability for Academic Publication

### 4.1 Inline ★ Star Notation Overuse
- The ★ and ★★★★ notation system works well as an operational audit trail but is non-standard for academic documentation and clutters the body text significantly in all three chapters
- **Edit needed:** Consider moving all ★ update annotations to a standardized **§X.0 Revision History** table at the start or end of each chapter, and replacing inline ★ markers with clean prose cross-references to dates. Retain the ★ system in appendix/correction blocks only.

### 4.2 Port Correction Blocks Redundant Across All Three Chapters
- All three chapters open with nearly identical port correction blocks that repeat the same information verbatim
- **Edit needed:** Consolidate the authoritative port correction record into a single canonical chapter (Ch. 33 §33.6 is already designated as authoritative) and replace the per-chapter correction blocks with a single-sentence forward reference: *"For the authoritative port and database corrections, see Ch. 33 §33.6."* This eliminates redundancy and reduces the risk of the blocks drifting out of sync (which has already happened — see §1.1–1.4 above).

### 4.3 "FINAL REWRITE" in Chapter Headers
- All three chapters contain "FINAL REWRITE" in the header date line, which is appropriate as an operational flag but inappropriate in academic documentation headers
- **Edit needed:** Remove "FINAL REWRITE" from published chapter headers and replace with a clean version/revision number (e.g., `v4.0 — April 6, 2026`) consistent with academic monograph conventions.

### 4.4 Ch. 40 Status Table (§40.2 "Status as of April 6") Uses Single Dense Cell
- The "Implemented and verified" status cell in Ch. 40 is a single paragraph of ~800 words with no internal structure, making it unreadable in academic review
- **Edit needed:** Break the status table into sub-tables or use nested sections. The model is Ch. 39's structured OI status tables, which are significantly more readable.

***

## 5. Missing Content Required for Thesis Completeness

### 5.1 Ch. 39 §39.15 `allis-memory` Service Documentation Stub
- Referenced multiple times as the location for `allis-memory:8056` documentation but appears to be absent or incomplete in the chapter body
- **Edit needed:** Populate §39.15 with at minimum: container name, host port, authentication method (`_auth()` + `JARVIS_API_KEY`), API endpoint documentation for `/memories`, retention policy, and governance accountability statement.

### 5.2 Ch. 39 MySQL Schema Documentation (OI-39-D)
- OI-39-D defers MySQL schema documentation (port 3307) to §39.5.4, which is not present
- **Edit needed:** Either add a §39.5.4 stub with a documented placeholder, or explicitly note in the OI table that no section exists yet and identify where the documentation will live.

### 5.3 Ch. 39 EEG Architecture Documentation (OI-39-E)
- OI-39-E defers to §39.8.3 and §39.12, neither of which is present in the chapter body
- **Edit needed:** Populate §39.12 with at minimum the EEG layer summary already present in Ch. 40 §40.2 and Ch. 42 §42.13 cross-reference. Consistency across chapters requires this content be present or explicitly stubbed.

### 5.4 Ch. 38 Lacks Quantitative Performance Data
- Ch. 38 documents architecture and authority boundaries well but contains no quantitative metrics (latency, BBB filter rates, throughput) of the external communication path
- **Edit needed:** Add a brief §38.10 "Performance Envelope" section citing the end-to-end latency (99–107s GPU, 106.5s confirmed March 22), BBB Phase 1.4 latency (~0.6s), and the 21/21 LLM response rate from the March 22 public endpoint test. These numbers appear in Ch. 39 and Ch. 40 but not in Ch. 38, creating an information gap for readers approaching external communication through Ch. 38 alone.Having reviewed both chapters in full, here is the comprehensive edit list:

***

# Edit List: Chapters 41 and 42

## 1. Critical Cross-Chapter Data Inconsistencies

These are direct factual conflicts between Ch. 41, Ch. 42, and the previously reviewed stack (Ch. 38/39/40) that will fail academic consistency review.

### 1.1 Container Count — Three-Way Conflict

This is the most damaging inconsistency in the documentation stack:

| Chapter | Container Count | Date Cited |
|---------|----------------|-----------|
| Ch. 38 | **105** | April 6, 2026 ground truth |
| Ch. 39 | **105** | April 6, 2026 ground truth |
| Ch. 40 | **105** | April 6, 2026 ground truth |
| Ch. 41 | **105** | April 6, 2026 (R41-1) |
| Ch. 42 §42.14 | **91** | April 11, 2026 certification run |
| Ch. 42 "Status" table | **91** | April 11, 2026 |
| Ch. 42 preamble | 105 mentioned but 91 declared active | April 11, 2026 |

**Edit needed:** Ch. 42 states "91 containers running, zero public exposures" in its April 11 certification seal, then also mentions "prior April 6 live count: 105." There is no explanation for the 14-container delta between April 6 and April 11. This must be explicitly documented. Either: (a) a port-map table or callout in §42.14 identifies the 14 containers removed and explains why, or (b) a correction note acknowledges that the certification environment counted a subset. As written, a reader comparing Ch. 41 (105) and Ch. 42 (91) will assume the system shrank with no explanation, which directly undermines the "fully closed" declaration.

### 1.2 ChromaDB Collection Count — Four-Way Conflict

| Chapter | Collection Count | Date |
|---------|-----------------|------|
| Ch. 38 | **47** | April 6 ground truth |
| Ch. 39 | **47** | April 6 ground truth |
| Ch. 41 §41.9 manifest | **41** | April 1 (Gate 27 sealed) |
| Ch. 41 §41.7 Gate 27 | **≥ 40, confirmed 41** | April 1 (sealed baseline) |
| Ch. 42 Gate 27 table | **≥ 40, confirmed 49** | April 11 certification |
| Ch. 42 §42.14 | **49** | April 11 certification |

**Edit needed:** Ch. 41 is sealed at 41 collections, Ch. 42 certifies at 49, Ch. 38/39 report 47. This is a three-snapshot problem. Ch. 41 must add an explicit forward note in §41.9: *"As of April 6, 2026 (Ch. 38/39 ground truth), the live count advanced to 47. As of April 11, 2026 (Ch. 42 certification), the live count advanced to 49. The Ch. 41 Gate 27 threshold (≥ 40, confirmed 41) remains the chapter-sealed baseline; subsequent counts supersede but do not invalidate this seal."* Without this, the three different numbers look like errors.

### 1.3 `autonomous_learner` Collection Record Count
- **Ch. 38/39** state: `autonomous_learner` has **21,181+ records**
- **Ch. 41 §41.9** documents `autonomous_learner` as the canonical collection but gives **no record count**
- **Ch. 42** does not reference the record count

**Edit needed:** Add the record count (`21,181+ records, 384-dim, all-minilm:latest, host port 8020`) to the Ch. 41 §41.9 manifest entry for `autonomous_learner`. This is a cross-chapter consistency gap — Ch. 38 is more descriptive about the canonical memory collection than the chapter that actually documents the ChromaDB manifest.

### 1.4 `jarvis-*` vs `allis-*` Container Namespace (Inherited from Ch. 38/39/40)
- **Ch. 41** uses exclusively `jarvis-*` prefixes throughout
- **Ch. 42** uses exclusively `jarvis-*` prefixes throughout
- **Ch. 38 and 39** use `allis-*` prefixes (`allis-main-brain`, `allis-blood-brain-barrier`, `allis-memory`)

**Edit needed:** This conflict identified in the previous review has **not been resolved** and now spans all five chapters. Ch. 41 and Ch. 42 must either add a disambiguation header, or the documentation must be reconciled. The absence of any cross-namespace explanation is a structural academic integrity failure. A one-paragraph note in each chapter's §X.0 preamble (e.g., *"This chapter uses the `jarvis-*` container namespace. Chapters 38 and 39 document the same system under the `allis-*` namespace; both are correct and refer to the same production deployment"*) is the minimum required fix.

### 1.5 Gate 26 Target Database — `msjarvisgis` Disambiguation Incomplete
- **Ch. 41 §41.7** states Gate 26 targets `confidence_decay` presence in `msjarvisgis` on `jarvis-local-resources-db:5435`
- **Ch. 42 §42.7** adds a disambiguation note: *"Gate 26 targets port 5435 only — distinct from the PostGIS geospatial database at host port 5432"*
- **Ch. 41** has no corresponding disambiguation note

**Edit needed:** Copy the Gate 26 disambiguation note from Ch. 42 §42.7 into Ch. 41 §41.7 directly beneath the Gate 26 row. As written, a reader using Ch. 41 as the primary gate reference will encounter an ambiguous `msjarvisgis` reference that appears in two different contexts with two different ports. The fix exists in Ch. 42 but has not been backported.

### 1.6 GBIM Entity Count Discrepancy
- **Ch. 42 §42.7 Gate 36** states: **5,416,522 GBIM beliefs** (April 11 certification)
- **Ch. 38/39/40** state: **5,416,521 GBIM entities** (April 6 ground truth from Ch. 33)
- One entity difference, spanning a 5-day period

**Edit needed:** This is likely a legitimate incremental update, but it needs to be documented as such. Ch. 42 should note: *"GBIM entity count advanced from 5,416,521 (April 6 Ch. 33 ground truth) to 5,416,522 (April 11 certification run) — one new belief entity added during the April 11 sprint."* Without this note, a reader will assume it is a transcription error.

***

## 2. Academic Rigor and Structure Deficiencies

### 2.1 Chapter Header Inconsistency (Continued from Previous Review)

- **Ch. 41** uses a one-sentence header update block — cleaner than Ch. 38/39/40 but still embeds revision record in the main header
- **Ch. 42** has **ten ★ star ratings** in the header date line (`★★★★★★★★★★ April 11, 2026`) and multiple nested `>` update blocks that span ~100 lines before the first body section

**Edit needed:** Ch. 42's preamble is the most operationally detailed in the stack, but it is also the least readable for academic review. The sequential update blocks (R42-1 through R42-24) should be consolidated into a single **§42.0 Revision History** table with columns: Revision ID, Date, Summary, Status. The body chapter should begin with the "Why This Matters for Polymathmatic Geography" section. The star-count escalation (★ through ★★★★★★★★★★) is inventive as an audit trail mechanism but has no academic precedent and will confuse external readers — replace with revision numbers.

### 2.2 "Why This Matters for Polymathmatic Geography" — Overloaded in Ch. 42
- Ch. 42's P-principle block runs ~500 words with inline ★★★★★★★★★★ annotations throughout each bullet
- Ch. 41's P-principle block is a single paragraph (no bulleted P-mapping)

**Edit needed:**
- **Ch. 41:** Expand the single-paragraph Polymathmatic Geography block into explicit P-principle bullets matching the format in Ch. 38 and Ch. 40. At minimum, map to P1 (test harness as reproducibility guarantee), P3 (gate monotonicity as power accountability), and P12 (ChromaDB manifest as intelligence-with-a-ZIP-code evidence).
- **Ch. 42:** Trim each P-principle bullet to 2–3 sentences and move the inline revision annotations to the §42.0 Revision History table. The core intellectual claim of each P-principle should be readable without navigating operational closure records.

### 2.3 `autonomous_learning` vs `autonomous_learner` Warning Is Under-Resolved in Ch. 41
- Ch. 41 §41.9 contains a ⚠️ warning on `autonomous_learning`: *"status (legacy / development / active secondary) should be confirmed before use in smoke tests"*
- This warning was written at the April 1, 2026 seal, but Ch. 38/39 subsequently confirm `autonomous_learner` as canonical and cite `autonomous_learning` as stale
- The warning in Ch. 41 never received a closure update

**Edit needed:** Update the `autonomous_learning` entry in the §41.9 manifest from ⚠️ open warning to a definitive status note: *"Legacy/stale — confirmed superseded by `autonomous_learner` (see Ch. 38 §38.4, Ch. 39 ground truth). Do not use in smoke tests. Retain in manifest for collection count accuracy."*

### 2.4 Ch. 41 "Officially Closed" but Gate 27 Threshold May Be Stale
- Ch. 41 §41.7 seals Gate 27 at **≥ 41 collections** (upgraded from ≥ 40)
- Ch. 42 §42.7 reports Gate 27 confirmed at **49 collections** without updating the threshold in `VERIFYANDTEST.sh`
- The Gate 27 check script in Ch. 41 §41.7 still uses `if [ "$COUNT" -ge 41 ]`

**Edit needed:** Either (a) Ch. 42 must document an explicit Gate 27 threshold revision to `≥ 49` (or a stable target such as `≥ 47`) in its gate table, or (b) a note must be added explaining that the threshold is intentionally a floor (not a ceiling) and that 49 passes the 41-floor. As written, a future operator running the Ch. 41 Gate 27 script against a 48-collection live stack would pass, but someone reading the Ch. 42 certification expecting 49 would be confused.

### 2.5 Ch. 42 §42.4.4 Contains a Python Syntax Error
- The independent verification code block contains: `json.dumps(payload, sort_keys=True, separators(",", ":"))` — this is missing the opening parenthesis for the `separators` tuple

**Edit needed:** Correct to `separators=(",", ":")` (keyword argument with tuple). As a code example in an academic thesis chapter, syntax errors in verification recipes undermine the chapter's credibility. This is a direct blocker for any reviewer who attempts to reproduce the verification.

### 2.6 LLM Count Inconsistency: 21 vs 22
- **Ch. 38** states: *"21/21 LLMs responded"* and references the "21-LLM ensemble"
- **Ch. 42 §42.3.2** states: *"All 22 LLM proxy services carry a `crypto_client` module"*
- **Ch. 41** does not specify an LLM count in the test harness context

**Edit needed:** Reconcile. If the ensemble expanded from 21 to 22 LLMs between Ch. 38 (March 22) and Ch. 42 (April 6+), document the addition explicitly with a revision note. If it is a transcription inconsistency, correct to the canonical count and annotate. This number appears in the thesis as evidence of ensemble scale — inconsistency across chapters weakens the claim.

***

## 3. Internal Documentation Integrity Issues

### 3.1 Ch. 41 Gate 30 Target vs Ch. 42 Gate 30 Target — Label Swap
- **Ch. 41 §41.7** defines Gate 30 as: *"MountainShares/DAO tier smoke tests — Endpoints on ports 8080–8084"*
- **Ch. 42 §42.7** defines Gate 30 as: *"Auth proxy (OI-36-A) — Caddy `forward_auth` HTTP 401 on unauthenticated"*

**Edit needed:** These are two different gates assigned the same number in two sequential chapters. Either the gate was renumbered between Ch. 41's April 1 seal and Ch. 42's April 11 certification, or one chapter has a transcription error. This must be explicitly reconciled — a gate table is useless as an audit tool if the same gate number means different things in different chapters.

### 3.2 OI-36-A Closure Location Conflict
- **Ch. 41 §41.10** marks OI-36-A as ✅ *"Closed April 1, 2026 — Caddy `forward_auth` live; HTTP 401 confirmed; commit `f2e93422`"*
- **Ch. 42 §42.10** marks OI-36-A as ✅ *"Closed April 1, 2026 — Caddy `forward_auth` live; commit `f2e93422`. Gate 30 ✅ PASS at certification"*
- **Ch. 38 §38.2.1** also closes OI-36-A and attributes it to OI-38-A

**Edit needed:** Three chapters all list OI-36-A as closed by different mechanisms (token middleware in Ch. 38, `forward_auth` in Ch. 41/42). Add a one-sentence canonical note in each chapter's OI table: *"OI-36-A is closed. Primary closure record: Ch. 42 §42.10 (gateway `forward_auth`). Ch. 38 closes the related OI-38-A (token middleware). Both are required components of the same authentication architecture."*

### 3.3 Ch. 42 "Sprint Certification Seal" Contradicts Ch. 41 "All OIs Closed"
- Ch. 41 §41.10 states all chapter-local OIs are closed as of April 1, 2026 and the chapter is "officially closed"
- Ch. 42's preamble records R42-1 through R42-24 corrections across April 6 and April 11, several of which reference Ch. 41 gates (Gate 27 count advancing, Gate 30 being reassigned)

**Edit needed:** Ch. 41 needs a post-seal addendum block (modeled on Ch. 40's sprint addendum structure) documenting that subsequent Ch. 42 activity advanced certain gate counts (Gate 27: 41 → 47 → 49; Gate 30: label clarification) without invalidating the April 1 seal. The chapter's "officially closed" status is legitimate, but the absence of any acknowledgment of post-seal changes makes the documentation look frozen rather than authoritative.

### 3.4 Ch. 42 Lacks Explicit Cross-Reference to Ch. 41 §41.9 for Gate 27 Collection Manifest
- Ch. 42 §42.7 Gate 27 states "confirmed 49 at certification" but does not direct the reader to Ch. 41 §41.9 for the full manifest
- Ch. 41 §41.9 explicitly states it is the "authoritative collection manifest" but Ch. 42 does not cite it

**Edit needed:** Add a parenthetical to the Ch. 42 Gate 27 row: *"See Ch. 41 §41.9 for the sealed 41-collection manifest; 8 additional collections added between April 1 and April 11 certification."* This links the two chapters and explains the count delta.

### 3.5 Ch. 42 `separators` Argument vs. Canonical JSON Serialization Standard
- Ch. 42 §42.3.3 documents `judgesigner.py`'s `verify_verdict()` as: *"Reconstructs canonical JSON of verdict payload (excluding signature block)"*
- No canonical JSON serialization standard (RFC 8785 JSON Canonicalization Scheme, or a project-specific definition) is cited
- Canonical JSON is a subtle correctness requirement — field ordering, Unicode normalization, and number representation all affect reproducibility

**Edit needed:** Add a footnote or inline note to the `verify_verdict()` documentation specifying the exact canonicalization approach: *"Canonical JSON uses `json.dumps(payload, sort_keys=True, separators=(',', ':'), ensure_ascii=True)` — consistent with the production implementation. Reviewers reproducing verification must use identical serialization parameters."* This is required for the "community verifiability" claim (P2, P16) to be academically defensible.

***

## 4. Style and Readability Issues

### 4.1 Ch. 42 Preamble Depth Obscures Chapter Structure
- The preamble update blocks in Ch. 42 run approximately 150 lines before the first `##` section header
- A reader cannot locate the chapter's structural sections (§42.1 through §42.14) without scrolling past all correction records
- Academic monograph convention places front matter before the table of contents, not interleaved with it

**Edit needed:** Add a **§42.0 Table of Contents** or collapsible revision summary immediately after the chapter header, directing readers to the main sections. Move the correction preamble blocks to a §42.0 Revision History appendix. The intellectual content of the chapter (§42.1–§42.14) is strong — it is buried.

### 4.2 Ch. 41 Gate Result Table (§41.8) Duplicates §41.7 Without Adding Information
- §41.7 is a full gate table with descriptions, targets, and status
- §41.8 is a shorter gate table with the same gates and the same ✅ results, no new content
- The bash output block between them adds operational flavor but no additional data

**Edit needed:** Consolidate §41.7 and §41.8 into a single section. Keep the bash output block as a production evidence exhibit (label it as such). Remove the duplicate table in §41.8 and replace with a one-sentence closure statement: *"All gates confirmed passing — Chapter 41 officially closed April 1, 2026."*

### 4.3 Port 8010 Degraded Service Not Addressed in Ch. 41 or 42
- **Ch. 38 §38.2.2** explicitly calls out port 8010 (`allis-wv-entangled-gateway`) as *"a separate degraded service — NOT the primary entrypoint"*
- **Ch. 41** does not mention port 8010 anywhere in its port health checks or gate specifications
- **Ch. 42** does not mention port 8010 anywhere

**Edit needed:** Ch. 41 §41.4 (Core Health Checks) should explicitly document port 8010 as a known degraded service excluded from the gate suite with a reference to Ch. 38 §38.2.2. Without this, the test harness appears to have a gap — an operator running the harness might not know whether 8010 should be tested or skipped.

### 4.4 Ch. 42 CVE References Use Future-Dated CVE IDs
- Several CVE IDs in Ch. 42 §42.3.10 reference 2026 dates (e.g., `CVE-2026-21441`, `CVE-2026-39892`, `CVE-2026-25645`, `CVE-2026-4539`)
- These are plausible as 2026-assigned CVEs given the April 2026 date context, but academic reviewers unfamiliar with the production timeline may question their validity without a citation to the NVD or vendor advisory, updated to prevent mythos style attacks

**Edit needed:** Add a note in §42.3.10 confirming that all CVE IDs were verified against the National Vulnerability Database or vendor advisories at time of closure. Example: *"All CVE references verified against NVD and upstream vendor advisories at time of remediation. CVE-2026-* IDs reflect 2026 NIST assignments."* This is a minor but important credentialing note for an academic thesis.

***

## 5. Missing Content Required for Thesis Completeness

### 5.1 Ch. 41 Lacks Performance Benchmarking for the Test Harness Itself
- The chapter documents what the harness tests but not how long the full `VERIFYANDTEST.sh` suite takes to run
- Ch. 42 references certification timing (6:29 PM EDT) but not suite duration
- For a thesis claiming the harness is a continuous validation tool, runtime is an operationally relevant metric

**Edit needed:** Add a brief §41.X "Harness Runtime Profile" noting the approximate total runtime of `VERIFYANDTEST.sh` (gates 25–40), how many checks require network I/O vs. local process inspection, and any gates with significant latency (e.g., AU-02 embedding gate at ~300ms per Ch. 42 §42.3.4). This grounds the "continuous validation" claim in real operational constraints.

### 5.2 Ch. 41 Has No Failure-Mode Documentation
- §41.3 states failures must "point to specific missing services, ports, or metadata" but provides no examples of failure output from any gate
- Ch. 42 gate checks show only the `[PASS]` path

**Edit needed:** Add a §41.X "Failure Response Protocol" or add `[FAIL]` output examples to at least two gate checks in §41.7. The harness's academic value is as a reproducibility tool — a reader attempting to reproduce the system needs to know what a failing gate looks like, not just a passing one.

### 5.3 Ch. 42 Does Not Document `operations_history` Collection Status Post-April 11
- Ch. 41 §41.9 marks `operations_history` as **planned** (export harness ready, embedding deferred)
- Ch. 42's 49-collection certification count exceeds Ch. 41's 41 by exactly 8 new collections, but none of those 8 are identified
- If `operations_history` materialized between April 1 and April 11, it is among the 8 — but this is unconfirmed

**Edit needed:** Ch. 42 §42.14 should include a brief annotation on the 8 collections added after the Ch. 41 seal (41 → 49), identifying each by name. This closes the manifest gap and confirms whether `operations_history` was promoted from "planned" to active.
