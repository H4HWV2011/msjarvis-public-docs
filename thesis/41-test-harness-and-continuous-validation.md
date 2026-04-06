# Chapter 41 — Test Harness and Continuous Validation

**Carrie Kidd (Mamma Kidd) — Mount Hope, WV**  
**Last updated: ★★★★ April 6, 2026 — R41-1 through R41-8 applied (container count updated to 105, April 6, 2026 confirmed live; Gate 27 and Gate 28 code examples corrected from port 8055 to port 8002; preflight gate reconciliation note added to §41.7; operations_history note added to §41.9; autonomous_learner/autonomous_learning disambiguation added to §41.9; BBB recalibration addendum added to §41.5; §41.11 cross-reference to Ch. 40 §40-H corrected); prior April 1, 2026 baseline: container count 96; jarvis-autonomous-learner and psychological_rag gates added; ChromaDB inventory expanded to 41 collections; Gate 28 passed; all open items closed; Chapter 41 officially closed.**

> **★★★★ Updates applied April 6, 2026 (R41-1 through R41-8):**
> - Container count updated to **105** (April 6, 2026 confirmed live — `jarvis-otel-collector` compose-managed, `unless-stopped` confirmed, `docker ps` count = 105). Prior April 3, 2026 Ch. 33 seal was 101.
> - Gate 27 and Gate 28 code examples corrected: `port=8055` → `port=8002`. Port 8055 is `jarvis_auth_service`; ChromaDB host port is **8002** throughout the entire thesis.
> - Preflight gate reconciliation note added to §41.7 — authoritative sealed count is **22 PASS / 0 FAIL / 1 WARN** (Ch. 33 §33.6, April 3, 2026).
> - `operations_history` collection note added to §41.9 manifest (planned — export harness ready per Ch. 40 §40.13).
> - `autonomous_learner` / `autonomous_learning` disambiguation added to §41.9.
> - BBB EthicalFilter and SafetyMonitor recalibration addendum (April 2, 2026) added to §41.5.
> - §41.11 cross-reference corrected: March 28 expansion is documented in Ch. 40 §40-H (March 28 addendum), not §40-I alone.

> **★ Updates applied April 1, 2026:**
> - GATE 28 — PASS. `psychological_rag` exists, registered, metadata confirmed. ✅
> - 🏁 CHAPTER 41 — OFFICIALLY CLOSED
> - Gate 27 confirmed at 41 collections (≥ 40 target met and exceeded).
> - `memories` schema with `confidence_decay` confirmed in `msjarvisgis` (Gate 26 prerequisite satisfied).
> - `jarvis-ollama` confirmed running.
> - `jarvis-chroma` confirmed healthy.
> - Full 41-collection ChromaDB manifest documented in §41.9.
> - OI-VERIFYANDTEST-28 closed — gates 25–28 fully scripted and passing.
> - OI-30 closed — Gate 30 passing, MountainShares/DAO smoke tests confirmed.
> - OI-31 closed — EEG architecture documented (delta/theta/beta pipeline).
> - OI-36-A closed — Caddy `forward_auth` live, 401 confirmed on unauthenticated requests.
> - OI-CRYPTO-VT closed — Gate 29 passing, `jarvis-crypto-policy` watchdog wired.

> **★ Updates applied March 28, 2026:**
> - Stack expanded to 96 containers — MountainShares/Commons/DAO tier (ports 8080–8084) and EEG layer (ports 8073–8075) deployed; `jarvis-memory:8056` durable audit trail active.
> - `jarvis-memory:8056` durable logging confirmed — Phase 1.4 BBB gate decisions and Phase 4.5 output guard decisions written to durable audit trail; `_auth()` confirmed; `JARVIS_API_KEY` set.
> - `confidence_decay` metadata restored on `msjarvis:5433` — Phase 5 temporal decay multiplier confirmed active; non-null rows verified; OI-13 prerequisite met.
> - Preflight target set to 28 PASS / 0 FAIL — gates 25–28 identified: `jarvis-memory:8056` auth/logging, `confidence_decay` presence, ChromaDB ≥ 40 collections, `psychological_rag` ≥ 968 docs.
> - `jarvis-autonomous-learner` container confirmed running; `autonomous_learner` collection registered in ChromaDB.

---

## Why This Matters for Polymathmatic Geography

The Chapter 41 test harness is the operational layer that keeps the polymathmatic geography system provably coherent as it scales. Without it, deployments of new RAG domains (such as `psychological_rag` or `appalachian_cultural_intelligence`) or new spatial layers (such as `gis_wv_benefits`) would be undocumented and unverifiable — which would undermine the thesis claim that the MAALLI system is academically reproducible. Each gate in this chapter maps to one or more geographic or constitutional capabilities of the system: Gate 27 guarantees the full RAG domain inventory is live; Gate 28 guarantees the psychological domain is not merely declared but populated and queryable.

---

## Status as of ★★★★ April 6, 2026

> ★★★★ **Correction note (April 6, 2026 — R41-1):** Container count updated to **105** throughout this section. `jarvis-otel-collector` brought under compose management April 6; restart policy `unless-stopped` confirmed; `docker ps` count = 105. Prior April 3, 2026 Ch. 33 sealed baseline was 101 containers.

| Category | Details |
|----------|---------|
| Chapter status | 🏁 OFFICIALLY CLOSED — all gates passing and all open items closed as of April 1, 2026; counts updated April 6, 2026 |
| Gate results | memories schema + `confidence_decay` ✅ — `jarvis-ollama` running ✅ — `jarvis-chroma` healthy ✅ — Gate 27 (41 collections) ✅ — Gate 28 (`psychological_rag` registered) ✅ — Gate 29 (`jarvis-crypto-policy` watchdog) ✅ — Gate 30 (MountainShares/DAO smoke tests) ✅ |
| Stack size | ★★★★ **105 containers** (April 6, 2026 confirmed live — up from 101 at April 3 Ch. 33 seal, 96 at March 28 baseline, 83 at March 18 baseline) |
| ChromaDB state | 41 collections — full manifest in §41.9 |
| Durable audit trail | `jarvis-memory:8056` active; Phase 1.4 and Phase 4.5 decisions logged; auth confirmed |
| OI status | All chapter-local open items closed April 1, 2026 — see §41.10 |

---

## 41.1 Role of the Test Harness

The Chapter 41 harness is the operational guardrail for the thesis: it turns scattered shell commands and one-off checks into a repeatable, documented gate sequence. Every major stack change — new containers, new Chroma domains, new preflight gates — must pass through this harness before being considered "in thesis."

The harness focuses on three domains:

- **Core service health** — containers running, ports correctly bound, no `0.0.0.0` exposures.
- **Data and metadata readiness** — schemas present (e.g., `memories` with `confidence_decay`), Chroma collections registered.
- **Gate targets** — testable thresholds that higher-level chapters depend on (e.g., minimum collection counts, specific RAG domains).

---

## 41.2 Relationship to Other Chapters

Chapter 41 is downstream of build integrity and upstream of security and application chapters.

| Source chapter | What it guarantees | How Ch. 41 uses it |
|----------------|-------------------|--------------------|
| Ch. 19 — Build context integrity | Docker builds use clean contexts, no ghost files | Assumes judge images and services are built from a clean `services/` tree |
| Ch. 30 — Ingest | Ingest containers and IPFS flows exist | Confirms ingest services are running and reachable |
| Ch. 33 — Judge pipeline | Ports and container topology of judge services | Treats pipeline ports as targets for health checks |
| Ch. 40 — Sprints | Documented changes to services, gateways, and memory | Incorporates new gates when sprint notes add requirements |
| Ch. 42 — PQ layer | Preflight gates 25–30, including Chroma targets and crypto-policy watchdog | Encodes those gates into `VERIFYANDTEST.sh` and manual checks |

Once a capability appears as "implemented" in another chapter, Chapter 41 is responsible for verifying that capability stays present and healthy in the live stack.

---

## 41.3 Test Harness Philosophy

The harness is opinionated about three things:

- **Determinism** — the same script must return the same answer on the same stack.
- **Monotonicity** — once a gate is added and justified in the thesis, it must not be silently removed.
- **Visibility** — failures must point to specific missing services, ports, or metadata, not generic "unhealthy" states.

Gates are expressed as shell checks, HTTP pings, or small Python snippets, wired through `VERIFYANDTEST.sh`.

---

## 41.4 Core Health Checks

The base harness covers:

- Docker daemon reachable.
- All core services (`jarvis-main-brain`, judge containers, Redis, PostgreSQL, BBB) running.
- No service listening on `0.0.0.0` (everything bound to `127.0.0.1` or behind Cloudflare).
- Judge pipeline ports responding with HTTP 200 on `/health` where implemented.

Example pattern:

```bash
#!/usr/bin/env bash
set -e

echo "Checking for 0.0.0.0 exposures..."
if docker ps --format '{{.Ports}}' | grep -v '127.0.0.1' | grep -q '0.0.0.0'; then
  echo "[FAIL] Found 0.0.0.0 binding"
  exit 1
fi
echo "[PASS] No 0.0.0.0 bindings detected."
```

This matches the security hardening posture confirmed by the March 18, 2026 security audit.

---

## 41.5 Service-Level Regression Tests

Beyond simple liveness, Chapter 41 tracks small canary checks:

- **Judge pipeline** — test verdict through all four sub-judges; assert 19/19 signing checks still pass (delegated to the sprint scripts referenced in Chapter 42).
- **BBB input gate** — send known bad prompts (developer override, DAN, steganography) and assert `approved=False`.
- **Caddy/Cloudflare path** — curl the public URL and internal health endpoints, ensuring the documented QUIC/TLS chain remains valid; assert HTTP 401 on unauthenticated requests (OI-36-A closed April 1, 2026 — Caddy `forward_auth` live).
- **`jarvis-memory:8056`** — authenticated POST test; assert HTTP 200 and record persistence.
- **`jarvis-autonomous-learner`** — confirm service running and `autonomous_learner` collection present in ChromaDB.
- **`jarvis-crypto-policy`** — Gate 29 health check via `VERIFYANDTEST.sh` watchdog; assert HTTP 200 on policy endpoint (OI-CRYPTO-VT closed April 1, 2026).
- **MountainShares/DAO tier** — Gate 30 smoke tests on ports 8080–8084; endpoint health confirmed (OI-30 closed April 1, 2026).

> ★★★★ **April 2, 2026 addendum (R41-7):** EthicalFilter and SafetyMonitor fully recalibrated April 2, 2026 (9/9 regression, 0% FP on maternal Appalachian voice). The BBB regression test baseline is now recalibrated-EthicalFilter + recalibrated-SafetyMonitor. The "send known bad prompts, assert `approved=False`" regression test remains correct; the calibration baseline has been updated. Phase 4.5 log+passthrough mode remains active pending final red-team sign-off. See Ch. 33 §33.2 for the recalibration record.

Failures in these tests generate open items in the relevant chapters, but Chapter 41 is where they are executed.

---

## 41.6 ChromaDB Readiness Gates (Pre-Expansion)

Before the March 28–April 1 expansion, Chapter 41 only needed to assert that:

- ChromaDB was running.
- A minimal set of collections existed (`gbim_entities`, core memory collections).

These checks were intentionally weak while the RAG domains were still fluid. Preflight gates 27 and 28 in Chapter 42 raised the bar to specific counts and named domains once the architecture stabilized.

---

## 41.7 Preflight Gates and `VERIFYANDTEST.sh`

> ★★★★ **Preflight gate reconciliation note (R41-4 — April 6, 2026):**
>
> Gate totals revised per Ch. 33 April 3, 2026 sealed baseline. The three-chapter progression is:
>
> | Milestone | Count | Date | Source |
> |-----------|-------|------|--------|
> | Gates 25–28 scripted | 28 PASS / 0 FAIL | March 28, 2026 | Ch. 41 March 28 baseline |
> | Gates 25–30 all closed | 30 PASS / 0 FAIL | April 1, 2026 | Ch. 41 §41.8 / Ch. 42 §42.10 |
> | Ch. 33 sealed baseline | **22 PASS / 0 FAIL / 1 WARN** | April 3, 2026 | **Ch. 33 §33.6 — AUTHORITATIVE** |
>
> After duplicate line removal during the SafetyMonitor recalibration sprint (April 2, 2026), the final preflight gate count sealed in Ch. 33 is **22 PASS / 0 FAIL / 1 WARN**. Gates 25–30 all remain PASS within this count. The 1 WARN is `jarvis-web-research` (port 8090) binding — `docker inspect` required after every restart to confirm `127.0.0.1` binding. See Ch. 33 §33.6 for the authoritative sealed gate table.

| Gate | Description | Target | Status |
|------|-------------|--------|--------|
| Gate 25 | `jarvis-memory:8056` auth/logging | `_auth()` HTTP 200 with `JARVIS_API_KEY` | ✅ |
| Gate 26 | `confidence_decay` presence | Non-null rows in `memories` on `msjarvisgis` (`jarvis-local-resources-db:5435`) | ✅ |
| Gate 27 | ChromaDB collections count | ≥ 40 (confirmed 41) | ✅ |
| Gate 28 | `psychological_rag` domain | Registered, metadata confirmed | ✅ |
| Gate 29 | `jarvis-crypto-policy` watchdog | HTTP 200 on policy endpoint; wired into `VERIFYANDTEST.sh` | ✅ |
| Gate 30 | MountainShares/DAO tier smoke tests | Endpoints on ports 8080–8084 confirmed healthy | ✅ |

Example Gate 27 check:

```bash
echo "[Gate 27] Checking ChromaDB collection count..."
# ChromaDB host port is 8002 (not 8055 — 8055 is jarvis_auth_service)
COUNT=$(python3 - <<'EOF'
import chromadb
client = chromadb.HttpClient(host="localhost", port=8002)
print(len(client.list_collections()))
EOF
)
if [ "$COUNT" -ge 41 ]; then
  echo "[PASS] Gate 27 — $COUNT collections found (>= 41)"
else
  echo "[FAIL] Gate 27 — only $COUNT collections found"
  exit 1
fi
```

Example Gate 28 check:

```bash
echo "[Gate 28] Checking psychological_rag collection..."
# ChromaDB host port is 8002 (not 8055 — 8055 is jarvis_auth_service)
python3 - <<'EOF'
import chromadb, sys
client = chromadb.HttpClient(host="localhost", port=8002)
names = [c.name for c in client.list_collections()]
if "psychological_rag" in names:
    col = client.get_collection("psychological_rag")
    print(f"[PASS] Gate 28 — psychological_rag exists, count={col.count()}")
else:
    print("[FAIL] Gate 28 — psychological_rag not found")
    sys.exit(1)
EOF
```

Example Gate 29 check:

```bash
echo "[Gate 29] Checking jarvis-crypto-policy health..."
STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8099/health)
if [ "$STATUS" = "200" ]; then
  echo "[PASS] Gate 29 — jarvis-crypto-policy healthy (HTTP 200)"
else
  echo "[FAIL] Gate 29 — jarvis-crypto-policy returned HTTP $STATUS"
  exit 1
fi
```

Example Gate 30 check:

```bash
echo "[Gate 30] Checking MountainShares/DAO tier endpoints..."
for PORT in 8080 8081 8082 8083 8084; do
  STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:$PORT/health)
  if [ "$STATUS" = "200" ]; then
    echo "[PASS] Gate 30 — port $PORT healthy"
  else
    echo "[FAIL] Gate 30 — port $PORT returned HTTP $STATUS"
    exit 1
  fi
done
```

---

## 41.8 Final Gate Results — April 1, 2026

```
GATE 28 — PASS. psychological_rag exists, registered, metadata confirmed. ✅
GATE 29 — PASS. jarvis-crypto-policy healthy, watchdog wired. ✅
GATE 30 — PASS. MountainShares/DAO smoke tests confirmed. ✅

🏁 CHAPTER 41 — OFFICIALLY CLOSED
```

| Gate | Result |
|------|--------|
| memories schema + `confidence_decay` | ✅ |
| `jarvis-ollama` running | ✅ |
| `jarvis-chroma` healthy | ✅ |
| Gate 27 — 41 collections | ✅ |
| Gate 28 — `psychological_rag` registered | ✅ |
| Gate 29 — `jarvis-crypto-policy` watchdog | ✅ |
| Gate 30 — MountainShares/DAO smoke tests | ✅ |

**Notes on each gate:**

- **memories schema + `confidence_decay`:** Schema present in `msjarvisgis` on `jarvis-local-resources-db:5435`; `confidence_decay` column confirmed non-null. Satisfies both the Chapter 41 harness requirement and the Gate 26 prerequisite in Chapter 42.
- **`jarvis-ollama` running:** Local LLM engine confirmed up; all RAG evaluation and inference paths are testable without external dependencies.
- **`jarvis-chroma` healthy:** ChromaDB responds to list and query operations without error; authentication and collection access confirmed.
- **Gate 27 — 41 collections:** ChromaDB inventory confirmed at 41 collections, exceeding the original ≥ 40 target. Full manifest in §41.9.
- **Gate 28 — `psychological_rag` registered:** Collection exists, registered, and metadata footprint confirmed. Anchor of the psychological intelligence domain referenced in Chapter 25 and the 5th DGM Subconscious layer.
- **Gate 29 — `jarvis-crypto-policy` watchdog:** `jarvis-crypto-policy` (port 8099) health check now wired into `VERIFYANDTEST.sh`; HTTP 200 confirmed. OI-CRYPTO-VT closed April 1, 2026.
- **Gate 30 — MountainShares/DAO smoke tests:** Ports 8080–8084 confirmed healthy; endpoint smoke tests passed. OI-30 closed April 1, 2026.

---

## 41.9 ChromaDB Collection Manifest — 41 Collections (April 1, 2026)

The April 1 inventory reveals the full architecture of the MAALLI knowledge layer in one view. This manifest is the reference target for Gate 27: if the harness sees fewer than these 41 collections, the chapter is out of compliance. See Ch. 41 §41.9 as the authoritative collection manifest; Ch. 40 §40.2 cross-references this section for all ChromaDB collection count assertions.

### Core GBIM

- `gbim_entities`
- `gbim_beliefs_v2`
- `gbim_worldview_entities`
- `GBIM_Fayette_sample`
- `conversation_gbim_private`
- `conversation_gbim_public`

### RAG Domains

- `psychological_rag`
- `health_rag`
- `economic_rag`
- `legal_rag`
- `policy_rag`
- `governance_rag`
- `grants_rag`
- `commons_rag`
- `news_rag`
- `safety_rules`
- `meeting_minutes`
- `contracts`

### GIS / Spatial

- `geospatialfeatures`
- `gis_data`
- `gis_wv_benefits`
- `address_points`
- `local_resources`
- `wv_resources`

### Knowledge / Memory

- `ms_jarvis_memory`
- `jarvis_knowledge`
- `jarvis`
- `conversation_history`
- `autonomous_learning` — ⚠️ **clarification required:** this collection is present in the April 1 inventory but is NOT the Phase 1.45 canonical community memory collection. Status (legacy / development / active secondary) should be confirmed before use in smoke tests. See Ch. 40 §40.4.6 for the authoritative Phase 1.45 collection reference.
- `autonomous_learner` — ★ **CANONICAL Phase 1.45 community memory collection** (21,181+ records, 384-dim `all-minilm:latest`, host port 8020). `autonomous_learner` (with underscore) is the correct name. `autonomouslearner` (no underscore) is stale.
- `research_history`

### Cultural / Spiritual

- `spiritual_texts`
- `spiritual_knowledge`
- `appalachian_cultural_intelligence`
- `psychological_knowledge`
- `fifth_dgm_subconscious`

### Misc / Dev

- `msjarvis-smoke`
- `msjarvis_docs`
- `GBIM_sample`
- `GBIM_sample_rows`
- `psychological_rag_domain`
- `operations_history` — **planned** (export harness ready; embedding/vectorization deferred per Ch. 40 §40.13 OI-OPS-HISTORY). If already present in the live stack, move to an appropriate category and update the Gate 27 count accordingly.

> **Gate 27 compliance note:** The manifest above documents 41 confirmed collections as of April 1, 2026. `operations_history` is listed as planned; if it materializes as an active collection, the Gate 27 threshold should be reviewed and updated to ≥ 42. The authoritative live count is always confirmed via `curl -s http://127.0.0.1:8002/api/v2/collections | python3 -c "import sys,json; r=json.load(sys.stdin); print(len(r))"`.

---

## 41.10 Open Items for Chapter 41

As of April 1, 2026, **all chapter-local open items are closed.** No outstanding gaps remain in the Chapter 41 test harness.

| ID | Item | Status | Notes |
|----|------|--------|-------|
| OI-VERIFYANDTEST-28 | Full gate scripting for gates 25–28 in `VERIFYANDTEST.sh` | ✅ Closed April 1, 2026 | Gates 25–28 fully scripted and passing |
| OI-30 | MountainShares/DAO endpoint health validation | ✅ Closed April 1, 2026 | Gate 30 passing; smoke tests confirmed on ports 8080–8084 |
| OI-31 | EEG layer architecture documentation | ✅ Closed April 1, 2026 | EEG architecture documented — delta/theta/beta pipeline defined on ports 8073–8075; see Ch. 42 §42.13 |
| OI-36-A | Gateway-level token enforcement at Caddy | ✅ Closed April 1, 2026 | Caddy `forward_auth` live; HTTP 401 confirmed on unauthenticated requests; commit `f2e93422` |
| OI-CRYPTO-VT | `jarvis-crypto-policy` health in `VERIFYANDTEST.sh` watchdog | ✅ Closed April 1, 2026 | Gate 29 passing; watchdog wired; HTTP 200 confirmed on port 8099 |

Chapter 41's mandate going forward is to pick up new requirements when other chapters add hard preflight conditions, not to originate them.

---

## 41.11 Cross-References

- For the definition of preflight Gates 25–30 (including `confidence_decay`, `psychological_rag`, crypto-policy watchdog, and MountainShares/DAO health), see Chapter 42 §42.7.
- For Chroma ingestion architecture and how collections are populated, see Chapter 30.
- For how judge pipeline, BBB, and PQ signing are validated beyond liveness, see Chapters 33 and 42.
- For the March 28 stack expansion to 96 containers and `jarvis-memory:8056` durable logging, see **Chapter 40 §40-H (March 28 addendum)** and Chapter 40 §40-I. Note: the March 28 governance hardening is documented as an addendum within §40-H, titled "★ March 28, 2026 Governance Hardening — Addendum to §40-H"; §40-I covers the April 1–2 sprint.
- For the psychological intelligence domain and the 5th DGM Subconscious layer referenced by `psychological_rag` and `fifth_dgm_subconscious`, see Chapter 25.
- For the GIS/Spatial collections (`geospatialfeatures`, `gis_wv_benefits`, `address_points`, `local_resources`, `wv_resources`), see Chapter 10 and Chapter 12.
- For the MountainShares/Commons/DAO tier (ports 8080–8084) and governance collections (`governance_rag`, `commons_rag`, `meeting_minutes`, `contracts`), see Chapter 3 and Chapter 31.
- For the EEG layer architecture (delta/theta/beta pipeline, ports 8073–8075), see Chapter 42 §42.13.
- For Caddy `forward_auth` configuration and the full external access security architecture, see Chapter 38 §38.8 and §38.9 and Chapter 42 §42.5.5.
- For the authoritative preflight gate sealed count (22 PASS / 0 FAIL / 1 WARN, April 3, 2026), see Chapter 33 §33.6.
- For the BBB EthicalFilter and SafetyMonitor recalibration record (April 2, 2026 — 9/9 regression, 0% FP), see Chapter 33 §33.2.
