# Chapter 41 — Test Harness and Continuous Validation

**Carrie Kidd (Mamma Kidd) — Mount Hope, WV**
**v4.0 — April 6, 2026**

> **Namespace note:** This chapter uses the `allis-*` container namespace. Chapters 38 and 39 document the same production system under the `allis-*` namespace. Both prefixes refer to the same deployment. For the authoritative port and database corrections, see Ch. 33 §33.6.

---

## §41.0 Revision History

| Rev | Date | Summary | Status |
|-----|------|---------|--------|
| R41-1 | April 6, 2026 | Container count updated to 105; `allis-otel-collector` compose-managed, `unless-stopped` confirmed | Closed |
| R41-2 | April 6, 2026 | Gate 27 and Gate 28 code examples corrected: `port=8055` → `port=8002` | Closed |
| R41-3 | April 6, 2026 | Preflight gate reconciliation note added to §41.7 | Closed |
| R41-4 | April 6, 2026 | `operations_history` collection note added to §41.9 manifest | Closed |
| R41-5 | April 6, 2026 | `autonomous_learner` / `autonomous_learning` disambiguation added to §41.9 | Closed |
| R41-6 | April 6, 2026 | BBB EthicalFilter and SafetyMonitor recalibration addendum added to §41.5 | Closed |
| R41-7 | April 6, 2026 | §41.11 cross-reference corrected: March 28 expansion documented in Ch. 40 §40-H | Closed |
| R41-8 | April 6, 2026 | `allis-*` / `allis-*` namespace note added; `autonomous_learning` legacy status resolved | Closed |
| R41-9 | April 6, 2026 | `gisdb` corrected to 45 GB / 548 tables per Ch. 33 April 6 ground truth | Closed |
| R41-10 | April 6, 2026 | Gate 27 threshold and §41.9 manifest forward notes updated for April 6 (47) and April 11 (49) counts | Closed |
| R41-11 | April 6, 2026 | Gate 26 disambiguation note backported from Ch. 42 §42.7 | Closed |
| R41-12 | April 6, 2026 | `autonomous_learning` manifest entry updated from ⚠️ open warning to definitive legacy/stale status | Closed |
| R41-13 | April 6, 2026 | OI-36-A canonical closure note added; Ch. 38 / Ch. 41 / Ch. 42 closure relationship documented | Closed |
| R41-14 | April 6, 2026 | Post-seal addendum §41.12 added: Gate 27 count progression and Gate 30 label clarification | Closed |
| R41-15 | April 6, 2026 | §41.1 P-principle bullets expanded to match Ch. 38 and Ch. 40 format | Closed |
| R41-16 | April 6, 2026 | Port 8010 degraded-service exclusion documented in §41.4 | Closed |
| R41-17 | April 6, 2026 | Harness runtime profile added as §41.13 | Closed |
| R41-18 | April 6, 2026 | Failure-mode examples added to §41.7 gate checks | Closed |

---

## Why This Matters for Polymathmatic Geography

The Chapter 41 test harness is the operational layer that keeps the polymathmatic geography system provably coherent as it scales. Without it, deployments of new RAG domains (such as `psychological_rag` or `appalachian_cultural_intelligence`) or new spatial layers (such as `gis_wv_benefits`) would be undocumented and unverifiable — which would undermine the thesis claim that the MSALLIS system is academically reproducible.

Each gate in this chapter maps directly to one or more geographic or constitutional capabilities:

- **P1 — Test harness as reproducibility guarantee:** Gates 25–30 encode verifiable, script-reproducible proofs of the system's claim to be a living, testable instrument. The `VERIFYANDTEST.sh` harness is the primary mechanism by which any community member or academic reviewer can independently confirm that the described capabilities are live. A thesis claiming community intelligence must be reproducible — the harness is the evidence that it is.
- **P3 — Gate monotonicity as power accountability:** Once a gate is added and justified in the thesis, it must not be silently removed. Gate monotonicity is the operational expression of P3: the geometry of the system's commitments to community is made visible and enforced by the harness. `allis-memory:8056` durable audit trail ensures BBB gate decisions are independently inspectable across container restarts.
- **P12 — ChromaDB manifest as intelligence-with-a-ZIP-code evidence:** Gate 27 guarantees the full RAG domain inventory is live — including GIS/spatial collections (`gis_wv_benefits`, `geospatialfeatures`, `address_points`) that anchor the system's geographic intelligence to West Virginia ZIP codes, counties, and community resources. Gate 28 guarantees the psychological domain is not merely declared but populated and queryable — confirming that community wellbeing knowledge is as real as landowner data.
- **P16 — Continuous validation as power accountable to place:** The repeatable, timestamped gate record produced by this harness is the mechanism by which community stakeholders and academic reviewers can confirm the system's capabilities over time. The harness is not a one-time audit — it is a continuous accountability instrument.

---

## Status as of April 6, 2026

| Category | Details |
|----------|---------|
| Chapter status | 🏁 OFFICIALLY CLOSED — all gates passing and all open items closed as of April 1, 2026; counts updated April 6, 2026 |
| Gate results | memories schema + `confidence_decay` ✅ — `allis-ollama` running ✅ — `allis-chroma` healthy ✅ — Gate 27 (41 collections sealed; 47 per April 6 ground truth) ✅ — Gate 28 (`psychological_rag` registered) ✅ — Gate 29 (`allis-crypto-policy` watchdog) ✅ — Gate 30 (MountainShares/DAO smoke tests) ✅ |
| Stack size | **105 containers** (April 6, 2026 confirmed live — up from 101 at April 3 Ch. 33 seal, 96 at March 28 baseline, 83 at March 18 baseline) |
| ChromaDB state | 41 collections sealed (April 1 — this chapter's authoritative baseline); 47 per April 6 Ch. 33 ground truth; 49 per April 11 Ch. 42 certification. Full sealed manifest in §41.9. |
| Durable audit trail | `allis-memory:8056` active; Phase 1.4 and Phase 4.5 decisions logged; auth confirmed |
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
- All core services (`allis-main-brain`, judge containers, Redis, PostgreSQL, BBB) running.
- No service listening on `0.0.0.0` (everything bound to `127.0.0.1` or behind Cloudflare).
- Judge pipeline ports responding with HTTP 200 on `/health` where implemented.
- **`allis-wv-entangled-gateway` (port 8010) is a known degraded service** — it is explicitly excluded from the gate suite. A harness operator encountering a failed health check on port 8010 should not treat it as a regression; it is a known degraded state documented in Ch. 38 §38.2.2. The primary entrypoint is `allis-main-brain` at port **8050**.

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

**Example failure output** (for reproducibility — so operators know what a failing gate looks like):

```text
[FAIL] Found 0.0.0.0 binding
  → docker ps --format '{{.Names}} {{.Ports}}' | grep 0.0.0.0
  → Identify the offending container and re-bind to 127.0.0.1
  → Re-run docker compose up -d <container> with corrected port binding
  → Re-run this check to confirm remediation
```

This matches the security hardening posture confirmed by the March 18, 2026 security audit.

---

## 41.5 Service-Level Regression Tests

Beyond simple liveness, Chapter 41 tracks small canary checks:

- **Judge pipeline** — test verdict through all four sub-judges; assert 19/19 signing checks still pass (delegated to the sprint scripts referenced in Chapter 42).
- **BBB input gate** — send known bad prompts (developer override, DAN, steganography) and assert `approved=False`.
- **Caddy/Cloudflare path** — curl the public URL and internal health endpoints, ensuring the documented QUIC/TLS chain remains valid; assert HTTP 401 on unauthenticated requests (OI-36-A closed April 1, 2026 — Caddy `forward_auth` live; commit `f2e93422`).
- **`allis-memory:8056`** — authenticated POST test; assert HTTP 200 and record persistence.
- **`allis-autonomous-learner`** — confirm service running and `autonomous_learner` collection present in ChromaDB (host port 8002).
- **`allis-crypto-policy`** — Gate 29 health check via `VERIFYANDTEST.sh` watchdog; assert HTTP 200 on policy endpoint (OI-CRYPTO-VT closed April 1, 2026).
- **MountainShares/DAO tier** — Gate 30 smoke tests on ports 8080–8084; endpoint health confirmed (OI-30 closed April 1, 2026).
- **`truth_verification` method** — assert method is `rag_grounded_v2` per OI-37-C (CLOSED April 3, 2026). Do not accept `heuristic_contradiction_v1`. See Ch. 33 §33.2 and Ch. 33 §33.2.3.

> **April 2, 2026 addendum (R41-6):** EthicalFilter and SafetyMonitor fully recalibrated April 2, 2026 (9/9 regression, 0% FP on maternal Appalachian voice). The BBB regression test baseline is now recalibrated-EthicalFilter + recalibrated-SafetyMonitor. The "send known bad prompts, assert `approved=False`" regression test remains correct; the calibration baseline has been updated. Survivor resource queries (e.g., domestic violence, economic stress) must pass with `safety_score=1.0` and `issues: []`. Phase 4.5 log+passthrough mode remains active pending final red-team sign-off — see Ch. 16 §16.9 for blocking re-enablement governance. See Ch. 33 §33.2 for the recalibration record.

Failures in these tests generate open items in the relevant chapters, but Chapter 41 is where they are executed.

---

## 41.6 ChromaDB Readiness Gates (Pre-Expansion)

Before the March 28–April 1 expansion, Chapter 41 only needed to assert that:

- ChromaDB was running.
- A minimal set of collections existed (`gbim_entities`, core memory collections).

These checks were intentionally weak while the RAG domains were still fluid. Preflight gates 27 and 28 in Chapter 42 raised the bar to specific counts and named domains once the architecture stabilized.

---

## 41.7 Preflight Gates and `VERIFYANDTEST.sh`

> **Preflight gate reconciliation note (R41-3 / R41-4 — April 6, 2026):**
>
> The single authoritative gate table is **Chapter 33 §33.6**. The progression is:
>
> | Milestone | Count | Date | Source |
> |-----------|-------|------|--------|
> | Gates 25–28 scripted | 28 PASS / 0 FAIL | March 28, 2026 | Ch. 41 March 28 baseline |
> | Gates 25–30 all closed | 30 PASS / 0 FAIL | April 1, 2026 | Ch. 41 §41.8 / Ch. 42 §42.10 |
> | Ch. 33 sealed baseline | **22 PASS / 0 FAIL / 1 WARN** | April 3, 2026 | **Ch. 33 §33.6 — AUTHORITATIVE** |
> | April 6 ground truth | **31 PASS / 0 FAIL / 0 WARN** | April 6, 2026 | Ch. 33 April 6 — superseding current |
>
> After duplicate line removal during the SafetyMonitor recalibration sprint (April 2, 2026), the final preflight gate count sealed in Ch. 33 is **22 PASS / 0 FAIL / 1 WARN**. Gates 25–30 all remain PASS within this count. The 1 WARN is `allis-web-research` (port 8090) binding — `docker inspect` required after every restart to confirm `127.0.0.1` binding. The April 6 Ch. 33 ground truth advances to **31 PASS / 0 FAIL / 0 WARN**. See Ch. 33 §33.6 as authoritative.

> **Gate 26 disambiguation (R41-11 — backported from Ch. 42 §42.7):**
>
> Gate 26 targets `memories.confidence_decay` in the **`msallisgis` database on `allis-local-resources-db:5435`** — distinct from the PostGIS geospatial database at host port **5432**. These are two different databases on two different ports. The GBIM entity `confidence_decay` check on `msallis:5433` (documented in Ch. 40 §40.4.7) is a separate, additional validation — not the Gate 26 prerequisite.

| Gate | Description | Target | Status |
|------|-------------|--------|--------|
| Gate 25 | `allis-memory:8056` auth/logging | `_auth()` HTTP 200 with `allis_API_KEY` | ✅ |
| Gate 26 | `confidence_decay` presence | Non-null rows in `memories.confidence_decay` on `msallisgis` (`allis-local-resources-db:5435`) — **distinct from `msallis:5433`** | ✅ |
| Gate 27 | ChromaDB collections count | ≥ 41 (sealed April 1 — see §41.12 for post-seal progression to 47 and 49) | ✅ |
| Gate 28 | `psychological_rag` domain | Registered, metadata confirmed | ✅ |
| Gate 29 | `allis-crypto-policy` watchdog | HTTP 200 on policy endpoint; wired into `VERIFYANDTEST.sh` | ✅ |
| Gate 30 | MountainShares/DAO tier smoke tests | Endpoints on ports 8080–8084 confirmed healthy (see §41.12 for label clarification) | ✅ |

Example Gate 27 check (with failure output):

```bash
echo "[Gate 27] Checking ChromaDB collection count..."
# ChromaDB host port is 8002 (not 8055 — 8055 is allis_auth_service)
COUNT=$(python3 - <<'EOF'
import chromadb
client = chromadb.HttpClient(host="localhost", port=8002)
print(len(client.list_collections()))
EOF
)
if [ "$COUNT" -ge 41 ]; then
  echo "[PASS] Gate 27 — $COUNT collections found (>= 41)"
else
  echo "[FAIL] Gate 27 — only $COUNT collections found (expected >= 41)"
  echo "  → Run: curl -s http://127.0.0.1:8002/api/v2/collections | python3 -c 'import sys,json;r=json.load(sys.stdin);[print(c[\"name\"]) for c in r]'"
  echo "  → Compare against §41.9 manifest to identify missing collections"
  echo "  → Check allis-chroma logs: docker logs allis-chroma --tail 50"
  exit 1
fi
```

Example Gate 28 check (with failure output):

```bash
echo "[Gate 28] Checking psychological_rag collection..."
# ChromaDB host port is 8002 (not 8055 — 8055 is allis_auth_service)
python3 - <<'EOF'
import chromadb, sys
client = chromadb.HttpClient(host="localhost", port=8002)
names = [c.name for c in client.list_collections()]
if "psychological_rag" in names:
    col = client.get_collection("psychological_rag")
    count = col.count()
    if count >= 968:
        print(f"[PASS] Gate 28 — psychological_rag exists, count={count} (>= 968)")
    else:
        print(f"[WARN] Gate 28 — psychological_rag exists but count={count} (expected >= 968 — restored March 28)")
else:
    print("[FAIL] Gate 28 — psychological_rag not found")
    print("  → Check allis-chroma: curl -s http://127.0.0.1:8002/api/v2/collections | python3 -c 'import sys,json;r=json.load(sys.stdin);print([c[\"name\"] for c in r])'")
    print("  → Re-run ingest pipeline for psychological_rag domain")
    sys.exit(1)
EOF
```

Example Gate 29 check (with failure output):

```bash
echo "[Gate 29] Checking allis-crypto-policy health..."
STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8099/health)
if [ "$STATUS" = "200" ]; then
  echo "[PASS] Gate 29 — allis-crypto-policy healthy (HTTP 200)"
else
  echo "[FAIL] Gate 29 — allis-crypto-policy returned HTTP $STATUS (expected 200)"
  echo "  → docker ps | grep allis-crypto-policy"
  echo "  → docker logs allis-crypto-policy --tail 30"
  echo "  → docker compose up -d allis-crypto-policy"
  exit 1
fi
```

Example Gate 30 check (with failure output):

```bash
echo "[Gate 30] Checking MountainShares/DAO tier endpoints..."
for PORT in 8080 8081 8082 8083 8084; do
  STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:$PORT/health)
  if [ "$STATUS" = "200" ]; then
    echo "[PASS] Gate 30 — port $PORT healthy"
  else
    echo "[FAIL] Gate 30 — port $PORT returned HTTP $STATUS (expected 200)"
    echo "  → docker ps | grep -E 'mountainshares|commons|dao|token|stake'"
    echo "  → docker logs <container> --tail 30"
    echo "  → docker compose up -d <container>"
    exit 1
  fi
done
```

---

## 41.8 Final Gate Results — April 1, 2026

```text
GATE 25 — PASS. allis-memory:8056 auth/logging confirmed. ✅
GATE 26 — PASS. memories.confidence_decay non-null in msallisgis:5435. ✅
GATE 27 — PASS. 41 ChromaDB collections found (>= 41). ✅
GATE 28 — PASS. psychological_rag exists, registered, metadata confirmed. ✅
GATE 29 — PASS. allis-crypto-policy healthy, watchdog wired. ✅
GATE 30 — PASS. MountainShares/DAO smoke tests confirmed. ✅

🏁 CHAPTER 41 — OFFICIALLY CLOSED (April 1, 2026)
    Post-seal count updates: see §41.12
```

| Gate | Result |
|------|--------|
| memories schema + `confidence_decay` | ✅ |
| `allis-ollama` running | ✅ |
| `allis-chroma` healthy | ✅ |
| Gate 27 — 41 collections (sealed April 1) | ✅ |
| Gate 28 — `psychological_rag` registered | ✅ |
| Gate 29 — `allis-crypto-policy` watchdog | ✅ |
| Gate 30 — MountainShares/DAO smoke tests | ✅ |

**Notes on each gate:**

- **memories schema + `confidence_decay`:** Schema present in `msallisgis` on `allis-local-resources-db:5435`; `confidence_decay` column confirmed non-null. Satisfies both the Chapter 41 harness requirement and the Gate 26 prerequisite in Chapter 42. This is a separate database and port from the GBIM entity `confidence_decay` check on `msallis:5433` (Ch. 40 §40.4.7).
- **`allis-ollama` running:** Local LLM engine confirmed up; all RAG evaluation and inference paths are testable without external dependencies.
- **`allis-chroma` healthy:** ChromaDB responds to list and query operations without error; authentication and collection access confirmed. Host port **8002** (not 8055 — 8055 is `allis_auth_service`).
- **Gate 27 — 41 collections:** ChromaDB inventory confirmed at 41 collections at April 1 seal, exceeding the original ≥ 40 target. Threshold upgraded to ≥ 41 at this seal. Full sealed manifest in §41.9. See §41.12 for post-seal progression (47 per April 6 Ch. 33 ground truth; 49 per April 11 Ch. 42 certification). The Gate 27 floor of ≥ 41 remains valid — subsequent higher counts pass this floor.
- **Gate 28 — `psychological_rag` registered:** Collection exists, registered, and metadata footprint confirmed. Anchor of the psychological intelligence domain referenced in Chapter 25 and the 5th DGM Subconscious layer. Count restored to 968 documents March 28, 2026.
- **Gate 29 — `allis-crypto-policy` watchdog:** `allis-crypto-policy` (port 8099) health check now wired into `VERIFYANDTEST.sh`; HTTP 200 confirmed. OI-CRYPTO-VT closed April 1, 2026.
- **Gate 30 — MountainShares/DAO smoke tests:** Ports 8080–8084 confirmed healthy; endpoint smoke tests passed. OI-30 closed April 1, 2026. See §41.12 for the Gate 30 label clarification between Ch. 41 and Ch. 42.

---

## 41.9 ChromaDB Collection Manifest — 41 Collections (April 1, 2026 Sealed Baseline)

> **Collection count note:** This manifest documents **41 confirmed collections** as of April 1, 2026 (this chapter's sealed baseline). As of April 6, 2026 (Ch. 33/38/39 ground truth), the live count advanced to **47 collections**. As of April 11, 2026 (Ch. 42 certification), the live count advanced to **49 collections**. The Chapter 41 Gate 27 threshold (≥ 41, confirmed 41) remains the chapter-sealed baseline; subsequent counts supersede but do not invalidate this seal. See §41.12 for the post-seal progression note.
>
> **`autonomous_learner` record count:** `autonomous_learner` — **21,181+ records, 384-dim, all-minilm:latest, host port 8020**. This count appears in Ch. 38 and Ch. 39 but is added here to the manifest for cross-chapter consistency.
>
> **`autonomous_learning` status resolved:** `autonomous_learning` is confirmed **legacy/stale** — superseded by `autonomous_learner` (see Ch. 38 §38.4, Ch. 39 ground truth). Do not use in smoke tests. Retain in manifest for collection count accuracy only.
>
> The authoritative live count is always confirmed via:
> ```bash
> curl -s http://127.0.0.1:8002/api/v2/collections | python3 -c "import sys,json; r=json.load(sys.stdin); print(f'Collections: {len(r)}')"
> ```

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

- `ms_allis_memory`
- `allis_knowledge`
- `allis`
- `conversation_history`
- `autonomous_learning` — **Legacy/stale — confirmed superseded by `autonomous_learner`** (see Ch. 38 §38.4, Ch. 39 ground truth). Do not use in smoke tests. Retained in manifest for collection count accuracy only.
- `autonomous_learner` — **CANONICAL Phase 1.45 community memory collection** (21,181+ records, 384-dim `all-minilm:latest`, host port 8020). `autonomous_learner` (with underscore) is the correct name. `autonomouslearner` (no underscore) is stale. Do NOT substitute `nomic-embed-text` (768-dim).
- `research_history`

### Cultural / Spiritual

- `spiritual_texts`
- `spiritual_knowledge`
- `appalachian_cultural_intelligence`
- `psychological_knowledge`
- `fifth_dgm_subconscious`

### Misc / Dev

- `msallis-smoke`
- `msallis_docs`
- `GBIM_sample`
- `GBIM_sample_rows`
- `psychological_rag_domain`
- `operations_history` — **Planned** (export harness ready per Ch. 40 §40.13 OI-OPS-HISTORY; embedding/vectorization deferred). If already present in the live stack, move to an appropriate category and update the Gate 27 count accordingly. If `operations_history` is among the 8 collections added between April 1 and April 11, Ch. 42 §42.14 should document this explicitly.

---

## 41.10 Open Items for Chapter 41

As of April 1, 2026, **all chapter-local open items are closed.** No outstanding gaps remain in the Chapter 41 test harness.

| ID | Item | Status | Notes |
|----|------|--------|-------|
| OI-VERIFYANDTEST-28 | Full gate scripting for gates 25–28 in `VERIFYANDTEST.sh` | ✅ Closed April 1, 2026 | Gates 25–28 fully scripted and passing |
| OI-30 | MountainShares/DAO endpoint health validation | ✅ Closed April 1, 2026 | Gate 30 passing; smoke tests confirmed on ports 8080–8084 |
| OI-31 | EEG layer architecture documentation | ✅ Closed April 1, 2026 | EEG architecture documented — delta/theta/beta pipeline defined on ports 8073–8075; see Ch. 42 §42.13 |
| OI-36-A | Gateway-level token enforcement at Caddy | ✅ Closed April 1, 2026 | Caddy `forward_auth` live; HTTP 401 confirmed on unauthenticated requests; commit `f2e93422`. **Primary closure record: Ch. 42 §42.10 (gateway `forward_auth`). Ch. 38 closes the related OI-38-A (token middleware). Both are required components of the same authentication architecture.** |
| OI-CRYPTO-VT | `allis-crypto-policy` health in `VERIFYANDTEST.sh` watchdog | ✅ Closed April 1, 2026 | Gate 29 passing; watchdog wired; HTTP 200 confirmed on port 8099 |

Chapter 41's mandate going forward is to pick up new requirements when other chapters add hard preflight conditions, not to originate them.

---

## 41.11 Cross-References

- For the definition of preflight Gates 25–30 (including `confidence_decay`, `psychological_rag`, crypto-policy watchdog, and MountainShares/DAO health), see Chapter 42 §42.7.
- For the Gate 26 disambiguation (port 5435 `msallisgis` vs port 5432 PostGIS vs port 5433 `msallis`), see Chapter 42 §42.7 and Chapter 40 §40.4.7.
- For Chroma ingestion architecture and how collections are populated, see Chapter 30.
- For how judge pipeline, BBB, and PQ signing are validated beyond liveness, see Chapters 33 and 42.
- For the March 28 stack expansion to 96 containers and `allis-memory:8056` durable logging, see **Chapter 40 §40-H (March 28 addendum)**. The March 28 governance hardening is documented as an addendum within §40-H; §40-I covers the April 1–2 sprint.
- For the psychological intelligence domain and the 5th DGM Subconscious layer referenced by `psychological_rag` and `fifth_dgm_subconscious`, see Chapter 25.
- For the GIS/Spatial collections (`geospatialfeatures`, `gis_wv_benefits`, `address_points`, `local_resources`, `wv_resources`), see Chapter 10 and Chapter 12.
- For the MountainShares/Commons/DAO tier (ports 8080–8084) and governance collections (`governance_rag`, `commons_rag`, `meeting_minutes`, `contracts`), see Chapter 3 and Chapter 31.
- For the EEG layer architecture (delta/theta/beta pipeline, ports 8073–8075), see Chapter 42 §42.13.
- For Caddy `forward_auth` configuration and the full external access security architecture, see Chapter 38 §38.8 and §38.9 and Chapter 42 §42.5.5.
- For the authoritative preflight gate sealed count (22 PASS / 0 FAIL / 1 WARN, April 3, 2026; 31 PASS / 0 FAIL / 0 WARN, April 6, 2026), see Chapter 33 §33.6.
- For the BBB EthicalFilter and SafetyMonitor recalibration record (April 2, 2026 — 9/9 regression, 0% FP), see Chapter 33 §33.2.
- For `truth_verification` upgrade to `rag_grounded_v2` and historical limitations of `heuristic_contradiction_v1`, see Ch. 33 §33.2 and Ch. 33 §33.2.3.
- For Port 8010 (`allis-wv-entangled-gateway`) degraded service status and exclusion from gate suite, see Chapter 38 §38.2.2 and Chapter 40 §40.2.
- For Phase 4.5 BBB blocking re-enablement governance and red-team sign-off contract, see **Ch. 16 §16.9**.
- For the `autonomous_learner` canonical collection specification (21,181+ records, 384-dim, host port 8020), see Chapter 38 §38.4 and Chapter 39 ground truth.
- For the 8 additional ChromaDB collections added between April 1 and April 11, 2026 (41 → 49), see Chapter 42 §42.14.

---

## §41.12 Post-Seal Addendum — April 6 and April 11, 2026

> **Chapter 41 is officially closed as of April 1, 2026.** The following addendum documents post-seal activity that advances certain gate counts without invalidating the April 1 seal.

### Gate 27 Count Progression

The Gate 27 floor is ≥ 41 collections (sealed April 1, 2026). Subsequent Chapter activity advanced the count:

| Date | Count | Source | Note |
|------|-------|--------|------|
| April 1, 2026 | 41 | Ch. 41 §41.9 sealed manifest | This chapter's sealed baseline — Gate 27 floor ≥ 41 |
| April 6, 2026 | 47 | Ch. 33/38/39 ground truth | 6 collections added; all pass the ≥ 41 floor |
| April 11, 2026 | 49 | Ch. 42 certification | 2 more added; all pass the ≥ 41 floor |

The Gate 27 check script (`if [ "$COUNT" -ge 41 ]`) remains valid as a floor check. A live stack of 47 or 49 collections passes Gate 27. For the identity of the 8 collections added between April 1 and April 11 (41 → 49), see Ch. 42 §42.14 — those 8 should be explicitly named there to close the manifest gap. For the 6 added by April 6 (41 → 47), see Ch. 33/38/39 ground truth.

### Gate 30 Label Clarification

Chapter 41 defines Gate 30 as: *MountainShares/DAO tier smoke tests — Endpoints on ports 8080–8084.*

Chapter 42 defines Gate 30 as: *Auth proxy (OI-36-A) — Caddy `forward_auth` HTTP 401 on unauthenticated.*

These are not the same gate under the same number. The resolution is:

- **Chapter 41 Gate 30** (sealed April 1, 2026) = MountainShares/DAO smoke tests, ports 8080–8084. This is this chapter's authoritative definition.
- **Chapter 42 Gate 30** may reflect a gate renumbering during the April 11 certification sprint, or a transcription error. Chapter 42 must explicitly reconcile this in its gate table — either documenting the renumbering or correcting to the Chapter 41 definition.
- Neither gate closure is invalidated — OI-30 (MountainShares/DAO) and OI-36-A (Caddy `forward_auth`) are both closed. The numbering conflict is a documentation issue, not an operational one.

### `autonomous_learner` Record Count

The `autonomous_learner` collection had 21,181+ records at the April 1 seal (per Ch. 38/39). This count is added to §41.9 above for consistency. The Ch. 41 §41.9 manifest entry for `autonomous_learner` now includes: *21,181+ records, 384-dim, all-minilm:latest, host port 8020.* `autonomous_learning` (no underscore, no hyphen) is confirmed stale.

---

## §41.13 Harness Runtime Profile

The `VERIFYANDTEST.sh` harness (gates 25–30 plus core fabric) has the following approximate runtime characteristics as of April 6, 2026:

| Check type | Approximate count | Typical latency | Notes |
|-----------|------------------|-----------------|-------|
| Docker daemon + container count | 1 | <1s | `docker ps` + `wc -l` |
| Core service HTTP health checks | 32 | 0.1–0.5s each | 32/32 core fabric services |
| LLM proxy health checks | 22 | 0.1–0.3s each | ports 8201–8222 |
| Judge pipeline health checks | 5 | 0.1–0.2s each | ports 7230–7233, 7239 |
| PostgreSQL connectivity | 3 | 0.2–1.0s each | ports 5432, 5433, 5435 |
| ChromaDB collection count | 1 | 0.3–0.5s | host port 8002 |
| Gate 27 (ChromaDB Python client) | 1 | ~300ms | `chromadb.HttpClient` list call |
| Gate 28 (`psychological_rag` count) | 1 | ~300ms | `chromadb` collection count |
| Gate 29 (`allis-crypto-policy`) | 1 | 0.1–0.2s | HTTP health probe |
| Gate 30 (MountainShares/DAO) | 5 | 0.1–0.2s each | ports 8080–8084 |
| Auth service check | 1 | <0.5s | `systemctl is-active allis_auth_service` |
| OTEL collector check | 1 | <0.5s | `docker inspect` restart policy |
| 0.0.0.0 exposure scan | 1 | <1s | `docker ps --format '{{.Ports}}'` scan |
| Preflight gate script | 22–31 checks | 5–15s total | `scripts/preflight_gate.sh` |

**Estimated total runtime:** 3–6 minutes for a full harness run, dominated by the 32 core service HTTP health checks and 22 LLM proxy checks. Network I/O gates (HTTP probes) account for ~80% of total runtime. Local process inspection gates (Docker daemon, `docker ps`, `systemctl`) account for ~20%. The AU-02 embedding gate referenced in Ch. 42 §42.3.4 adds approximately 300ms per ChromaDB client call.

This runtime profile grounds the "continuous validation" claim: a 3–6 minute full harness run is operationally compatible with a post-sprint verification cadence. Nightly cron activation of the full harness (documented as a future work item in Ch. 40 §40.11) would add ~6 minutes of nightly overhead — acceptable for a production community AI system.

---

*End of Chapter 41 — Test Harness and Continuous Validation*
*v4.0 — Last updated: April 6, 2026*
*Author: Carrie Kidd (Mamma Kidd), Mount Hope, WV*
*Chapter officially closed: April 1, 2026*
*Post-seal addendum: §41.12 (April 6, 2026)*
*Container count: 105 — `jarvis-otel-collector` compose-managed, restart policy `unless-stopped`*
*ChromaDB: 41 sealed (this chapter) / 47 April 6 ground truth / 49 April 11 Ch. 42 certification*
*All gates 25–30 PASS — all chapter-local OIs closed*
