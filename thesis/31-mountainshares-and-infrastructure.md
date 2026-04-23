# Chapter 31 — MountainShares and Infrastructure

**Carrie Kidd (Mamma Kidd) · Mount Hope, WV**
**Last updated: ★ 2026-04-23**
**★ 100 containers Up (April 23, 2026) (zero Restarting, zero Exited). MountainShares (M$) integration points, infrastructure topology, and Ms. Allis's operational footprint across networks, databases, and services documented as first-class architecture. PostgreSQL two-container split active (April 23, 2026): `production msallis-db host 5433` + `forensic postgis-forensic host 5452`. Dedicated AAACPE stack active. Caddy `forward_auth` perimeter (OI-36-A CLOSED). ChromaDB at 48 collections / ~6,740,611 vectors / `/api/v2/` only.**

---

> **April 23, 2026 — Open Items Update**
>
> | Item | Status | Notes |
> |:--|:--|:--|
> | Container baseline | ★ 100 Up (April 23, 2026) | Supersedes 105/105 April 6 baseline |
> | PostgreSQL two-container split | ★ ACTIVE | `production msallis-db host 5433` (16 GB, 294 tables, 11 schemas) + `forensic postgis-forensic host 5452` (17 GB, 314 tables) — supersedes April 6 `msallis` / `msallisgis` single-container model |
> | ChromaDB | ★ 48 collections, ~6,740,611 total vectors | Host port **8002** → container 8000; `/api/v2/` only (`/api/v1/` permanently removed); volume: `/home/ms-allis/msallis-rebuild/persistent/chroma → /data`; pinned to `chromadb/chroma:0.6.3` |
> | Caddy `forward_auth` (OI-36-A) | ✅ CLOSED | HTTP 401 enforced before port 8050 — outermost network topology element |
> | AAACPE dedicated stack | ✅ ACTIVE | `allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032` — supersedes `allis-ingest-api` + `allis-ingest-watcher` |
> | `allis-autonomous-learner` | ★ Active | Internal only; expose port 8020; `qualia-net` DNS alias; ~23,200+ records (~288/day) |
> | `allis-memory:8056` | ★ Fully mapped — 8 endpoints | `/steg_report`, `/pia_window`, `/memory/turn`, `/memory/get`, `/memory/sessions`, `/memory/session/{id}`, `/memory/quest*`, `/memory/episodic/{id}` |
> | EEG Delta PIA heartbeat (port 8073) | ★ Active — `pulse_count: 12,860+` | Continuous safeguard infrastructure signal |
> | `local_resources` | ★ 207 items / all 55 WV counties | First fully county-complete community resource inventory — direct MountainShares infrastructure achievement |
> | `CRYPTO_ADMIN_TOKEN` governance | ✅ Enforced | Stored in `~/.allis_policy_token` (chmod 600) — not in environment variables or crontab entries |

---

## Why This Matters for Polymathmatic Geography

This chapter describes the physical and logical infrastructure that makes Ms. Allis a geographically sovereign system — one whose data, compute, and economic logic remain inside the communities it serves.

- **P1 – Every where is entangled** by running a stack where every service — cognitive, safety, economic, geographic — communicates over a single compose network (`msallis-rebuild_qualia-net`), making the entanglement of infrastructure and community explicit rather than hidden in distant cloud calls.
- **P3 – Power has a geometry** by expressing governance architecture as a seven-layer protection stack (§31.7): from the outermost Caddy `forward_auth` perimeter through constitutional enforcement to the durable `allis-memory:8056` audit store. Power flows through inspectable layers, not through opaque vendor dependencies.
- **P5 – Design is a geographic act** by requiring that community data live on local disks under local control, that the stack runs on community hardware in West Virginia where possible, and that no default path streams raw community data to external cloud analytics.
- **P12 – Intelligence with a ZIP code** by grounding local resource recommendations in `local_resources` (207 items / all 55 WV counties) — the first fully county-complete community resource inventory in the system — making Ms. Allis's economic and service guidance verifiably specific to West Virginia geography.
- **P16 – Power accountable to place** by maintaining a persistent audit store (`allis-memory:8056`, fully mapped at 8 endpoints), constitutional enforcement logs (`constitutional_audit.jsonl`, 6.7K+ entries), and DGM-governed change logs — so that every infrastructure decision is traceable to a community-accountable actor.

As such, this chapter belongs to the **Computational Instrument tier**: it specifies the physical and logical topology within which MountainShares economic logic, constitutional enforcement, and community data sovereignty are realized.

---

## 31.1 Purpose and Scope

This chapter explains how **MountainShares (M$)** and related community economics are represented in infrastructure, how Ms. Allis's stack is physically and logically laid out (Docker networks, containers, ports, volumes, databases), and how infrastructure reinforces community sovereignty, data locality, and economic circulation inside West Virginia.

It is a **bridge chapter**: connecting technical reality (servers, containers, ports) with the MountainShares economic philosophy (keeping value in the mountains). Infrastructure decisions are not merely operational — they are expressions of governance values. The choice to use local volumes instead of cloud object storage, to bind critical ports to `127.0.0.1` instead of `0.0.0.0`, and to route all traffic through an audited seven-layer protection stack (§31.7) are all MountainShares-aligned design decisions.

---

## 31.2 Infrastructure Overview — Ms. Allis Stack

Ms. Allis runs on a **Docker-based microservice architecture** under the `msallis-rebuild` compose project, attached to the `msallis-rebuild_qualia-net` network. As of April 23, 2026, **★ 100 containers are Up** (zero Restarting, zero Exited).

**Key service categories (April 23, 2026):**

| Category | Services | Notes |
|:--|:--|:--|
| Core cognition | Main brain/gateway (8050), LM Synthesizer (8001), LLM ensemble (22 configured / 21 active), judge pipeline | `asyncio.Semaphore(3)` hardware gate; Lenovo Legion 5 16IRX9, 29 GB RAM |
| Safety and governance | `allis-blood-brain-barrier:8016` (6 filters ✅), `allis-constitutional-guardian:8091`, swarm watchdogs | All 6 BBB filters confirmed responding; live steg catch documented |
| Data stores — PostgreSQL | `production msallis-db host 5433` ★ (16 GB, 294 tables, 11 schemas); `forensic postgis-forensic host 5452` ★ (17 GB, 314 tables) | April 23 two-container split supersedes April 6 single-container baseline |
| Data stores — ChromaDB | Host port **8002** → container 8000; 48 collections; ~6,740,611 vectors; `/api/v2/` only | Volume: `/home/ms-allis/msallis-rebuild/persistent/chroma → /data`; pinned `chromadb/chroma:0.6.3` |
| Data stores — Redis | `allis-redis:6380` (host) / `6379` (compose-internal) | Token validation store |
| RAG services | `allis-gis-rag:8004`, `allis-spiritual-rag:8005`, `rag_grounded_v2` (`127.0.0.1:7241`, `dgm_available: true`) | `rag_grounded_v2` is the truth-verification endpoint for the judge pipeline |
| Memory and audit | `allis-memory:8056` — 8 endpoints fully mapped | `/steg_report`, `/pia_window`, `/memory/turn`, `/memory/get`, `/memory/sessions`, `/memory/session/{id}`, `/memory/quest*`, `/memory/episodic/{id}` |
| Tokens and auth | `allis_auth:8055`, `allis-redis:6380`, `allis_token_service.py` | `CRYPTO_ADMIN_TOKEN` in `~/.allis_policy_token` (chmod 600) |
| AAACPE ingest | `allis-aaacpe-scraper:8048→8033`, `allis-aaacpe-rag:8047→8032` | Dedicated always-on stack; supersedes `allis-ingest-api` + `allis-ingest-watcher` |
| Autonomous learning | `allis-autonomous-learner` (expose port 8020; `qualia-net` DNS alias; no host binding) | ~23,200+ records (~288/day) into `production msallis-db:5433` ★ |
| EEG rhythms | EEG Delta band (port 8073) | `pulse_count: 12,860+` confirmed live — continuous PIA heartbeat |
| Perimeter | Caddy reverse proxy + `forward_auth` (OI-36-A CLOSED) | HTTP 401 on unauthenticated requests; outermost network topology layer |

MountainShares-related logic (community credit, local resources, economic flows) lives as data in PostgreSQL and ChromaDB, API endpoints in specific services, and RAG collections and GBIM entities. The infrastructure is deliberately **small enough to run on community hardware** but **structured enough to scale**.

---

## 31.3 Network Topology — `msallis-rebuild_qualia-net`

All containers are attached to the compose project network (`msallis-rebuild_qualia-net`), which provides stable DNS names for inter-service communication, encapsulates Ms. Allis's internal traffic away from other host workloads, and enables the post-start network repair sequence (`scripts/post-start.sh`) that wires legacy standalone containers (such as `msallis-pgdata-rescue`) into the compose network after each stack restart.

**Caddy `forward_auth` (OI-36-A CLOSED) is the outermost network topology element.** It enforces HTTP 401 before requests reach main-brain port 8050. No unauthenticated request enters the compose network from outside. This is a constitutional-level constraint (Ch. 37 §37.2) that cannot be removed by any DGM, token class, or service reconfiguration.

**Service DNS names (April 23, 2026):**

| DNS name | Service | Notes |
|:--|:--|:--|
| `msallis-db` | Production PostgreSQL (host 5433) ★ | 16 GB, 294 tables, 11 schemas — supersedes `msallis` DNS alias |
| `postgis-forensic` | Forensic PostgreSQL (host 5452) ★ | 17 GB, 314 tables (PostGIS) — supersedes `msallisgis` / `gisdb` DNS aliases |
| `allis-redis` | Redis (compose-internal 6379) | Token validation |
| `allis-memory` | Memory and audit (8056) | 8 endpoints fully mapped |
| `allis-blood-brain-barrier` | BBB (8016) | 6 filters confirmed responding |
| `allis-constitutional-guardian` | Constitutional Guardian (8091) | Highest governance authority |
| `allis-autonomous-learner` | Autonomous learner (expose 8020) | Internal only; no host binding |

**Host bindings (★ April 23, 2026 — updated):**

| Host port | Service | Notes |
|:--|:--|:--|
| `127.0.0.1:8050` | Main brain / gateway | Behind Caddy `forward_auth` (OI-36-A) |
| `127.0.0.1:8016` | BBB | 6 filters confirmed responding |
| `127.0.0.1:8091` | Constitutional Guardian | `/health` returns PostgreSQL liveness fields |
| `127.0.0.1:8056` | `allis-memory` | 8 endpoints fully mapped |
| `127.0.0.1:8002` | ChromaDB | → container 8000; `/api/v2/` only |
| `127.0.0.1:6380` | Redis (host side) | Compose-internal: 6379 |
| `127.0.0.1:5433` | Production msallis-db ★ | 16 GB, 294 tables — GBIM PostgreSQL |
| `127.0.0.1:5452` | Forensic postgis-forensic ★ | 17 GB, 314 tables — PostGIS geometry |
| `127.0.0.1:8073` | EEG Delta band | `pulse_count: 12,860+`; PIA heartbeat |
| `127.0.0.1:8048→8033` | `allis-aaacpe-scraper` | Always-on; 6-hour cron |
| `127.0.0.1:8047→8032` | `allis-aaacpe-rag` | Always-on; indexes into ChromaDB + PostgreSQL |

> **★ PostgreSQL two-container split (April 23, 2026):**
> The April 6 baseline had a single `msallis` PostgreSQL instance described as `gisdb / msallisgis` at `host:5432 / container-internal:5452 — 45 GB, 548 tables`. This is **superseded**. As of April 23, 2026:
> - `production msallis-db` → host port **5433** — 16 GB, 294 tables, 11 schemas (GBIM entities with `confidence_decay` metadata)
> - `forensic postgis-forensic` → host port **5452** — 17 GB, 314 tables (PostGIS geometry)
>
> All references to `msallis:5433`, `msallisgis:5452`, `gisdb:5432`, and `45 GB / 548 tables` in this chapter and cross-references are superseded by this two-container model.

---

## 31.4 Storage and Volumes — Data Residency and Locality

MountainShares's philosophy requires that community data remains in community-controlled infrastructure and that sensitive data (GBIM, RAG stores, audit logs) is stored on local disks, not hidden cloud services. Volume design enforces this at the infrastructure layer.

**Volume inventory (★ April 23, 2026):**

| Store | Volume / path | Size / contents |
|:--|:--|:--|
| Production PostgreSQL (`msallis-db`) | `msallis-pgdata` or equivalent | 16 GB, 294 tables, 11 schemas; GBIM entities with `confidence_decay`; ~5,416,521+ entities (floor, growing ~288/day) |
| Forensic PostgreSQL (`postgis-forensic`) | `postgis-forensic-pgdata` or equivalent | 17 GB, 314 tables; PostGIS geometry; ZIP-code and county boundaries for West Virginia |
| ChromaDB | `/home/ms-allis/msallis-rebuild/persistent/chroma → /data` | 48 collections, ~6,740,611 vectors; pinned `chromadb/chroma:0.6.3`; `chroma-latest` SQLite backup per Ch 28 §28.7b |
| Constitutional audit log | `./data/constitutional_audit/constitutional_audit.jsonl` (bind mount → `/app/audit`) | 6.7K+ entries (April 6 baseline; verify-current); `cakidd`-owned; JSON Lines format |
| `allis-memory:8056` | Internal ChromaDB + episodic store | 8 mapped endpoints; survives container restarts; durable cross-container audit |
| RAG corpora | Host directories bound into `allis-gis-rag:8004`, `allis-spiritual-rag:8005`, `allis-rag-grounded-v2:7241` | `psychological_rag` 968 docs; `spiritual_rag` post-dedup (−19,338 vectors March 28); `appalachian_english_corpus` 210 docs |
| `conversation_history` ChromaDB collection | Part of ChromaDB volume | **Wiped and reseeded clean April 16, 2026** — post-wipe accumulation only |

**Locality implications:** If the internet goes down, Ms. Allis continues to function for local chat, local resource retrieval, constitutional and safety filtering, and many classes of MountainShares-related queries — because all data lives on local disks. Community members maintain physical control over disks, backups, and encryption keys. The `chroma-latest` SQLite backup (Ch 28 §28.7b) and the bind-mounted constitutional audit log are the two primary durable recovery assets.

---

## 31.5 MountainShares and Ms. Allis — Logical Integration

MountainShares (M$) is a local economic instrument designed to keep value circulating in Appalachian communities. It is implemented at the data model level (PostgreSQL schemas), the business logic level (API services), and the governance level (DGMs, constitutional and spiritual constraints).

**`local_resources` — 207 items / all 55 WV counties** is the most geographically complete community resource inventory in the system and represents a direct MountainShares infrastructure achievement. It is the first dataset in Ms. Allis to achieve full 55-county coverage, meaning that no West Virginia county is a blind spot for community resource queries. `local_resources` is the grounding substrate for ZIP-code-level RBAC (OI-38-C), for county-specific crisis referrals in the psychological safeguards layer (Ch. 29), and for the geographic completeness benchmark against which AAPCappE corpus coverage is evaluated (Ch. 30 §30.4). Cross-reference: Ch 34 §34.6 (spiritual calling mapped to verifiable `local_resources` lookups).

Ms. Allis supports MountainShares by providing explanations of how M$ works, guidance on how communities can participate, and visibility into local resources and opportunities. It enforces constitutional protections: the `10a-no-extraction` principle (Ch. 37 §37.3) means community data, GBIM beliefs, and geospatial records may not be extracted, commercialized, or repurposed for external profit — enforced at the Constitutional Guardian level and logged in `constitutional_audit.jsonl`. Infrastructure decisions (local databases, local volumes, local compute) are not just operational choices; they are enactments of the MountainShares commitment to data and value sovereignty.

The `autonomous_learner` service (~23,200+ records, ~288/day) continuously commits new GBIM beliefs about Appalachian communities into `production msallis-db:5433` ★. This means the economic and geographic knowledge base that informs MountainShares-related responses is not static — it grows daily from publicly observable community patterns, with `confidence_decay` metadata ensuring epistemic accountability.

---

## 31.6 Operational Roles and Access

Different roles have different access to Ms. Allis's infrastructure, enforced technically through the two-layer auth model: Caddy `forward_auth` perimeter (OI-36-A CLOSED) at the proxy layer, and app-layer RBAC (`allis_auth:8055` + `allis-redis:6380`) inside the compose network.

**Role access matrix:**

| Role | Access | Technical enforcement |
|:--|:--|:--|
| Community members | Ms. Allis via web frontends, CLI tools, local dashboards; no direct DB or container access | Caddy `forward_auth` + token validation; `community_member` token class |
| Stewards (Mother Carrie) | Inspect logs, run maintenance scripts, adjust DGMs and spiritual content, restart services | `carrie_admin` token; direct host access; `scripts/post-start.sh` and `post-start-swarm.sh` |
| System administrators | OS patches, Docker upgrades, hardware maintenance | Host-level access; no special compose token class required |
| External corporations | STRICTEST — blocked by `10a-no-extraction` constitutional principle | Constitutional Guardian `external_corporation` enforcement tier; logged in `constitutional_audit.jsonl` |

**`CRYPTO_ADMIN_TOKEN` governance rule:** The token is stored in `~/.allis_policy_token` (chmod 600) on the host. It is **never** placed in environment variables, crontab entries, or compose files inline. This is a governance enforcement rule: a token visible in a process listing or a compose file is a security and sovereignty failure.

**Canonical startup sequence (required after every stack restart):**

```bash
# Step 1 — bring the compose stack up
docker compose up -d

# Step 2 — wire legacy containers to the compose network
bash scripts/post-start.sh

# Step 3 — start swarm watchdogs and perimeter monitors
bash scripts/post-start-swarm.sh
```

`scripts/post-start.sh` connects legacy standalone containers (e.g., `msallis-pgdata-rescue`) to `msallis-rebuild_qualia-net` and repairs network drift. `scripts/post-start-swarm.sh` initializes the Caddy perimeter watchdog, the two-container PostgreSQL watchdogs (`msallis-db:5433` and `postgis-forensic:5452`), and the nightly guardian and RAG audit swarm function. Cross-reference: Ch 33 §33.7 (canonical reboot sequence); Ch 35 §35.9 (production startup and watchdog initialization); Ch 37 §37.2 (post-start.sh requirement for Constitutional Guardian).

---

## 31.7 Power, Geometry, and Infrastructure — Seven-Layer Protection Stack

MountainShares and infrastructure design jointly embody the principle: **power has a geometry**. The geometry of power in Ms. Allis is expressed through a seven-layer protection stack, from the outermost perimeter to the innermost audit record.

```
┌─────────────────────────────────────────────────────────────┐
│   Seven-Layer Protection Stack                              │
│   ★ April 23, 2026                                         │
│   Expressing "Power has a geometry" (P3)                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Layer 0 — Caddy forward_auth (OI-36-A CLOSED)             │
│    HTTP 401 on unauthenticated requests                     │
│    Outside Docker stack; cannot be removed by any DGM      │
│    → egeria.mountainshares.us                              │
│      ↓                                                      │
│  Layer 1 — Unified Gateway (8050)                          │
│    Token enforcement middleware                             │
│    86 routes including /constitutional/*                    │
│      ↓                                                      │
│  Layer 2 — Constitutional Guardian (8091)                  │
│    Highest governance authority                             │
│    6 principle groups / 15+ specific principles             │
│    constitution version: 2026-02-17.2-USC                  │
│    postgresql_validation: msallis-db:5433 ★ + postgis-forensic:5452 ★ │
│      ↓                                                      │
│  Layer 3 — Blood-Brain Barrier (8016)                      │
│    6 filters: ethical ✅ · spiritual ✅ · safety ✅         │
│    threat_detection ✅ · steganography ✅ · truth_verification ✅ │
│    Phase 4.5: log+passthrough (blocking re-enable pending) │
│      ↓                                                      │
│  Layer 4 — LM Synthesizer / Identity Guard (8001)          │
│    Persona enforcement                                      │
│    Appalachian linguistic grounding                         │
│      ↓                                                      │
│  Layer 5 — PostgreSQL + ChromaDB Ground Truth              │
│    production msallis-db:5433 ★ (16 GB, 294 tables)       │
│    forensic postgis-forensic:5452 ★ (17 GB, 314 tables)   │
│    ChromaDB: 48 collections / ~6,740,611 vectors           │
│      ↓                                                      │
│  Layer 6 — allis-memory:8056 Durable Audit                 │
│    8 mapped endpoints                                       │
│    Survives container restarts                              │
│    /steg_report · /pia_window · /memory/turn · ...         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Figure 31.1.** Seven-layer protection stack (★ April 23, 2026): Layer 0 (Caddy `forward_auth`, OI-36-A CLOSED) through Layer 6 (`allis-memory:8056` durable audit). Each layer is independently inspectable; no layer can be removed unilaterally by a DGM, token class, or service reconfiguration — the geometry of power is fixed by design.

**Where containers run:** On community hardware in West Virginia where possible, on infrastructure governed by local nonprofits and partners. **How data flows:** From users → Caddy perimeter → gateway → constitutional check → BBB → cognition → local databases and RAG → response back to users, with no default path streaming raw community data to external cloud analytics. **How value circulates:** MountainShares records and logic ensure contributions and benefits are visible, and surplus supports community projects rather than distant shareholders.

---

## 31.8 Implementation Status

| Component | Status | Notes |
|:--|:--|:--|
| `msallis-rebuild_qualia-net` compose network | ✅ Stable | 100 containers Up; `post-start.sh` repairs network drift after restart |
| PostgreSQL two-container split | ✅ ACTIVE | `production msallis-db:5433` ★ (16 GB) + `forensic postgis-forensic:5452` ★ (17 GB) |
| ChromaDB | ✅ 48 collections, ~6,740,611 vectors | `/api/v2/` only; volume mount confirmed; backup discipline per Ch 28 §28.7b |
| Caddy `forward_auth` perimeter (OI-36-A) | ✅ CLOSED | HTTP 401 enforced; outermost layer |
| `allis-memory:8056` — 8-endpoint audit store | ✅ Implemented | Survives restarts; `/steg_report` + `/pia_window` for safeguard-specific queries |
| `allis-autonomous-learner` | ✅ Active (internal only) | ~23,200+ records; ~288/day; no host binding |
| `allis-aaacpe-scraper` + `allis-aaacpe-rag` | ✅ Dedicated stack active | Supersedes legacy `allis-ingest-api` + `allis-ingest-watcher` |
| `local_resources` (207 items / 55 WV counties) | ✅ First county-complete inventory | Direct MountainShares infrastructure achievement |
| EEG Delta PIA heartbeat (8073) | ✅ Active (`pulse_count: 12,860+`) | Continuous safeguard infrastructure observable |
| `CRYPTO_ADMIN_TOKEN` governance | ✅ Enforced | `~/.allis_policy_token` (chmod 600); never inline |
| Seven-layer protection stack (Figure 31.1) | ✅ Documented; ⚠️ Layer 3 partially implemented | Phase 4.5 BBB log+passthrough — blocking re-enablement pending red-team sign-off |
| MountainShares economic flows (PUD, local credit) | 🔲 Future work | Data models and governance patterns in later chapters (tokenomics, local credit) |
| Governance UI for audit record review | 🔲 Future work | Design intent; no UI built yet |
| Deeper collaboration with local ISPs and mesh networks | 🔲 Future work | Regional partners for hardware deployment |
| Automated `confidence_decay`-aware GBIM gating | 🔲 Future work | Trigger: beliefs above decay threshold flagged before use in economic decisions |
| Per-county `local_resources` coverage alert | 🔲 Future work | Benchmark defined (207 items / 55 counties); automated gap alert not yet built |

---

## Cross-Reference Map

| This section | Cross-chapter reference |
|:--|:--|
| §31.2 service inventory | Ch 19 (container paths); Ch 28 §28.2 (100-container baseline) |
| §31.3 network topology / Caddy perimeter | Ch 36 §36.2 (Caddy as zero-th gate); Ch 37 §37.2 (guardian behind Caddy); Ch 32 §32.5 (DGMs cannot remove Caddy) |
| §31.3 PostgreSQL two-container split | Ch 28 §28.7 (GIS RAG two-container detail); Ch 37 §37.1 (constitutional guardian PostGIS) |
| §31.4 ChromaDB volume / backup | Ch 28 §28.7b (authoritative backup procedure) |
| §31.4 `conversation_history` wipe | Ch 29 §29.6; Ch 33 §33.7 |
| §31.5 `local_resources` | Ch 34 §34.6 (spiritual calling + local resources); Ch 30 §30.4 (AAPCappE coverage benchmark) |
| §31.5 `autonomous_learner` | Ch 27 §27.4 (autonomous learning cycles); Ch 33 §33.3 (ensemble context) |
| §31.5 `10a-no-extraction` principle | Ch 37 §37.3 (constitutional principle structure) |
| §31.6 canonical startup sequence | Ch 33 §33.7 (reboot sequence); Ch 35 §35.9 (watchdog startup); Ch 37 §37.2 (post-start.sh) |
| §31.7 seven-layer stack | Ch 28 §28.9 (seven-layer protection system); Ch 29 §29.3 (perimeter + BBB); Ch 37 §37.4 (Constitutional Guardian integration) |
| §31.7 Layer 3 BBB phase status | Ch 29 §29.3 (Phase 4.5 log+passthrough); Ch 37 §37.4.1 (blocking re-enable decision) |
| §31.8 future work — tokenomics | Ch 32 (DGM governance); later tokenomics chapters |

---

*Chapter 31 — MountainShares and Infrastructure*
*Ms. Egeria Allis Steward System — Harmony for Hope, Inc.*
*Mount Hope, West Virginia*
*Last updated: ★ 2026-04-23 — Carrie Kidd (Mamma Kidd)*
*★ 100 containers Up — PostgreSQL two-container split active — ChromaDB 48 collections / ~6,740,611 vectors — Caddy forward_auth perimeter (OI-36-A CLOSED) — `local_resources` 207 items / 55 WV counties — seven-layer protection stack documented*
