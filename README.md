> New here? Start with **[How to Read This Thesis](docs/how-to-read-this-thesis.md)** for
> reading paths and a guide to research vs. engineering claims.

**A Constitutional, Community-Governed AI System**  
*Glassbox Architecture, Spatially Grounded in West Virginia, AGPL-3.0*

[LICENSE](LICENSE)

***

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

***

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

- **22‑Model LLM Fabric**  
  - Ensemble of 22 models accessed through internal proxies (for example,
    `llm1‑proxy` … `llm22‑proxy`).  
  - Invoked as a sequential or semi‑parallel sweep; some model timeouts are tolerated
    and reported in aggregate.

Port numbers, exact service counts, and deployment topology may vary across environments;
public documentation focuses on concepts and interfaces rather than a fixed production
layout.

***

## 🌟 What Is Ms. Egeria Jarvis?

Multi-tier AI consciousness system built on:

- **Constitutional Governance**: Explicit principles and constraints described in the
  Quantarithmia and MountainShares thesis chapters.  
- **Security-Aware Design**: Architecture and processes shaped by prior smart-contract
  corruption incidents and a conservative stance on public financial code.  
- **Geographic Grounding**: Extensive West Virginia geospatial data integrated through
  GBIM and the GeoDB spatial body.  
- **Community Accountability**: Tight coupling to MountainShares and Harmony for Hope as
  a community-centered research and governance context.  
- **Glassbox Transparency**: Public thesis, high-level architecture, and API overview
  instead of opaque, undocumented behavior.  

***

## 📊 System Overview

| Component                  | Description                                                                 | Documentation                                            |
|---------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------|
| **Gateway**               | External `/chat` API surface via the unified gateway, fronted by Cloudflare | [API Overview](docs/API-OVERVIEW.md)                    |
| **Main Brain**            | Ultimate collective orchestrator bridging RAG, neuro services, and LLMs     | [Thesis Systems Overview](thesis/00-thesis-overview.md) |
| **Consciousness**         | Multi-layer, multi-agent reasoning, GBIM, and Hilbert-space belief state    | [Ms. Jarvis Thesis](thesis/thesis.md)                   |
| **Constitutional / Governance** | Norms, speech rules, phased governance, DAO integration               | [Thesis Systems Overview](thesis/00-thesis-overview.md) |
| **GIS / GBIM**            | Geospatial belief model and West Virginia spatial body                      | [Thesis Systems Overview](thesis/00-thesis-overview.md) |
| **Security Model**        | High-level threat model and safeguards                                      | [Security Overview](security/SECURITY-OVERVIEW.md)      |

Port numbers, exact service counts, and internal deployment topology are implementation
details and may not match any particular runtime; the public docs focus on concepts and
architecture rather than a fixed production layout.

***

## 🚀 Quickstart: Talk to Ms. Jarvis (Conceptual)

The concrete request and response schema are documented in the OpenAPI spec and API
overview; this section gives a high‑level, non‑binding example of how clients interact
with the public `/chat` surface.

### External (via Cloudflare)

- Intended for normal application and community use.  
- Subject to Cloudflare timeouts for long‑running multi‑LLM analyses.

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
```bash

Internal (diagnostics and deep evaluations)

In controlled environments, an internal /chat endpoint on the main brain can be used
for long‑running 22‑LLM evaluations that may exceed Cloudflare’s request timeout.


