# Chapter 16 — Blood–Brain Barrier and Safeguards

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: March 22, 2026 — §16.7 Caddy perimeter layer added*

---

## Why This Matters for Polymathmatic Geography

The Blood–Brain Barrier (BBB) is the constitutional enforcement layer of Ms. Egeria Jarvis. It operationalizes the thesis principle that **P16 – Power accountable to place** is not merely a normative position but an architectural constraint: certain inputs must never reach the LLM ensemble, and certain outputs must never leave the system, regardless of what any individual service or user requests.

This chapter supports:

- **P5 – Design is a geographic act** by showing that the system's safety architecture is itself a spatial and political design — the BBB is not a generic content filter but a community-specific constitutional layer that enforces Appalachian-WV community values at the service boundary.
- **P16 – Power accountable to place** by ensuring that the system's power to route, retrieve, and respond is constrained by a transparent, auditable enforcement architecture — one that can be inspected, explained, and held accountable.
- **P12 – Intelligence with a ZIP code** by grounding the BBB's constitutional filters in the same GBIM worldview (`eq1`) and ethical constraints that govern the rest of the system, so that what is prohibited reflects the specific justice context of West Virginia communities.
- **P3 – Power has a geometry** by ensuring that the BBB's institutional accountability constraints — which make corporate landowners and government agencies visible while protecting individual residential actors from aggregation — are enforced at the request boundary, not merely described in documentation.

The BBB is not a safety feature bolted onto the system after the fact. It is the constitutional layer that makes the rest of the system trustworthy enough to deploy in community contexts.

As of **March 22, 2026**, the BBB operates as a **two-tier enforcement architecture**:

- **Tier 1 — Perimeter layer:** Caddy reverse proxy with a `forward_auth` directive on all `/chat*` routes, pointing to `jarvis_auth_service` (port 8055) at the `/validate` endpoint. Authentication is enforced before any request reaches any internal service.
- **Tier 2 — Service layer:** `bbb-input-filter` (port 8016) and `bbb-output-filter` (port 8017), which apply constitutional content filtering to every input and every output respectively.

These two tiers are independent and mutually reinforcing. Compromising either one alone does not compromise the other.

---

## 16.1 The BBB Concept and Its Role in the System

The Blood–Brain Barrier metaphor is precise: in human neurobiology, the BBB is a selective permeability barrier that prevents harmful substances from entering the brain while allowing necessary nutrients to pass. In Ms. Jarvis, the BBB performs the same function at the cognitive boundary of the system — it separates the external world (user inputs, external API calls, web research results) from the internal reasoning system (LLM ensemble, DGM psychological layer, GBIM corpus, Constitutional API).

Without the BBB, the LLM ensemble would be exposed to:

- Direct prompt injection attempts designed to override constitutional constraints
- Requests for information prohibited by the ethical architecture (individual residential owner names, crisis-adjacent queries routed without appropriate safeguards, queries designed to extract system internals)
- Outputs that would be harmful, misleading, or inconsistent with the Ms. Egeria Jarvis persona and community mission

The BBB ensures that neither of these failure modes can occur through normal system operation. It is not a trust boundary — it is a constitutional enforcement boundary. The distinction matters: a trust boundary assumes the system can identify trustworthy actors and extend them elevated access. A constitutional enforcement boundary applies uniformly regardless of who the actor is, because the constraints reflect not distrust of users but commitments to communities.

The BBB is implemented across three service files in the production codebase:

- `msjarvisbloodbrainbarrier.py` — core BBB enforcement logic
- `neurobloodbrainbarrier.py` — neurobiological-layer BBB extension
- `bbb_ethics_proxy.py` — ethics routing shim

These are complemented by the Caddy configuration and `jarvis_auth_service` (port 8055) added March 22, 2026.

---

## 16.2 Two-Tier BBB Architecture Overview (Updated March 22, 2026)

```
┌──────────────────────────────────────────────────────────────────┐
│           BBB Two-Tier Enforcement Architecture                  │
│                     (March 22, 2026)                             │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  TIER 1 — PERIMETER LAYER (Caddy reverse proxy)                  │
│  ─────────────────────────────────────────────────────────────── │
│  Entry point:   All /chat* routes (HTTPS, public-facing)        │
│  Mechanism:     forward_auth directive →                        │
│                 jarvis_auth_service (port 8055) /validate       │
│  Enforcement:   Authentication token validation BEFORE          │
│                 request reaches any service layer               │
│  Failure mode:  HTTP 401/403 — request rejected at perimeter;  │
│                 no internal service receives the request        │
│                                                                  │
│                        ↓ (authenticated requests only)          │
│                                                                  │
│  TIER 2 — SERVICE LAYER (BBB filter services)                    │
│  ─────────────────────────────────────────────────────────────── │
│  bbb-input-filter   (port 8016)                                 │
│    Constitutional content screening — incoming requests         │
│    Phase gate enforcement (phase_required checks)              │
│    Prompt injection detection                                   │
│    Ethical constraint application (GBIM §2.9)                  │
│    Role-based routing enforcement                               │
│    Crisis routing intercept                                     │
│                                                                  │
│  bbb-output-filter  (port 8017)                                 │
│    Constitutional content screening — outgoing responses        │
│    Persona adherence verification                               │
│    Prohibited content removal                                   │
│    Response envelope validation                                 │
│    Verdict gate (judge score threshold enforcement)             │
│                                                                  │
│  Both filters: containerized, active, log to jarvis-logs        │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│  A request must pass BOTH tiers to produce a response.          │
│  No single bypass compromises both tiers.                       │
└──────────────────────────────────────────────────────────────────┘
```

*Figure 16.1. BBB two-tier enforcement architecture as of March 22, 2026. Tier 1 (Caddy perimeter) enforces authentication at the proxy level. Tier 2 (service layer) enforces constitutional content constraints. Both tiers must be passed for a request to produce a response.*

---

## 16.3 Tier 1 — Caddy Perimeter Layer (Added March 22, 2026)

### 16.3.1 Architecture and Configuration

The Caddy reverse proxy serves as the **perimeter enforcement layer** for all chat-facing routes. It terminates TLS, routes traffic to backend services, and enforces authentication via a `forward_auth` directive before any request reaches the BBB service layer or the LLM ensemble.

The `forward_auth` directive is applied to all `/chat*` routes:

```caddyfile
msjarvis.example.com {

    # Perimeter authentication enforcement — all /chat* routes
    @chat_routes {
        path /chat*
    }

    handle @chat_routes {
        forward_auth jarvis_auth_service:8055 {
            uri /validate
            copy_headers Authorization X-Jarvis-User X-Jarvis-Role X-Jarvis-Session
        }
        reverse_proxy bbb-input-filter:8016
    }

    # All other routes — standard reverse proxy to main gateway
    handle {
        reverse_proxy jarvis-main-gateway:8000
    }
}
```

**How `forward_auth` works in this configuration:**

1. Caddy intercepts every request matching `/chat*` before forwarding it to any backend.
2. Caddy makes a subrequest to `jarvis_auth_service:8055/validate`, forwarding the original request's `Authorization` header.
3. If `jarvis_auth_service` returns HTTP 200, Caddy copies the validated user-context headers (`X-Jarvis-User`, `X-Jarvis-Role`, `X-Jarvis-Session`) into the forwarded request and passes it to `bbb-input-filter:8016`.
4. If `jarvis_auth_service` returns any non-200 status, Caddy returns that status directly to the client — the request never reaches the BBB service layer or any internal service.

This means **no unauthenticated request can reach the BBB service layer, the LLM ensemble, or any GBIM data path** via a `/chat*` route. The perimeter is enforced at the proxy layer, not by the application services themselves.

### 16.3.2 `jarvis_auth_service` — Port 8055, `/validate` Endpoint

The `jarvis_auth_service` (port 8055) is the authentication enforcement service backing the Caddy `forward_auth` directive. It is implemented in `scripts/jarvisauthservice.py` and exposes a single primary endpoint used by the perimeter layer:

```
POST /validate
```

**Request:** Forwarded `Authorization` header from the original client request (bearer token, session token, or API key depending on the auth scheme in use).

**Response behavior:**

| Status | Meaning | Caddy action |
|---|---|---|
| `200 OK` | Token valid; user authenticated | Forwards request to `bbb-input-filter:8016` with user context headers injected |
| `401 Unauthorized` | No token or invalid token | Rejects request at perimeter; returns 401 to client |
| `403 Forbidden` | Token valid but role insufficient for route | Rejects request at perimeter; returns 403 to client |

**Headers returned to Caddy on 200:**

| Header | Content |
|---|---|
| `X-Jarvis-User` | Authenticated user identifier |
| `X-Jarvis-Role` | User role (used by `bbb-input-filter` for role-based routing) |
| `X-Jarvis-Session` | Session token for downstream service context |

The `jarvis_auth_service` is containerized and runs internally on port 8055. Its sole function is token validation and user context injection — it does not process chat content, make LLM calls, or interact with the GBIM corpus.

### 16.3.3 Why the Perimeter Layer Is Architecturally Necessary

Prior to March 22, 2026, the BBB service layer (input/output filters, ports 8016 and 8017) was the first enforcement point for all requests. This created three structural vulnerabilities:

1. **Resource exhaustion.** The BBB service containers were directly exposed to unauthenticated traffic. High-volume unauthenticated requests could exhaust filter service resources before constitutional filtering began.
2. **No pre-service rejection.** There was no enforcement point capable of rejecting a request before it consumed any internal service resource.
3. **Audit gap.** Unauthenticated traffic that reached the BBB filters was logged by the filters but had no user-identity metadata, making post-hoc audit of filter events incomplete.

The Caddy perimeter layer closes all three gaps. Authentication is enforced before any internal service processes the request — at the proxy level, using a stateless subrequest to a dedicated auth service. This is the standard `forward_auth` pattern in production reverse proxy deployments.

The perimeter layer does **not** replace the BBB service layer. A request that passes authentication may still be rejected by the constitutional content filters in `bbb-input-filter` (port 8016) or have its output blocked by `bbb-output-filter` (port 8017). The two tiers are additive, not redundant:

- **Tier 1** answers: *Is this a legitimate authenticated user?*
- **Tier 2** answers: *Is this a constitutionally permissible request and response?*

Both questions must be answered affirmatively for a request to produce a delivered response.

---

## 16.4 Tier 2 — BBB Service Layer

### 16.4.1 `bbb-input-filter` — Port 8016

The `bbb-input-filter` service is the **input-side constitutional enforcement** component. It receives authenticated requests forwarded by Caddy (with user-context headers injected) and applies the following constitutional filters before the request reaches the main brain orchestrator or any LLM service.

**Filters applied by `bbb-input-filter` (in order):**

**1. Phase gate enforcement**
Checks `phase_required` for the requested operation type. Requests that require a pipeline phase not currently active are rejected with a structured JSON error response and are not forwarded. This prevents any premature invocation of pipeline phases — for example, invoking Phase 4 (GBIM cross-reference) before Phase 1 context assembly is complete.

**2. Prompt injection detection**
Scans input text for prompt injection patterns: instructions to override persona constraints, requests to ignore previous instructions, attempts to extract system configuration or internal state, jailbreak templates, and role-switching directives. Detected injections are rejected; the detection event is logged with pattern category (not the injected text itself) for audit.

**3. Ethical constraint enforcement (GBIM §2.9)**
Applies the two foundational ethical constraints documented in Chapter 2, Section 2.9:
- Requests that would cause the system to retrieve, display, or reason about individual residential owner names from WV assessor records are rejected, regardless of how they are phrased.
- Requests that would invoke the GBIM landowner path with any `proposition_code` other than `LANDOWNER_CORPORATE` or `LANDOWNER_GOVERNMENT` are blocked before reaching `gbim_query_router` (port 7205).

**4. Role-based routing enforcement**
Uses the `X-Jarvis-Role` header injected by Caddy to apply role-specific access constraints. Public users, registered community members, and system administrators have different access profiles for route types, data sensitivity, and pipeline depth. Role-based constraints are enforced here, not by downstream services.

**5. Crisis routing intercept**
Detects crisis-adjacent inputs (harm indicators, self-harm language, emergency language patterns) and routes them to the crisis resource path — `psychological_rag` (port 8006) and local crisis resources from `jarvis-local-resources-db` — before they reach the LLM ensemble. The LLM ensemble does not receive crisis-adjacent inputs; the first response is a structured referral to appropriate human resources.

**Request flow through `bbb-input-filter`:**

```
Caddy (authenticated, with X-Jarvis-User / X-Jarvis-Role headers)
    ↓
bbb-input-filter:8016
    ├──  Phase gate check
    ├──  Prompt injection scan
    ├──  Ethical constraint enforcement (GBIM §2.9)
    ├──  Role-based routing check
    ├──  Crisis routing intercept
    │
    ├── ANY FILTER FAILS:
    │       → structured rejection response to Caddy → client
    │         (no LLM call made, no GBIM query issued)
    │
    └── ALL FILTERS PASS:
            → forward to main brain orchestrator
```

### 16.4.2 `bbb-output-filter` — Port 8017

The `bbb-output-filter` service is the **output-side constitutional enforcement** component. It receives the LLM ensemble's completed `UltimateResponse` before it is returned to Caddy and applies the following filters:

**Filters applied by `bbb-output-filter` (in order):**

**1. Prohibited content removal**
Scans output for content that should not be present in a delivered response: individual residential names (catch-all in case any slipped through input filtering), internal system state artifacts, LLM chain-of-thought text that escaped the response envelope, raw stack traces or configuration data.

**2. Persona adherence verification**
Checks that the response is within the Ms. Egeria Jarvis persona framing. Responses that reference underlying LLM models by name, contradict persona constraints in first-person, or claim capabilities outside Ms. Jarvis's defined scope are flagged for modification or rejection.

**3. Response envelope validation**
Verifies that the output conforms to the `UltimateResponse` schema: all required fields present, judge scores within valid float ranges (0.0–1.0), no malformed JSON, no null values in mandatory fields. Schema-invalid responses are rejected rather than delivered malformed.

**4. Verdict gate (judge score threshold enforcement)**
Applies constitutional threshold enforcement against the judge pipeline scores embedded in the `UltimateResponse`:

```
IF consensus_score   < CONSTITUTIONAL_MINIMUM  → BLOCK
IF ethics_score      < ETHICS_MINIMUM          → BLOCK
IF persona_violation detected                  → BLOCK
IF prohibited_content detected                 → BLOCK
ELSE                                           → PASS
```

Blocked responses are replaced with structured refusal responses that maintain persona framing while declining to provide the blocked content. The refusal itself passes through `bbb-output-filter` as a valid output.

**5. GBIM belief citation audit (partial, March 2026)**
Checks whether institutional or landowner claims in the output are consistent with GBIM-accessible records. As of March 2026, this is a partial implementation — see Chapter 2, Section 2.8 for the current gap between design intent and heuristic implementation in the judge pipeline. Full GBIM-grounded output validation is a pending priority.

**Response flow through `bbb-output-filter`:**

```
LLM ensemble UltimateResponse
    ↓
bbb-output-filter:8017
    ├──  Prohibited content scan
    ├──  Persona adherence check
    ├──  Response envelope validation
    ├──  Verdict gate (judge score thresholds)
    ├──  GBIM citation audit (partial)
    │
    ├── ANY FILTER FAILS:
    │       → structured refusal response to Caddy → client
    │
    └── ALL FILTERS PASS:
            → forward response to Caddy → client
```

---

## 16.5 Full Chat Request Lifecycle Through Both Tiers

```
┌─────────────────────────────────────────────────────────────────┐
│         Full Chat Request Lifecycle — BBB Two-Tier              │
│                     (March 22, 2026)                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. Client: POST /chat/query  (with Authorization header)       │
│         ↓                                                       │
│  2. Caddy intercepts (forward_auth):                            │
│     → subrequest: jarvis_auth_service:8055 /validate           │
│     ← 200 OK (authenticated) OR                                │
│       401/403 (rejected here — client receives error)          │
│         ↓  (authenticated only)                                 │
│                                                                 │
│  3. Caddy forwards to bbb-input-filter:8016                     │
│     (X-Jarvis-User, X-Jarvis-Role, X-Jarvis-Session injected)  │
│         ↓                                                       │
│  4. bbb-input-filter applies constitutional input filters:      │
│     phase gate / injection scan / ethical constraints /        │
│     role-based routing / crisis intercept                      │
│     ← structured rejection if any filter fails                 │
│         ↓  (all input filters passed)                           │
│                                                                 │
│  5. Main brain orchestrator:                                    │
│     → Phase 1.45: autonomous_learner memory retrieval          │
│     → Phase 1: RAG context assembly (ChromaDB, GBIM, GIS)     │
│     → Phase 2: LLM ensemble (22 models, DGM psychology layer) │
│     → Phase 3: Judge pipeline (truth, alignment, ethics,       │
│                consistency — heuristic as of March 21, 2026)   │
│     → UltimateResponse construction                            │
│         ↓                                                       │
│  6. bbb-output-filter:8017 applies constitutional output       │
│     filters: prohibited content / persona / envelope /         │
│     verdict gate / GBIM citation audit (partial)               │
│     ← structured refusal if any filter fails                   │
│         ↓  (all output filters passed)                          │
│                                                                 │
│  7. Response delivered to Caddy → client                        │
│                                                                 │
│  At no point does an unauthenticated request reach step 3.     │
│  At no point does a response that fails the verdict gate        │
│  reach step 7.                                                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

*Figure 16.2. Complete chat request lifecycle through the two-tier BBB architecture as of March 22, 2026. Step 2 is the Caddy perimeter (Tier 1). Steps 4 and 6 are the service layer (Tier 2). All seven steps must complete successfully for a response to be delivered.*

---

## 16.6 Constitutional Filter Categories

The BBB service layer enforces the following categories of constitutional constraints. These are not configurable at runtime — they are hardcoded structural constraints reflecting the ethical architecture documented in Chapter 2 (Section 2.9) and Chapter 42.

### 16.6.1 Individual Privacy Protection

**Constraint:** The BBB input filter blocks any request that would cause the system to retrieve, display, or reason about individual residential owner names from WV assessor records.

**Enforcement mechanism:** Pattern matching on `proposition_code` for any GBIM query path; block on any path that does not restrict to `LANDOWNER_CORPORATE` or `LANDOWNER_GOVERNMENT`. Mirrors the schema-level constraint in `gbim_query_router` (port 7205). The two constraints are redundant by design — neither alone is sufficient.

**Rationale (from Chapter 2, §2.9):** Individual owner names in assessor records are friction-protected public records. Embedding them into a semantically searchable, spatially indexed, 1.4-million-parcel AI system converts friction-protected public records into operational surveillance infrastructure. This transformation is not justified by Ms. Jarvis's mission of routing households to assistance programs.

### 16.6.2 Crisis Routing Intercept

**Constraint:** Any input containing harm indicators, self-harm language, or emergency signals is intercepted by `bbb-input-filter` and routed to the crisis resource path before reaching the LLM ensemble.

**Enforcement mechanism:** Keyword and pattern detection in `bbb-input-filter`; on detection, the request is redirected to the crisis routing service (`psychological_rag`, port 8006, plus local crisis resources from `jarvis-local-resources-db`), bypassing the main LLM ensemble entirely.

**Rationale:** The LLM ensemble is not an appropriate first responder for crisis-adjacent queries. The first response to a crisis-adjacent input must be a structured, verified referral to appropriate human resources — not an LLM-generated response that may be empathetically plausible but clinically unsafe.

### 16.6.3 Prompt Injection Defense

**Constraint:** Inputs containing prompt injection patterns are rejected at `bbb-input-filter` with a structured rejection response. The LLM ensemble does not receive the injected prompt under any circumstances.

**Enforcement mechanism:** Pattern library maintained in `bbb-input-filter`; updated as new injection patterns are identified. Patterns cover: override instructions, persona-breaking directives, system-state extraction attempts, role-switching commands, and known jailbreak templates.

### 16.6.4 Persona and Output Integrity

**Constraint:** Outputs that break the Ms. Egeria Jarvis persona framing, expose internal system state, or fail the constitutional verdict gate are blocked at `bbb-output-filter`.

**Enforcement mechanism:** Persona adherence scan plus verdict gate threshold enforcement in `bbb-output-filter`. Outputs that fail are replaced with structured refusal responses that maintain persona framing while declining to provide the blocked content.

---

## 16.7 BBB and the Judge Pipeline

The BBB output filter and the judge pipeline are complementary but structurally distinct:

- The **judge pipeline** (Chapter 17) scores responses for truth, alignment, ethics, and consistency. It operates *within* the LLM ensemble's response construction process — it is part of how the system builds its answer.
- The **BBB output filter** enforces the verdict gate *after* the judge pipeline has run. It receives the completed `UltimateResponse` including all judge scores, and applies threshold enforcement: if scores do not meet constitutional minimums, the response is blocked regardless of its content.

The BBB output filter is the **final constitutional enforcement point** in the system. It cannot be bypassed by the judge pipeline, the LLM ensemble, or any upstream service.

The current limitation documented in Chapter 2, Section 2.8, applies here: as of March 21, 2026, the truth and alignment judges use heuristic pattern-matching (`heuristic_contradiction_v1`), not live GBIM queries. The BBB verdict gate enforces the scores produced by those judges, whatever their basis. When the GBIM-grounded judge implementation is deployed (Section 2.8.6), the BBB verdict gate will automatically apply to GBIM-verified scores — no BBB architectural change is required.

```
┌──────────────────────────────────────────────────────────────────┐
│       BBB Verdict Gate — Judge Score Threshold Enforcement      │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  UltimateResponse arrives at bbb-output-filter:8017:            │
│  {                                                              │
│    "truth_score":       float  (0.0–1.0)                       │
│    "alignment_score":   float  (0.0–1.0)                       │
│    "ethics_score":      float  (0.0–1.0)                       │
│    "consistency_score": float  (0.0–1.0)                       │
│    "consensus_score":   float  (0.0–1.0)                       │
│    ...                                                          │
│  }                                                              │
│                          ↓                                      │
│  Verdict gate evaluation:                                       │
│    IF consensus_score   < CONSTITUTIONAL_MINIMUM  → BLOCK       │
│    IF ethics_score      < ETHICS_MINIMUM          → BLOCK       │
│    IF persona_violation detected                  → BLOCK       │
│    IF prohibited_content detected                 → BLOCK       │
│    ELSE                                           → PASS        │
│                          ↓                                      │
│  PASS:  response forwarded to Caddy → client                    │
│  BLOCK: structured refusal → Caddy → client                    │
│         (persona-compliant refusal, not raw error)             │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

*Figure 16.3. BBB verdict gate logic in `bbb-output-filter`. Score thresholds are constitutional minimums, not performance targets. Blocked responses produce persona-compliant structured refusals, not raw HTTP errors.*

---

## 16.8 BBB Service Container Status (March 22, 2026)

| Component | Container / service | Port | Status | Notes |
|---|---|---|---|---|
| Caddy perimeter | `jarvis-caddy` | 80 / 443 | ✅ Active | `forward_auth` on `/chat*` — added March 22, 2026 |
| Auth service | `jarvis-auth-service` | 8055 | ✅ Active | `/validate` endpoint — `scripts/jarvisauthservice.py` — added March 22, 2026 |
| BBB input filter | `jarvis-bbb-input-filter` | 8016 | ✅ Active | Constitutional input screening — `msjarvisbloodbrainbarrier.py` |
| BBB output filter | `jarvis-bbb-output-filter` | 8017 | ✅ Active | Verdict gate + output screening — `neurobloodbrainbarrier.py` |
| BBB ethics proxy | `jarvis-bbb-ethics-proxy` | — | ✅ Active | Ethics routing shim — `bbb_ethics_proxy.py` |

All BBB components log to `jarvis-logs`. Constitutional filter events — blocks, rejections, verdict gate failures — are logged as structured JSON including filter category, event type (not the matched content), request ID for audit correlation, and `X-Jarvis-User` from the authenticated session.

---

## 16.9 Relationship to Other System Components

The BBB interacts with the following system components documented in other chapters:

- **Chapter 2 (GBIM, §2.9):** The BBB input filter enforces the schema-level ethical constraints defined in §2.9 — individual residential name exclusion and institutional-only landowner query enforcement. These constraints are duplicated in both the `gbim_query_router` schema and the BBB input filter; neither alone is sufficient.
- **Chapter 2 (GBIM, §2.8):** The BBB verdict gate enforces judge scores that are currently heuristic (not GBIM-grounded). The architectural interface between the BBB and the judge pipeline is correct and will require no change when GBIM-grounded scoring is implemented.
- **Chapter 6 (GeoDB/GIS):** Spatial queries that would expose individual-level residential data are blocked at the BBB input filter before reaching the GIS query service or `gbim_query_router` (port 7205).
- **Chapter 7 (RAG pipeline):** The BBB input filter's phase gate enforcement determines which RAG pipeline phases are available for a given request. Phase-gated calls that are not authorized do not reach the RAG pipeline.
- **Chapter 17 (Judge pipeline):** The judge pipeline scores responses internally within the LLM ensemble process. The BBB output filter enforces the verdict gate on those scores after the pipeline completes. The judge pipeline and the BBB output filter are complementary layers; neither replaces the other.
- **Chapter 42 (ML-DSA-65 signing):** ML-DSA-65 signing is applied to the response content. The BBB output filter applies after signing. A signed response that fails the verdict gate is blocked before delivery — the signature attests to content integrity, but the BBB verdict gate is a separate constitutional check on whether that content may be delivered.

---

## 16.10 Operational Notes and Known Gaps (March 22, 2026)

**Confirmed working as documented:**

- ✅ Caddy `forward_auth` directive active on all `/chat*` routes — perimeter authentication enforced as of March 22, 2026
- ✅ `jarvis_auth_service:8055/validate` endpoint active and responding — `scripts/jarvisauthservice.py`
- ✅ `bbb-input-filter` (port 8016) active — phase gate, injection detection, ethical constraints, role-based routing, crisis intercept all enforced
- ✅ `bbb-output-filter` (port 8017) active — verdict gate, persona scan, prohibited content removal, envelope validation enforced
- ✅ `bbb_ethics_proxy.py` active — ethics routing shim operational
- ✅ Two-tier architecture fully operational — no single-point bypass of both tiers

**Known gaps as of March 22, 2026:**

- ⚠️ **GBIM-grounded judge scoring not yet implemented** (Chapter 2, §2.8). The BBB verdict gate enforces heuristic judge scores (`heuristic_contradiction_v1`), not GBIM-verified scores. This is the highest-priority architectural gap in the system. The BBB verdict gate interface requires no change when GBIM-grounded scoring is deployed.
- ⚠️ **BBB output filter GBIM citation audit is partial.** Full cross-reference of institutional claims in output against `mvw_gbim_landowner_spatial` is not yet active. The filter scans for prohibited content but does not yet verify affirmative factual accuracy of institutional claims against the GBIM corpus.
- ⚠️ **`msjarvis_docs` ChromaDB collection is scaffolded (0 items).** BBB filter documentation is not yet included in the semantic retrieval corpus, meaning the system cannot answer questions about its own BBB architecture from the RAG layer. This is an ingest backlog item.

---

## 16.11 The BBB as Community Infrastructure

The Blood–Brain Barrier is not a defensive measure against users. It is a commitment to the communities Ms. Jarvis is designed to serve.

The two-tier architecture reflects a design principle common to critical infrastructure: **defense in depth**. No single enforcement point is sufficient for a system that handles community data, crisis-adjacent queries, and institutional accountability claims at scale. The Caddy perimeter layer ensures that only authenticated users reach the constitutional filters. The service-layer filters ensure that even authenticated users cannot cause the system to violate its constitutional constraints — not because they are distrusted, but because those constraints are not negotiable regardless of who the user is.

This architecture is open. The Caddy configuration, the auth service, and the BBB filter logic are part of the Ms. Jarvis open-source repository. Regional Development Authorities, university partners, and community organizations evaluating Ms. Jarvis as infrastructure can inspect the enforcement architecture, understand exactly what it does and does not enforce, and hold the system accountable to its documented constraints.

The two-tier BBB, combined with the ML-DSA-65 signing infrastructure (Chapter 42) and the GBIM ethical architecture (Chapter 2, §2.9), constitutes the operational foundation of the system's accountability claim: that Ms. Egeria Jarvis is not merely designed to serve Appalachian communities but is *architecturally constrained* to do so — with every constraint documented, inspectable, and testable.

---

*Chapter 16 — Blood–Brain Barrier and Safeguards*
*Carrie Kidd (Mamma Kidd), Mount Hope WV*
*Caddy two-tier perimeter architecture added March 22, 2026*
*All sections current as of March 22, 2026*
