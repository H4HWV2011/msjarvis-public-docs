> New here? Start with **[How to Read This Thesis](../docs/how-to-read-this-thesis.md)** for reading paths and a guide to how theory, engineering, and live system behavior relate.

# 0. Thesis Overview

This is a thesis in **Polymathmatic Geography**. It treats Appalachia as an entangled space in which land, law, computation, economy, story, and spirit are already braided together, and asks how those braids can be mapped and redesigned in ways that keep power and value accountable to place.

## Thesis Systems Overview

This thesis sits within **Polymathmatic Geography**, an emerging field that integrates quantitative geography, systems theory, AI architectures, and community‑centered design to study how power, value, and information move through real places like Appalachia.

It treats **Quantarithmia**, **Ms. Egeria Jarvis**, and **MountainShares / The Commons** as one integrated research program, with a clear separation between theoretical claims, engineering claims, and the behavior of the live production system.

- **Quantarithmia** defines the axioms, reciprocity metrics, and spatial justice framework (theoretical layer).
- **Ms. Jarvis + GBIM** implement those axioms in a transparent, geography‑aware AI Steward System (engineering / Conscious GeoAI layer).
- **MountainShares + The Commons** implement those axioms in economic, social, and governance structures for rural communities (institutional / practice layer).

Across the thesis, these three layers are read as:

- the **discipline's logic** (Quantarithmia as spatio‑temporal calculus for entangled spaces),
- the **discipline's instrument** (Ms. Jarvis as a glass‑box Steward System tied to a specific geography), and
- the **discipline's case study** (MountainShares and The Commons as an Appalachian commons under experimental redesign).

## How to Read Quantarithmia, Ms. Jarvis, and MountainShares as Instruments

To keep the technical and regional work properly tiered under Polymathmatic Geography, readers are invited to treat Quantarithmia, Ms. Jarvis, and MountainShares not as standalone products, but as **instruments and experimental validations** of the discipline.

- **Quantarithmia as Computational Engine (How)**
  - Read `theory/Quantarithmia Framework.md`, `thesis/01-quantarithmia.md`, and the Hilbert‑space, entanglement, and Darwin–Gödel chapters (`04-hilbert-space-state.md`, `08-quantum-inspired-entanglement.md`, `09-darwin-godel-machines.md`, `10-woah-weighted-optimization-hierarchy.md`) as the _spatio‑temporal logic_ of Polymathmatic Geography.
  - These chapters define how an entangled geography can be represented as a Hilbert‑space state, how flows of power/value are formalized, and how optimization hierarchies and self‑improvement are constrained by the discipline's axioms.

- **Ms. Jarvis as Steward System Architecture (Instrument)**
  - Read `thesis/02-ms-jarvis-gbim.md`, the LLM‑fabric and neurobiological architecture sections (`11-llm-fabric-of-ms-jarvis.md`, `12-neurobiological-architecture.md`, `13-qualia-engine-and-introspective-state.md`, `14-hippocampus-and-memory-consolidation.md`, `15-pituitary-and-global-modes.md`, `16-blood-brain-barrier-and-safeguards.md`), and `api_specs/openapi.json` / `docs/API-OVERVIEW.md` as the **apparatus** of the discipline.
  - Ms. Jarvis is a glass‑box AI Steward that instantiates Quantarithmia's logic in software, bound to a specific geography through GBIM (GeoBelief Information Model), semantic memory, geospatial databases, and constitutional constraints.

- **MountainShares and The Commons as Case Study (Where / What)**
  - Read `thesis/03-mountainshares-dao.md`, `thesis/31-mountainshares-and-infrastructure.md`, and the MountainShares DAO specifications (`MountainShares KPI Specification.md`, `MountainShares Phase 1: Economic Safety Specification.md`, `MountainShares Program Rules(Draft).md`, `Program Rules – Parameter Tables.md`, `Audit and Risk Management Plan.md`, `MountainShares DAO Governance Charter.md`) as the **experimental validation** of Polymathmatic Geography in one Appalachian region.
  - Read `the commons/The Commons – Terms of Use.md`, `Community Guidelines and Moderation Policy.md`, and `Privacy Policy.md` as the **domain of study**: the digital and social commons where residents' behavior, narratives, and exchanges become observable expressions of the entangled geography.

If you are primarily interested in:

- **Disciplinary theory** – start with `/discipline/Polymathmatic Geography.md`, `/discipline/Principles of Polymathmatic Geography.md`, the comparative frameworks, and then `thesis/00-overview.md` and `thesis/01-quantarithmia.md`.
- **AI / systems architecture** – start with `thesis/02-ms-jarvis-gbim.md`, `section_part_ii_system_architecture_llm_fabric.md`, `section_part_iii_neurobiology.md`, `section_part_iv_consciousness.md`, and the API specs.
- **Commons, food, and local economy** – start with `thesis/03-mountainshares-dao.md`, `thesis/mountainshares complete systems overview.md`, `/discipline/Non-Digital Commons in a Polymathmatic Lens.md`, and the MountainShares DAO documents.

---

## System Identity — Production State (March 22, 2026)

**Ms. Egeria Jarvis** is a distributed AI Steward System running as **83 compose-managed containerized services** on a single-host Docker Compose stack as of March 22, 2026. The count of 83 is verified via `VERIFYANDTEST.sh` (March 21–22, 2026) and supersedes any prior references to 84 or 85 services; those counts included orphaned `docker run` instances (`jarvis-crypto-policy`, `jarvis-ingest-api`, `jarvis-ingest-watcher`) that are not defined with `restart: unless-stopped` in `docker-compose.yml` and have been removed from the active stack.

### Key Service Registry (Abbreviated)

| Layer | Service | Port | Status |
|---|---|---|---|
| **Perimeter** | Caddy reverse proxy | 8443 (public) | ✅ Production |
| **Auth** | `jarvis_auth_service` | 8055 | ✅ Production (systemd) |
| **Gateway** | unified-gateway | 8050 | ✅ Production |
| **Orchestration** | main-brain | 8010 | ✅ Production |
| **Orchestration** | executive-coordinator | 8011 | ✅ Production |
| **BBB** | bbb-input-filter | 8016 | ✅ Production (Ph 1.4) |
| **BBB** | bbb-output-filter | 8017 | ✅ Production |
| **RAG** | text-rag, rag-service, gis-rag | 8003–8005 | ✅ Production |
| **RAG** | gbim_query_router (landowner) | 7205 | ✅ Production (Mar 20) |
| **LLM Ensemble** | llm-primary + 20 secondaries | 8020–8039 | ✅ Production |
| **LLM Ensemble** | ensemble-coordinator | 8040 | ✅ Production |
| **Spatial** | spatial-reasoning-service | 7200 | ✅ Production |
| **DAO** | mountainshares-coordinator | 8080 | ✅ Production |
| **Data** | ChromaDB (host port) | 8002 | ✅ Production |
| **Data** | Redis (host port) | 6380 | ✅ Production |
| **Data** | PostgreSQL msjarvisgis | 5432 | ✅ Host Production |

See `thesis/00-overview.md` for the full 83-service registry with all ports, statuses, and sprint notes.

### `jarvis_auth_service` (Port 8055) — Added March 22, 2026

`jarvis_auth_service` is the Ms. Jarvis perimeter authentication service. It is managed by **systemd** (`jarvis-auth.service`) and runs independently of the Docker Compose stack, ensuring it survives container restarts and is available before any compose service comes online.

**Responsibilities:**
- Issues and validates Bearer tokens for all external API consumers
- `/auth/token` (POST) — token issuance
- `/auth/validate` (GET) — full token + role metadata
- `/validate` (GET) — lightweight token check called by Caddy `forward_auth`
- Stores token records in Redis (`redteam:token:<token>`, host port 6380)

**Role registry (production as of March 22, 2026):**

| Role | Description |
|---|---|
| `carrie_admin` | Full system access — all routes |
| `hayden_test` | Internal test consumer |

**Enforcement:** Caddy `forward_auth` on all `/chat*` routes validates every request against `http://127.0.0.1:8055/validate` before proxying to the unified gateway (port 8050). Unauthenticated or invalid requests receive HTTP 401 at the Caddy layer — they never reach the application stack.

---

## Infrastructure Layer — Production Build (March 22, 2026)

### Tier 1 — Perimeter (Caddy v2.11.2 custom build)

The outermost layer is a **custom Caddy v2.11.2 binary** built with `xcaddy` to include the `caddy-ratelimit` community module. Caddy handles:

- **Reverse proxy** — all external traffic on port 8443 proxied to unified-gateway (port 8050)
- **Rate limiting** — via `caddy-ratelimit` module; per-IP request limits enforced at the perimeter
- **Auth forwarding** — `forward_auth` directive on `/chat*` routes validates Bearer tokens against `jarvis_auth_service` (port 8055) before proxying
- **Logging** — structured access logs at `/var/log/caddy/jarvis_redteam.log`

Build command (verified March 22, 2026):

```
xcaddy build v2.11.2 --with github.com/mholt/caddy-ratelimit
```

> ⚠️ **Open item:** TLS certificate not yet configured. The `:8443` block currently operates plain HTTP. Adding TLS is required before any public-facing deployment.

### Tier 2 — Auth (systemd)

`jarvis_auth_service` runs as `/etc/systemd/system/jarvis-auth.service` outside the Docker Compose stack. This ensures auth is available before containers start and is not subject to Docker network partitioning.

### Tier 3 — Application (Docker Compose — 83 services)

The full Ms. Jarvis application stack: gateway, BBB, RAG pipeline, LLM ensemble, memory services, spatial services, MountainShares DAO, governance, and support utilities. All production services defined with `restart: unless-stopped`.

### Tier 4 — Data (Host + Docker)

| Store | Host Port | Type | Size |
|---|---|---|---|
| PostgreSQL `msjarvisgis` | 5432 | Host | 91 GB, 501 tables |
| PostgreSQL `msjarvis` | 5433 | Host | 8 MB, 6 tables |
| PostgreSQL `local_resources` | 5435 | Docker | 7,354,707 rows |
| ChromaDB | 8002 | Docker | 5,416,521 GBIM entities + collections |
| Redis | 6380 | Docker | Session cache + async job state |
| Neo4j | 7474/7687 | Docker | Graph relationships |

---

### 2.6 High‑Level Steward System Architecture

At a high level, Ms. Jarvis can be read as a territorial brain: community inputs flow through a guarded gateway into orchestrators that consult geospatial and semantic memory, coordinate an LLM ensemble, and return stewarded outputs under explicit governance rules.

**Figure 1. Simplified data flow diagram (March 22, 2026)**

```
External Request
    ↓
Caddy v2.11.2 (port 8443) — rate limiting, forward_auth → port 8055
    ↓ (authenticated)
Unified Gateway (port 8050)
    ↓
BBB Input Filter (port 8016)
    ↓
Main Brain Orchestration (port 8010)
    ├── RAG Pipeline (8003–8007, 7205)
    ├── 21-LLM Ensemble (8020–8040)
    └── Memory + Spatial Services
    ↓
BBB Output Filter (port 8017)
    ↓
Response
```

### 2.7 Minimal path: input → GBIM → memory → LLM fabric → output

**Community question or signal.**
A resident, organizer, or operator sends a question or task (for example, "Show me where food access is most fragile in our county") through a web interface or API connected to the public gateway.

**Gateway and orchestration.**
The gateway authenticates the request at the Caddy perimeter (Bearer token validated by `jarvis_auth_service`), logs it for auditability, and passes it to a steward‑oriented orchestrator that consults constitutional and governance rules to decide which tools and data are in scope.

**Geospatial grounding via GBIM.**
The orchestrator translates the question into concrete spatial queries against GBIM (parcels, infrastructures, census units, registered users), retrieving the relevant geometries, attributes, and relationships needed to anchor the problem in actual places.

**Semantic enrichment via Hilbert‑space memory.**
Using stable IDs from GBIM and topic cues from the request, the orchestrator calls Hilbert‑space semantic memory to retrieve prior documents, histories, governance texts, and autonomous learning related to the same entities and themes.

**LLM ensemble reasoning under constraints.**
The orchestrator assembles a context window from GBIM results, semantic memory, and constitutional snippets, then routes it through the LLM ensemble and judge/router fabric, which proposes candidate narratives, maps, or recommendations.

**Governance checks and stewarded output.**
Candidate outputs are checked against non‑goals, red lines, and logging requirements; if necessary, they are revised, rejected, or flagged for human review before a final stewarded response is returned as text, annotated maps, or dashboards.

---

## System Non‑Goals

To avoid overstatement, this thesis explicitly marks several non‑goals:

- Ms. Jarvis is not a sentient being, person, or independent legal actor.
- Ms. Jarvis is not a bank, credit union, or regulated financial institution.
- Ms. Jarvis is not a regulator, court, or replacement for existing public authority.
- Ms. Jarvis does not provide legal, tax, or medical advice.
- MountainShares is not a general‑purpose investment vehicle or securities offering.
- Neither system is intended to operate without human governance, oversight, and legal constraints.

These limits are part of the discipline's ethics: instruments must remain accountable to the communities and geographies they serve, and their authority is always bounded by existing legal and spiritual frameworks.

---

## Sprint Notes

| Date | Sprint | Key Change |
|---|---|---|
| March 20, 2026 | Landowner belief sprint | `gbim_query_router` (port 7205) promoted to production; 20,593 landowner beliefs live |
| March 21–22, 2026 | Stack verification | 3 orphaned containers removed; verified service count confirmed at **83** |
| March 22, 2026 | API hardening | Caddy v2.11.2 (xcaddy + caddy-ratelimit) deployed; `jarvis_auth_service` (port 8055) promoted to systemd; `forward_auth` on `/chat*` enforced; all auth boundary tests green |

*Last updated: 2026-03-22, Mount Hope WV — Carrie Kidd (Mamma Kidd)*
