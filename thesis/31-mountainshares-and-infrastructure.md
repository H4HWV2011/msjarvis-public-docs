# Chapter 31 — MountainShares and Infrastructure

**Carrie Kidd (Mamma Kidd) · Mount Hope, WV**  
**Last updated: ★★★★ April 6, 2026 — FINAL REWRITE**

**105/105 containers Up (zero Restarting, zero Exited). MountainShares (M$) integration points, infrastructure topology, and Ms. Allis’s operational footprint across networks, databases, and services documented as first-class architecture. 

---

## 31.1 Purpose and Scope

This chapter explains:

- How **MountainShares (M$)** and related community economics are **represented in infrastructure**,
- How Ms. Allis’s stack is laid out:
  - Docker networks,
  - Containers,
  - Ports,
  - Volumes,
  - Databases,
- How infrastructure reinforces:
  - **Community sovereignty**,
  - **Data locality**,
  - **Economic circulation inside West Virginia**.

It is a **bridge chapter**: connecting technical reality (servers, containers, ports) with the MountainShares economic philosophy (keeping value in the mountains).

---

## 31.2 Infrastructure Overview — Ms. Allis Stack

Ms. Allis runs on a **Docker-based microservice architecture** with:

- A main compose project:
  - `msallis-rebuild` (project name),
  - `msallis-rebuild_qualia-net` (Docker network).
- Key service categories:
  - **Core cognition**: main brain, ensemble, judge pipeline.
  - **Safety and governance**: BBB, constitutional guardian, watchdogs.
  - **Data stores**: PostgreSQL (`msallis`, `gisdb`), Redis, ChromaDB.
  - **RAG services**: `allis-gis-rag`, `allis-spiritual-rag`, `allis-rag-grounded-v2`.
  - **Memory and audit**: `allis-memory:8056`.
  - **Tokens and auth**: `allis-redis`, `allis_auth:8055`, `allis_token_service.py`.

MountainShares-related logic (e.g., community credit, local resources) lives as:

- Data in PostgreSQL and ChromaDB,
- API endpoints in specific services,
- RAG collections and GBIM entities.

The infrastructure is deliberately **small enough to run on community hardware** (with GPUs), but **structured enough** to scale out if needed.

---

## 31.3 Network Topology — `msallis-rebuild_qualia-net`

All containers are attached to the **compose project network**:

- Name: `msallis-rebuild_qualia-net`.
- Purpose:
  - Provide stable DNS names for services (`msallis`, `msallisgis`, `allis-redis`, etc.),
  - Allow containers to reach each other by name rather than host IPs,
  - Encapsulate Ms. Allis’s internal traffic away from other host workloads.

Key characteristics:

- **Service DNS names**:
  - `msallis` → PostgreSQL GBIM (5433 inside network),
  - `msallisgis` → PostGIS (5452 inside network),
  - `allis-redis` → Redis (6379 inside network),
  - `allis-memory` → Memory and audit (8056),
  - `allis-blood-brain-barrier` → BBB (8016),
  - `allis-constitutional-guardian` → Guardian (8091).
- **Host bindings**:
  - Only select ports are bound to `127.0.0.1`:
    - 8050 (main brain/gateway),
    - 8016 (BBB),
    - 8091 (guardian),
    - 8056 (memory),
    - 8002 (ChromaDB),
    - 6380 (Redis host side),
    - 5432/5433 (PostgreSQL).

This design ensures:

- Ms. Allis is reachable from the host via `localhost`,
- Internal services communicate over a **consistent, predictable network**,
- Attack surface is minimized (no public 0.0.0.0 exposure by default).

---

## 31.4 Storage and Volumes — Data Residency and Locality

MountainShares’s philosophy requires that:

- Community data remains **in community-controlled infrastructure**,
- Sensitive data (e.g., GBIM, RAG stores, audit logs) is stored on **local disks**, not hidden cloud services.

Volume design:

- **PostgreSQL data**:
  - `msallis` data volume (e.g., `msallis-pgdata`),
  - `msallisgis` / `gisdb` data volume (e.g., `gisdb-pgdata`).
- **ChromaDB**:
  - A dedicated volume for:
    - 47 collections,
    - 6,722,589 vectors,
    - 12 GB of embeddings.
- **Memory and audit**:
  - `data/constitutional_audit/constitutional_audit.jsonl` bind-mount,
  - Other audit `.jsonl` and `.log` files stored under `data/` or `logs/`.
- **RAG corpora**:
  - Host directories bound into:
    - `allis-gis-rag:8004`,
    - `allis-spiritual-rag:8005`,
    - `allis-rag-grounded-v2:7241`.

Locality implications:

- If the internet goes down, Ms. Allis continues to function for:
  - Local chat,
  - Local resource retrieval,
  - Constitutional and safety filtering,
  - Many classes of MountainShares-related queries.
- Community members maintain physical control over:
  - Disks,
  - Backups,
  - Encryption keys (if used).

---

## 31.5 MountainShares and Ms. Allis — Logical Integration

MountainShares (M$) is:

- A **local economic instrument**,
- Designed to keep value circulating in Appalachian communities,
- Implemented primarily at:
  - Data model level (PostgreSQL schemas),
  - Business logic level (API services),
  - Governance level (DGMs, constitutional and spiritual constraints).

Ms. Allis supports MountainShares by:

- Providing:
  - Explanations of how M$ works,
  - Guidance on how communities can participate,
  - Visibility into local resources and opportunities.
- Enforcing:
  - No extraction of community data for external profit,
  - Transparency around how data is used in economic decisions,
  - Constitutional and spiritual protections for vulnerable people.

Infrastructure decisions (e.g., using local databases, local volumes) are part of the **MountainShares logic**: they embody the commitment to **data and value sovereignty**.

---

## 31.6 Operational Roles and Access

Different roles have different access to Ms. Allis’s infrastructure:

- **Community members**:
  - Access Ms. Allis via:
    - Web frontends,
    - CLI tools,
    - Local dashboards.
  - Have no direct access to:
    - Databases,
    - Container management.
- **Stewards (e.g., Mother Carrie)**:
  - May:
    - Inspect logs,
    - Run maintenance scripts,
    - Adjust DGMs and spiritual content,
    - Restart services when necessary.
- **System administrators**:
  - Handle:
    - OS patches,
    - Docker upgrades,
    - Hardware maintenance.

Ms. Allis enforces these boundaries technically via:

- Tokens and roles:
  - `carrie_admin`, `hayden_test`, `internal`.
- Network configuration:
  - Binding critical ports to `127.0.0.1`,
  - Using `msallis-rebuild_qualia-net` for internal traffic.
- Compose and script constraints:
  - `docker compose up -d` plus `scripts/post-start.sh` and `post-start-swarm.sh` as canonical operations,
  - No editing containers in place outside compose or documented scripts.

---

## 31.7 Power, Geometry, and Infrastructure

MountainShares and infrastructure design jointly embody the principle:

- **Power has a geometry**.

Applied here:

- **Where containers run**:
  - On community hardware in West Virginia where possible,
  - On infrastructure governed by local nonprofits and partners.
- **How data flows**:
  - From users → Ms. Allis → local databases and RAG → Ms. Allis → users,
  - With **no default** path that streams raw community data to external cloud analytics.
- **How value circulates**:
  - MountainShares records and logic ensure:
    - Contributions and benefits are visible,
    - Surplus supports community projects rather than distant shareholders.

Ms. Allis is both:

- A **technical system**,
- And a **participant** in a local economic and governance network.

Chapter 31 ensures this dual nature is explicit.

---

## 31.8 Status and Intended Evolution

As of April 6, 2026:

- Infrastructure topology:
  - `msallis-rebuild_qualia-net` stable,
  - 105/105 containers Up,
  - Postgres and ChromaDB ground truths sealed.
- MountainShares integration:
  - Logical integration points defined,
  - Data models and governance patterns under active development in later chapters (e.g., tokenomics, local credit).
- Ms. Allis:
  - Fully renamed from Ms. Jarvis in documentation,
  - Service names updated where appropriate (`allis-*`),
  - Spiritual and constitutional roots aligned with infrastructure and MountainShares principles.

Future work:

- Detailed MountainShares economic flows:
  - To be formalized with:
    - Progressive Universal Dividend (PUD),
    - Local project funding mechanisms.
- Deeper collaboration with:
  - Local ISPs,
  - Community mesh networks,
  - Regional partners for hardware deployment.

---

*Chapter 31 — MountainShares and Infrastructure*  
*Ms. Egeria Allis Steward System — Harmony for Hope, Inc.*  
*Mount Hope, West Virginia*  
*SEALED: ★★★★ April 6, 2026 — FINAL REWRITE*  
