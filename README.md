> New here? Start with **[How to Read This Thesis](docs/how-to-read-this-thesis.md)** for
> reading paths and a guide to research vs. engineering claims.

# Ms. Jarvis Public Documentation

**Conscious GeoAI for rural governance and spatial justice in Appalachia.**  
**No black box. Place‑aware, community‑governed AI for real towns.**

**A Constitutional, Community-Governed AI System**  
*Glassbox architecture, spatially grounded in West Virginia, AGPL‑3.0*

[LICENSE](LICENSE)

---

## Polymathmatic Commons Context

Ms. Egeria Jarvis, MountainShares, and The Commons form a single **polymathmatic commons stack**: land, law, computation, economy, story, and spirit treated as one entangled geography rather than separate silos. The discipline behind this stack is **Polymathmatic Geography**, articulated in:

- [Polymathmatic Geography: A Manifesto](discipline/Polymathmatic%20Geography%3A%20A%20Manifesto.md)  
- [Principles of Polymathmatic Geography](discipline/Principles%20of%20Polymathmatic%20Geography.md)  
- [Non‑Digital Commons in a Polymathmatic Lens](discipline/Non-Digital%20Commons%20in%20a%20Polymathmatic%20Lens.md)  
- [Polymathmatic Geography and Commons Theory](discipline/Polymathmatic%20Geography%20and%20Commons%20Theory.md)

The Commons is the **primary entangled subject space** in this repository: a social–economic–digital commons where inhabitants’ behavior becomes data, and that data returns as geometry—flows, maps, ledgers, dashboards, and narratives they can see and contest.

For methods, syllabi, and comparative frames, see:

- [Methods](discipline/Methods.md)  
- [Discipline and Instruments](discipline/Discipline%20and%20Instruments.md)  
- [Comparative Frameworks in Geography and Commons](discipline/Comparative%20Frameworks%20in%20Geography%20and%20Commons.md)  
- [Polymathmatic Geography Syllabus](discipline/polymathmatic%20geography%20syllabus.md)  
- [Case Studies](discipline/case_studies.md)

---

## ⚠️ IMPORTANT: Source Code Access

**This repository contains DOCUMENTATION ONLY – no executable code.**

Ms. Jarvis’s public documentation was created after serious security incidents involving
MountainShares and related smart‑contract or financial infrastructure hosted on public
GitHub.

For security reasons:

- ✅ **Architecture & APIs**: Documented here at a conceptual and interface level  
- ✅ **Constitutional principles and governance model**: Public and auditable in thesis
  and overview documents  
- ✅ **Source code**: Available via a separate, access‑controlled process  
- ❌ **Not published as open code in this repository**

Security is part of the polymathmatic axiom that **power must be accountable to place** and that systems must remain **transparent and traceable**; the bounty approach to hardening and improvement is therefore a polymathmatic design choice, not just an engineering one.

To request source access, see:

- [SOURCE_ACCESS.md](security/SOURCE_ACCESS.md)  
- [Security Overview](security/SECURITY-OVERVIEW.md)  
- [Security CONTRIBUTING](security/CONTRIBUTING.md)

---

## 🌐 Current Runtime Surfaces (High-Level)

> The details below describe the *shape* of the live system without exposing deployment
> secrets or full port maps.

- **Unified Gateway (External API Surface)**  
  - Public entrypoint for external clients, fronted by Cloudflare and domain configuration.  
  - Canonical public path: `POST https://jarvis.mountainshares.us/chat`  
  - Handles authentication, request validation, and forwarding to the main brain.  
  - Request/response schema: [OpenAPI spec](api_specs/openapi.json) and [API Overview](docs/API-OVERVIEW.md)

- **Main Brain (Ultimate Collective Orchestrator)**  
  - Internal FastAPI service responsible for routing, RAG, GBIM calls, and multi‑LLM orchestration.  
  - Exposes an internal `/chat` interface for deep evaluations and diagnostics.

- **21‑Model LLM Fabric**  
  - Ensemble of models accessed through internal proxies, orchestrated as a fabric.  
  - Used for sequential / semi‑parallel sweeps; timeouts tolerated and reported.

Port numbers, exact service counts, and deployment topology may vary across environments; public documentation focuses on concepts and interfaces rather than a fixed production layout.

---

## 🌟 What Is Ms. Egeria Jarvis?

Ms. Jarvis is a **Conscious GeoAI system for rural governance**: an AI architecture that
grounds reasoning in geography, community history, and explicit constitutional rules
instead of operating as a generic cloud assistant.

She is built on:

- **Conscious GeoAI framing**  
  - Geospatial belief state and GIS body (GBIM + GeoDB) that tie beliefs and recommendations to real West Virginia places and infrastructures.  
  - Core thesis chapters:  
    - [02 – Ms. Jarvis and GBIM](thesis/02-ms-jarvis-gbim.md)  
    - [06 – GeoDB Spatial Body](thesis/06-geodb-spatial-body.md)  
    - [07 – RAG Pipeline and Routers](thesis/07-rag-pipeline-and-routers.md)

- **Constitutional governance**  
  - Norms and constraints described in Quantarithmia and MountainShares DAO docs:  
    - [Quantarithmia Framework](theory/Quantarithmia%20Framework.md)  
    - [MountainShares DAO Governance Charter](mountainshares-dao/MountainShares%20DAO%20Governance%20Charter.md)  
    - [37 – Constitutional Principles Service](thesis/37-constitutional-principles-service.md)

- **Neurobiological and consciousness architecture**  
  - Multi‑layer, multi‑agent system inspired by hippocampus, pituitary, qualia, etc.:  
    - [12 – Neurobiological Architecture](thesis/12-neurobiological-architecture.md)  
    - [13 – Qualia Engine and Introspective State](thesis/13-qualia-engine-and-introspective-state.md)  
    - [14 – Hippocampus and Memory Consolidation](thesis/14-hippocampus-and-memory-consolidation.md)  
    - [25 – Consciousness Coordinator and Services](thesis/25-consciousness-coordinator-and-services.md)

- **Community accountability**  
  - Anchored in MountainShares, The Commons, and Harmony for Hope:  
    - [MountainShares DAO](mountainshares-dao/mountainshares-dao.md)  
    - [MountainShares Thesis Chapter](thesis/03-mountainshares-dao.md)  
    - [31 – MountainShares and Infrastructure](thesis/31-mountainshares-and-infrastructure.md)  
    - [The Commons – Terms of Use](the%20commons/The%20Commons%20%E2%80%93%20Terms%20of%20Use.md)

- **Glassbox transparency**  
  - Public thesis and system overview instead of opaque behavior:  
    - [Thesis Overview](thesis/00-thesis-overview.md)  
    - [Section – System Architecture & LLM Fabric](thesis/section_part_ii_system_architecture_llm_fabric.md)  
    - [Section – Consciousness](thesis/section_part_iv_consciousness.md)  
    - [40 – System Audit and Operational Validation](thesis/40-system-audit-and-operational-validation.md)

For reading paths through these layers, see:

- [Index / Hub](docs/index.md)  
- [Further Reading](docs/further_reading.md)

---

## 🏔️ MountainShares, The Commons, and Branding

Ms. Jarvis lives inside a larger **Appalachian commons economy**:

- **MountainShares** – closed‑loop currency and mutual credit system:  
  - [Economic Safety Specification](mountainshares-dao/MountainShares%20Phase%201%3A%20Economic%20Safety%20Specification.md)  
  - [Program Rules (Draft)](mountainshares-dao/MountainShares%20Program%20Rules(Draft).md)  
  - [Program Rules – Parameter Tables](mountainshares-dao/Program%20Rules%20%E2%80%93%20Parameter%20Tables.md)  
  - [KPI Specification](mountainshares-dao/MountainShares%20KPI%20Specification.md)  
  - [Audit and Risk Management Plan](mountainshares-dao/Audit%20and%20Risk%20Management%20Plan.md)  
  - [Terms and Conditions](mountainshares-dao/Terms%20and%20Conditions.md)

- **The Commons** – observation and interaction surface for the discipline:  
  - [Community Guidelines and Moderation Policy](the%20commons/Community%20Guidelines%20and%20Moderation%20Policy.md)  
  - [Privacy Policy](the%20commons/Privacy%20Policy.md)  
  - [The Commons – Terms of Use](the%20commons/The%20Commons%20%E2%80%93%20Terms%20of%20Use.md)

- **Branding and flyers** – symbolic geometry of the commons:  
  - [MountainShares Coin](branding/MountainShares%20Coin.png)  
  - [MountainShares Logo](branding/MountainShares%20Logo.jpg)  
  - [MountainShares Mascot](branding/MountainSharesMascot.png)  
  - [MS Taglines Flyer](flyers/MS%20Taglines.png)  
  - [MountainShares Rewards Flyer](flyers/MountainShares%20Rewards.png)  
  - [MountainShares Branding & Flyers](branding/MountainShares%20Branding%20%26%20Flyers.md)

Branding is treated as part of commons infrastructure, not decoration: logos, coins, taglines, and mascots are symbolic pipes that route attention, trust, and value alongside ledgers and DAOs.

---

## 📊 System Overview (Docs Map)

| Component                         | Description                                                                 | Documentation                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| **Gateway**                      | External `/chat` API surface                                                | [API Overview](docs/API-OVERVIEW.md), [OpenAPI](api_specs/openapi.json)       |
| **Main Brain**                   | Orchestrator bridging RAG, GBIM, neuro services, and LLM fabric             | [Thesis Overview](thesis/00-thesis-overview.md), [LLM Fabric](thesis/11-llm-fabric-of-ms-jarvis.md) |
| **Conscious GeoAI / GBIM**       | Geospatial belief model and WV spatial body                                 | [GBIM](thesis/02-ms-jarvis-gbim.md), [GeoDB Body](thesis/06-geodb-spatial-body.md) |
| **Neurobiological Stack**        | Hippocampus, pituitary, qualia, safeguards                                  | [Neurobiology](thesis/section_part_iii_neurobiology.md)                       |
| **Constitutional / Governance**  | Norms, speech rules, phased governance, DAO integration                     | [09 – Darwin–Gödel Machines](thesis/09-darwin-godel-machines.md), [37 – Constitutional Principles](thesis/37-constitutional-principles-service.md) |
| **Security Model**               | Threat model, bounty posture, access‑controlled code                        | [SECURITY-OVERVIEW](security/SECURITY-OVERVIEW.md), [SOURCE_ACCESS](security/SOURCE_ACCESS.md) |
| **MountainShares DAO**           | Economic safety, KPIs, program rules, governance                            | `mountainshares-dao/` docs and [03 – MountainShares DAO](thesis/03-mountainshares-dao.md) |
| **The Commons**                  | App‑level governance, privacy, moderation                                   | `the commons/` docs as listed above                                           |

---

## 🚀 Quickstart: Talk to Ms. Jarvis (Conceptual)

Concrete request/response schemas live in the OpenAPI spec and API overview; this is a conceptual example.

### External (via Cloudflare)

Intended for normal application and community use; subject to Cloudflare timeouts.

```bash
curl -s -X POST 'https://jarvis.mountainshares.us/chat' \
  -H 'Content-Type: application/json' \
  -H 'x-api-key: <your-key>' \
  --data '{
    "user_id": "example-user",
    "username": "example.username",
    "message": "Hello Ms. Jarvis, who are you?",
    "metadata": { "source": "docs-readme-example" }
  }'
