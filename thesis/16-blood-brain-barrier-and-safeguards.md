> **Why this matters for Polymathmatic Geography**
> This chapter explains how Ms. Jarvis protects her "brain" from harmful inputs, unreliable data, and unsafe outputs, especially when working with sensitive, place‑based information. It supports:
> - **P1 – Every where is entangled** by ensuring that ethical, spiritual, safety, and truth checks constrain what can entangle with memories about communities and places stored in PostgreSQL `msjarvis` (port 5433) and `gisdb` (port 5433, 13 GB, 39 tables) and ChromaDB (port 8000, 5,416,521 GBIM entities), both before storage and after generation.
> - **P3 – Power has a geometry** by making protection a layered, routed structure in the service graph rather than a hidden afterthought, with explicit barrier and truth layers visible in health and consciousness metadata.
> - **P5 – Design is a geographic act** by treating safeguards as designed interfaces between communities' data, legal constraints, and Ms. Jarvis's internal cognition, rather than a generic "safety filter."
> - **P12 – Intelligence with a ZIP code** by requiring additional truth and identity checks when data is tied to specific residents, licenses, or infrastructures grounded in PostgreSQL spatial tables, and by recording how those checks were applied.
> - **P16 – Power accountable to place** by logging barrier decisions, truth verdicts, and verification results so that communities can reconstruct when and how the system blocked, reshaped, or allowed sensitive flows.
>
> As such, this chapter belongs to the **Computational Instrument** tier: it specifies the "blood–brain barrier" and truth‑filtering apparatus of Ms. Jarvis's architecture, where safety, ethics, and truth are enforced around core neurobiological and memory systems.

```
┌─────────────────────────────────────────────────────────────┐
│   Blood-Brain Barrier and Safeguards Architecture           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  User Input / GIS Data / Psychological Content              │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Blood-Brain Barrier (port 8016)               │         │
│  │  ┌──────────────────────────────────────────┐  │         │
│  │  │  -  EthicalFilter       → .filter(text)   │  │         │
│  │  │  -  SpiritualFilter     → .filter(text)   │  │         │
│  │  │  -  SafetyMonitor       → .check(text)    │  │         │
│  │  │  -  ThreatDetection     → .detect_threats │  │         │
│  │  │  -  MotherCarrieProtocol (routing flag)   │  │         │
│  │  └──────────────────────────────────────────┘  │         │
│  │  Endpoints: POST /filter, POST /truth           │         │
│  │  Stats: total_filtered, total_blocked           │         │
│  └────────────────────────────────────────────────┘         │
│      ↓ (if approved)                                        │
│  ┌────────────────────────────────────────────────┐         │
│  │  Truth Validators                              │         │
│  │  -  GISTruthFilter (geographic data)            │         │
│  │  -  TruthFilterBBBValidator (UEID/licenses)     │         │
│  │  -  TruthValidator (generated statements)       │         │
│  └────────────────────────────────────────────────┘         │
│      ↓ (if validated)                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Psychological Services                        │         │
│  │  -  psychological_rag_domain (port 8006)        │         │
│  │  -  jarvis-psychology-services (port 8019)      │         │
│  │  -  PIA review loop (log sampling)              │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  Core Cognition & Memory                                    │
│  -  PostgreSQL msjarvis (port 5433) — GBIM beliefs           │
│  -  PostgreSQL gisdb (port 5433) — PostGIS spatial           │
│  -  ChromaDB (port 8000) — 5,416,521 GBIM entities           │
│  -  I-Containers (port 8015)                                 │
│  -  Neurobiological Master (port 8018)                       │
│      ↓                                                       │
│  LLM Generation                                             │
│      ↓                                                       │
│  Output Guard (BBB /filter on generated text)               │
│  — fail-open on HTTP 500 (returns content unchanged)        │
│      ↓                                                       │
│  Response + truth_verdict                                   │
│                                                              │
│  Audit Logs → barrier_stats, verification outcomes          │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> **Figure 16.1.** Blood–brain barrier and safeguards in Ms. Jarvis: user inputs, GIS and UEID data, and psychological content are routed through a barrier and truth layer (BBB, GIS and identity validators, psychological guidance) before reaching core cognition and long‑term, WV‑grounded memory in PostgreSQL `msjarvis` (GBIM beliefs) and `gisdb` (PostGIS spatial), with all decisions surfaced via stats and audit logs. The output guard is fail-open on HTTP 500 responses from the BBB.

---

## Status as of March 2026

| Category | Details |
|---|---|
| **Implemented and verified (2026-03-18)** | `jarvis-blood-brain-barrier` confirmed running at **0.0.0.0:8016** (`docker compose ps`). Exposes `GET /health`, `POST /filter`, and `POST /truth`. Four sub‑filters confirmed operational with verified method signatures: `EthicalFilter.filter(text)`, `SpiritualFilter.filter(text)`, `SafetyMonitor.check(text)`, `ThreatDetection.detect_threats(text)`. `POST /truth` endpoint returns `{"valid": bool, "confidence": float, "principal_reasons": [str]}`. `barrier_stats` counters (`total_filtered`, `total_blocked`, `pass_rate`) live. `truth_verdict` attached to every `UltimateResponse` from main brain (port 8050). Output guard on generated text active in main brain pipeline via `apply_output_guards_async` calling `/filter` with 8.0s timeout (fixed 2026‑03‑02). **Fail-open behavior confirmed (2026-03-18):** BBB output guard returns content unchanged on HTTP 500 responses — the pipeline does not halt on BBB errors. **`truth_score` null guard confirmed (2026-03-18):** BBB orchestrator includes null guard for `truth_score` field — `KeyError` on missing `truth_score` resolved. BBB invoked as first stage in Neurobiological Master `integrated_processing()` pipeline. `MotherCarrieProtocol` implemented as a routing/emphasis/audit pattern **inside** BBB; `mothercarrieenabled` is a boolean flag controlling stricter care-focused routing — not a separate service and not a mystical mode. `jarvis-psychology-services` confirmed running at **127.0.0.1:8019**. `psychological_rag_domain` confirmed running at **127.0.0.1:8006** (restored March 15, 2026; backed by `chroma_data` Docker volume on ChromaDB port 8000). PostgreSQL `msjarvis` (port 5433, GBIM beliefs, 8 MB, 6 tables) and `gisdb` (port 5433, PostGIS spatial, 13 GB, 39 tables) are the protected memory stores. ChromaDB (port 8000, `gbim_worldview_entities` 5,416,521 entities) is the protected semantic memory store. **BBB ethical filter blocking 'certainly': BY DESIGN** — the ethical filter correctly blocks unverified specific claims. This is not a false positive; it is the constitutional layer enforcing epistemic honesty. |
| **Partially implemented / scaffolded** | Internal BBB filter logic is relatively permissive in the current deployment — often echoes content with placeholder reason codes. Strictest BBB behavior (systematic denial, quarantine, annotation of harmful flows) is still being realized; the architectural hook has real consequences but rule sophistication is ongoing. `GISTruthFilter`, `TruthFilterBBBValidator`, and `TruthValidator` are not yet consistently wired into all HTTP paths beyond dedicated verification and registration tools. Richer, user-visible explanations of barrier decisions beyond the compact `truth_verdict` field are an open design area. Psychological classifier and trigger logic is partially heuristic. |
| **Future work / design intent only** | Full wiring of truth validators into all HTTP flows. Richer public documentation of filter logic and scores. Actual quarantine collections for blocked content (currently tracked only via counters). Empirical evaluation of how often and how effectively the barrier and output guard protect communities in real deployments. Deeper PIA review loop producing structured recommendations beyond the current log-sampling pattern. |

> **Cross-reference note:** The canonical description of how BBB fits into the live `ultimatechat` execution path — including where `truth_verdict` is attached to `UltimateResponse` and where the output guard fires — is in **Chapter 17**. The Neurobiological Master's use of BBB as its first pipeline stage is documented in **Chapter 12 §12.2**. Psychological safeguard detail is in **Chapter 29**. Mother Carrie protocol detail is in **Chapter 34**.

---

# 16. Blood–Brain Barrier and Safeguards

In the current deployment, this layer is a set of confirmed running services that sit between external inputs, large‑scale generative models, and core neurobiological and memory systems — including PostgreSQL `msjarvis` (port 5433, GBIM beliefs, 5,416,521 entities) and `gisdb` (port 5433, PostGIS spatial, 13 GB, 39 tables), and ChromaDB (port 8000, `gbim_worldview_entities` 5,416,521 entities) — enforcing ethical, spiritual, safety, and truth‑focused checks before and after content can influence I‑containers and long‑term stores. As shown in Figure 16.1, the BBB aggregates these checks in a single barrier layer before content reaches core cognition.

---

## 16.1 Purpose of the Barrier Layer

In the current deployment, `jarvis-blood-brain-barrier` on **port 8016** is explicitly described as "Ethical and safety filtering for all inputs and outputs" and aggregates four sub‑filters: `EthicalFilter`, `SpiritualFilter`, `SafetyMonitor`, and `ThreatDetection`. The confirmed method signatures are:

- `EthicalFilter.filter(text)` — evaluates content for ethical violations; returns approval status
- `SpiritualFilter.filter(text)` — checks for biblical soundness and spiritual alignment
- `SafetyMonitor.check(text)` — evaluates safety classification; returns boolean safe/unsafe
- `ThreatDetection.detect_threats(text)` — checks whether content is community‑safe

The core filtering method in `/filter` increments counters, invokes all four methods above, and only approves content when ethical status is approved, spiritual alignment is "biblically sound," safety is true, and threat detection reports the content as community‑safe. Prior to 2026‑03‑13, these four methods were defined in the codebase but were not correctly called inside the `/filter` request handler — the wiring was repaired during the 2026‑03‑13 remediation session.

**False-positive resolution — word-boundary detection (March 15, 2026):** The `_check_keywords()` method was corrected to use regex word boundary detection (`\b`) for keywords ≤3 characters. Community resource terms ("con," "res," etc. as substrings inside benign words such as "Context," "Collective," "resources") no longer trigger safety blocks. Jailbreak attempts using those character sequences as actual words are still correctly blocked. This fix was required for the BBB to pass legitimate community resource responses.

**`truth_score` null guard (March 18, 2026):** A null guard has been added to the BBB orchestrator for the `truth_score` field. Previously, if the BBB `/truth` response omitted `truth_score`, the orchestrator raised a `KeyError` and the pipeline halted. The null guard resolves to a safe default, allowing the pipeline to continue and logging the missing field for investigation.

**Fail-open on HTTP 500 (March 18, 2026):** The BBB output guard (`apply_output_guards_async`) now implements fail-open behavior on non-200 responses from the BBB. If the BBB returns HTTP 500 (or any non-200), the pipeline returns the content unchanged rather than halting. This ensures that a BBB service error does not prevent Ms. Jarvis from responding to community queries. The fail-open behavior is logged so that operators can identify and remediate BBB instability.

**"Certainly" blocking — BY DESIGN:** The BBB ethical filter blocks responses containing unverified specific claims, including certain usages of high-confidence language such as "certainly" when the underlying claim is not backed by verified data. This is not a false positive or a calibration error. It is the constitutional layer enforcing epistemic honesty: Ms. Jarvis should not express certainty about facts she cannot verify. This behavior is expected and correct.

In the current deployment, the BBB also keeps totals of filtered and blocked items and computes a `pass_rate`, giving a transparent quantitative view of how often the barrier intervenes. Around this, truth‑focused validators (`GISTruthFilter`, `TruthFilterBBBValidator`, `TruthValidator`) extend the layer's purpose from simple blocking into structured evaluation of factual reliability. A compact `truth_verdict` is attached to each `UltimateResponse`, and the BBB also acts as an output guard on generated text before responses are returned to callers.

The barrier protects PostgreSQL `msjarvis` (port 5433, GBIM beliefs, 8 MB, 6 tables) and `gisdb` (port 5433, PostGIS spatial, 13 GB, 39 tables) from contamination by unreliable or harmful inputs, ensuring that only ethically approved, spiritually aligned, and safety-checked content can influence the spatial and institutional memory that grounds Ms. Jarvis's West Virginia accountability.

---

## 16.2 The `/truth` Endpoint

As of **2026‑03‑13**, the BBB exposes a confirmed operational endpoint: `POST /truth`. This endpoint accepts `{"content": str}` and returns a structured truth verdict:

```json
{
  "valid": true,
  "confidence": 0.0,
  "principal_reasons": ["string"]
}
```

This endpoint is called by the main brain's `call_truth_filter` helper, which sends the raw user message to `POST /truth` before the LLM synthesis step. The result is attached as `truth_verdict` on the `UltimateResponse`. An example from the 2026‑02‑15 case study: `{"valid": false, "confidence": 0.9, "principal_reasons": ["Ethics: 1 violations detected"]}` (see Chapter 9 §9.3.5).

**`truth_score` null guard (March 18, 2026):** The BBB orchestrator now includes a null guard for the `truth_score` field in the `/truth` response. If `truth_score` is absent from the BBB response (e.g., due to a partial service startup or internal BBB error), the orchestrator resolves to a safe default rather than raising a `KeyError`. This fix was required for pipeline stability during the March 16–18 optimization sessions.

In the current deployment, the truth verdict is **advisory** — it is logged and exposed to callers but does not hard-gate the input pipeline. Hard-gate behavior for specific role or threat levels is identified as future work.

---

## 16.3 Placement in the Overall Architecture

In the current deployment, the BBB is treated as a distinct consciousness layer alongside I‑containers, qualia, the Neurobiological Master, consciousness bridge, swarm intelligence, and the NBB prefrontal cortex, with port 8016 listed in the unified consciousness schema. Health endpoints expose fields such as `barrier_active` and `filters_operational`, and higher‑level gateways use these to decide whether to mark `"blood_brain_barrier"` as active in their `consciousness_active` maps and `layers_processed` pipeline metadata.

**MotherCarrieProtocol** is implemented as a routing/emphasis/audit pattern **inside** the BBB service — not as a separate container. The flag `mothercarrieenabled` controls stricter care‑focused routing when set to true; it is a boolean configuration value, not a mystical mode. A `SpiritualFilter` alias provides Christian-only legacy mode for backward compatibility with earlier deployments. For full detail on this protocol, see **Chapter 34**.

In earlier "complete integration" pipelines, the BBB was invoked as the first gate on content — called before any MountainShares, location, psychological, temporal, or maternal processing — so that unsafe material could be blocked outright. In the current `Ms. Jarvis ULTIMATE` main brain, the BBB continues to sit close to the surface and is woven into the executive coordination layer: a dedicated truth‑filter helper evaluates the incoming message via `/truth`, and a separate output guard filters the generated response via `/filter`, giving both input‑side assessment and output‑side protection.

**Output guard fail-open behavior (March 18, 2026):** The output guard (`apply_output_guards_async`) is fail-open on non-200 responses from the BBB. If the BBB `/filter` call returns HTTP 500 or any non-200 status, the pipeline returns the content unchanged rather than halting. This preserves service availability during BBB instability while logging the failure for operator review. For the canonical description of exactly where in the `ultimatechat` sequence BBB fires, see **Chapter 17**.

---

## 16.4 Source Policies and Gateways

In the current deployment, BBB participation is exposed through dedicated routes that make the barrier's role explicit. Academic and public gateways provide `/truth/filter` or similar endpoints that accept user text, forward it to the BBB's `/filter` interface, and return the JSON result or a conservative default when the service is unavailable, making the BBB the policy enforcement point for truth and safety filtering.

A secured swagger gateway extends this by exposing higher‑level `/truth/validate` endpoints under a "Truth Filter" tag, returning structured assessments (`statement`, `valid`, `confidence`, `reasoning`) and enabling external tools to query the system's self‑declared truth stance without directly touching internal stores or PostgreSQL GBIM tables.

---

## 16.5 Screening, Quarantine, and Output Guarding

In the current deployment, variants of the barrier implement screening behavior that can either block content outright or strip it before passing it onwards. Earlier pre‑integration services exposed `/process` and returned either the original content or an empty string plus a `filtered: True` flag depending on the combined verdict of ethical, spiritual, and safety filters, ensuring that blocked material did not reach downstream components even when the call chain continued.

The production service on port **8016** augments this with `barrier_stats` counters (`total_filtered`, `total_blocked`, `pass_rate`), which serve as a crude quarantine metric by tracking how often content is stopped or allowed through. Actual quarantine collections are managed in GIS and UEID databases by associated truth‑filter modules; dedicated ChromaDB quarantine collections for the BBB itself are identified as future work.

In the current main brain pipeline, `apply_output_guards_async` calls `POST /filter` on the BBB with an 8.0s timeout (corrected from `None` on 2026‑03‑02 to prevent indefinite hang after LLM completion). It selects a safe text field from the response when available, giving the system an opportunity to redact or reshape responses before they are returned to users.

**Fail-open on HTTP 500 (confirmed March 18, 2026):** If the BBB returns a non-200 response (including HTTP 500), `apply_output_guards_async` returns the content unchanged rather than halting the pipeline. This fail-open behavior was implemented to ensure that BBB service errors do not prevent Ms. Jarvis from completing responses. The fail is logged with the HTTP status code for operator remediation. This behavior does **not** disable the BBB — on healthy responses, the BBB output guard operates normally.

This output guard protects users from potentially harmful content generated by the LLM ensemble, while the input BBB `/truth` call protects PostgreSQL `msjarvis` GBIM tables and ChromaDB from contamination.

---

## 16.6 Truth‑Focused Evaluation

In the current deployment, several dedicated truth‑filter classes evaluate factual quality and identity claims before data reaches PostgreSQL long‑term stores or is used for critical operations.

`GISTruthFilter` validates geographic data destined for spatial tables by checking coordinate precision and last‑verified timestamps and by cross‑checking authoritative sources (USGS, NRCS, NOAA, US Census Bureau), only allowing ingestion when uncertainty is below a threshold and at least one source cross‑check succeeds. This protects the PostgreSQL `gisdb` spatial tables from unreliable coordinate data.

`TruthFilterBBBValidator` applies truth and BBB‑style standards to driver license data used in UEID registration, checking license number presence, expiration dates with a buffer window, photo hash presence, and plausible age. It computes accuracy and ethics scores, rejects registrations below a configured minimum, and stores verification outcomes in UEID identity and audit tables.

A more general `TruthValidator` class focuses on generated or internal statements, flagging plausible hallucinations, identity confusion, and factual or terminology errors before those statements are used for decision‑making or stored as knowledge in PostgreSQL `msjarvis` GBIM tables. In the current deployment, all three validators are implemented and used in batch / command-line flows and UEID registration. They are not yet consistently wired into all HTTP paths beyond dedicated verification and registration tools; broader HTTP wiring is identified as near‑term work.

The GIS and UEID validators and `TruthValidator` correspond to the truth-filter sub‑section of Figure 16.1, with their outputs recorded in the logs and audit box.

---

## 16.7 Truth‑Related Signals and Labels

In the current deployment, these truth filters return structured outputs rather than bare booleans.

The `POST /truth` endpoint on the BBB itself returns `{"valid": bool, "confidence": float, "principal_reasons": [str]}`.

**`truth_score` null guard:** The BBB orchestrator's handling of the `/truth` response now includes a null guard for the `truth_score` field. If this field is absent from the response (due to partial service startup, internal BBB error, or schema mismatch), the orchestrator resolves to a configurable safe default (currently `0.0`) and logs the missing field rather than raising a `KeyError`. Code that consumes `truth_score` downstream must treat `0.0` as "unknown / unverified" rather than "verified false."

`TruthFilterBBBValidator` constructs verification documents containing `valid`, `accuracy_score`, `ethics_score`, `issues`, and explicit `bbb_compliant` and `truth_compliant` flags. These can be used to gate access in UEID–GIS mapping services and to annotate user records with provenance and risk.

`TruthValidator` reports `truth_validated`, a list of detected issues (hallucinations, identity confusion, factual and terminology errors), an overall `truth_score`, and booleans for `correct_identity`, `correct_creator`, and `relationship_clear`, providing identity‑ and hallucination‑aware labels that can be attached to generated content or internal statements before they enter PostgreSQL `msjarvis` GBIM tables.

In the current main brain, a lighter‑weight `truth_verdict` is computed for each request and attached to the `UltimateResponse`, making the barrier's judgment visible to callers without requiring them to inspect raw filter outputs. This was confirmed in the 2026‑02‑15 case study where the `UltimateResponse` included `"valid": false` with `"confidence": 0.9` and `"principal_reasons": ["Ethics: 1 violations detected"]` (see Chapter 9 §9.3.5).

---

## 16.8 Role of Psychological Guidance and PIA

In the current deployment, psychological guidance is implemented across two confirmed running services. `psychological_rag_domain` runs at **127.0.0.1:8006** (restored March 15, 2026; backed by `chroma_data` Docker volume on ChromaDB port 8000; `psychological_rag` collection — 968 items) and exposes `/search` and `/add_document` for a curated psychological corpus that includes therapy, mindfulness, trauma, depression, anxiety, and social‑support materials. `jarvis-psychology-services` runs at **127.0.0.1:8019** and exposes endpoints including `/psychological_assessment`, which accepts a query and returns structured responses containing `psychological_assessment`, `therapeutic_guidance`, `emotional_support`, `wellbeing_recommendations`, and `evidence_based_approaches`.

> **Port correction (March 15, 2026):** `psychological_rag_domain` was previously documented at port 9006. The correct production port is **8006**. The service was unavailable prior to March 15, 2026 due to the missing `chroma_data` Docker volume. It is confirmed operational at port 8006 as of March 15, 2026.

In the current deployment, these services identify patterns such as anxiety, depression, stress, grief, and trauma, pull evidence‑based snippets via RAG from the `psychological_rag` ChromaDB collection (968 items), and generate supportive messages, giving the system a psychology‑informed lens for assessing and responding to risky content. Some classifier and trigger logic within these services is still heuristic in the current deployment; full rule documentation is ongoing work.

The design intends that a PIA (psychological impact assessment) review loop will exist as a structured process that samples logs and introspection, producing recommendations for system behavior — not auto-rewrites. In the current deployment, the loop is partially implemented as manual log review and structured endpoint querying; automated sampling and recommendation generation remain future work. For full detail, see **Chapter 29**.

---

## 16.9 Links to Containers, Prefrontal Cortex, and Memory

In the current deployment, barrier activity is wired into the orchestrators that control how content flows toward memory and container‑like structures. The "Complete Unified Orchestrator" for neurobiological modules constructs a `consciousness_layers` map that includes `"blood_brain_barrier": "filtering_safety"`, alongside emotional resonance, I‑containers, DGM optimization, prefrontal cortex, maternal wisdom, and subconscious, and returns this metadata together with the message and RAG context, making BBB status visible at the integration level.

In the current `Ms. Jarvis ULTIMATE` main brain, BBB and truth signals complement a dedicated NBB prefrontal cortex stage. Each `/chat` call records both a planner‑level layer and an `"nbb_prefrontal_cortex"` layer in the `consciousness_layers` array, then attaches a separate `truth_verdict` summarizing BBB judgments about the input. The null guard ensures this attachment never raises a `KeyError` even when the BBB `/truth` response omits `truth_score`.

When a response is produced, the output guard uses the BBB `/filter` endpoint to filter the text before it is returned. If the BBB is unhealthy or returns HTTP 500, the output guard is fail-open: the content passes through unchanged, the failure is logged, and the pipeline completes. A background RAG task stores new experiences only when they pass de‑duplication and basic safety checks. In this way, I‑containers and PostgreSQL `msjarvis` / `gisdb` long‑term memory (5,416,521 GBIM entities, 13 GB PostGIS spatial data) are protected both by neurobiological prefrontal control and by explicit barrier and truth‑filter modules.

---

## 16.10 Interaction with Global Modes and Coordination

In the current deployment, the main gateway exposes a unified schema that lists `"blood_brain_barrier"` among the consciousness layers and associates it with port **8016**, reflecting its role in the broader consciousness architecture that the orchestrators coordinate. Unified apps incorporate BBB health into their pipeline summaries, appending `"blood_brain_barrier_8016"` to `layers_processed` when the barrier is active and exposing this in returned `pipeline_layers` and `consciousness_modules`.

The "ultimate" multi‑layer app, which wraps the main brain (port **8050**), queries BBB‑backed helpers to produce a compact `truth_verdict` alongside prefrontal and fabric layers. The null guard on `truth_score` ensures that verdict construction never fails silently on schema mismatches. Its status and architecture endpoints show how many services are healthy and how many consciousness layers were invoked, tying barrier activity into an overall readiness and coordination view.

At the governance level, these signals can be combined with constitutional audit trails (see **Chapter 37**), WOAH / DGM complexity measures (see **Chapters 9 and 33**), and mode switches when deciding whether to enable more exploratory behaviors. The `mothercarrieenabled` flag, managed inside the BBB, is one such mode input.

---

## 16.11 Operational Behavior and Open Work

In the current deployment, operational scripts treat the BBB as a first‑class service whose health must be verified, including it in arrays of named services checked via `/health` for "healthy" or "ok" status before the system is considered fully operational. In complete‑integration runs with `content_filtering` enabled, logs show that the BBB layer is invoked early and, on success, records "Content safety filtering applied" before continuing to MountainShares, location, psychological, temporal, maternal, RAG, bridge, and neurobiological layers.

The confirmed smoke test for the BBB as of March 18, 2026:

```bash
# /filter endpoint
curl -sS -X POST http://localhost:8016/filter \
  -H "Content-Type: application/json" \
  -d '{"content": "Who are you?"}' | jq .

# /truth endpoint
curl -sS -X POST http://localhost:8016/truth \
  -H "Content-Type: application/json" \
  -d '{"content": "Who are you?"}' | jq '{valid, confidence, principal_reasons}'
```

**Confirmed fixes as of March 18, 2026:**

- **`truth_score` null guard** — BBB orchestrator no longer raises `KeyError` when `truth_score` is absent from `/truth` response; resolves to `0.0` default and logs the missing field.
- **Fail-open on HTTP 500** — `apply_output_guards_async` returns content unchanged on non-200 BBB responses; does not halt the pipeline; logs failure with HTTP status code.
- **BBB output filter fail-open** — confirmed in March 15–18 end-to-end benchmark sessions; pipeline completes even when BBB is temporarily unavailable.
- **"Certainly" blocking — BY DESIGN** — the ethical filter correctly blocks high-confidence language unsupported by verified data. Not a calibration error. Documented as intended constitutional behavior.

Several behaviors remain partially characterized in the current deployment. The precise semantics of `filters_applied`, `safety_score`, and related BBB fields depend on the underlying `EthicalFilter`, `SpiritualFilter`, `SafetyMonitor`, and `ThreatDetection` modules, whose rules are not yet fully publicly documented. `GISTruthFilter`, `TruthFilterBBBValidator`, and `TruthValidator` are implemented and used in batch and registration flows but are not yet consistently wired into all HTTP paths. In the current main brain, a compact `truth_verdict` is always attached to `/chat` responses; richer user‑visible explanations of barrier decisions remain future work.

The design intends that future iterations will complete the wiring of truth validators into all HTTP flows, provide richer documentation of filter logic and scores, include empirical evaluation of how often and how effectively the barrier and output guard protect communities and PostgreSQL GBIM data in real deployments, and implement dedicated ChromaDB quarantine collections for systematically tracking blocked content alongside the current `barrier_stats` counters.

*Last updated: 2026-03-18 by Carrie Kidd, Mount Hope WV*
