> New here? Start with **[How to Read This Thesis](docs/how-to-read-this-thesis.md)** for
> reading paths and a guide to research vs. engineering claims.

# Ms. Jarvis Public Documentation

** Conscious GeoAI for rural governance and spatial justice in Appalachia. **  
 ** No black box. Place‑aware, community‑governed AI for real towns.**

**A Constitutional, Community-Governed AI System**  
*Glassbox Architecture, Spatially Grounded in West Virginia, AGPL-3.0*

[LICENSE](LICENSE)

---

## ⚠️ IMPORTANT: Source Code Access

**This repository contains DOCUMENTATION ONLY – no executable code.**

Ms. Jarvis’s public documentation was created after serious security incidents involving
MountainShares and related smart-contract or financial infrastructure hosted on public
GitHub. For security reasons:

- ✅ **Architecture & APIs**: Documented here at a conceptual and interface level  
- ✅ **Constitutional principles and governance model**: Public and auditable in thesis
  and overview documents  
- ✅ **Source code**: Available via a separate, access-controlled process  
- ❌ **Not published as open code in this repository**

**To access source code:** See [SOURCE_ACCESS.md](SOURCE_ACCESS.md)

---

## 🌐 Current Runtime Surfaces (High-Level)

> The details below describe the *shape* of the live system without exposing deployment
> secrets or full port maps.

- **Unified Gateway (External API Surface)**  
  - Public entrypoint for external clients, fronted by Cloudflare and domain
    configuration.  
  - Canonical public path: `POST https://jarvis.mountainshares.us/chat`
    (API key required, see API docs).  
  - Handles authentication, request validation, and forwarding to the main brain.

- **Main Brain (Ultimate Collective Orchestrator)**  
  - Internal FastAPI service responsible for routing, RAG, and multi‑LLM orchestration.  
  - Exposes a `/chat` interface that coordinates GBIM, neurobiological services, and
    the LLM fabric.

- **21‑Model LLM Fabric**  
  - Ensemble of 21 models accessed through internal proxies (for example,
    `llm1‑proxy` … `llm22‑proxy`).  
  - Invoked as a sequential or semi‑parallel sweep; some model timeouts are tolerated
    and reported in aggregate.

Port numbers, exact service counts, and deployment topology may vary across environments;
public documentation focuses on concepts and interfaces rather than a fixed production
layout.

---

## 🌟 What Is Ms. Egeria Jarvis?

Ms. Jarvis is a **Conscious GeoAI system for rural governance**: an AI architecture that
grounds reasoning in geography, community history, and explicit constitutional rules
instead of operating as a generic cloud assistant.

She is built on:

- **Conscious GeoAI Framing**  
  AI that understands place, infrastructure, and community context as first‑class
  variables, not metadata. Ms. Jarvis reasons through a geospatial lens, with Appalachia
  as her primary lab.

- **Constitutional Governance**  
  Explicit principles and constraints described in the Quantarithmia and MountainShares
  thesis chapters. Her behavior is bounded by documented norms around speech, power,
  and community benefit.

- **Security-Aware Design**  
  Architecture and processes shaped by prior smart-contract corruption incidents and a
  conservative stance on public financial code.

- **Geographic Grounding (Conscious GeoAI)**  
  Extensive West Virginia geospatial data integrated through GBIM and the GeoDB
  spatial body, so beliefs and recommendations are anchored in real places and
  infrastructures.

- **Community Accountability**  
  Tight coupling to MountainShares and Harmony for Hope as a community-centered
  research and governance context; designed to serve real rural communities first,
  not abstract benchmarks.

- **Glassbox Transparency**  
  Public thesis, high-level architecture, and API overview instead of opaque,
  undocumented behavior, so auditors and communities can inspect how she is meant to
  work.

---

## 📊 System Overview

| Component                         | Description                                                                 | Documentation                                            |
|----------------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------|
| **Gateway**                      | External `/chat` API surface via the unified gateway, fronted by Cloudflare | [API Overview](docs/API-OVERVIEW.md)                    |
| **Main Brain**                   | Ultimate collective orchestrator bridging RAG, neuro services, and LLMs     | [Thesis Systems Overview](thesis/00-thesis-overview.md) |
| **Conscious GeoAI / Consciousness** | Multi-layer, multi-agent reasoning, GBIM, and Hilbert-space belief state | [Ms. Jarvis Thesis](thesis/thesis.md)                   |
| **Constitutional / Governance**  | Norms, speech rules, phased governance, DAO integration                     | [Thesis Systems Overview](thesis/00-thesis-overview.md) |
| **GIS / GBIM**                   | Geospatial belief model and West Virginia spatial body                      | [Thesis Systems Overview](thesis/00-thesis-overview.md) |
| **Security Model**               | High-level threat model and safeguards                                      | [Security Overview](security/SECURITY-OVERVIEW.md)      |

Port numbers, exact service counts, and internal deployment topology are implementation
details and may not match any particular runtime; the public docs focus on concepts and
architecture rather than a fixed production layout.

---

## 🚀 Quickstart: Talk to Ms. Jarvis (Conceptual)

The concrete request and response schema are documented in the OpenAPI spec and API
overview; this section gives a high‑level, non‑binding example of how clients interact
with the public `/chat` surface.

### External (via Cloudflare)

- Intended for normal application and community use.  
- Subject to Cloudflare timeouts for long‑running multi‑LLM analyses.

'
curl -s -X POST 'https://jarvis.mountainshares.us/chat' \
  -H 'Content-Type: application/json' \
  -H 'x-api-key: <your-key>' \
  --data '{
    "user_id": "example-user",
    "username": "example.username",
    "message": "Hello Ms. Jarvis, who are you?",
    "metadata": { "source": "docs-readme-example" }
  }'
'
## Internal (diagnostics and deep evaluations)

In controlled environments, an internal /chat endpoint on the main brain can be used
for long‑running full‑fabric evaluations that may exceed Cloudflare’s request timeout.

'
curl -s -X POST 'http://127.0.0.1:18018/chat' \
  -H 'Content-Type: application/json' \
  --data '{
    "user_id": "diagnostic-user",
    "message": "Run a full fabric expert analysis and report which models succeeded or failed."
  }'
'

## Conceptual Response Shape

Actual fields are defined in api_specs/openapi.json and may evolve; conceptually,
responses include:

    response: string – synthesized narrative response from the main brain.

    services_used: string[] – high‑level record of services or fabrics involved.

    consciousness_level: string – for example, "ultimate_collective" for full‑fabric
    runs.

    processing_time: number – approximate wall‑clock seconds for the request.

Future versions may optionally expose a per‑model results[] structure and a summary
field for fabric diagnostics.
📜 License: AGPL-3.0

This system and documentation are licensed under GNU Affero General Public License
v3.0.

## High-level summary (not legal advice):

    ✅ You may use, study, modify, and distribute covered works.

    ✅ Network deployment of modified versions requires offering corresponding source to
    users.

    ✅ Derivatives must remain under AGPL-3.0–compatible terms.

See LICENSE for the full text.
🔒 Security Model

Ms. Jarvis’s design is explicitly shaped by security failures in earlier smart-contract
and financial infrastructure work associated with MountainShares.

## Problem (historical context)
Public repositories handling sensitive financial logic proved vulnerable to corruption
and misuse, motivating a stricter separation between documentation and code.

## Approach

    Security-aware design from the outset.

    No production financial or biometric code in public repositories.

    Constitutional and governance constraints documented for external audit.

    Sensitive implementation details and operational configuration kept behind an
    access-controlled process.

See Security Overview for more detail.
## 📚 Documentation
For Users and Community Partners

    API Overview – How external systems interact with Ms. Jarvis.

    Thesis Systems Overview – Integrated view of polymathamatical geography,
    Quantarithmia, Ms. Jarvis, and MountainShares.

    Researcher Position – Methodology and author positionality.

## For Developers and Auditors

    SOURCE_ACCESS.md – How to request access to code and deeper
    technical materials.

    Security Overview – Conceptual security and threat model.

## For Researchers

    Ms. Jarvis Thesis – Core treatment of polymathamatical geography,
    Quantarithmia, GBIM, consciousness architecture, and governance structures.

(Previously listed files such as architecture/SYSTEM_ARCHITECTURE.md,
architecture/CONSCIOUSNESS.md, architecture/GIS_SYSTEM.md,
governance/CONSTITUTIONAL_PRINCIPLES.md, security/BIOMETRIC_WALLET.md,
security/BLOCKCHAIN_SECURITY.md, security/SECURITY.md, docs/GETTING_STARTED.md,
and api_specs/swagger-export/ are not present on the main branch and are therefore
not linked here.)

## 🤝 Organizations

    MountainShares – DAO-based economic and governance system used as the primary
    institutional case study for spatial justice and community-first infrastructure.

    Harmony for Hope – 501(c)(3) nonprofit in Fayette County, West Virginia, serving as
    an on-the-ground community partner.

Academic collaborations in West Virginia are an active goal of the research program but
are not formal institutional partnerships unless explicitly documented elsewhere.

## 🌍 Community

    Location: Mount Hope, West Virginia.

    Mission: Community-first AI with constitutional governance, spatial justice, and
    rural peace at its core.

    Values: Transparency, accountability, and local empowerment.

## 📧 Contact

    Email: h4hwv2011@gmail.com

    Source Access: See SOURCE_ACCESS.md

    Issues: Use GitHub Issues for documentation and research questions only.

### Built with ❤️ in West Virginia
“No black box. Full transparency. Community first.”
