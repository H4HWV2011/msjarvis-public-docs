# Ms. Jarvis Academic Partnership Gateway v4.3

This document describes the public, glass‑box API surface of the Ms. Jarvis Academic Partnership Gateway and the ULTIMATE orchestrator. It corresponds to:

- `api_specs/openapi.json` (Academic Partnership Gateway v4.3)
- `api_specs/openapi-ultimate.json` (Ms. Jarvis ULTIMATE v1.0.0)

For conceptual background on how this API fits into the broader research program, see:

- **Discipline and Instruments**: https://github.com/H4HWV2011/msjarvis-public-docs/blob/main/docs/Discipline%20and%20Instruments.md  
- **Discipline / Methods**: https://github.com/H4HWV2011/msjarvis-public-docs/blob/main/docs/discipline/Methods.md  

---

## Disciplinary Context

Within Polymathmatic Geography, the API is the primary glass‑box interface of a polymathmatic instrument rather than a generic microservice layer. It exposes the control surfaces, data flows, and safeguards by which researchers can probe and reconfigure a live “thinking with place” system.

Several design choices reflect this disciplinary framing:

- **Instrument, not just service mesh**  
  The gateway aggregates more than 30 microservices—consciousness layers, GIS research, RAG, biometric proxies, constitutional guards, ethical gates, and infrastructure watchers—into a single, inspectable instrument for studying entangled social–spatial systems. The OpenAPI documents enumerate these components explicitly (for example, tags such as `GIS-RESEARCH`, `Consciousness`, `Ethical Guards`, `Infrastructure-Summary`, `Autonomous-Learner`), mirroring how scientific instruments expose subsystems for calibration and joint use.

- **Glass‑box architecture**  
  The description for v4.3 emphasizes “No blackbox components; full audit trail”. Endpoints like `/manifest`, `/architecture`, `/docs/architecture`, `/docs/services-manifest`, `/microservices/registry`, `/storage/complete`, and `/data/inventory` provide architectural and data inventories, allowing researchers to trace which services, models, and stores participate in each interaction. This aligns with the epistemic commitments described in Discipline and Instruments, where instruments must make their internal operations legible to inquiry rather than hiding them behind opaque abstractions.

- **Methodological hooks**  
  The API is structured to support multi‑phase research methods described in discipline/Methods.md, such as:
  - spatial queries and exports (`/gis/query`, `/gis/exports/csv`, `/gis/exports/json`, `/gis/exporter`);
  - multi‑layer reasoning (`/consciousness/chat`, `/consciousness/status`, `/consciousness/layers`, `/consciousness/dgm-bridges`, `/dgm`, `/woah/proxy`, `/fractal/dgm`);
  - autonomous learning and topic suggestion (`/learning/status`, `/learning/suggest`, `/research/activity`, `/research/summary`, `/knowledge/growth`);
  - constraint and governance inspection (`/constitutional/status`, `/constitutional/principles`, `/constitutional/audit`, `/constitutional/transparency`, `/guards/status`, `/guards/mother-carrie/policy`, `/guards/spiritual-root/policy`, `/guards/test`).

  These endpoints give researchers access not only to outputs (answers, maps) but to the evolving state of methods themselves: which services were used, how constitutional and ethical constraints were applied, and how knowledge stores are changing over time.

- **Consciousness and orchestration as method**  
  The ULTIMATE API (`/chat`, `/chat/async`, `/chat/status/{job_id}`, `/health`, `/`) formalizes “Ultimate Chat” as a high‑stakes reasoning method. `UltimateResponse` returns not just a textual response but also `services_used`, `consciousness_level`, `processing_time`, and `architecture_layers`. This turns each call into a small, self‑documenting experiment on a configured consciousness stack, consistent with the multi‑layer consciousness integration described in Quantarithmia documents (for example, https://github.com/H4HWV2011/msjarvis-public-docs/blob/main/docs/Quantarithmia%20Overview.md).

- **Ethical and constitutional transparency**  
  Constitutional and ethical guard endpoints make the normative infrastructure itself queryable. Researchers can list immutable principles, inspect recent blocked violations, and retrieve human‑readable policy statements associated with “Mother Carrie” and “Spiritual Root” guardrails. This corresponds to the insistence in Discipline and Instruments that instruments used in community and governance contexts must externalize their normative scaffolding, not only their technical internals.

- **Operational traces as research data**  
  Method‑tracking and infrastructure endpoints (`/tracking/health`, `/tracking/analytics/performance`, `/tracking/analytics/active`, `/tracking/traces/recent`, `/infrastructure/status`, `/infrastructure/watchdog/status`, `/infrastructure/locks/active`, `/infrastructure/nohup/processes`, `/research/activity`, `/research/summary`, `/knowledge/growth`) transform operational traces into first‑class research data. They support methodological questions about how the instrument allocates attention, how often it consults certain services, and how knowledge and infrastructure evolve during a study—an explicit concern in polymathmatic methods.

In combination, these features make the API documentation not just a technical reference but a map of the instrument’s disciplinary commitments: spatially grounded, multi‑modal, ethically constrained, and open to inspection at every layer.

---

## Core APIs (Gateway v4.3)

This section summarizes major endpoint families defined in `Ms. Jarvis Academic Partnership Gateway v4.3`.

- **Core and health**
  - `/`, `/health`, `/registry`  
  - `/manifest`, `/architecture`  
  - `/docs/architecture`, `/docs/services-manifest`  

- **Consciousness and orchestration**
  - `/consciousness/chat`, `/consciousness/status`, `/consciousness/layers`, `/consciousness/dgm-bridges`  
  - `/dgm`, `/fractal/dgm`, `/woah/proxy`, `/ollama/orchestrator`, `/qualia`  

- **Spatial and GIS**
  - `/gis/query`, `/gis/exports/csv`, `/gis/exports/json`, `/gis/health`, `/gis/exporter`  

- **RAG, models, and storage**
  - `/models`, `/rag/supervisor`  
  - `/storage/chromadb`, `/storage/complete`, `/data/inventory`  

- **Identity, governance, and ethics**
  - `/biometric/ueid`, `/ueid/proxy`  
  - `/constitutional/status`, `/constitutional/principles`, `/constitutional/audit`, `/constitutional/transparency`  
  - `/guards/status`, `/guards/mother-carrie/policy`, `/guards/spiritual-root/policy`, `/guards/test`  
  - `/license` (AGPL‑3.0, source transparency)

- **Autonomous learning and research monitoring**
  - `/learning/status`, `/learning/suggest`  
  - `/research/activity`, `/research/summary`, `/knowledge/growth`  

- **Infrastructure and method tracking**
  - `/tracking/health`, `/tracking/analytics/performance`, `/tracking/analytics/active`, `/tracking/traces/recent`  
  - `/infrastructure/watchdog/status`, `/infrastructure/scheduler/venv-status`, `/infrastructure/locks/active`, `/infrastructure/nohup/processes`, `/infrastructure/status`  

- **User access and protection**
  - `/auth/token`, `/api/protected/status`  

These families should be read together with the disciplinary framing in Discipline and Instruments and discipline/Methods, which explain how to use the gateway not only to “call models” but to design, observe, and critique the behavior of the polymathmatic instrument as it operates in real communities and geographies.

---

## ULTIMATE API (High‑stakes Orchestration)

The ULTIMATE OpenAPI specification defines a focused surface for high‑stakes, deeply orchestrated reasoning.

- `GET /health` – liveness of the ULTIMATE service.  
- `GET /` – root description of the ULTIMATE orchestrator.  
- `POST /chat` – synchronous “Ultimate Chat” with structured `UltimateResponse`.  
- `POST /chat/async` and `GET /chat/status/{job_id}` – asynchronous job handling for longer or more complex conversations.

`UltimateResponse` explicitly reports:

- `response` – the synthesized answer.  
- `services_used` – list of subsystems consulted.  
- `consciousness_level` – declarative indicator of which consciousness stack was engaged.  
- `processing_time` – elapsed time.  
- `architecture_layers` – number of architecture layers traversed.

This design continues the glass‑box commitment: every high‑stakes answer is accompanied by a minimal provenance record suitable for methodological analysis and governance review.

For guidance on integrating these APIs into research workflows—such as spatio‑theological case studies, governance simulations, or community co‑analysis—see:

- https://github.com/H4HWV2011/msjarvis-public-docs/blob/main/docs/discipline/Methods.md  
- https://github.com/H4HWV2011/msjarvis-public-docs/blob/main/docs/Discipline%20and%20Instruments.md  
