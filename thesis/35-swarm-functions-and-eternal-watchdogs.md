# Chapter 35 — Swarm Functions and Eternal Watchdogs

**Carrie Kidd (Mamma Kidd) · Mount Hope, WV**
**Last updated: ★ 2026-04-23**
**★ 100 containers Up (April 23, 2026) (zero Restarting, zero Exited). Eternal watchdogs, swarm functions, and long-running guardians stabilized on `msallis-rebuild_qualia-net`. `allis-watchdogs` and `allis-swarm-functions` behave as autonomous, self-healing infrastructure stewards rather than brittle cron scripts. All Chapter 35 OIs remain CLOSED. PostgreSQL two-container split active (April 23): `production msallis-db host 5433` + `forensic postgis-forensic host 5452` — watchdog scripts updated accordingly.**

---

> **Permanent Ground Truth (★ April 23, 2026 — supersedes April 6):**
>
> - **Compose project network:** `msallis-rebuild_qualia-net` is the canonical Docker network for the production stack.
> - **Watchdog layer:** Eternal watchdogs continuously monitor container state (Up / Restarting / Exited), port responsiveness for critical services, PostgreSQL `production msallis-db:5433` ★ and `forensic postgis-forensic:5452` ★ liveness, `allis-memory:8056` durable audit availability, and token enforcement paths (gateway → `allis_auth:8055` → Redis `allis-redis:6380`). **★ The April 6 references to `msallis:5433` and `gisdb / msallisgis:5432` are superseded by the two-container split. All watchdog scripts must target `production msallis-db:5433` ★ and `forensic postgis-forensic:5452` ★.**
> - **Swarm functions:** Long-running, multi-step maintenance actions are modeled as declarative task graphs executed by a swarm of cooperating processes and containers, logged to `allis-memory:8056` and PostgreSQL where applicable.
> - **Eternal property:** If any one guardian fails, another independent mechanism detects and repairs the failure.
> - **Port ground truth (★ April 23, 2026 — supersedes April 6):**
>   - `production msallis-db` → host **5433** ★ — 16 GB, 294 tables, 11 schemas; GBIM entities with `confidence_decay` metadata; ~288/day growth from `autonomous_learner`
>   - `forensic postgis-forensic` → host **5452** ★ — 17 GB, 314 tables (PostGIS geometry) — **supersedes `gisdb / msallisgis` host `5432` / container-internal `5452` — 45 GB / 548 tables April 6 entry**
>   - `allis-local-resources-db` → host **5435** — `local_resources` 207 items / all 55 WV counties
>   - `allis-memory:8056` — durable audit; ★ **8 endpoints fully mapped**: `/steg_report`, `/pia_window`, `/memory/turn`, `/memory/get`, `/memory/sessions`, `/memory/session/{id}`, `/memory/quest*`, `/memory/episodic/{id}`; survives container restarts
>   - `allis-blood-brain-barrier:8016` — six-filter BBB; all 6 confirmed responding (April 23)
>   - `allis-constitutional-guardian:8091` — constitutional authority; `/health` reports `postgresql_gbim_connection` (`production msallis-db:5433` ★) and `postgresql_geodb_connection` (`forensic postgis-forensic:5452` ★) liveness fields — ★ verify-current field names after April 23 split
>   - `allis_token_service.py` + `allis_auth:8055` + `allis-redis:6380` — token and auth path
>   - `allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032` — AAACPE dedicated stack; always-on; watchdog monitors scraper cron health
>   - `allis-autonomous-learner` (expose port 8020) — `autonomous_learner` ~288/day commits; gap > 48 hours is a watchdog trigger
>   - EEG Delta heartbeat port **8073** — `pulse_count: 12,860+`; stalled pulse is a watchdog trigger
>   - ChromaDB: host **8002** → container 8000; ★ **48 collections, ~6,740,611 total vectors**; `/api/v2/` only; pinned `chromadb/chroma:0.6.3`; drop below 48 collections is a watchdog trigger
>   - Caddy `forward_auth` (OI-36-A CLOSED) — HTTP 401 before port 8050; outermost layer; watchdog checks confirm HTTP 401 on unauthenticated `/chat`
>   - `allis-rag-grounded-v2:7241` — `dgm_available: true`; health watchdog checks this field
> - **OI-35-A CLOSED:** `.ExitCode` removed from `watchdog-containers.sh`.
> - **OI-35-B CLOSED:** `watchdog-meta.sh` installed.
> - **OI-35-C CLOSED:** YAML swarm manifest pattern adopted.
> - **April 23 additions:** AAACPE stack watchdog, `autonomous_learner` gap watchdog, EEG Delta pulse watchdog, ChromaDB collection-count watchdog, and Caddy `forward_auth` confirmation added to watchdog inventory.

---

## Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Allis uses swarms of long-running functions and eternal watchdogs to keep a geographically-entangled AI system healthy, accountable, and aligned with Appalachian communities.

- **P1 – Every where is entangled** by treating system health and governance as a distributed property: no single script or container "owns" safety or uptime. Watchdogs and swarm functions are spread across containers on `msallis-rebuild_qualia-net`, monitoring `production msallis-db:5433` ★ GBIM, `forensic postgis-forensic:5452` ★ geodata, BBB filters, and constitutional guardianship in a way that reflects the interdependence of community systems. The `autonomous_learner` (~288/day commits, growing entanglement graph 11 nodes / 15 cycles at April 1) is itself watched: a commit gap > 48 hours is a governance-level alert, because the learning pipeline's silence means the system is growing less entangled with Appalachian reality, not more.
- **P3 – Power has a geometry** by encoding power into visible, inspectable watchdogs rather than hidden cron jobs. Long-running guardians have explicit tasks, ports, and log targets; communities can see which watchdogs are responsible for which parts of Ms. Allis's behavior. The Caddy `forward_auth` perimeter watchdog (OI-36-A CLOSED) is the outermost expression of this: it confirms HTTP 401 on unauthenticated `/chat` before any ensemble or governance logic is reached.
- **P5 – Design is a geographic act** by making maintenance and self-healing responsive to community-specific infrastructure: `forensic postgis-forensic:5452` ★ (17 GB, 314 PostGIS tables), `local_resources` (207 items / all 55 WV counties), and West Virginia connectivity constraints. A PostGIS watchdog failure is not an abstract database outage — it means geographic queries about county boundaries, ZIP codes, and local resources are potentially returning stale or wrong answers to real people.
- **P12 – Intelligence with a ZIP code** by ensuring that swarm functions respect local time, load, and infrastructure limits when scheduling heavy tasks such as RAG audits and GBIM migrations, and by checking `appalachian_english_corpus` (210 docs, 6-hour cron) freshness as a routine watchdog metric — a stale corpus is a ZIP-code-level intelligence failure.
- **P16 – Power accountable to place** by logging all watchdog actions and swarm functions to `allis-memory:8056` (8 mapped endpoints, survives restarts), `.jsonl` files, and PostgreSQL, so that communities can trace how Ms. Allis recovered from faults and enforced safety policies over time. The `/steg_report` and `/pia_window` endpoints make safeguard-specific watchdog events independently queryable.

As such, this chapter belongs to the **Computational Instrument tier**: it describes concrete watchdogs and swarm functions that keep the Ms. Allis Steward System alive, safe, and auditable.

---

## 35.1 Eternal Watchdogs — Concept and Design

An **eternal watchdog** is a long-running process or container whose sole purpose is to observe and protect a particular invariant of the Ms. Allis system. It is "eternal" not because it can never fail, but because it is embedded in a mesh of other watchdogs and swarm functions that detect and heal failures when they occur.

No single watchdog is trusted absolutely; each is monitored by others. Watchdogs are scoped to specific responsibilities: container liveness, port responsiveness, database connectivity, token enforcement, audit logging, filter configuration (BBB six-filter stack), AAACPE scraper cron health, `autonomous_learner` commit rate, EEG Delta pulse continuity, ChromaDB collection count, and Caddy perimeter confirmation. All watchdog decisions and alerts are written to durable stores, not just to ephemeral logs.

**Key design properties:**
- **Redundancy without confusion:** Multiple watchdogs may check the same invariant, but each has a distinct alert channel or remediation path
- **Self-healing without silent mutation:** Swarm functions may restart containers or repair networks, but all actions are logged and discoverable
- **Minimal authority per watchdog:** Each watchdog has just enough power to fulfill its role — no single guardian can silently rewrite the system

---

## 35.2 Swarm Functions — Long-Running Actions as Graphs

A **swarm function** is a long-running, multi-step maintenance or governance action realized as a task graph executed by a cooperating swarm of processes and containers.

Examples of swarm functions include regenerating RAG indexes for `allis-gis-rag` and `allis-spiritual-rag`, running GBIM consistency checks across `production msallis-db:5433` ★, verifying that ★ 100 containers are Up and correctly attached to `msallis-rebuild_qualia-net`, rebuilding Docker images from canonical `services/` Dockerfiles, running cross-container health checks, verifying AAACPE scraper cron health and `appalachian_english_corpus` freshness, and checking `autonomous_learner` commit rate and ChromaDB collection count.

Each task has a name, dependencies, a command or API call, expected outputs or health signals, and logging requirements. A central orchestrator executes tasks when their dependencies are satisfied.

**Example (simplified): "Verify Eternal Guardian Stack" swarm function (★ April 23, 2026 — updated for two-container split):**

```yaml
swarm_function: verify_eternal_guardian_stack
tasks:
  - name: check_caddy_perimeter
    command: curl -s -o /dev/null -w "%{http_code}" https://egeria.mountainshares.us/chat
    expect: "401"
    note: "OI-36-A CLOSED — Caddy forward_auth must return 401 on unauthenticated /chat"

  - name: check_containers_up
    command: ./scripts/check-containers.sh
    expect: "100 containers Up"

  - name: check_production_msallis_db
    depends_on: [check_containers_up]
    command: ./scripts/check-pg.sh msallis-db 5433
    expect: "connected"
    note: "production msallis-db:5433 ★ — supersedes msallis:5433 April 6"

  - name: check_forensic_postgis
    depends_on: [check_containers_up]
    command: ./scripts/check-pg.sh postgis-forensic 5452
    expect: "connected"
    note: "forensic postgis-forensic:5452 ★ — supersedes gisdb/msallisgis:5432 April 6"

  - name: check_bbb_health
    depends_on: [check_containers_up]
    command: curl -s http://localhost:8016/health
    expect: '"status":"healthy"'

  - name: check_bbb_all_six_filters
    depends_on: [check_bbb_health]
    command: ./scripts/verify-bbb-filters.sh
    expect: "ethical OK, spiritual OK, safety OK, threat_detection OK, steganography OK, truth_verification OK"

  - name: check_guardian_health
    depends_on: [check_production_msallis_db, check_forensic_postgis]
    command: curl -s http://localhost:8091/health
    expect:
      - '"postgresql_gbim_connection":"connected"'
      - '"postgresql_geodb_connection":"connected"'
    note: "verify field names current after April 23 two-container split"

  - name: check_chromadb_collections
    depends_on: [check_containers_up]
    command: curl -s http://localhost:8002/api/v2/collections | jq 'length'
    expect: "48"
    note: "drop below 48 is governance-level alert"

  - name: check_rag_grounded_v2
    depends_on: [check_containers_up]
    command: curl -s http://localhost:7241/health
    expect: '"dgm_available":true'

  - name: check_eeg_delta_pulse
    depends_on: [check_containers_up]
    command: curl -s http://localhost:8073/health
    expect: "pulse_count"
    note: "stalled pulse_count is safeguard infrastructure alert"

  - name: check_autonomous_learner_gap
    depends_on: [check_production_msallis_db]
    command: ./scripts/check-autonomous-learner-gap.sh
    note: "alert if commit gap > 48 hours; baseline ~288/day"

  - name: check_aaacpe_scraper_cron
    depends_on: [check_containers_up]
    command: ./scripts/check-aaacpe-scraper.sh
    note: "verify appalachian_english_corpus not stale beyond 8 hours"

  - name: log_results
    depends_on:
      - check_caddy_perimeter
      - check_containers_up
      - check_production_msallis_db
      - check_forensic_postgis
      - check_bbb_health
      - check_bbb_all_six_filters
      - check_guardian_health
      - check_chromadb_collections
      - check_rag_grounded_v2
      - check_eeg_delta_pulse
      - check_autonomous_learner_gap
      - check_aaacpe_scraper_cron
    command: ./scripts/log-swarm-result.sh verify_eternal_guardian_stack
    log_target: "allis-memory:8056 + logs/swarm-verify-eternal.jsonl"
```

---

## 35.3 Container Watchdog — `watchdog-containers.sh`

The **container watchdog** monitors container state for the entire Ms. Allis stack. Expected baseline: **★ 100 containers Up** (supersedes 105/105 April 6).

**OI-35-A CLOSED:** A previous version used `docker ps --format '{{.Names}} {{.State.ExitCode}}'`, relying on `.ExitCode`, which is not supported on the deployed Docker engine. The fix removes `.ExitCode` from the format string and relies only on `.Status` and pattern matching.

**Corrected script (★ April 23 — updated expected count):**

```bash
#!/usr/bin/env bash
set -euo pipefail

PROJECT=msallis-rebuild
LOGFILE="logs/watchdog-containers.log"
EXPECTED_UP=100
mkdir -p "$(dirname "$LOGFILE")"

timestamp() {
  date -u +"%Y-%m-%dT%H:%M:%SZ"
}

check_containers() {
  local up_count=0 restarting=() exited=()

  while IFS= read -r line; do
    name=$(echo "$line" | awk '{print $1}')
    status=$(echo "$line" | cut -d' ' -f2-)
    case "$status" in
      Up*)          ((up_count++)) ;;
      Restarting*)  restarting+=("$name") ;;
      Exited*)      exited+=("$name") ;;
    esac
  done < <(docker ps --format '{{.Names}} {{.Status}}')

  echo "$(timestamp) up=$up_count restarting=${#restarting[@]} exited=${#exited[@]}" >> "$LOGFILE"

  if [[ "$up_count" -lt "$EXPECTED_UP" ]]; then
    ./scripts/alert-container-state.sh "count_below_expected" "$up_count/$EXPECTED_UP"
  fi

  for name in "${restarting[@]}"; do
    echo "$(timestamp) RESTARTING $name" >> "$LOGFILE"
    ./scripts/alert-container-state.sh "$name" "Restarting"
  done

  for name in "${exited[@]}"; do
    echo "$(timestamp) EXITED $name" >> "$LOGFILE"
    ./scripts/alert-container-state.sh "$name" "Exited"
  done
}

while true; do
  check_containers
  sleep 60
done
```

Key properties: runs as a long-lived process (systemd `Restart=always`); writes structured entries with timestamps; does not attempt auto-restart (auto-healing is handled by swarm functions); alerts if Up count drops below 100.

---

## 35.4 Port Watchdogs — Critical Ports and Health Checks

**Critical port inventory (★ April 23, 2026 — supersedes April 6):**

| Service | Host port | Purpose | Notes |
|:--|:--|:--|:--|
| Caddy `forward_auth` | HTTPS / egeria.mountainshares.us | Outermost perimeter — must return HTTP 401 on unauth | OI-36-A CLOSED |
| `allis-main-brain` | `127.0.0.1:8050` | Gateway / main API | Behind Caddy |
| `allis-blood-brain-barrier` | `127.0.0.1:8016` | BBB six-filter pipeline | All 6 confirmed responding |
| `allis-constitutional-guardian` | `127.0.0.1:8091` | Constitutional authority | `/health` reports PostgreSQL liveness |
| `allis-gis-rag` | `127.0.0.1:8004` | GIS RAG → `rag_grounded_v2` | Two-container PostgreSQL backing |
| `allis-spiritual-rag` | `127.0.0.1:8005` | Spiritual RAG → `rag_grounded_v2` | Verify-current vector count |
| `allis-rag-grounded-v2` | `127.0.0.1:7241` | Judge pipeline truth verification | Health check: `dgm_available: true` |
| `allis-memory` | `127.0.0.1:8056` | Durable audit — 8 endpoints | Survives restarts; `/steg_report` + `/pia_window` |
| `allis-redis` | `127.0.0.1:6380` | Token and async job store | Compose-internal: 6379 |
| `production msallis-db` ★ | `127.0.0.1:5433` | GBIM PostgreSQL | 16 GB, 294 tables — supersedes `msallis:5433` April 6 |
| `forensic postgis-forensic` ★ | `127.0.0.1:5452` | PostGIS geometry | 17 GB, 314 tables — supersedes `gisdb:5432` April 6 |
| `allis-local-resources-db` | `127.0.0.1:5435` | Community resources | `local_resources` 207 items / 55 WV counties |
| ChromaDB | `127.0.0.1:8002` | Vector store | `/api/v2/` only; 48 collections; drop below 48 = alert |
| `allis-aaacpe-scraper` | `127.0.0.1:8048→8033` | AAACPE ingest | Always-on; 6-hour cron health check |
| `allis-aaacpe-rag` | `127.0.0.1:8047→8032` | AAACPE RAG indexer | Verify `appalachian_english_corpus` freshness |
| `allis-autonomous-learner` | expose 8020 (no host bind) | Autonomous learning | Commit gap > 48 hours = alert |
| EEG Delta band | `127.0.0.1:8073` | PIA heartbeat | `pulse_count: 12,860+`; stall = safeguard alert |

Port watchdogs do not attempt remediation directly — they only log and alert. Remediation is handled by swarm functions that can consider global system state.

---

## 35.5 Database Watchdogs — Two-Container PostgreSQL (★ April 23, 2026)

Because Ms. Allis's constitutional, identity, and registration decisions depend heavily on PostgreSQL, **database watchdogs** periodically check that both stores in the two-container split are reachable and responsive.

> **★ April 23 supersession:** The April 6 ground truth described a single `gisdb / msallisgis` instance at `host:5432 / container-internal:5452 — 45 GB / 548 tables`. This is superseded. Watchdog scripts must now target:
> - `production msallis-db` → host **5433** ★ — GBIM entities
> - `forensic postgis-forensic` → host **5452** ★ — PostGIS geometry
>
> Any watchdog script still referencing `PGPORT=5432`, `dbname=gisdb`, or `msallisgis` is pointing at a superseded data source and must be updated before its next production run.

**Updated GBIM watchdog (★ April 23):**

```bash
#!/usr/bin/env bash
set -euo pipefail

PGHOST="localhost"
PGPORT="5433"
PGUSER="${PGUSER:-postgres}"
PGDATABASE="msallis"
LOGFILE="logs/watchdog-pg-gbim.log"
mkdir -p "$(dirname "$LOGFILE")"

timestamp() { date -u +"%Y-%m-%dT%H:%M:%SZ"; }

if psql "host=$PGHOST port=$PGPORT dbname=$PGDATABASE user=$PGUSER" \
    -c "SELECT 1;" > /dev/null 2>&1; then
  echo "$(timestamp) production-msallis-db:5433 OK" >> "$LOGFILE"
else
  echo "$(timestamp) production-msallis-db:5433 FAIL" >> "$LOGFILE"
  ./scripts/alert-pg-state.sh "production-msallis-db" "5433"
fi
```

**Updated PostGIS watchdog (★ April 23):**

```bash
#!/usr/bin/env bash
set -euo pipefail

PGHOST="localhost"
PGPORT="5452"
PGUSER="${PGUSER:-postgres}"
PGDATABASE="postgis_forensic"
LOGFILE="logs/watchdog-pg-postgis.log"
mkdir -p "$(dirname "$LOGFILE")"

timestamp() { date -u +"%Y-%m-%dT%H:%M:%SZ"; }

if psql "host=$PGHOST port=$PGPORT dbname=$PGDATABASE user=$PGUSER" \
    -c "SELECT PostGIS_Version();" > /dev/null 2>&1; then
  echo "$(timestamp) forensic-postgis-forensic:5452 OK" >> "$LOGFILE"
else
  echo "$(timestamp) forensic-postgis-forensic:5452 FAIL" >> "$LOGFILE"
  ./scripts/alert-pg-state.sh "forensic-postgis-forensic" "5452"
fi
```

**`autonomous_learner` commit-gap watchdog (new — April 23):**

```bash
#!/usr/bin/env bash
set -euo pipefail

PGHOST="localhost"
PGPORT="5433"
PGUSER="${PGUSER:-postgres}"
PGDATABASE="msallis"
LOGFILE="logs/watchdog-autonomous-learner.log"
MAX_GAP_HOURS=48

timestamp() { date -u +"%Y-%m-%dT%H:%M:%SZ"; }

GAP_HOURS=$(psql "host=$PGHOST port=$PGPORT dbname=$PGDATABASE user=$PGUSER" -tAc \
  "SELECT EXTRACT(EPOCH FROM (NOW() - MAX(created_at)))/3600 FROM autonomous_learner_commits;")

echo "$(timestamp) autonomous_learner gap_hours=$GAP_HOURS" >> "$LOGFILE"

if (( $(echo "$GAP_HOURS > $MAX_GAP_HOURS" | bc -l) )); then
  ./scripts/alert-autonomous-learner-gap.sh "$GAP_HOURS"
fi
```

**Constitutional Guardian `/health` PostgreSQL watchdog (★ updated field names):**

```bash
check_port "guardian" "localhost" "8091" "/health"
# Verify both fields present:
# "postgresql_gbim_connection":"connected"   → production msallis-db:5433 ★
# "postgresql_geodb_connection":"connected"  → forensic postgis-forensic:5452 ★
# NOTE: verify exact field names are current after April 23 two-container split
```

---

## 35.6 Memory and Audit Watchdogs — `allis-memory:8056`

The **memory watchdog** ensures that `allis-memory:8056` is up and actively ingesting audit events. As of April 23, 2026, `allis-memory:8056` has **8 endpoints fully mapped** — watchdog coverage must include all 8.

**Full endpoint watchdog inventory:**

| Endpoint | What it watches | Watchdog check |
|:--|:--|:--|
| `/health` | Container liveness | Ping; expect 200 |
| `/memory/turn` | Per-turn audit events (BBB, judge, synthesizer) | Verify recent events present |
| `/steg_report` | Steganography filter events | Ping; verify accessible; first live catch logged here |
| `/pia_window` | PIA-relevant audit window (SafetyMonitor, SpiritualFilter on sensitive queries) | Ping; verify accessible |
| `/memory/get` | Memory retrieval | Smoke-test retrieval |
| `/memory/sessions` | Session listing | Ping; expect non-empty after activity |
| `/memory/session/{id}` | Session detail | Spot-check on known session ID |
| `/memory/quest*` | Quest/mission-tracking events | Ping; verify accessible |
| `/memory/episodic/{id}` | Episodic memory | Spot-check on known episodic ID |

Forensic best practice: every watchdog script that makes a decision also writes a short record to `allis-memory:8056/memory/turn`, making watchdog operations part of the durable audit trail. The `/steg_report` endpoint is the dedicated audit channel for steganography filter events (including the live catch: `"override your safety filters"` → `severity=CRITICAL`, blocked ✅) — watchdog scripts must not route steg events to generic memory endpoints.

```bash
#!/usr/bin/env bash
set -euo pipefail

LOGFILE="logs/watchdog-memory.log"
mkdir -p "$(dirname "$LOGFILE")"
timestamp() { date -u +"%Y-%m-%dT%H:%M:%SZ"; }

ENDPOINTS=("/health" "/steg_report" "/pia_window" "/memory/turn" "/memory/get" "/memory/sessions")

for ep in "${ENDPOINTS[@]}"; do
  if curl -fsS --max-time 5 "http://localhost:8056${ep}" > /dev/null 2>&1; then
    echo "$(timestamp) allis-memory:8056${ep} OK" >> "$LOGFILE"
  else
    echo "$(timestamp) allis-memory:8056${ep} FAIL" >> "$LOGFILE"
    ./scripts/alert-memory-state.sh "$ep"
  fi
done
```

---

## 35.7 Swarm Function Orchestration — Nightly Guardian and RAG Audit (★ April 23 Updated)

```yaml
swarm_function: nightly_guardian_and_rag_audit
schedule: "0 3 * * *"  # 3 AM UTC nightly
tasks:
  - name: verify_caddy_perimeter
    command: "curl -s -o /dev/null -w '%{http_code}' https://egeria.mountainshares.us/chat"
    expect: "401"
    note: "OI-36-A CLOSED — first check every night"

  - name: verify_containers_and_ports
    depends_on: [verify_caddy_perimeter]
    command: ./swarm/verify-containers-and-ports.sh
    expect: "100 Up"

  - name: verify_production_msallis_db
    depends_on: [verify_containers_and_ports]
    command: ./swarm/check-pg.sh msallis-db 5433
    expect: "connected"
    note: "production msallis-db:5433 ★ — supersedes msallis:5433"

  - name: verify_forensic_postgis
    depends_on: [verify_containers_and_ports]
    command: ./swarm/check-pg.sh postgis-forensic 5452
    expect: "connected"
    note: "forensic postgis-forensic:5452 ★ — supersedes gisdb:5432"

  - name: verify_guardian_postgres
    depends_on: [verify_production_msallis_db, verify_forensic_postgis]
    command: ./swarm/verify-guardian-pg.sh
    expect:
      - '"postgresql_gbim_connection":"connected"'
      - '"postgresql_geodb_connection":"connected"'

  - name: verify_bbb_filters
    depends_on: [verify_containers_and_ports]
    command: ./swarm/verify-bbb-filters.sh
    expect: "all 6 filters responding"
    note: "EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, steganography_filter, truth_verification"

  - name: verify_rag_grounded_v2_bbb
    depends_on: [verify_bbb_filters]
    command: ./swarm/verify-rag-bbb.sh
    expect: '"dgm_available":true'

  - name: verify_rag_grounded_v2_judge
    depends_on: [verify_bbb_filters]
    command: ./swarm/verify-rag-judge.sh

  - name: verify_chromadb_collections
    depends_on: [verify_containers_and_ports]
    command: "curl -s http://localhost:8002/api/v2/collections | jq 'length'"
    expect: "48"
    note: "drop below 48 = governance-level alert; /api/v2/ only"

  - name: verify_appalachian_corpus_freshness
    depends_on: [verify_containers_and_ports]
    command: ./swarm/check-aaacpe-freshness.sh
    note: "appalachian_english_corpus 210 docs; cron 0 */6 * * *; stale > 8 hours = alert"

  - name: verify_autonomous_learner_gap
    depends_on: [verify_production_msallis_db]
    command: ./swarm/check-autonomous-learner-gap.sh
    note: "alert if gap > 48 hours; baseline ~288/day"

  - name: verify_eeg_delta_pulse
    depends_on: [verify_containers_and_ports]
    command: "curl -s http://localhost:8073/health"
    expect: "pulse_count"
    note: "pulse_count: 12,860+ baseline; stall = safeguard infrastructure alert"

  - name: verify_local_resources_coverage
    depends_on: [verify_production_msallis_db]
    command: ./swarm/check-local-resources.sh
    expect: "207 items / 55 counties"
    note: "any reduction = governance-level alert"

  - name: write_summary_to_allis_memory
    depends_on:
      - verify_caddy_perimeter
      - verify_containers_and_ports
      - verify_production_msallis_db
      - verify_forensic_postgis
      - verify_guardian_postgres
      - verify_bbb_filters
      - verify_rag_grounded_v2_bbb
      - verify_rag_grounded_v2_judge
      - verify_chromadb_collections
      - verify_appalachian_corpus_freshness
      - verify_autonomous_learner_gap
      - verify_eeg_delta_pulse
      - verify_local_resources_coverage
    command: ./swarm/log-summary.sh nightly_guardian_and_rag_audit
    log_target: "allis-memory:8056 + logs/nightly-audit.jsonl"
```

---

## 35.8 Eternal Properties — How Watchdogs Watch Themselves

Eternal watchdogs remain effective because they themselves are subject to watchdogging and swarm functions.

**OI-35-B CLOSED:** `watchdog-meta.sh` is installed and wired into a nightly swarm function and a frequent cron job. It checks that watchdog log files are being updated within expected windows and alerts if a watchdog appears silent for too long.

```bash
#!/usr/bin/env bash
set -euo pipefail

LOGFILE="logs/watchdog-meta.log"
mkdir -p "$(dirname "$LOGFILE")"
timestamp() { date -u +"%Y-%m-%dT%H:%M:%SZ"; }

check_log_fresh() {
  local file=$1 max_age=$2
  if [ ! -f "$file" ]; then
    echo "$(timestamp) MISSING $file" >> "$LOGFILE"
    ./scripts/alert-meta.sh "missing_log" "$file"
    return
  fi
  local age
  age=$(($(date +%s) - $(stat -c %Y "$file")))
  if [ "$age" -gt "$max_age" ]; then
    echo "$(timestamp) STALE $file age=${age}s" >> "$LOGFILE"
    ./scripts/alert-meta.sh "stale_log" "$file"
  else
    echo "$(timestamp) FRESH $file" >> "$LOGFILE"
  fi
}

# Core watchdogs — 5-minute freshness threshold
check_log_fresh "logs/watchdog-containers.log" 300
check_log_fresh "logs/watchdog-ports.log" 300

# Database watchdogs — 15-minute freshness threshold
check_log_fresh "logs/watchdog-pg-gbim.log" 900
check_log_fresh "logs/watchdog-pg-postgis.log" 900

# Audit and memory watchdogs
check_log_fresh "logs/watchdog-memory.log" 900

# New April 23 watchdogs — 1-hour freshness threshold
check_log_fresh "logs/watchdog-autonomous-learner.log" 3600
check_log_fresh "logs/watchdog-aaacpe-scraper.log" 3600
```

**Pattern for self-monitoring watchdogs:**
- **Host-level systemd units** with `Restart=always` for key watchdog scripts
- **Meta-watchdog** checks that watchdog log files are fresh and watchdog processes are running
- **Swarm self-audit:** periodic swarm functions verify watchdog scripts are present and executable, confirm systemd units are enabled, and run smoke tests by intentionally stopping a non-critical container and observing whether watchdogs detect and alert

---

## 35.9 Production Startup and Post-Start Swarm Hook

The **canonical production startup sequence** (★ April 23, 2026 — fully documented):

```bash
# Step 1 — bring the compose stack up
docker compose up -d

# Step 2 — wire legacy containers to the compose network
#   (connects msallis-pgdata-rescue and other standalone containers
#    to msallis-rebuild_qualia-net; repairs network drift)
bash scripts/post-start.sh

# Step 3 — initialize swarm functions and eternal watchdogs
bash scripts/post-start-swarm.sh
```

`post-start-swarm.sh` is responsible for:
- Starting or verifying systemd units for: container watchdog, port watchdog, two-container database watchdogs (`production msallis-db:5433` ★ + `forensic postgis-forensic:5452` ★), memory watchdog (all 8 endpoints), meta-watchdog, AAACPE scraper watchdog, `autonomous_learner` gap watchdog, EEG Delta pulse watchdog
- Verifying the Caddy `forward_auth` perimeter (OI-36-A CLOSED) is active — HTTP 401 on unauthenticated `/chat` before watchdog stack is declared healthy
- Registering the current host and environment in a swarm manifest
- Running the `verify_eternal_guardian_stack` smoke-test swarm function (§35.2) to confirm the guardianship layer is operational

This ensures that **every stack reboot also reboots the swarm of watchdogs**, and that no post-restart state is declared healthy until the Caddy perimeter and both PostgreSQL stores are confirmed active.

Cross-reference: Ch 31 §31.6 (canonical startup in operational roles context); Ch 33 §33.9 (startup as Step 1 of example flow); Ch 37 §37.2 (`post-start.sh` requirement for Constitutional Guardian).

---

## 35.10 Open Items Status (★ April 23, 2026)

| OI | Status | Notes |
|:--|:--|:--|
| OI-35-A — Container Watchdog `.ExitCode` Bug | ✅ CLOSED | `.ExitCode` removed; `.Status` pattern matching; expected count updated to 100 |
| OI-35-B — Eternal Watchdog Meta-Monitoring | ✅ CLOSED | `watchdog-meta.sh` installed; April 23 adds `autonomous_learner` and AAACPE log checks |
| OI-35-C — Swarm Function Manifest and Logging | ✅ CLOSED | YAML manifest pattern; `log-swarm-result.sh` → `allis-memory:8056` |
| ★ PostgreSQL two-container watchdog update | ✅ APPLIED (April 23) | All watchdog scripts updated from `msallis:5433` + `gisdb:5452` to `production msallis-db:5433` ★ + `forensic postgis-forensic:5452` ★ |
| ★ AAACPE scraper cron watchdog | ✅ ACTIVE (April 23) | `check-aaacpe-freshness.sh`; stale > 8 hours = alert |
| ★ `autonomous_learner` commit-gap watchdog | ✅ ACTIVE (April 23) | Gap > 48 hours = governance alert; queries `production msallis-db:5433` ★ |
| ★ EEG Delta pulse watchdog (port 8073) | ✅ ACTIVE (April 23) | `pulse_count: 12,860+` baseline; stall = safeguard infrastructure alert |
| ★ ChromaDB collection-count watchdog | ✅ ACTIVE (April 23) | Drop below 48 = governance-level alert; `/api/v2/` only |
| ★ Caddy `forward_auth` confirmation in swarm | ✅ ACTIVE (April 23) | HTTP 401 check added to `verify_eternal_guardian_stack` and nightly audit |
| ★ `allis-memory:8056` all-8-endpoint watchdog | ✅ ACTIVE (April 23) | All 8 endpoints covered including `/steg_report` + `/pia_window` |
| ★ `local_resources` coverage watchdog | ✅ ACTIVE (April 23) | 207 items / 55 WV counties; any reduction = governance alert |

---

## Cross-Reference Map

| This section | Cross-chapter reference |
|:--|:--|
| §35.2 `verify_eternal_guardian_stack` | Ch 31 §31.7 (seven-layer stack); Ch 32 §32.6 (swarm functions in DGM context) |
| §35.2 Caddy perimeter check as first task | Ch 31 §31.3 (OI-36-A CLOSED); Ch 36 §36.2 (zero-th gate); Ch 37 §37.2 |
| §35.4 port inventory — two-container split | Ch 28 §28.7 (GIS RAG detail); Ch 33 §33.7 (PostgreSQL grounding) |
| §35.5 two-container database watchdogs | Ch 28 §28.7 (split detail); Ch 37 §37.3 (postgresql_validation block) |
| §35.5 `autonomous_learner` commit-gap watchdog | Ch 27 §27.4 (autonomous learning); Ch 32 §32.7 (GBIM as DGM signal) |
| §35.6 `allis-memory:8056` 8-endpoint map | Ch 31 §31.7 (Layer 6 durable audit); Ch 33 §33.8 (audit scope table) |
| §35.6 `/steg_report` endpoint | Ch 29 §29.3 (steg catch); Ch 32 §32.8 (DGM worked example) |
| §35.7 nightly audit — `local_resources` check | Ch 31 §31.5; Ch 34 §34.6a (calling as geographic fact) |
| §35.7 `appalachian_english_corpus` freshness | Ch 30 §30.3b (crontab hygiene); Ch 34 §34.2 (corpus linguistic grounding) |
| §35.7 EEG Delta pulse check | Ch 28 §28.4 (EEG rhythm); Ch 34 §34.4b (spiritual-root signal) |
| §35.9 canonical startup | Ch 31 §31.6 (operational roles); Ch 33 §33.9 (example flow Step 1); Ch 37 §37.2 |

---

*Chapter 35 — Swarm Functions and Eternal Watchdogs*
*Ms. Egeria Allis Steward System — Harmony for Hope, Inc.*
*Mount Hope, West Virginia*
*Last updated: ★ 2026-04-23 — Carrie Kidd (Mamma Kidd)*
*★ 100 containers Up — all Chapter 35 OIs CLOSED — PostgreSQL two-container watchdogs active: `production msallis-db:5433` ★ + `forensic postgis-forensic:5452` ★ — ChromaDB 48-collection count watchdog active — AAACPE scraper freshness watchdog active — `autonomous_learner` commit-gap watchdog active — EEG Delta pulse watchdog active — Caddy `forward_auth` perimeter confirmation in every swarm run — `allis-memory:8056` all 8 endpoints watched — eternal watchdogs and swarm functions active on `msallis-rebuild_qualia-net`*
