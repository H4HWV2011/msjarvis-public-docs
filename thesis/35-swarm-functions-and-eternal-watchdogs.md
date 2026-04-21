# Chapter 35 — Swarm Functions and Eternal Watchdogs

**Carrie Kidd (Mamma Kidd) · Mount Hope, WV**  
**Last updated: ★★★★ April 6, 2026 — FINAL REWRITE**  
**105/105 containers Up (zero Restarting, zero Exited). All Chapter 35 OIs CLOSED. Ch. 36, 37, and 38 sprint contracts opened and structurally wired. Eternal watchdogs, swarm functions, and long-running guardians stabilized on `msallis-rebuild_qualia-net`; `allis-watchdogs` and `allis-swarm-functions` now behave as autonomous, self-healing infrastructure stewards rather than brittle cron scripts.**

---

> **Permanent ground truth for this chapter (★★★★ April 6, 2026):**
>
> - **Compose project network:** `msallis-rebuild_qualia-net` is the canonical Docker network for the production stack.
> - **Watchdog layer:** Eternal watchdogs are implemented as containers and scripts that continuously monitor:
>   - Container state (Up / Restarting / Exited),
>   - Port responsiveness for critical services,
>   - PostgreSQL `msallis:5433` and `gisdb` / `msallisgis:5432` liveness,
>   - `allis-memory:8056` durable audit availability,
>   - Token enforcement paths (gateway → `allis_auth:8055` → Redis `allis-redis:6380`).
> - **Swarm functions:** Long-running, multi-step maintenance actions (e.g., rebuilding images, regenerating indexes, running RAG audits, and cross-container health checks) are modeled as **swarm functions**:
>   - Declarative **task graphs** with dependencies,
>   - Executed by a **swarm of cooperating processes and containers**,
>   - Logged to `allis-memory:8056` and PostgreSQL where applicable.
> - **Eternal property:** Watchdogs and swarm functions are designed so that if any one guardian fails, **another independent mechanism detects and repairs the failure**.
> - **Port ground truth (cross-chapter alignment):**
>   - `msallis:5433` — GBIM entities with `confidence_decay` metadata.
>   - `gisdb` / `msallisgis`: host `5432` / container-internal `5452` — ★ 45 GB / 548 tables (Ch. 33 April 6, 2026).
>   - `allis-memory:8056` — durable audit and memory service.
>   - `allis-blood-brain-barrier:8016` — six-filter BBB.
>   - `allis-constitutional-guardian:8091` — constitutional authority.
>   - `allis_token_service.py` + `allis_auth:8055` + `allis-redis:6380` — token and auth path.
> - **Watchdog cosmetic fix (Sprint 3):** `.ExitCode` template field was removed from `watchdog-containers.sh` to match the deployed Docker version (no `.ExitCode` in `docker ps --format`); failure mode documented as part of this chapter.

---

## Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Allis uses swarms of long-running functions and eternal watchdogs to keep a geographically-entangled AI system healthy, accountable, and aligned with Appalachian communities.

- **P1 – Every where is entangled** by treating system health and governance as a distributed property: no single script or container “owns” safety or uptime. Watchdogs and swarm functions are spread across containers on `msallis-rebuild_qualia-net`, monitoring `msallis` GBIM, `gisdb` geodata, BBB filters, and constitutional guardianship in a way that reflects the interdependence of community systems.
- **P3 – Power has a geometry** by encoding power into visible, inspectable watchdogs rather than hidden cron jobs. Long-running guardians have explicit tasks, ports, and log targets; communities can see which watchdogs are responsible for which parts of Ms. Allis’s behavior.
- **P5 – Design is a geographic act** by making maintenance and self-healing responsive to community-specific infrastructure: PostGIS `gisdb` (45 GB / 548 tables), county-level services, and West Virginia connectivity constraints.
- **P12 – Intelligence with a ZIP code** by ensuring that swarm functions respect local time, load, and infrastructure limits when scheduling heavy tasks such as RAG audits and GBIM migrations.
- **P16 – Power accountable to place** by logging all watchdog actions and swarm functions to durable audit stores (`allis-memory:8056`, `.jsonl` files, and PostgreSQL), so that communities can trace how Ms. Allis recovered from faults and enforced safety policies over time.

As such, this chapter belongs to the **Computational Instrument tier**: it describes concrete watchdogs and swarm functions that keep the Ms. Allis Steward System alive, safe, and auditable.

---

## 35.1 Eternal Watchdogs — Concept and Design

An **eternal watchdog** is a long-running process or container whose sole purpose is to observe and protect a particular invariant of the Ms. Allis system. It is “eternal” not because it can never fail, but because it is **embedded in a mesh of other watchdogs and swarm functions** that detect and heal failures when they occur.

In this architecture:

- No single watchdog is trusted absolutely; each is monitored by others.
- Watchdogs are **scoped** to specific responsibilities:
  - Container liveness,
  - Port responsiveness,
  - Database connectivity,
  - Token enforcement,
  - Audit logging,
  - Filter configuration (e.g., BBB six-filter stack).
- All watchdog decisions and alerts are written to durable stores, not just to ephemeral logs.

**Key design properties:**

1. **Redundancy without confusion:** Multiple watchdogs may check the same invariant, but each is clearly documented and has a distinct alert channel or remediation path.
2. **Self-healing without silent mutation:** Swarm functions may restart containers or repair networks, but all actions are logged and discoverable.
3. **Minimal authority per watchdog:** Each watchdog has just enough power to fulfill its role — no single guardian can silently rewrite the system.

---

## 35.2 Swarm Functions — Long-Running Actions as Graphs

A **swarm function** is a long-running, multi-step maintenance or governance action realized as a **task graph** executed by a cooperating swarm of processes and containers.

Examples of swarm functions include:

- Regenerating RAG indexes for `allis-gis-rag` and `allis-spiritual-rag`,
- Running GBIM consistency checks across `msallis:5433`,
- Verifying that all 105/105 containers are Up and correctly attached to `msallis-rebuild_qualia-net`,
- Rebuilding Docker images from canonical `services/` Dockerfiles (e.g., for RAG and guardian services),
- Running cross-container health checks to ensure `allis-constitutional-guardian`, BBB, and gateway are all alive and wired correctly.

Swarm functions are described declaratively:

- Each task has:
  - A name,
  - Dependencies,
  - A command or API call,
  - Expected outputs or health signals,
  - Logging requirements (where to write status and audit records).
- A central orchestrator (which may itself be redundant and watched) executes tasks when their dependencies are satisfied.

**Example (simplified): “Verify Eternal Guardian Stack” swarm function**

```yaml
swarm_function: verify_eternal_guardian_stack
tasks:
  - name: check_containers_up
    command: ./scripts/check-containers.sh
    expect: "105/105 Up"
  - name: check_msallis_postgres
    depends_on: [check_containers_up]
    command: ./scripts/check-pg.sh msallis 5433
    expect: "connected"
  - name: check_msallisgis_postgis
    depends_on: [check_containers_up]
    command: ./scripts/check-pg.sh msallisgis 5452
    expect: "connected"
  - name: check_bbb_health
    depends_on: [check_containers_up]
    command: curl -s http://localhost:8016/health
    expect: '"status":"healthy"'
  - name: check_guardian_health
    depends_on: [check_msallis_postgres, check_msallisgis_postgis]
    command: curl -s http://localhost:8091/health
    expect:
      - '"postgresql_gbim_connection":"connected"'
      - '"postgresql_geodb_connection":"connected"'
  - name: log_results
    depends_on:
      - check_containers_up
      - check_msallis_postgres
      - check_msallisgis_postgis
      - check_bbb_health
      - check_guardian_health
    command: ./scripts/log-swarm-result.sh verify_eternal_guardian_stack
```

The goal is to make maintenance **visible and inspectable**, not ad-hoc.

---

## 35.3 Container Watchdog — `watchdog-containers.sh`

The **container watchdog** monitors container state for the entire Ms. Allis stack.

**Original failure mode (documented and corrected):**

- A previous version used `docker ps --format '{{.Names}} {{.State.ExitCode}}'`, relying on `.ExitCode`, which is **not supported** on the deployed Docker engine.
- This caused the script to print errors and fail to parse output correctly.

**Permanent fix:**

- Remove `.ExitCode` from the format string.
- Use only supported fields such as `.Names`, `.Status`, and `.RunningFor`.
- Translate `Status` strings into Up/Exited/Restarting categories.

**Corrected script (simplified):**

```bash
#!/usr/bin/env bash
set -euo pipefail

PROJECT=msallis-rebuild
LOGFILE="logs/watchdog-containers.log"
mkdir -p "$(dirname "$LOGFILE")"

timestamp() {
  date -u +"%Y-%m-%dT%H:%M:%SZ"
}

check_containers() {
  docker ps --format '{{.Names}} {{.Status}}' |
  while read -r name status; do
    case "$status" in
      Up*) state="Up" ;;
      Restarting*) state="Restarting" ;;
      Exited*) state="Exited" ;;
      *) state="Unknown" ;;
    esac

    echo "$(timestamp) $name $state" >> "$LOGFILE"

    if [[ "$state" != "Up" ]]; then
      ./scripts/alert-container-state.sh "$name" "$state"
    fi
  done
}

while true; do
  check_containers
  sleep 60
done
```

**Key properties:**

- Runs as a long-lived process (systemd service or container) on the host.
- Writes structured entries with timestamps to `logs/watchdog-containers.log`.
- Calls `alert-container-state.sh` only when containers are Restarting or Exited.
- Does **not** attempt auto-restart; auto-healing is handled by a separate swarm function.

---

## 35.4 Port Watchdogs — Critical Ports and Health Checks

To ensure that critical services remain reachable, **port watchdogs** perform regular checks against a set of canonical endpoints.

**Critical ports (non-exhaustive):**

| Service                         | Port mapping                    | Purpose                                          |
|:--------------------------------|:--------------------------------|:------------------------------------------------|
| `allis-main-brain`             | `127.0.0.1:8050`               | Gateway / main API                               |
| `allis-blood-brain-barrier`    | `127.0.0.1:8016`               | BBB six-filter pipeline                          |
| `allis-constitutional-guardian`| `127.0.0.1:8091`               | Constitutional authority                         |
| `allis-gis-rag`                | `127.0.0.1:8004`               | GIS RAG for `rag_grounded_v2`                   |
| `allis-spiritual-rag`          | `127.0.0.1:8005`               | Spiritual RAG for `rag_grounded_v2`             |
| `allis-rag-grounded-v2`        | `127.0.0.1:7241`               | Judge pipeline `rag_grounded_v2` component      |
| `allis-memory`                 | `127.0.0.1:8056`               | Durable audit and memory                        |
| `allis-redis`                  | `127.0.0.1:6380`               | Token and async job store                       |
| `msallis`                      | `127.0.0.1:5433`               | GBIM PostgreSQL                                  |
| `gisdb` / `msallisgis`         | `127.0.0.1:5432`               | PostGIS                                          |

**Port watchdog script (simplified):**

```bash
#!/usr/bin/env bash
set -euo pipefail

LOGFILE="logs/watchdog-ports.log"
mkdir -p "$(dirname "$LOGFILE")"

timestamp() {
  date -u +"%Y-%m-%dT%H:%M:%SZ"
}

check_port() {
  local name=$1 host=$2 port=$3 path=$4
  local url="http://$host:$port$path"

  if curl -fsS --max-time 5 "$url" > /dev/null; then
    echo "$(timestamp) $name OK $url" >> "$LOGFILE"
  else
    echo "$(timestamp) $name FAIL $url" >> "$LOGFILE"
    ./scripts/alert-port-state.sh "$name" "$url"
  fi
}

while true; do
  check_port "main_brain" "localhost" "8050" "/health"
  check_port "bbb"        "localhost" "8016" "/health"
  check_port "guardian"   "localhost" "8091" "/health"
  check_port "memory"     "localhost" "8056" "/health"
  sleep 60
done
```

Port watchdogs **do not** attempt remediation directly; they only log and alert. Remediation is handled by swarm functions that can consider global system state.

---

## 35.5 Database Watchdogs — `msallis` and `gisdb`

Because Ms. Allis’s constitutional, identity, and registration decisions depend heavily on PostgreSQL, **database watchdogs** periodically check that:

- `msallis:5433` is reachable and responsive,
- `gisdb` / `msallisgis:5452` is reachable from inside the Docker network,
- Key tables (e.g., GBIM entities, ZCTA boundaries) are present,
- Liveness is visible in service `/health` endpoints (e.g., `allis-constitutional-guardian:8091`).

**Host-side GBIM check (simplified):**

```bash
#!/usr/bin/env bash
set -euo pipefail

PGHOST="localhost"
PGPORT="5433"
PGUSER="${PGUSER:-postgres}"
PGDATABASE="msallis"
LOGFILE="logs/watchdog-pg-gbim.log"
mkdir -p "$(dirname "$LOGFILE")"

timestamp() {
  date -u +"%Y-%m-%dT%H:%M:%SZ"
}

if psql "host=$PGHOST port=$PGPORT dbname=$PGDATABASE user=$PGUSER" \
    -c "SELECT 1;" > /dev/null 2>&1; then
  echo "$(timestamp) msallis:5433 OK" >> "$LOGFILE"
else
  echo "$(timestamp) msallis:5433 FAIL" >> "$LOGFILE"
  ./scripts/alert-pg-state.sh "msallis" "5433"
fi
```

**Guardian `/health` PostgreSQL watchdog:**

- The `allis-constitutional-guardian` `/health` endpoint now reports:
  - `"postgresql_gbim_connection": "connected"` or `"error: ..."`
  - `"postgresql_geodb_connection": "connected"` or `"error: ..."`
- A watchdog task calls this endpoint and alerts whenever either field is not `"connected"`.

This ensures that **database liveness is visible from both host and container perspectives**.

---

## 35.6 Memory and Audit Watchdogs — `allis-memory:8056`

The **memory watchdog** ensures that `allis-memory:8056` is up and actively ingesting audit events.

Responsibilities:

- Ping `allis-memory:8056/health` regularly.
- Verify that recent gate decisions are present:
  - BBB filter events,
  - Identity enforcement events,
  - Token validation events (`allis_auth:8055`),
  - Constitutional guardian decisions,
  - Swarm function and watchdog operations themselves.

**Example verification snippet:**

```bash
#!/usr/bin/env bash
set -euo pipefail

LOGFILE="logs/watchdog-memory.log"
mkdir -p "$(dirname "$LOGFILE")"

timestamp() {
  date -u +"%Y-%m-%dT%H:%M:%SZ"
}

if curl -fsS --max-time 5 "http://localhost:8056/health" > /dev/null; then
  echo "$(timestamp) allis-memory:8056 OK" >> "$LOGFILE"
else
  echo "$(timestamp) allis-memory:8056 FAIL" >> "$LOGFILE"
  ./scripts/alert-memory-state.sh
fi
```

Forensic best practice: every watchdog script that makes a decision can also write a short record to `allis-memory:8056`, making watchdog operations part of the durable audit trail.

---

## 35.7 Swarm Function Orchestration — Example Patterns

Swarm functions can be orchestrated using simple tools (e.g., `bash` and `cron`) or more advanced task runners. The core pattern is:

1. **Describe tasks** in a YAML or JSON manifest.
2. **Resolve dependencies** and build an execution order.
3. **Execute tasks** with reasonable timeouts and retries.
4. **Log outcomes** to:
   - `allis-memory:8056`,
   - `.jsonl` or `.log` files,
   - PostgreSQL tables where appropriate.

**Example: “Nightly Guardian and RAG Audit” swarm function**

```yaml
swarm_function: nightly_guardian_and_rag_audit
schedule: "0 3 * * *"  # 3 AM UTC nightly
tasks:
  - name: verify_containers_and_ports
    command: ./swarm/verify-containers-and-ports.sh
  - name: verify_guardian_postgres
    depends_on: [verify_containers_and_ports]
    command: ./swarm/verify-guardian-pg.sh
  - name: verify_bbb_filters
    depends_on: [verify_containers_and_ports]
    command: ./swarm/verify-bbb-filters.sh
  - name: verify_rag_grounded_v2_bbb
    depends_on: [verify_bbb_filters]
    command: ./swarm/verify-rag-bbb.sh
  - name: verify_rag_grounded_v2_judge
    depends_on: [verify_bbb_filters]
    command: ./swarm/verify-rag-judge.sh
  - name: write_summary_to_allis_memory
    depends_on:
      - verify_containers_and_ports
      - verify_guardian_postgres
      - verify_bbb_filters
      - verify_rag_grounded_v2_bbb
      - verify_rag_grounded_v2_judge
    command: ./swarm/log-summary.sh nightly_guardian_and_rag_audit
```

The goal is for **every critical invariant** to be checked at least daily by a swarm function with full audit.

---

## 35.8 Eternal Properties — How Watchdogs Watch Themselves

Eternal watchdogs remain effective because they themselves are **subject to watchdogging and swarm functions**.

Patterns used in Ms. Allis:

- **Host-level systemd units** with `Restart=always` for key watchdog scripts (e.g., container and port watchdogs).
- **Meta-watchdog** that:
  - Checks that watchdog processes are running,
  - Verifies that watchdog log files are being updated,
  - Alerts if a watchdog appears “silent” for too long.
- **Swarm self-audit:** periodic swarm functions that:
  - Verify watchdog scripts are present and executable,
  - Confirm systemd units are enabled,
  - Run “smoke tests” by intentionally stopping a non-critical container and observing whether watchdogs detect and alert.

Example meta-watchdog snippet:

```bash
#!/usr/bin/env bash
set -euo pipefail

LOGFILE="logs/watchdog-meta.log"
mkdir -p "$(dirname "$LOGFILE")"

timestamp() {
  date -u +"%Y-%m-%dT%H:%M:%SZ"
}

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

check_log_fresh "logs/watchdog-containers.log" 300
check_log_fresh "logs/watchdog-ports.log" 300
check_log_fresh "logs/watchdog-pg-gbim.log" 900
check_log_fresh "logs/watchdog-memory.log" 900
```

This makes watchdog failure **detectable** and auditable.

---

## 35.9 Production Startup and Post-Start Swarm Hook

As documented in Chapters 33, 36, and 37, the **canonical production startup sequence** is:

```bash
# Step 1 — bring the compose stack up
docker compose up -d

# Step 2 — wire legacy containers to the compose network
bash scripts/post-start.sh
```

Chapter 35 adds a **Step 3** for swarm initialization:

```bash
# Step 3 — initialize swarm functions and eternal watchdogs
bash scripts/post-start-swarm.sh
```

`post-start-swarm.sh` is responsible for:

- Starting or verifying systemd units for:
  - Container watchdog,
  - Port watchdog,
  - Database watchdog,
  - Memory watchdog,
  - Meta-watchdog.
- Registering the current host and environment in a swarm manifest so that future maintenance functions know where to run.
- Running a quick “smoke test” swarm function (e.g., `verify_eternal_guardian_stack`) to ensure that the guardianship layer is operational.

This ensures that **every stack reboot** also reboots the swarm of watchdogs.

---

## 35.10 Open Items — Chapter 35 (★★★★ All CLOSED)

As of April 6, 2026, all Chapter 35 open items are closed:

- **OI-35-A — Container Watchdog `.ExitCode` Bug:**
  - **Issue:** The watchdog referenced `.ExitCode` in `docker ps --format`, which is unsupported in the deployed Docker engine.
  - **Fix:** Remove `.ExitCode` from the format string; rely on `.Status` and pattern matching; document this chapter as the permanent record of the failure mode.
  - **Status:** ✅ CLOSED. `watchdog-containers.sh` updated; log and alert patterns confirmed.

- **OI-35-B — Eternal Watchdog Meta-Monitoring:**
  - **Issue:** No meta-watchdog existed to ensure that watchdog logs were fresh and watchdog processes were running.
  - **Fix:** Implement `watchdog-meta.sh` and wire it into a nightly swarm function plus a frequent cron job; logs to `logs/watchdog-meta.log`.
  - **Status:** ✅ CLOSED. Meta-watchdog installed and documented.

- **OI-35-C — Swarm Function Manifest and Logging:**
  - **Issue:** Swarm functions were implicit and undocumented, implemented as one-off scripts.
  - **Fix:** Define YAML-based swarm manifests and `log-swarm-result.sh` to push summary records into `allis-memory:8056`.
  - **Status:** ✅ CLOSED. Swarm manifest pattern adopted for nightly guardian and RAG audits.

---

## 35.11 Summary

Chapter 35 formalizes the **swarm functions and eternal watchdogs** that keep Ms. Allis alive, safe, and accountable:

- Watchdogs continuously monitor containers, ports, databases, memory, and themselves.
- Swarm functions perform long-running maintenance and governance tasks using declarative task graphs.
- All guardian actions are logged to durable stores, making maintenance and safety **transparent and auditable**.
- A documented startup sequence (`docker compose up -d`, `post-start.sh`, `post-start-swarm.sh`) ensures that the swarm of watchdogs comes up alongside the core services.
- All Chapter 35 open items are closed, and the eternal guardianship layer is stable for future expansion in Chapters 36–38.

---

*Chapter 35 — Swarm Functions and Eternal Watchdogs*  
*Ms. Egeria Allis Steward System — Harmony for Hope, Inc.*  
*Mount Hope, West Virginia*  
*SEALED: ★★★★ April 6, 2026 — FINAL REWRITE*  
*105/105 containers Up — eternal watchdogs and swarm functions active on `msallis-rebuild_qualia-net`*  
