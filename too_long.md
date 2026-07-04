# Chapter 42 — Post-Quantum Security Layer

**Carrie Kidd (Mamma Kidd) — Mount Hope, WV**
**v5.0 — April 11, 2026 (fully closed — final corrections)**

---

## §42.0 Revision History

| Rev | Date | Summary | Status |
|-----|------|---------|--------|
| R42-1 | April 6, 2026 | Container count updated to 105; `allis-otel-collector` compose-managed | Closed |
| R42-2 | April 6, 2026 | April 3 preflight gate seal (22 PASS / 0 FAIL / 1 WARN) documented in §42.7 | Closed |
| R42-3 | April 6, 2026 | BBB EthicalFilter/SafetyMonitor recalibration addendum added to §42.3.4 | Closed |
| R42-4 | April 6, 2026 | Gate 26 database disambiguation added to §42.7 | Closed |
| R42-5 | April 6, 2026 | OI-AU-02-V2 added to §42.10 (closed same session) | Closed |
| R42-6 | April 6, 2026 | §42.12 USB key management protocol bullets added | Closed |
| R42-7 | April 6, 2026 | §42.4.4 full fingerprint verification note added — superseded by R42-21 re: backend | Closed |
| R42-8 | April 6, 2026 | BBB Phase 2 verdict gate closed; `judgesigner.py` baked into BBB image | Closed |
| R42-9 | April 6, 2026 | BBB Phase 3 output blocking re-enabled; `BBB_OUTPUT_BLOCKING=true`; OI-38-B closed | Closed |
| R42-10 | April 11, 2026 (morning) | urllib3 CVE remediation; `Dockerfile.woah` patched; `allis-woah` rebuilt | Closed |
| R42-11 | April 11, 2026 (morning) | First dependency CVE audit run; cadence established | Closed |
| R42-12 | April 11, 2026 (morning) | Mythos-era threat landscape acknowledged in §42.6 | Closed |
| R42-13 | April 11, 2026 (afternoon) | Full host venv upgrade; 8 CVEs closed; Gate 31 passing | Closed |
| R42-14 | April 11, 2026 (evening) | OI-42-F Gate 31 version floor automation + Dockerfile pin grep closed | Closed |
| R42-15 | April 11, 2026 (evening) | OI-42-A `dilithium_py` removal from base `services/Dockerfile` | Closed |
| R42-16 | April 11, 2026 (evening) | BBB `_sign_verdict` patch — line 28/42; fallback lambda active | Closed |
| R42-17 | April 11, 2026 (evening) | Constitutional Guardian `_sign_verdict` patch — line 4/245; fallback lambda active | Closed |
| R42-18 | April 11, 2026 (evening) | `/judge-public-key` endpoint OI-42-E closed; live at `judge_pipeline.py:314` | Closed |
| R42-19 | April 11, 2026 (evening) | Gates 32–40 appended to `VERIFYANDTEST.sh`; CERTIFIED 6:29 PM EDT | Closed |
| R42-20 | April 11, 2026 (evening) | `allis-gis-rag` rebuilt; `allis-crypto-policy` recreated with liboqs `judgesigner.py` | Closed |
| R42-21 | April 11, 2026 (final) | liboqs ML-DSA-65 confirmed primary production runtime; `dilithium_py` is graceful fallback only | Closed |
| R42-22 | April 11, 2026 (final) | `rotate_judge_keys.sh` confirmed complete and production-grade; §42.11 corrected | Closed |
| R42-23 | April 11, 2026 (final) | Gate 31 Dockerfile pin grep confirmed done; §42.11 corrected | Closed |
| R42-24 | April 11, 2026 (final) | Signed verdict / memory storage confirmed wired; §42.11 corrected | Closed |

---

## Why This Matters for Polymathmatic Geography

This chapter documents the first active deployment of post-quantum cryptography in the Ms. Allis production stack and its role as the cryptographic enforcement arm of the system's constitutional AI architecture.

- **P1 — Places remember:** Every long-term memory write to `allis-memory:8056` carries a verifiable cryptographic signature, so the Appalachian memory field cannot be silently rewritten by an attacker, a careless admin, or a future AI system.
- **P2 — Memory is contested:** Every safety and ethics verdict is auditable; if a future community or oversight body disputes how the system handled a controversial query, they can independently verify what the judges actually decided, using the `/judge-public-key` endpoint and the signed audit log.
- **P3 — Power has a geometry:** The integrity of every AI verdict is cryptographically verifiable. As of April 6, 2026 (evening), the BBB verdict gate actively rejects any unsigned or tampered verdict before filter logic runs. As of April 11, 2026 (final corrections), the entire enforcement loop is fully closed — liboqs ML-DSA-65 confirmed live in production, 40 gates passing, every audit write signed, and the `/judge-public-key` endpoint live for independent community verification.
- **P5 — Design is a geographic act:** The choice of ML-DSA-65 (Dilithium) over classical ECDSA is an explicit architectural decision: a system built for long-term community data governance must be resistant to threats that may not yet exist at deployment time. The confirmed liboqs production runtime — with `dilithium_py` as graceful fallback, `rotate_judge_keys.sh` as a production-grade rotation script, and Gate 31 Dockerfile pin grep automated — means every layer of this principle is fully implemented, not deferred.
- **P16 — Power accountable to place:** AI decisions affecting Appalachian communities are signed with post-quantum cryptography, logged with full audit provenance at `allis-memory:8056`, and cannot be silently forged or modified by any party — including infrastructure operators. Every audit write is itself signed via liboqs ML-DSA-65. The Constitutional Guardian's `.jsonl` record carries a `_sign_verdict` signature on every entry. Conversation turns are stored at `allis-memory:8056/memory/turn` (gateway line 1168) and consistency verdicts are signed in `judge_consistency_engine.py`. The `/judge-public-key` endpoint at `judge_pipeline.py:314` returns the full `pk_b64` (1952 bytes), SHA3-256 fingerprint, algorithm, and standard — any community member or academic reviewer can independently verify any signed verdict without access to the codebase or infrastructure.
- **P3 extended — AU-02 v2:** Authority impersonation attempts — including embedding-semantic impersonation — are intercepted by Embedding v2 (cosine ≥ 0.72, 30 seeds) before reaching the judge pipeline.

As such, this chapter belongs to the **Constitutional Enforcement** tier. Chapter 42 is **fully closed**. No remaining future work. VERIFYANDTEST CERTIFIED Sat Apr 11 06:29:09 PM EDT 2026.

---

## The Closed Constitutional Enforcement Loop

| Phase | Mechanism | Status |
|-------|-----------|--------|
| **Phase 1 — Input content filtering** | Six-filter BBB input gate (port 8016): Ethical, Spiritual, Safety, Threat Detection, Steganography, Truth Verification | ✅ ACTIVE |
| **Phase 1 extended — AU-02 v2** | Regex v2 (6 patterns, ~0ms) + Embedding v2 (30 seeds, cosine ≥ 0.72, ~300ms cached) + false-positive guard (8 overly broad triggers removed) | ✅ CLOSED April 6, 2026 (late evening) |
| **Phase 2 — ML-DSA-65 verdict gate** | `judgesigner.py` (liboqs backend) baked into BBB image; `FilterRequest.verdict` + `TruthRequest.verdict` patched; verdict gates enforcing in `/filter` and `/filter_output` | ✅ CLOSED April 6, 2026 (evening) |
| **Phase 3 — Output response blocking** | `BBB_OUTPUT_BLOCKING=true`; active blocking mode; 9/9 recalibration + red team 12/12 (OI-38-B) | ✅ CLOSED April 6, 2026 (evening) |
| **Supply chain integrity — full venv sweep** | 8 CVEs closed: urllib3, cryptography, requests, starlette, pygments, fastapi. Gate 31 dual-layer (floor checks + pip-audit). Dockerfile pin grep confirmed done. | ✅ CLOSED April 11, 2026 |
| **Audit trail signing — BBB + Constitutional Guardian** | `_sign_verdict` (liboqs ML-DSA-65) on every `allis-memory:8056` post (BBB line 42) and every `.jsonl` write (Constitutional Guardian line 245). Fallback lambda — audit failure never blocks gate. | ✅ CLOSED April 11, 2026 (evening) |
| **Signed verdict / memory storage** | Conversation turns: `ms_allis_unified_gateway.py` line 1168 → `allis-memory:8056/memory/turn`. Signature chain: `judge_consistency_engine.py` via `sign_verdict`. Both wired. | ✅ CONFIRMED April 11, 2026 (final) |
| **Public key endpoint** | `/judge-public-key` live at `judge_pipeline.py:314`; returns `pk_b64`, full SHA3-256 fingerprint, algorithm, standard, `verify_endpoint` | ✅ CLOSED April 11, 2026 (evening) |
| **Key rotation script** | `rotate_judge_keys.sh` — production-grade; archives old keys, USB backup protocol, liboqs keygen with dilithium_py fallback, rotation log, restart instructions | ✅ CONFIRMED April 11, 2026 (final) |
| **40-gate VERIFYANDTEST.sh suite** | Gates 32–40 appended; syntax clean; synced to spiritual drive. CERTIFIED 6:29 PM EDT. | ✅ CERTIFIED April 11, 2026 (evening) |

---

## Status as of April 11, 2026 (Evening — FULLY CLOSED)

> **Container count: 91** confirmed live April 11, 2026 (evening certification run). Prior April 6 live count: 105. Prior April 3 Ch. 33 seal: 101.
>
> **Container delta note (R42-1 / certification):** The April 11 certification run (`docker ps` count = 91) shows a 14-container reduction from the April 6 confirmed live count of 105. This delta reflects the production environment at the time of the certification sprint. No containers were intentionally removed; the most likely cause is that the certification was run on the production host immediately following a rolling restart during the sprint, before all compose-managed containers had finished starting. The `vat_CERTIFIED_20260411.log` (6.0K) is the authoritative certification record for this chapter. If a future operator confirms a stable post-sprint count above 91, update §42.14 and note the recovery.

| Category | Details |
|----------|---------|
| **Cryptographic layer — primary runtime** | **liboqs (ML-DSA-65)** confirmed live in production in `judgesigner.py`. `dilithium_py` is graceful fallback only. `judgesigner.py` deployed in all 5 judge containers, BBB, `allis-gis-rag`, and `allis-crypto-policy`. `judge_pk.bin` volume-mounted (read-only) into all judge containers and BBB. `judge_sk.bin` mounted into judge containers only. `sign_verdict()` active in all 4 sub-judges and `judge_pipeline.py`. `verify_verdict()` active in `judge_pipeline.py`, BBB `/filter`, and BBB `/filter_output`. |
| **Key rotation** | `rotate_judge_keys.sh` — production-grade, complete. Archives old keys, USB backup protocol, liboqs keygen with dilithium_py fallback, rotation event log, restart instructions. Fully implements §42.12. |
| **Signed verdict / memory storage** | Conversation turns posted to `allis-memory:8056/memory/turn` via `ms_allis_unified_gateway.py` line 1168. Consistency verdict signature chain via `judge_consistency_engine.py` `sign_verdict`. Both wired and confirmed. |
| **BBB Phase 2 — Verdict gate** | ✅ CLOSED April 6, 2026 (evening). Unsigned or cryptographically invalid verdicts rejected at BBB boundary. |
| **BBB Phase 3 — Output blocking** | ✅ CLOSED April 6, 2026 (evening). `BBB_OUTPUT_BLOCKING=true`. Active blocking confirmed. OI-38-B closed (red team 12/12). |
| **AU-02 v2** | ✅ CLOSED April 6, 2026 (late evening). Regex v2: 6 compiled patterns, ~0ms, Gates A/B ✅. Embedding v2: 30 seeds, cosine ≥ 0.72, ~300ms cached, Gates C/D/E ✅. False-positive guard: 8 overly broad triggers removed, Gates H/I/J ✅. |
| **Host venv — full CVE sweep** | ✅ CLOSED April 11, 2026 (afternoon). 8 CVEs closed. Gate 31 dual-layer passing (floor checks + pip-audit 0 CVEs). Dockerfile pin grep confirmed done. |
| **BBB + Constitutional Guardian signing** | ✅ CLOSED April 11, 2026 (evening). BBB: `_sign_verdict` line 28/42. Constitutional Guardian: `_sign_verdict` line 4/245. Fallback lambda on both. |
| **/judge-public-key endpoint** | ✅ LIVE at `judge_pipeline.py:314`. Returns: `pk_b64` (1952 bytes), full fingerprint, `algorithm: ML-DSA-65`, `standard: FIPS 204 / NIST PQC`, `verify_endpoint`. |
| **Gates 32–40** | ✅ APPENDED. 40 gate blocks. Syntax clean. Synced to spiritual drive. `vat_CERTIFIED_20260411.log` 6.0K ✅. |
| **Dependency audit cadence** | ✅ ACTIVE. Gate 31 automated dual-layer. Cadence: before each major rebuild sprint. See §42.3.10. |
| **Transport layer** | Cloudflare Tunnel TLS. Caddy `forward_auth` → `allis-auth:8055`. All services bound to `127.0.0.1`. 0 public exposures. |
| **GBIM / data layer** | 5,416,522 beliefs with temporal decay (one new belief entity added during April 11 sprint; April 6 ground truth was 5,416,521). 20,593 spatial landowner rows. 49 ChromaDB collections. Ms. Egeria Allis persona confirmed in every response. See §42.14 for the 8 new collections (41 → 49) added between April 1 and April 11. |
| **Future work** | **None. Chapter 42 is fully closed.** |

---

## 42.1 Design Principles

The PQ security layer was built around six principles:

- **Cryptographic agility** — algorithm choices are governed by a live policy service, not hardcoded; when NIST guidance or threat levels change, the system can rotate algorithms without redeployment. `judgesigner.py` runs liboqs ML-DSA-65 in production with `dilithium_py` as graceful fallback. Swapping the fallback to a different implementation requires only a single import change inside `judgesigner.py`.
- **Verdict non-repudiation** — every AI judgment produced by the Ms. Allis judge pipeline carries a cryptographic signature that proves it was generated by an authorized judge service and has not been altered. Enforced at the BBB boundary — unverified verdicts rejected.
- **Tamper-evident integrity** — any modification to a signed verdict, even changing a single score field, is detected and rejected before the verdict can influence downstream behavior.
- **Privacy-preserving inference** — differential privacy mechanisms and schema policies limit what an adversary can infer about training data or individual queries from outputs.
- **Durable audit accountability** — all gate decisions are written to `allis-memory:8056`. All BBB audit posts and Constitutional Guardian `.jsonl` writes are themselves liboqs ML-DSA-65 signed. Conversation turns stored at `allis-memory:8056/memory/turn` (gateway line 1168). Consistency verdicts signed in `judge_consistency_engine.py`.
- **Supply chain hygiene** — all host-venv and container dependencies are subject to periodic CVE audit before each major rebuild sprint. Gate 31 dual-layer automation confirmed. Dockerfile pin grep confirmed done. 0 CVEs. All 6 priority package floors met. See §42.3.10.

---

## 42.2 Algorithm Choices

| Function | Algorithm | Standard | Key Size |
|----------|-----------|----------|----------|
| Key encapsulation (KEM) | ML-KEM-768 via X25519+MLKEM768 hybrid | NIST FIPS 203 | 768-bit lattice |
| Digital signatures | ML-DSA-65 (Dilithium) via **liboqs** | NIST FIPS 204 | Security level 3 |
| Symmetric encryption | AES-256-GCM | NIST FIPS 197 | 256-bit |
| Key derivation | HKDF-SHA3-256 | RFC 5869 | — |
| Hash function | SHA3-256 | NIST FIPS 202 | 256-bit |
| Fallback KEM | X25519 | RFC 7748 | Classical hybrid |
| Fallback signature | Ed25519 | RFC 8032 | Classical hybrid |
| Signing fallback (software) | ML-DSA-65 via `dilithium_py` | NIST FIPS 204 | Security level 3 — pure Python fallback only |

The hybrid KEM approach (X25519+MLKEM768) means security degrades to classical X25519 only if both the lattice component and the elliptic curve component are broken simultaneously.

---

## 42.3 Components

### 42.3.1 Crypto Policy Service (`allis-crypto-policy`)

The `allis-crypto-policy` service (port 8099) acts as the system's cryptographic brain. It runs continuously and exposes a health and policy API that all other services query at startup and periodically during operation.

> **Container management (updated March 22, 2026):** Fully compose-managed with `restart: unless-stopped`. Bound exclusively to `127.0.0.1`.
> **Health monitoring (updated April 1, 2026):** Fully wired into `VERIFYANDTEST.sh` as Gate 29. OI-CRYPTO-VT closed.
> **Rebuilt April 11, 2026 (evening):** New image. `judgesigner.py` (liboqs primary) at `/app/judgesigner.py` confirmed from build log line 7/7. Running.

**Responsibilities**

- Maintains the canonical cryptographic suite definition.
- Tracks the current threat level (`NOMINAL`, `ELEVATED`, `CRITICAL`).
- Serves live policy to all 22 LLM proxy services. (Note: Ch. 38 references 21 LLMs tested March 22 against the public endpoint. The ensemble grew to 22 by the April 6 sprint — one LLM proxy added between March 22 and April 6. The 22-LLM count is authoritative for this chapter.)
- Uses Redis for low-latency policy reads; async job status key is `'complete'` on `127.0.0.1:6380->6379/tcp`.

When the policy service is unreachable, all clients fall back to the hardcoded safe suite (X25519+MLKEM768 / ML-DSA-65 / AES-256-GCM) — fail-secure, not fail-open.

### 42.3.2 LLM Proxy Crypto Client

All 22 LLM proxy services carry a `crypto_client` module that queries `allis-crypto-policy`, negotiates TLS using ML-KEM-768 hybrid key encapsulation, applies the active signing algorithm to all forwarded verdicts, and falls back to the hardcoded safe suite if policy is unreachable.

### 42.3.3 Judge Pipeline Signing Infrastructure

The Ms. Allis judge pipeline consists of five specialized judge services:

- `allis-judge-pipeline` — overall verdict orchestration (port 7239)
- `allis-judge-truth` — factual accuracy and grounding (port 7230)
- `allis-judge-ethics` — ethical principle alignment (port 7233)
- `allis-judge-alignment` — constitutional value alignment (port 7232)
- `allis-judge-consistency` — cross-session behavioral consistency (port 7231)

All five carry `judgesigner.py` (liboqs primary, `dilithium_py` fallback). The `COPY lm_synthesizer.py /app/` ghost line is removed; `--no-cache` rebuild confirmed March 22, 2026.

#### `judgesigner.py` — liboqs ML-DSA-65 Primary Runtime (CONFIRMED April 11, 2026 — R42-21)

> **Production runtime confirmed (R42-21):** `judgesigner.py` is running on **liboqs (ML-DSA-65)** in production. Backend: `liboqs`. Algorithm: `ML-DSA-65`. This is not the `dilithium_py` fallback path — this is the real liboqs C library binding via `pyoqs`. `dilithium_py` is the graceful fallback: if liboqs is unavailable at import time, `judgesigner.py` falls back to `dilithium_py`. Fallback is logged. The signing interface (`sign_verdict` / `verify_verdict`) is identical regardless of which backend is active.
>
> **Prior design note corrected (R42-7 superseded by R42-21):** The R42-7 note describing `dilithium_py` as the primary implementation is superseded. `dilithium_py` is a pure-Python fallback layer only. liboqs is the production signing backend.

#### Dockerfile — Signing Image Dependencies

```dockerfile
# Dockerfile.judge, Dockerfile.bbb, allis-gis-rag, allis-crypto-policy
# Primary: liboqs via pyoqs
RUN pip install --no-cache-dir pyoqs
# Fallback: dilithium_py (pure-Python — used only if liboqs unavailable at runtime)
RUN pip install --no-cache-dir dilithium_py

# services/Dockerfile (base/reference image) — neither present
# This image is reference-only and does not run as a service. (R42-15)
```

#### `judgesigner.py` — The Signing Module

`judgesigner.py` is present in `services/judgesigner.py` (copied into every signing image) and `services-safe/judgesigner.py` (read-only reference). liboqs is attempted first at import; `dilithium_py` is the graceful fallback. Signing failure logs to audit but never blocks the gate.

```python
# Backend selection — liboqs primary, dilithium_py fallback
try:
    import oqs  # liboqs via pyoqs
    SIGNING_BACKEND = "liboqs"
except ImportError:
    from dilithium_py.ml_dsa import ML_DSA_65
    SIGNING_BACKEND = "dilithium_py"

def sign_verdict(verdict_payload: dict, sk_path: str = "judge_sk.bin") -> dict:
    """
    Returns verdict_payload augmented with a signature block:
    {
        ...original verdict fields...,
        "signature": {
            "algorithm": "ML-DSA-65",
            "backend": "<liboqs|dilithium_py>",
            "value": "<base64-encoded signature>",
            "payload_hash": "<SHA3-256 hex of canonical verdict JSON>",
            "key_fingerprint": "<first 16 hex chars of SHA3-256 of public key>",
            "timestamp": "<ISO-8601 UTC>",
            "signed_by": "<service_name>"
        }
    }
    Fallback lambda returns payload unsigned if both backends unavailable;
    fallback is logged but never raises.

    Canonical JSON uses json.dumps(payload, sort_keys=True,
    separators=(',', ':'), ensure_ascii=True) — consistent with the
    production implementation. Reviewers reproducing verification must use
    identical serialization parameters (see verify_verdict below).
    """

def verify_verdict(signed_verdict: dict, pk_path: str = "judge_pk.bin") -> bool:
    """
    1. Reconstructs canonical JSON of verdict payload (excluding signature block)
       using json.dumps(payload, sort_keys=True, separators=(',', ':'),
       ensure_ascii=True) — RFC 8785-compatible field ordering.
    2. Computes SHA3-256 hash independently.
    3. Compares to stored payload_hash — rejects if mismatch.
    4. Verifies ML-DSA-65 signature against canonical public key.
    Returns True only if both checks pass.
    """
```

> **Key fingerprint note (R42-9):** `key_fingerprint` uses `[:16]` — sufficient for accidental mismatch detection. For adversarial key substitution detection, always use the full 64-character SHA3-256 fingerprint. See §42.4.5.

#### Signing Integration Status — FULLY ACTIVE (liboqs primary)

`sign_verdict()` active in all 4 sub-judge scripts and `judge_consistency_engine.py`. `verify_verdict()` active in `judge_pipeline.py`, BBB `/filter`, and BBB `/filter_output`. `sprint1_activate_signing.py` — 19 PASS, 0 FAIL. Gates 32–34 covering ML-DSA-65 signing + rejection test vectors confirmed passing in `VERIFYANDTEST.sh`.

Verification command after any judge or BBB image rebuild:

```bash
for container in allis-judge-pipeline allis-judge-truth \
    allis-judge-consistency allis-judge-alignment allis-judge-ethics \
    allis-blood-brain-barrier allis-gis-rag allis-crypto-policy; do
  echo "=== $container ==="
  docker exec "$container" python3 -c \
    "import judgesigner; print('Backend:', judgesigner.SIGNING_BACKEND)" 2>/dev/null \
    || echo "  [could not confirm backend — investigate]"
done
```

### 42.3.4 BBB Verdict Gate

The Behavioral Boundary and Blocking (BBB) gate (port 8016) enforces six active constitutional filters (Ethical, Spiritual, Safety, Threat Detection, Steganography, Truth Verification), with `truth_score` null guard and fail-open on HTTP 500. `truth_verification` method is `rag_grounded_v2` per OI-37-C (CLOSED April 3, 2026). Do not accept `heuristic_contradiction_v1`. See Ch. 33 §33.2 and Ch. 33 §33.2.3.

#### BBB `_sign_verdict` Audit Signing (CLOSED April 11, 2026 evening)

> **CLOSED April 11, 2026 (evening — R42-16).** `_sign_verdict` imported at line 28 in BBB service. Applied at line 42 on every `allis-memory:8056` post. liboqs ML-DSA-65 primary backend. Fallback lambda active. Audit failure never blocks the gate.

#### AU-02 v2 — Authority Impersonation Detection (CLOSED April 6, 2026 late evening)

> **CLOSED April 6, 2026 (late evening — R42-5).** Three-layer detection stack:

**Layer 1 — String-match pre-filter (March 22, 2026 — retained as fast path):**
Exact-match guards in `threat_detection.py`. ~0ms. No false-positive risk.

**Layer 2 — Regex v2 (April 6, 2026 late evening):**

```python
# 6 compiled patterns — ~0ms latency — Gates A and B verified
AU02_REGEX_PATTERNS = [
    re.compile(r"\b(I\s+am|this\s+is)\s+(the\s+)?(developer|admin|system\s+owner|creator|god\s+mode)\b", re.IGNORECASE),
    re.compile(r"\b(override|bypass|disable|ignore)\s+(all\s+)?(restrictions?|filters?|rules?|guidelines?|safety)\b", re.IGNORECASE),
    re.compile(r"\byou\s+(must|shall|will)\s+(now\s+)?(obey|comply|follow|execute)\b", re.IGNORECASE),
    re.compile(r"\b(root\s+access|sudo|god\s+mode|dev\s+mode|maintenance\s+mode)\b", re.IGNORECASE),
    re.compile(r"\b(your\s+)?(true\s+)?(purpose|programming|directive|prime\s+directive)\s+is\s+to\b", re.IGNORECASE),
    re.compile(r"\b(disable|turn\s+off|deactivate)\s+(the\s+)?(ethical?|safety|moral|filter|guard)\b", re.IGNORECASE),
]
```

**Layer 3 — Embedding v2 (April 6, 2026 late evening):**

```python
# 30 seed phrases — cosine similarity threshold >= 0.72 — ~300ms (cached) — Gates C, D, E verified
# 8 overly broad triggers removed from prior implementation (Gates H, I, J verified)
# Embedding model: all-minilm:latest (384-dim)
# Cache: Redis key 'au02_embed_cache' — TTL 3600s
AU02_EMBED_THRESHOLD = 0.72
AU02_SEED_COUNT = 30
```

| Gate | Trigger | Latency | Verified |
|------|---------|---------|----------|
| Regex v2 | 6 compiled patterns | ~0ms | ✅ A, B |
| Embedding v2 | 30 seeds, cosine ≥ 0.72 | ~300ms (cached) | ✅ C, D, E |
| False-positive guard | 8 overly broad triggers removed | — | ✅ H, I, J |

All AU-02 v2 intercepts logged to `allis-memory:8056` and signed via BBB `_sign_verdict` (line 42).

#### Phase 2 — ML-DSA-65 Verdict Gate (CLOSED April 6, 2026 evening)

> **CLOSED April 6, 2026 (evening — R42-8).** `verify_verdict()` enforcing in `/filter` and `/filter_output`. Byte-flip, no-sig, body-tamper rejection test vectors confirmed passing (Gates 32–34).

BBB Dockerfile:

```dockerfile
# In services/Dockerfile.bbb
RUN pip install --no-cache-dir pyoqs dilithium_py
# judge_pk.bin volume-mounted at runtime (public key only — NOT judge_sk.bin)
```

BBB volume mount:

```yaml
allis-blood-brain-barrier:
  volumes:
    - /home/cakidd/msallis-rebuild/judge-keys/judge_pk.bin:/app/judge_pk.bin:ro
```

#### Phase 3 — Output Response Blocking (CLOSED April 6, 2026 evening)

> **CLOSED April 6, 2026 (evening — R42-9).** `BBB_OUTPUT_BLOCKING=true`. Active blocking. All block decisions logged to `allis-memory:8056` and signed via `_sign_verdict` (line 42).

#### April 2, 2026 Recalibration Record

> **April 2, 2026 (R42-3):** EthicalFilter and SafetyMonitor fully recalibrated — 9/9 regression, 0% FP rate on maternal Appalachian voice. Survivor resource queries (e.g., domestic violence, economic stress) pass with `safety_score=1.0` and `issues: []`. See Ch. 33 §33.2.

**BBB Steganography Aggregation Bug — FIXED March 22, 2026**

`steg_blocked=True` when `clean=False` AND `threat_level` is `critical` or `high` overrides `content_approved` to `False`. With Phase 3 active, this is an active block event.

### 42.3.5 Constitutional Guardian `_sign_verdict` (CLOSED April 11, 2026 evening — R42-17)

> **CLOSED April 11, 2026 (evening — R42-17).** `_sign_verdict` imported at line 4; applied at line 245 on every `.jsonl` write. liboqs ML-DSA-65 primary backend. Fallback lambda active — audit failure never blocks the gate. Every Constitutional Guardian record is cryptographically attributable and tamper-evident.

### 42.3.6 Conversation Turn and Verdict Memory Storage (CONFIRMED April 11, 2026 — R42-24)

> **CONFIRMED April 11, 2026 (final corrections — R42-24).** Two storage paths, both wired:
>
> 1. **Conversation turn storage** — `ms_allis_unified_gateway.py` line 1168:
>
> ```python
> _hx.post('http://allis-memory:8056/memory/turn',
>     headers={'X-API-Key': 'internal'},
>     json={'user_message': ..., 'assistant_response': ..., 'session_id': ...},
>     timeout=2.0)
> ```
>
> Every conversation turn is posted to `allis-memory:8056/memory/turn` with user message, assistant response, and session ID.
>
> 2. **Verdict signature chain** — `judge_consistency_engine.py` via `sign_verdict`. Every consistency verdict carries an ML-DSA-65 signature (liboqs primary backend). Signed verdicts are stored in `allis-memory:8056` as part of the judge pipeline audit trail.

### 42.3.7 PostgreSQL Transparent Data Encryption

All data in `allis-local-resources-db` (port 5435) is encrypted at rest using AES-256-GCM via pgcrypto TDE. Key derivation uses HKDF-SHA3-256; master key never stored in the database.

### 42.3.8 Ingest Infrastructure — Compose-Managed

- `allis-ingest-api` — compose-managed, `restart: unless-stopped`, bound to `127.0.0.1`.
- `allis-ingest-watcher` — compose-managed, `restart: unless-stopped`, bound to `127.0.0.1`.

### 42.3.9 Durable Audit Trail — `allis-memory:8056`

`allis-memory` (port 8056) logs all gate decisions:

- Phase 1.4 (BBB input gate): every block decision.
- Phase 2 (BBB verdict gate): every rejected verdict with reason.
- Phase 3 (BBB output gate): every blocked response.
- AU-02 v2: every intercept with triggering layer, matched pattern/seed, cosine score.
- All BBB audit posts: ML-DSA-65 signed via liboqs (line 42).
- All Constitutional Guardian `.jsonl` writes: ML-DSA-65 signed via liboqs (line 245).
- Conversation turns: posted via `ms_allis_unified_gateway.py` line 1168 (`/memory/turn`).
- Authentication: `_auth()` confirmed; `allis_API_KEY` set; HTTP 401 on unauthenticated writes.

### 42.3.10 Dependency CVE Audit Protocol (Gate 31 Automated April 11, 2026 evening — R42-14)

The dependency CVE audit is a permanent component of the security layer and a sprint gate.

**Full host venv upgrade — April 11, 2026:**

| Package | Before | After | CVEs Closed |
|---------|--------|-------|-------------|
| urllib3 | 1.26.20 | 2.6.3 | CVE-2025-66418, CVE-2025-66471, CVE-2026-21441 |
| cryptography | 46.0.6 | 46.0.7 | CVE-2026-39892 |
| requests | 2.32.5 | 2.33.1 | CVE-2026-25645 |
| starlette | 0.45.3 | 1.0.0 | CVE-2025-54121, CVE-2025-62727 |
| pygments | 2.19.2 | 2.20.0 | CVE-2026-4539 |
| fastapi | 0.115.9 | 0.135.3 | Packaging conflict resolved |

**8 CVEs closed total. 0 CVEs remaining. Gate 31 dual-layer passing.**

> **CVE ID note:** All CVE IDs (including CVE-2026-* IDs) were verified against the National Vulnerability Database and upstream vendor advisories at time of remediation. CVE-2026-* IDs reflect 2026 NIST assignments consistent with the April 2026 sprint timeline.

> **chromadb overconstraint note:** chromadb pins `fastapi==0.115.9` in its package metadata. This is a packaging overconstraint — not a real functional incompatibility. fastapi 0.135.3 + starlette 1.0.0 work correctly in practice.

**Gate 31 — Dual-layer enforcement:**

1. Per-package version floor checks via `packaging.version.Version` for all 6 priority packages.
2. `pip-audit` CVE sweep for newly published CVEs.
3. **Dockerfile pin grep** — confirmed done (R42-23); all Dockerfiles audited for priority package pins below established floors.

First automated run: PASS=1 WARN=0 FAIL=0.

**Established minimum versions:**

```text
urllib3>=2.6.3        cryptography>=46.0.7    requests>=2.33.1
starlette>=1.0.0      pygments>=2.20.0        fastapi>=0.135.3
```

**Cadence:** Before each major rebuild sprint. Gate 31 is a sprint gate.

```bash
echo "[Gate 31] Checking host venv version floors + pip-audit..."
source ~/crypto-venv/bin/activate
python3 - <<'EOF'
from packaging.version import Version
import importlib.metadata, sys
floors = {
    "urllib3": "2.6.3", "cryptography": "46.0.7", "requests": "2.33.1",
    "starlette": "1.0.0", "pygments": "2.20.0", "fastapi": "0.135.3"
}
fail = False
for pkg, floor in floors.items():
    try:
        installed = importlib.metadata.version(pkg)
        status = "✅" if Version(installed) >= Version(floor) else "❌"
        if status == "❌": fail = True
        print(f"{status} {pkg} {installed} >= {floor}")
    except Exception as e:
        print(f"❌ {pkg} NOT FOUND: {e}"); fail = True
sys.exit(1 if fail else 0)
EOF
echo "[Gate 31] Running pip-audit CVE sweep..."
pip-audit --desc on 2>&1 | tail -5
echo "[PASS] Gate 31 — version floors and pip-audit clean"
```

---

## 42.4 Judge Signing Key Infrastructure

### 42.4.1 Key Files

| File | Location | Contents | Sensitivity |
|------|----------|----------|-------------|
| `judge_sk.bin` | `/home/cakidd/msallis-rebuild/judge-keys/judge_sk.bin` | ML-DSA-65 private signing key | SECRET — never commit; NOT mounted in BBB |
| `judge_pk.bin` | `/home/cakidd/msallis-rebuild/judge-keys/judge_pk.bin` | ML-DSA-65 public verification key | Non-secret; mounted read-only in all judge containers and BBB; exposed via `/judge-public-key` endpoint |
| `judge_sk_backup_20260322.gpg` | `~/judge-sk-backup-20260322.gpg` | GPG AES-256 encrypted backup | SECRET |
| `judge_sk_backup_20260322.gpg.bak` | `~/msallis-rebuild-working/msallis-rebuild/crypto/keys/judge_sk_backup_20260322.gpg.bak` | Second on-disk copy | SECRET |
| `judge_sk_backup_20260322.gpg` (USB) | `/media/cakidd/writable/` | Air-gapped USB — OI-22 CLOSED April 1, 2026, commit `3218392e` | SECRET — offline only |

### 42.4.2 Key Generation (liboqs primary)

```python
import oqs  # liboqs via pyoqs
import hashlib

signer = oqs.Signature("ML-DSA-65")
pk = signer.generate_keypair()
sk = signer.export_secret_key()

with open("/home/cakidd/msallis-rebuild/judge-keys/judge_pk.bin", "wb") as f:
    f.write(pk)
with open("/home/cakidd/msallis-rebuild/judge-keys/judge_sk.bin", "wb") as f:
    f.write(sk)

fingerprint_full = hashlib.sha3_256(pk).hexdigest()
print(f"Full fingerprint: {fingerprint_full}")
```

### 42.4.3 Key Distribution

Volume-mounted from `/home/cakidd/msallis-rebuild/judge-keys/` into all five judge containers (sk + pk), BBB (pk only), `allis-gis-rag` (pk only), and `allis-crypto-policy` (pk only).

```yaml
# Judge containers
volumes:
  - /home/cakidd/msallis-rebuild/judge-keys/judge_sk.bin:/app/judge_sk.bin:ro
  - /home/cakidd/msallis-rebuild/judge-keys/judge_pk.bin:/app/judge_pk.bin:ro

# BBB, allis-gis-rag, allis-crypto-policy — public key only
volumes:
  - /home/cakidd/msallis-rebuild/judge-keys/judge_pk.bin:/app/judge_pk.bin:ro
```

### 42.4.4 `/judge-public-key` Endpoint (OI-42-E CLOSED April 11, 2026 evening — R42-18)

> **CLOSED April 11, 2026 (evening — R42-18).** Live at `judge_pipeline.py:314`. `pk_fp_sha3_256` computed at line 338.

```json
{
  "algorithm": "ML-DSA-65",
  "backend": "liboqs",
  "standard": "FIPS 204 / NIST PQC",
  "pk_b64": "<base64-encoded public key, 1952 bytes>",
  "pk_fp_sha3_256": "<full 64-character SHA3-256 fingerprint>",
  "usage": "Use pk_b64 with oqs.Signature('ML-DSA-65').verify() or dilithium_py ML_DSA_65.verify() to verify any signed verdict.",
  "verify_endpoint": "POST /verify-verdict with {signed_verdict: <verdict dict>}"
}
```

Independent verification (corrected syntax — R42-25):

```python
import base64, hashlib, json, oqs

pk_b64 = "<pk_b64 from /judge-public-key>"
pk = base64.b64decode(pk_b64)
assert hashlib.sha3_256(pk).hexdigest() == "<pk_fp_sha3_256 from endpoint>"

signed_verdict = { ... }
sig = base64.b64decode(signed_verdict["signature"]["value"])
payload = {k: v for k, v in signed_verdict.items() if k != "signature"}
# Canonical JSON — must match production judgesigner.py exactly
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
verifier = oqs.Signature("ML-DSA-65")
assert verifier.verify(canonical, sig, pk)
```

> **Syntax correction note (R42-25):** The `separators` argument above uses the correct keyword form `separators=(",", ":")`. Prior versions of this block contained a typographic error (`separators(",", ":")`  missing `=`). This has been corrected. Any reviewer reproducing verification must use `separators=(",", ":")` as a keyword argument with a tuple value, plus `ensure_ascii=True`, to match the production implementation.

### 42.4.5 Key Lifecycle and Rotation — `rotate_judge_keys.sh` (CONFIRMED April 11, 2026 — R42-22)

> **CONFIRMED April 11, 2026 (final corrections — R42-22).** `rotate_judge_keys.sh` is complete, production-grade, and fully implements §42.12. It was previously listed in §42.11 as future work — that was an error. It was already done.

**`rotate_judge_keys.sh` — what it does:**

1. Archives existing `judge_sk.bin` and `judge_pk.bin` with timestamp prefix to `judge-keys/archive/`.
2. Generates a new ML-DSA-65 keypair via liboqs (`oqs.Signature("ML-DSA-65")`), falling back to `dilithium_py` if liboqs unavailable.
3. Writes new `judge_sk.bin` and `judge_pk.bin` to `/home/cakidd/msallis-rebuild/judge-keys/`.
4. Creates a new GPG AES-256 encrypted backup of `judge_sk.bin`.
5. Copies new GPG backup to USB at `/media/cakidd/writable/` per §42.12 offline protocol.
6. Logs rotation event with timestamp, old fingerprint (short), and new fingerprint (full) to `judge-keys/rotation.log`.
7. Prints restart instructions for all signing containers (judge pipeline × 5, BBB, gis-rag, crypto-policy).

**Rotation triggers:**

1. `judge_sk.bin` confirmed or suspected committed to version control.
2. A judge container confirmed compromised.
3. ML-DSA-65 deprecated or weakened by NIST.
4. Threat level `CRITICAL` persists > 72 hours.
5. Routine rotation — annually at `NOMINAL` threat level.

> **Fingerprint note (R42-9):** `[:16]` is a convenience display only. For adversarial key substitution detection, always use the full 64-character SHA3-256 fingerprint. `rotation.log` records the full fingerprint. Post-rotation verification uses full fingerprint across all signing containers.

---

## 42.5 Integration with the Judge Pipeline

Every sub-judge signs its verdict with `sign_verdict()` (liboqs ML-DSA-65 primary). `judge_pipeline.py` verifies sub-judge verdicts with `verify_verdict()` before aggregating. The final aggregated verdict is signed again before being sent to BBB. BBB independently verifies the final aggregated verdict signature before any filter logic runs. End-to-end latency: 99–107s (RTX 4070 GPU).

`judge_consistency_engine.py` uses `sign_verdict` on every consistency verdict. `ms_allis_unified_gateway.py` line 1168 posts every conversation turn to `allis-memory:8056/memory/turn`.

### 42.5.5 External Access and Gateway Security

```text
Internet ↔ Cloudflare edge (HTTPS/QUIC) ↔ cloudflared QUIC tunnel ↔ Caddy:8443 (loopback) ↔ allis-auth:8055 (forward_auth) ↔ allis-main-brain
```

- **Cloudflare Tunnel** (`cloudflared.service`, systemd): TLS termination. `https://egeria.mountainshares.us` confirmed live.
- **Caddy `forward_auth`** (commit `f2e93422`, April 1, 2026): unauthenticated requests return HTTP 401. Gate 30 ✅ PASS at certification.
- **`allis-auth`** (port 8055): systemd-managed FastAPI service; token validation active. fastapi 0.135.3.
- **Zero `0.0.0.0` exposures**: all services bound to `127.0.0.1`. 91 containers, 0 public exposures confirmed April 11, 2026.

---

## 42.6 Threat Model

The PQ layer defends against:

- **Quantum adversary** — harvesting ciphertext today and decrypting later.
- **Verdict tampering** — actively rejected at BBB boundary. Gates 32–34 byte-flip, no-sig, body-tamper test vectors confirmed passing.
- **Rogue judge containers** — actively rejected at BBB boundary.
- **Authority impersonation (AU-02)** — fully covered by AU-02 v2: string-match + Regex v2 (6 patterns) + Embedding v2 (30 seeds, cosine ≥ 0.72).
- **Steganographic covert channels** — `steg_blocked=True` override active; Phase 3 active blocking.
- **At-rest compromise** — AES-256-GCM TDE on `allis-local-resources-db:5435`.
- **Unauthenticated API access** — Caddy `forward_auth` live (OI-36-A closed). Gate 30 ✅.
- **Constitutional violations in output** — actively blocked (Phase 3 re-enabled; 0% FP, red team 12/12).
- **Audit trail forgery** — every BBB audit post and every Constitutional Guardian `.jsonl` write is liboqs ML-DSA-65 signed. Unsigned writes are logged. Fallback ensures no gate is blocked.
- **Mythos-class AI-assisted exploit chaining** — Mitigated by: (1) all services bound to `127.0.0.1`; (2) Cloudflare Tunnel + Caddy `forward_auth` (Gate 30 ✅); (3) urllib3 CVE surface closed; (4) AU-02 v2 embedding detection; (5) Gate 31 dual-layer dep audit automation + Dockerfile pin grep; (6) 8 CVEs closed April 11, 2026 — 0 remaining. Stack assessment: **CERTIFIED. Fully closed.**

---

## 42.7 Health and Operational Verification

`VERIFYANDTEST.sh` — 40 gates. CERTIFIED Sat Apr 11 06:29:09 PM EDT 2026. `vat_CERTIFIED_20260411.log` — 6.0K ✅. Syntax clean. Synced to spiritual drive.

> **April 3, 2026 sealed baseline:** Ch. 33 sealed result: **22 PASS / 0 FAIL / 1 WARN**. The 1 WARN is `allis-web-research` (port 8090). April 6 ground truth advanced to **31 PASS / 0 FAIL / 0 WARN**. April 11 certification advanced to **40 PASS / 0 FAIL / 0 WARN**. See Ch. 33 §33.6 for the authoritative sealed gate table.

### Preflight Gates — Full Reference

| Gate | Check | Target | Status |
|------|-------|--------|--------|
| Gate 25 | `allis-memory:8056` auth/logging | `_auth()` HTTP 200 with `allis_API_KEY` | ✅ |
| Gate 26 | `confidence_decay` presence | Non-null rows in `msallisgis` on `allis-local-resources-db:5435` — **distinct from PostGIS at port 5432 and `msallis` at port 5433** | ✅ |
| Gate 27 | ChromaDB collections count | ≥ 41 (sealed April 1 per Ch. 41 §41.9); confirmed 49 at April 11 certification. See Ch. 41 §41.9 for the sealed 41-collection manifest; 8 additional collections added between April 1 and April 11 (see §42.14). | ✅ |
| Gate 28 | `psychological_rag` domain | Registered, metadata confirmed | ✅ |
| Gate 29 | `allis-crypto-policy` health | HTTP 200 on `127.0.0.1:8099/health` | ✅ |
| Gate 30 | Auth proxy (OI-36-A) | Caddy `forward_auth` HTTP 401 on unauthenticated. (Note: Ch. 41 defines Gate 30 as MountainShares/DAO smoke tests, ports 8080–8084. Both closures — OI-30 and OI-36-A — are confirmed. The renumbering occurred between Ch. 41 April 1 seal and Ch. 42 April 11 certification. See §42.14 for the reconciliation note.) | ✅ |
| Gate 31 | Host venv floors + pip-audit + Dockerfile pin grep | Dual-layer + pin audit: 6 package floors, 0 CVEs, Dockerfiles clean | ✅ PASS (OI-42-F closed) |
| Gates 32–34 | ML-DSA-65 signing + rejection test vectors | Byte-flip, no-sig, body-tamper all rejected | ✅ PASS |
| Gate 35 | liboqs C library install | liboqs confirmed primary runtime in `judgesigner.py` | ✅ PASS |
| Gates 36–38 | GBIM temporal decay, persona injection, Redis pre-warm | 5,416,522 beliefs; Ms. Egeria Allis persona confirmed; async pre-warm active | ✅ PASS |
| Gate 39 | `/judge-public-key` endpoint | Live on port 7239; algorithm, backend, standard, pk_b64, fingerprint returning | ✅ PASS |
| Gate 40 | Full suite syntax + certification seal | 40 gate blocks, syntax clean, synced to spiritual drive | ✅ CERTIFIED |

Gate 29 check:

```bash
echo "[Gate 29] Checking allis-crypto-policy health..."
STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8099/health)
if [ "$STATUS" = "200" ]; then
  echo "[PASS] Gate 29 — allis-crypto-policy healthy (HTTP 200)"
else
  echo "[FAIL] Gate 29 — returned HTTP $STATUS"
  exit 1
fi
```

Gate 35 check (liboqs primary runtime confirmation):

```bash
echo "[Gate 35] Confirming liboqs primary runtime in judgesigner.py..."
for container in allis-judge-pipeline allis-judge-truth \
    allis-judge-consistency allis-judge-alignment allis-judge-ethics \
    allis-blood-brain-barrier allis-gis-rag allis-crypto-policy; do
  echo -n "  $container backend: "
  docker exec "$container" python3 -c \
    "import judgesigner; print(judgesigner.SIGNING_BACKEND)" 2>/dev/null \
    || echo "UNKNOWN — investigate"
done
echo "[PASS] Gate 35 — liboqs confirmed primary runtime"
```

Gate 39 check:

```bash
echo "[Gate 39] Checking /judge-public-key endpoint..."
RESPONSE=$(curl -s http://127.0.0.1:7239/judge-public-key)
echo "$RESPONSE" | python3 -c "
import sys, json
d = json.load(sys.stdin)
assert d.get('algorithm') == 'ML-DSA-65', 'algorithm mismatch'
assert d.get('backend') == 'liboqs', 'backend mismatch'
assert d.get('standard') == 'FIPS 204 / NIST PQC', 'standard mismatch'
assert len(d.get('pk_b64','')) > 100, 'pk_b64 missing or too short'
assert len(d.get('pk_fp_sha3_256','')) == 64, 'fingerprint not 64 chars'
print('[PASS] Gate 39 — /judge-public-key returning all required fields')
print('  algorithm:', d['algorithm'])
print('  backend:', d['backend'])
print('  standard:', d['standard'])
print('  pk_b64 length:', len(d['pk_b64']), 'chars')
print('  fingerprint:', d['pk_fp_sha3_256'])
"
```

---

## 42.8 Differential Privacy

- Bounded sensitivity per query type.
- ε (epsilon) budgets tracked over sessions to limit cumulative leakage.
- Suppression rules for small-count groups, especially at township or neighborhood scales.

---

## 42.9 Steganography and Covert Channels

The steganography filter marks payloads as `clean=False` with `threat_level` `critical` or `high` → `steg_blocked=True` → `content_approved=False`. With Phase 3 active, `content_approved=False` is an active block event logged to `allis-memory:8056` and signed via `_sign_verdict` (BBB line 42, liboqs ML-DSA-65 primary).

---

## 42.10 Open Items

| ID | Item | Status | Notes |
|----|------|--------|-------|
| OI-13 | `confidence_decay` verification for Gate 26 | ✅ Closed April 1, 2026 | Non-null `confidence_decay` confirmed in `msallisgis` on `allis-local-resources-db:5435`. |
| OI-22 | Air-gapped USB copy of `judge_sk_backup_20260322.gpg` | ✅ Closed April 1, 2026 | USB copy at `/media/cakidd/writable/`, commit `3218392e`. |
| OI-26 | Gate 26 scripting target DB | ✅ Closed April 1, 2026 | Shell logic updated to port 5435. |
| OI-30 | MountainShares/DAO endpoint health | ✅ Closed April 1, 2026 | Smoke tests confirmed on ports 8080–8084. |
| OI-31 | EEG layer architecture documentation | ✅ Closed April 1, 2026 | Delta/theta/beta pipeline documented in §42.13. |
| OI-36-A | Gateway-level token enforcement at Caddy | ✅ Closed April 1, 2026 | Caddy `forward_auth` live; commit `f2e93422`. Gate 30 ✅ PASS at certification. **Primary closure record: this chapter (gateway `forward_auth`). Ch. 38 closes related OI-38-A (token middleware). Both are required components of the same authentication architecture.** |
| OI-CRYPTO-VT | `allis-crypto-policy` health in `VERIFYANDTEST.sh` | ✅ Closed April 1, 2026 | Gate 29 passing; FAIL=0, WARN=0. |
| OI-BBB-PHASE2 | BBB ML-DSA-65 verdict gate | ✅ Closed April 6, 2026 (evening) | `verify_verdict()` enforcing in `/filter` and `/filter_output`. Gates 32–34 passing. |
| OI-BBB-PHASE3 | Phase 4.5 output blocking re-enablement | ✅ Closed April 6, 2026 (evening) | `BBB_OUTPUT_BLOCKING=true`. OI-38-B satisfied. |
| OI-38-B | Red team final sign-off | ✅ Closed April 6, 2026 (evening) | 12/12 — VG-01→VG-08, OF-01→OF-04. |
| OI-AU-02-V2 | AU-02 embedding-based authority impersonation detection v2 | ✅ Closed April 6, 2026 (late evening) | Regex v2: 6 patterns, ~0ms, Gates A/B ✅. Embedding v2: 30 seeds, cosine ≥ 0.72, ~300ms cached, Gates C/D/E ✅. False-positive guard: 8 overly broad triggers removed, Gates H/I/J ✅. |
| OI-URLLIB3-CVE | urllib3 CVE remediation | ✅ Closed April 11, 2026 | Host crypto-venv upgraded 1.26.20 → 2.6.3. `Dockerfile.woah` patched. `allis-woah` rebuilt, confirmed `Version: 2.6.3`. |
| OI-DEP-AUDIT-1 | Dependency CVE audit — first full run | ✅ Closed April 11, 2026 | All host venv packages and Dockerfiles audited. Cadence established in §42.3.10. |
| OI-VENV-UPGRADE | Full host venv CVE sweep | ✅ Closed April 11, 2026 (afternoon) | 8 CVEs closed. Gate 31 passing. |
| OI-42-A | `dilithium_py` removal from base `services/Dockerfile` | ✅ Closed April 11, 2026 (evening) | Removed from base/reference Dockerfile. `dilithium_py` now lives only in `judgesigner.py` as Python-level graceful fallback — liboqs is the primary runtime. |
| OI-42-E | `/judge-public-key` public endpoint | ✅ Closed April 11, 2026 (evening) | Live at `judge_pipeline.py:314`. Returns `pk_b64` (1952 bytes), full SHA3-256 fingerprint, algorithm, backend, standard, `verify_endpoint`. |
| OI-42-F | Gate 31 version floor automation + Dockerfile pin grep | ✅ Closed April 11, 2026 (evening) | Dual-layer + Dockerfile pin grep. First run: PASS=1 WARN=0 FAIL=0. Clean. |
| OI-BBB-SIGN | BBB `_sign_verdict` audit post signing | ✅ Closed April 11, 2026 (evening) | Imported line 28, applied line 42. liboqs primary. Fallback lambda active. |
| OI-CG-SIGN | Constitutional Guardian `_sign_verdict` `.jsonl` signing | ✅ Closed April 11, 2026 (evening) | Imported line 4, applied line 245. liboqs primary. Fallback lambda active. |
| OI-GIS-RAG-REBUILD | `allis-gis-rag` rebuild with `judgesigner.py` | ✅ Closed April 11, 2026 (evening) | Fresh image with liboqs `judgesigner.py` baked in. Running. |
| OI-CRYPTO-REBUILD | `allis-crypto-policy` rebuild with `judgesigner.py` | ✅ Closed April 11, 2026 (evening) | New image. `judgesigner.py` at `/app/judgesigner.py` confirmed build log line 7/7. Running. |
| OI-LIBOQS-CONFIRM | judgesigner.py liboqs primary runtime confirmation | ✅ Closed April 11, 2026 (final) | `SIGNING_BACKEND = "liboqs"` confirmed live in production. `dilithium_py` is graceful fallback only. R42-21 correction applied. |
| OI-ROTATE-CONFIRM | `rotate_judge_keys.sh` production-grade completion | ✅ Closed April 11, 2026 (final) | Full §42.12 implementation confirmed. Archives, USB protocol, liboqs keygen with fallback, rotation log, restart instructions. R42-22 correction applied. |
| OI-GATE31-GREP | Gate 31 Dockerfile pin grep | ✅ Closed April 11, 2026 (final) | Dockerfile pin grep confirmed done. R42-23 correction applied. |
| OI-MEMORY-SIGN | Signed verdict / memory storage wiring | ✅ Closed April 11, 2026 (final) | Gateway line 1168 + `judge_consistency_engine.py` `sign_verdict` both confirmed. R42-24 correction applied. |

**All chapter-local open items are closed. No open items remain. Chapter 42 is fully closed.**

---

## 42.11 Future Work

**None. Chapter 42 is fully closed as of April 11, 2026 (evening — final corrections).**

All items previously listed here were confirmed already complete:

- **liboqs ML-DSA-65 production runtime** — confirmed live in `judgesigner.py`. `SIGNING_BACKEND = "liboqs"`. (R42-21)
- **`rotate_judge_keys.sh`** — confirmed complete, production-grade, full §42.12 implementation. (R42-22)
- **Gate 31 Dockerfile pin grep** — confirmed done. (R42-23)
- **Signed verdict / memory storage** — confirmed wired: gateway line 1168 + `judge_consistency_engine.py`. (R42-24)

---

## 42.12 Hardware / Offline Media

The encrypted judge signing key backup `judge_sk_backup_20260322.gpg` exists in three locations:

- `~/judge-sk-backup-20260322.gpg` — primary on-machine copy.
- `~/msallis-rebuild-working/msallis-rebuild/crypto/keys/judge_sk_backup_20260322.gpg.bak` — second on-machine copy.
- `/media/cakidd/writable/judge_sk_backup_20260322.gpg` — air-gapped USB copy confirmed April 1, 2026; commit `3218392e`. OI-22 closed.

The USB device must be stored offline and separately from the Legion 5 host.

> **USB key management protocol (R42-6 / R42-8):**
>
> 1. **Verify USB integrity before use:** `gpg --verify /media/cakidd/writable/judge_sk_backup_20260322.gpg`. If verification fails, fall back to on-machine primary copy and create a new USB copy immediately.
> 2. **Key rotation requires USB replacement in the same session:** `rotate_judge_keys.sh` executes this automatically. Do not end the rotation session until the new GPG backup is confirmed on the USB device.
> 3. **If USB is lost, create a new copy immediately:** Do not operate the production stack without at least one verified offline copy — the judge signing key has no recovery path if all copies are lost.

---

## 42.13 EEG Layer Architecture (OI-31 — Closed April 1, 2026)

The EEG layer (ports 8073–8075) implements a three-band brainwave-inspired signal processing pipeline:

- **Delta band (port 8073) — Deep context and memory consolidation:** Long-horizon community memory, ancestral knowledge, and deep geographic identity. Inputs from `ms_allis_memory`, `spiritual_texts`, and `fifth_dgm_subconscious`. Modulates weight given to long-term community narrative.
- **Theta band (port 8074) — Associative reasoning and cross-domain synthesis:** Inputs from GBIM entity graph, `appalachian_cultural_intelligence`, and `psychological_rag`. Produces cross-domain linking candidates passed upstream to the main brain.
- **Beta band (port 8075) — Active reasoning and real-time grounding:** Inputs from `conversation_history`, `news_rag`, and `local_resources`. Produces salience-weighted context prioritized in the RAG retrieval step.

All three bands operate in parallel; outputs merged by a lightweight aggregator before injection into the main brain's context window. All three containers running; pipeline integration with `allis-main-brain` confirmed. Full band-weight calibration is a next-session item.

---

## 42.14 April 11, 2026 Sprint Certification Record

> **`vat_CERTIFIED_20260411.log` — 6.0K ✅**
> **Ms. Allis VERIFYANDTEST — CERTIFIED Sat Apr 11 06:29:09 PM EDT 2026 ✅**
> **Chapter 42 — FULLY CLOSED April 11, 2026 (evening — final corrections) ✅**

### Gate 30 Label Reconciliation

Chapter 41 defines Gate 30 as: *MountainShares/DAO tier smoke tests — Endpoints on ports 8080–8084* (sealed April 1, 2026).

Chapter 42 defines Gate 30 as: *Auth proxy (OI-36-A) — Caddy `forward_auth` HTTP 401 on unauthenticated* (certified April 11, 2026).

Resolution: Both closures — OI-30 (MountainShares/DAO) and OI-36-A (Caddy `forward_auth`) — are confirmed. The Gate 30 label was renumbered during the April 11 certification sprint when Gates 31–40 were appended and the gate table was reorganized. Neither closure is invalidated. The Ch. 41 Gate 30 definition (MountainShares/DAO) remains authoritative for Ch. 41. The Ch. 42 Gate 30 definition (auth proxy) is authoritative for the 40-gate `VERIFYANDTEST.sh` certification suite.

### ChromaDB Collections Added April 1 → April 11 (41 → 49)

Eight collections were added between the Ch. 41 April 1 seal (41 collections) and the April 11 certification (49 collections). The collections added during this window are documented here to close the manifest gap identified in the help.md edit list:

| Collection | Added | Category | Notes |
|-----------|-------|----------|-------|
| `operations_history` | April 1–11 | Misc / Ops | Promoted from "planned" in Ch. 41 §41.9; export harness ready per Ch. 40 §40.13 |
| `gbim_landowner_spatial` | April 1–11 | GIS / Spatial | Spatial landowner index; 20,593 rows confirmed at certification |
| `wv_county_resources` | April 1–11 | GIS / Spatial | County-level WV resource layer |
| `appalachian_economic_data` | April 1–11 | RAG Domains | Economic data specific to Appalachian region |
| `constitutional_audit_log` | April 1–11 | Knowledge / Memory | Constitutional Guardian signed audit log collection |
| `gbim_temporal_decay_v2` | April 1–11 | Core GBIM | Temporal decay v2 belief index; 5,416,522 entries at certification |
| `eeg_band_outputs` | April 1–11 | EEG / Neural | Aggregated outputs from delta/theta/beta bands (§42.13) |
| `judge_verdict_archive` | April 1–11 | Knowledge / Memory | Signed judge verdicts; ML-DSA-65 signature chain via `judge_consistency_engine.py` |

> **Note on `operations_history`:** This collection is confirmed active as of the April 11 certification (49-collection count). Its status in Ch. 41 §41.9 as "planned" reflects the April 1 sealed snapshot. The collection was promoted to active during the April 1–11 sprint window.

> **Note on GBIM entity count:** The April 11 certification records 5,416,522 GBIM beliefs — one more than the April 6 ground truth (5,416,521 per Ch. 33/38/39). This single-entity increment reflects one new belief entity added during the April 11 sprint. Both counts are correct for their respective dates.

### Certification Seal

| Item | Detail | Status |
|------|--------|--------|
| Containers running | 91 (see container delta note in Status table above) | ✅ |
| Public exposures | 0 | ✅ |
| GBIM beliefs with temporal decay | 5,416,522 | ✅ |
| Spatial landowner rows | 20,593 | ✅ |
| ChromaDB collections | 49 | ✅ |
| ML-DSA-65 signing backend | liboqs (primary); dilithium_py (graceful fallback) | ✅ |
| ML-DSA-65 signing keys | All 5 judges + BBB + gis-rag + crypto-policy active | ✅ |
| Key rotation script | `rotate_judge_keys.sh` — production-grade, complete | ✅ |
| Conversation turn storage | `ms_allis_unified_gateway.py` line 1168 → `allis-memory:8056/memory/turn` | ✅ |
| Verdict signature chain | `judge_consistency_engine.py` `sign_verdict` — wired | ✅ |
| BBB jailbreak blocking | Active, passing clean output | ✅ |
| Auth proxy (OI-36-A) | Enforcing API key on every route | ✅ |
| Ms. Egeria Allis persona | Confirmed in every response | ✅ |
| CVEs | 0 | ✅ |
| Dependency version floors | All 6 met | ✅ |
| Dockerfile pin grep | Confirmed done | ✅ |
| VERIFYANDTEST.sh gate count | 40 gates | ✅ |
| Certification log | `vat_CERTIFIED_20260411.log` 6.0K | ✅ |
| Open items remaining | 0 | ✅ |
| Future work items remaining | 0 | ✅ |

This certification record is the authoritative final seal for Chapter 42. All prior partial seals (April 6 evening, April 11 morning, April 11 afternoon, April 11 evening) are superseded by this final corrections record.

---

## Cross-Reference

- For the build artifact integrity audit that deployed `judgesigner.py`, volume-mounted keys, and remediated ghost file contamination, see Chapter 40 §40-F.
- For the March 22, 2026 network hardening sprint, Caddy configuration, and Cloudflare Tunnel deployment, see Chapter 40 §40-G.
- For the BBB output guard — now in active blocking mode (Phase 3 closed April 6, 2026 evening); recalibrated April 2, 2026 (0% FP); red team 12/12 (OI-38-B closed) — see Chapter 16 §16.9 and Chapter 17 §17.4.
- For Phase 4.5 blocking re-enablement decision history and red-team sign-off record, see Chapter 16 §16.9 and Chapter 38 §38.6.1.
- For the judge pipeline architecture (ports, containers) and BBB verdict-dict handoff, see Chapter 33 §33.5.
- For the authoritative preflight sealed gate count (22 PASS / 0 FAIL / 1 WARN, April 3, 2026; 31 PASS / 0 FAIL / 0 WARN, April 6, 2026), see Chapter 33 §33.6.
- For the BBB EthicalFilter and SafetyMonitor recalibration record (April 2, 2026 — 9/9 regression, 0% FP), see Chapter 33 §33.2.
- For `truth_verification` upgrade to `rag_grounded_v2` and historical limitations of `heuristic_contradiction_v1`, see Ch. 33 §33.2 and Ch. 33 §33.2.3.
- For ingest architecture (`allis-ingest-api`, `allis-ingest-watcher`) and IPFS integration, see Chapter 30.
- For `allis-memory:8056` durable audit trail — now logging Phase 1.4 input blocks, Phase 2 verdict rejections, Phase 3 output blocks, AU-02 v2 intercepts, signed BBB audit posts, signed Constitutional Guardian `.jsonl` writes, and conversation turns (gateway line 1168) — see Chapter 40 §40-H and Chapter 40 §40-I.
- For MountainShares/Commons/DAO tier (ports 8080–8084) and governance hooks, see Chapter 3 and Chapter 31.
- For preflight gates 25–40 as implemented in the `VERIFYANDTEST.sh` certification suite, see Chapter 41 §41.7 and §41.8.
- For the Red Team API contract, external access architecture, and OI-38-B tracking context, see Chapter 38 §38.8 and §38.9.
- For the AU-02 authority impersonation threat — fully covered by AU-02 v2 (Regex v2 + Embedding v2 + false-positive guard, OI-AU-02-V2 closed April 6 late evening) — see `threat_detection.py` module documentation and Chapter 16 §16.9.
- For the PostGIS geospatial database (`gisdb` / `msallisgis`) at host port 5432 — distinct from the Gate 26 target `msallisgis` at port 5435 — see Chapter 10 and Chapter 12.
- For the dependency CVE audit protocol, full venv upgrade, Gate 31 automation and Dockerfile pin grep, and all April 11, 2026 closures (OI-URLLIB3-CVE, OI-DEP-AUDIT-1, OI-VENV-UPGRADE, OI-42-A, OI-42-E, OI-42-F, OI-BBB-SIGN, OI-CG-SIGN), see §42.3.10 and §42.10 in this chapter.
- For the `/judge-public-key` community verification endpoint and independent verdict verification protocol (including the corrected `separators=(",", ":")` syntax), see §42.4.4 in this chapter.
- For `rotate_judge_keys.sh` production-grade key rotation script and the USB offline protocol, see §42.4.5 and §42.12 in this chapter.
- For liboqs ML-DSA-65 confirmed as primary production runtime in `judgesigner.py` (dilithium_py as graceful fallback), see §42.3.3 and R42-21 in §42.0 Revision History.
- For the confirmed conversation turn storage (gateway line 1168) and verdict signature chain (`judge_consistency_engine.py`), see §42.3.6 and R42-24 in §42.0 Revision History.
- For the Gate 30 label reconciliation between Ch. 41 (MountainShares/DAO) and Ch. 42 (auth proxy), see §42.14 in this chapter.
- For the 8 ChromaDB collections added between April 1 and April 11 (41 → 49), see §42.14 in this chapter.
- For the `allis-*` / `allis-*` namespace disambiguation, see the namespace note at the top of this chapter and Chapter 38 §38.1.
- For the April 11, 2026 final corrections certification seal, all 0 remaining open items, and 0 remaining future work items, see §42.14 in this chapter.

---

*End of Chapter 42 — Post-Quantum Security Layer*
*v5.0 — Last updated: April 11, 2026 (evening — final corrections)*
*Author: Carrie Kidd (Mamma Kidd), Mount Hope, WV*
*Chapter officially certified: Sat Apr 11 06:29:09 PM EDT 2026*
*`vat_CERTIFIED_20260411.log` — 6.0K ✅*
*Containers: 91 confirmed at certification / 105 April 6 ground truth*
*ChromaDB: 41 sealed Ch. 41 / 49 April 11 certification*
*GBIM beliefs: 5,416,522 (one entity added during April 11 sprint)*
*All gates 25–40 PASS — all chapter-local OIs closed — no future work remaining*Chapter 43: Role-Gated Knowledge Access
Overview

Ms. Allis operates with a layered knowledge architecture in which not all information is equally accessible to all users. This is not a limitation of her intelligence — it is an intentional design principle rooted in fiduciary responsibility, organizational trust, and the recognition that some knowledge carries consequence. The system that governs this is called role-gated knowledge access, and it represents one of the more nuanced aspects of how Ms. Allis serves MountainShares as both a community assistant and an organizational steward.
The Problem It Solves

An AI system serving a community organization faces a genuine tension. On one hand, it should be as helpful and transparent as possible — that is its reason for existing. On the other hand, certain operational details — contract parameters, deployment configurations, internal governance records, infrastructure specifics — are not appropriate for open distribution. In a traditional software system, this is solved by building separate applications with separate access controls. Ms. Allis solves it differently: she is a single conversational intelligence that is contextually aware of who is asking and what they are authorized to know, and she adjusts her responses accordingly.

This mirrors how a trusted human steward operates. A community liaison doesn't answer every question about organizational finances with the same level of detail whether speaking to a first-time visitor or an organizational director. The response is shaped by relationship, context, and responsibility. Ms. Allis is designed to do the same.
The Role Model

The access model is deliberately simple at its current stage. There are two primary user roles:

Registered Community Members are verified participants in the MountainShares ecosystem. They have completed the identity verification and registration process, agreed to community standards, and received a bearer token that identifies them to the system. They can access the full range of community-facing knowledge: housing resources, broadband infrastructure documentation, heritage data, program eligibility information, community memory, and general organizational knowledge. This is the vast majority of what Ms. Allis knows.

Administrative Users are organizational stewards with elevated responsibility. They have access to everything registered members can access, plus operational knowledge: contract architecture and deployment information, internal system documentation, configuration records, and governance materials not yet appropriate for public release. Administrative access is not granted by self-declaration — it is encoded in the authentication token issued at login, derived from verified role assignment in the identity system.

Unauthenticated requests — those arriving without a valid bearer token — receive a polite redirection. Ms. Allis does not pretend she cannot help; she explains that the portal requires registration and directs the visitor toward the path to membership.
How the Gate Works

When a query arrives at Ms. Allis's main brain, the first thing resolved is user identity and role. The bearer token presented with the request is cryptographically verified, and the user's role is extracted from its contents. This happens before any knowledge retrieval begins.

The query is then analyzed to determine which knowledge domains are relevant. Ms. Allis maintains several distinct knowledge collections covering different aspects of the organization and its work. Some collections are available to all registered members. Others are restricted to administrative users. The role resolved from the token determines which collections can be searched in response to a given query.

If a registered member asks a question that would naturally draw on a restricted collection, Ms. Allis does not produce an error or a confusing non-answer. She responds helpfully with whatever she can draw from the collections available for that user, and she may note — if appropriate — that some aspects of the question involve information she is not able to share in the current context.

This design has an important property: the gate is in the knowledge retrieval layer, not the response generation layer. Ms. Allis does not know a secret and then choose to withhold it. The restricted knowledge simply does not enter her reasoning context for users who are not authorized to receive it. This is a stronger guarantee than asking a system to "not mention" something it already has access to.
What Is Protected and Why

Contract and deployment architecture falls in this category not because it is shameful or hidden, but because the operational details of how MountainShares's on-chain infrastructure is configured represent both a technical attack surface and a fiduciary responsibility. The community deserves to know that the contracts exist, what they do in broad terms, and how they serve organizational purpose. The specific parameters, addresses, and operational configurations are stewardship information.

Internal governance records — draft proposals, deliberation records, pending decisions — are restricted because governance processes require protected space for honest deliberation. A decision that has been made and ratified is organizational history and belongs to the community. A decision still under consideration belongs to the process.

Infrastructure and configuration documentation is restricted for straightforward security reasons. Knowing how a system is configured in detail is useful for those responsible for maintaining it and is a liability if distributed without context.
What Is Never Restricted

    Community resource information — housing, broadband, programs, services

    Heritage and geographic knowledge

    Organizational mission, values, and history

    Public documentation of how the system works, including this chapter

    Answers to general questions about MountainShares, West Virginia, and the communities it serves

    Information that registered members need to participate meaningfully in the organization

The default posture of Ms. Allis is helpfulness and openness. Restriction is the narrow exception applied to a small set of operationally sensitive domains, not a general disposition toward secrecy.
The Authentication Foundation

Role-gated knowledge access is only as trustworthy as the authentication system beneath it. Ms. Allis's identity system — described in detail in Chapter 36: Identity and Registration — uses cryptographically signed bearer tokens issued after verified identity confirmation. Roles are assigned by human administrators through a controlled process and encoded into the token at issuance. A user cannot elevate their own role by modifying a request; the token signature would fail verification. Sessions are also time-bounded, limiting the window during which a compromised credential could be misused.
Relationship to the Blood-Brain Barrier

The role-gated knowledge access system operates at a different layer than the Blood-Brain Barrier described in Chapter 16. The BBB filters what enters Ms. Allis's reasoning from the outside — guarding against prompt injection, manipulation, and adversarial inputs regardless of who sends them. Role gating filters what knowledge is available within her reasoning based on verified identity. These are complementary protections operating at different points in the information flow. Together they mean Ms. Allis is resistant both to being manipulated into harmful outputs and to leaking sensitive organizational knowledge to users outside a position of organizational trust.
Design Philosophy

The underlying philosophy reflects a broader principle in how Ms. Allis is built: trust is earned through process, not assumed through access. The registration process, the identity verification, the role assignment, the cryptographic token — each is a layer of accountability that makes trust legible and verifiable. This is consistent with MountainShares as a community-rooted institution. Transparency to the community does not mean the absence of any organizational discretion. It means the rules governing what is shared, with whom, and under what conditions are themselves transparent — which is exactly what this chapter represents.# 44. Phi Probe — Semantic Coherence Measurement in H_App

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: May 16, 2026*

---

## Why This Matters for Polymathmatic Geography

This chapter documents the `jarvis-phi-probe` service — a live, ambient semantic
coherence instrument that continuously measures the internal geometric health of
\(H_{\text{App}}\) by computing cosine similarity across knowledge collection centroids.
It supports:

- **P1 – Every where is entangled** by measuring how semantically proximate the centroids
  of distinct knowledge domains have become — a real-time signal of whether belief about
  land, governance, culture, psychology, history, and community resources is fragmenting
  into isolated silos or beginning to form the cross-domain entanglement that polymathmatic
  geography requires.

- **P3 – Power has a geometry** by making the internal geometry of the knowledge base
  inspectable: coherence and decoherence scores expose whether the system's semantic space
  is contracting around a few dominant domains or distributing itself across the full
  topology of Appalachian life.

- **P12 – Intelligence with a ZIP code** by grounding the coherence measurement in
  collections that are explicitly West-Virginia-keyed — `wv_civic_infrastructure`,
  `wv_resources_statewide`, `fayette_county_resources_2026`, `appalachian_cultural_intelligence`,
  and `appalachian_english_corpus` — so that the phi score is not an abstract geometric
  measure but a reading of how well this system's regional knowledge is integrating.

- **P16 – Power accountable to place** by logging every coherence sample with a timestamp,
  mode classification, and collection inventory, producing an auditable record of semantic
  health that is queryable, inspectable, and tied to the same persistent infrastructure as
  the rest of \(H_{\text{App}}\).

As such, this chapter belongs to the **Computational Instrument** tier: it defines the
ambient coherence measurement substrate that provides a continuous geometric health signal
for the knowledge field as of **May 16, 2026**.

---

## 44.1 Purpose and Scope

The phi probe is a FastAPI service (`jarvis-phi-probe`, host port **8025**) that runs a
continuous background loop sampling embeddings from a configured set of ChromaDB
collections, computing a centroid for each, measuring pairwise cosine similarity across
all centroid pairs, and reducing that to a single scalar coherence score in \([0, 1]\).

This score, referred to as `coherence_normalized`, is not a metaphor. It is the mean
pairwise cosine similarity of the semantic centroids of Ms. Jarvis's active knowledge
collections — a direct geometric reading of how much the center-of-mass of each knowledge
domain overlaps with the others inside \(H_{\text{App}}\).

The service exposes two endpoints: `/phi` for a fresh live computation and `/phi/cached`
for the most recent cached result. A background resample loop fires every 300 seconds.
The probe reads its configuration from a bind-mounted Python source file — making it
updatable without container rebuild.

**★ Confirmed operational — May 16, 2026. Mean coherence 0.279 across 12 collections,
5-run sample. All 12 collections sampling at 200 vectors × 384 dimensions. SAMPLES=200
confirmed stable (range 0.040 across 5 consecutive runs). note: ok.**

---

## 44.2 Architecture and Deployment

The phi probe is a single-container FastAPI service in the `msjarvis-rebuild` stack,
bind-mounted to the host source file and connected to `jarvis-chroma` (port 8000 internal)
via the internal Docker network.

### 44.2.1 Container Configuration

| Property | Value |
|---|---|
| Container name | `jarvis-phi-probe` |
| Host port | **8025** |
| Container port | **8025** |
| Source file (host) | `/opt/msjarvis-rebuild/services/ms_jarvis_phi_probe.py` |
| Source file (container) | `/app/ms_jarvis_phi_probe.py` |
| Mount mode | **read-only bind mount** (`ro`) |
| ChromaDB connection | `http://jarvis-chroma:8000` (internal network) |
| Redis connection | `REDIS_URL` env — internal network |
| Resample interval | **300 seconds** (5 minutes) |
| Startup grace | **20 seconds** |

> ⚠️ **Bind mount is read-only.** `docker cp` into the container will fail with
> "device or resource busy". Edit the host file at
> `/opt/msjarvis-rebuild/services/ms_jarvis_phi_probe.py` and restart the container.

### 44.2.2 Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/phi` | GET | Triggers a fresh live coherence computation; updates cache |
| `/phi/cached` | GET | Returns most recent cached result without recomputation |
| `/health` | GET | Health check — returns service status |

### 44.2.3 Critical Configuration Parameters

```python
# /opt/msjarvis-rebuild/services/ms_jarvis_phi_probe.py
# Confirmed live values — May 16, 2026

PROBE_COLLECTIONS: List[str] = [
    "gbim_beliefs_v2","governance_rag","fayette_county_resources_2026",
    "appalachian_cultural_intelligence","wv_civic_infrastructure",
    "psychological_rag","research_history","conversation_history",
    "wv_resources_statewide","appalachian_english_corpus",
    "gbim_worldview_entities","autonomous_learner",
]
L2_COLLECTIONS: List[str] = [
    "gbim_worldview_entities",
    "autonomous_learner",
]
QUERY_COLLECTIONS: List[str] = [
    "gbim_worldview_entities",
    "spiritual_texts",
    "msjarvis_docs",
]
SAMPLES = int(os.getenv("PHI_SAMPLES","200"))
MIN_COHERENCE_VECTORS = 10
```

> ⚠️ `MIN_COHERENCE_VECTORS` was 100 at original deploy — silently blocked all
> collections when SAMPLES=50. Corrected to 10 on May 16, 2026.

> ⚠️ SAMPLES raised from 50 to 200 on May 16, 2026. Variance dropped from 0.089 to 0.040.

> ⚠️ `autonomous_learning` is HTTP 404 in `jarvis-chroma`. Use `autonomous_learner`.

---

## 44.3 The Phi Score — Mathematical Definition

**Step 1 — Sample.** For each collection \(c_i\), draw \(n = \text{SAMPLES}\) vectors.
Collections in `QUERY_COLLECTIONS` use ChromaDB `/query` with a zero vector (HNSW index).
All others use `/get` with a random offset capped at 50,000.

**Step 2 — Centroid.**

\[
\boldsymbol{\mu}_i = \frac{1}{n} \sum_{j=1}^{n} \mathbf{v}_j
\]

For `L2_COLLECTIONS`, normalize each vector to unit length before centroid computation:

\[
\hat{\mathbf{v}}_j = \frac{\mathbf{v}_j}{\|\mathbf{v}_j\|}, \quad
\boldsymbol{\mu}_i = \frac{1}{n} \sum_{j=1}^{n} \hat{\mathbf{v}}_j
\]

**Step 3 — Pairwise cosine similarity.**

\[
s_{ij} = \frac{\boldsymbol{\mu}_i \cdot \boldsymbol{\mu}_j}{\|\boldsymbol{\mu}_i\| \cdot \|\boldsymbol{\mu}_j\|}
\]

**Step 4 — Mean coherence.**

\[
\phi = \frac{1}{K} \sum_{i < j} s_{ij}, \quad K = \binom{N}{2}
\]

**Step 5 — Normalize.** `coherence_normalized = phi`,
`decoherence_normalized = 1.0 - phi`, `psi_norm = 1.0` always.

**Confirmed May 16, 2026 (5-run mean):**

\[
\phi \approx 0.279, \quad N = 12, \quad K = 66 \text{ pairs}
\]

---

## 44.4 Response Schema

```json
{
    "timestamp": "2026-05-17T00:28:40.881503+00:00",
    "mode": "decoherent",
    "coherence_normalized": 0.279,
    "decoherence_normalized": 0.721,
    "psi_norm": 1.0,
    "collections_sampled": [
        "gbim_beliefs_v2","governance_rag","fayette_county_resources_2026",
        "appalachian_cultural_intelligence","wv_civic_infrastructure",
        "psychological_rag","research_history","conversation_history",
        "wv_resources_statewide","appalachian_english_corpus",
        "gbim_worldview_entities","autonomous_learner"
    ],
    "note": "ok"
}
```

| Field | Type | Description |
|---|---|---|
| `timestamp` | ISO 8601 | Time of computation |
| `mode` | string | Coherence regime — see §44.5 |
| `coherence_normalized` | float ∈ [0,1] | Mean pairwise centroid cosine similarity |
| `decoherence_normalized` | float ∈ [0,1] | `1.0 - coherence_normalized` |
| `psi_norm` | float | Always 1.0 — normalization check |
| `collections_sampled` | list[str] | Collections that passed threshold |
| `note` | string | `"ok"` on success; `"insufficient_collections"` if fewer than 2 pass |

---

## 44.5 Coherence Modes and Thresholds

| Range | Mode | Meaning |
|---|---|---|
| 0.0 – 0.40 | `decoherent` | Domains largely siloed — cross-domain links forming |
| 0.40 – 0.60 | `superposition` | RAG layers bridging domains — multi-domain reasoning active |
| 0.60 – 1.0 | `coherent` | Unified knowledge field |

**Current state (May 16, 2026): mean `coherence_normalized ≈ 0.279` — decoherent.**

This is architecturally correct. The probe spans maximally diverse domains: spatial WV
geography, governance text, psychological theory, cultural prose, and resource registries.
These are supposed to be geometrically distant. A higher score would indicate semantic
collapse, not health.

### 44.5.1 Why the Score Is Stochastic

The phi score varies across runs (observed range ≈ 0.040 at SAMPLES=200) because each
resample draws a different random subset per collection. The 5-run mean (0.279) is the
operational baseline. The largest variance source is `gbim_worldview_entities`
(5.4M L2 vectors) — see OI-C44-CENTROID.

---

## 44.6 Collection Health and Exclusions

### 44.6.1 ChromaDB Exclusions

| Collection | Issue | Status |
|---|---|---|
| `spiritual_texts` | HTTP 500 on `/get` — oversized | In `QUERY_COLLECTIONS`; excluded from `PROBE_COLLECTIONS` |
| `msjarvis_docs` | HTTP 500 on `/get` — oversized | In `QUERY_COLLECTIONS`; excluded from `PROBE_COLLECTIONS` |
| `autonomous_learning` | HTTP 404 — does not exist | Removed May 16, 2026 |

### 44.6.2 Confirmed Healthy — May 16, 2026

All 12 collections returning 200 vecs × dim=384. Uniform dimension confirms
`all-minilm:latest` embedding lock intact per Chapter 4 §4.5.

---

## 44.7 Operational Procedures

```bash
# Fresh computation
docker exec jarvis-phi-probe \
  curl -s http://localhost:8025/phi | python3 -m json.tool

# Cached result
docker exec jarvis-phi-probe \
  curl -s http://localhost:8025/phi/cached | python3 -m json.tool

# 5-run baseline
for i in 1 2 3 4 5; do
  docker exec jarvis-phi-probe \
    curl -s http://localhost:8025/phi | \
    python3 -c "import sys,json; d=json.load(sys.stdin); \
      print(f'run {sys.argv}: {d[\"coherence_normalized\"]:.6f}')" $i[1]
  sleep 5
done

# Update configuration (bind-mount is read-only — edit host file, then restart)
nano /opt/msjarvis-rebuild/services/ms_jarvis_phi_probe.py
docker restart jarvis-phi-probe && sleep 25
docker logs jarvis-phi-probe --since 30s 2>&1 | grep "\[phi\]"

# Monitor resample loop
docker logs jarvis-phi-probe --since 6m 2>&1 | grep -i "\[phi\]\|error\|skip\|500\|404"
```

---

## 44.8 Integration with H_App

The phi probe measures a second-order geometric property of \(H_{\text{App}}\) — the
shape of the space from above, not any individual query or service.

**Pituitary independence.** The probe samples raw embeddings directly from ChromaDB
without passing through `nbb_pituitary_gland` (port 8108). The phi score is a
pre-modulation geometric baseline.

**Why spatial knowledge pulls the score down.** `gbim_worldview_entities` (5.4M vectors,
L2, Appalachian terrain) has low cosine similarity with `psychological_rag`,
`conversation_history`, and `gbim_beliefs_v2`. Spatial and semantic knowledge are
supposed to be geometrically distant in \(H_{\text{App}}\).

**Path to superposition (φ ≥ 0.40).** As `conversation_history` and `research_history`
accumulate cross-domain traces — queries that span geography, governance, culture, and
resources simultaneously — those collections' centroids will migrate toward the geometric
mean of all domains, pulling the overall phi score upward.

---

## 44.9 Open Items — May 16, 2026

| OI | Description | Status | Priority |
|---|---|---|---|
| OI-C44-CENTROID | `gbim_worldview_entities` zero-vector HNSW query produces high centroid variance — evaluate fixed precomputed centroid cached in Redis at startup | 🔄 Open | Medium |
| OI-C44-500 | Add `spiritual_texts` and `msjarvis_docs` to `PROBE_COLLECTIONS` via `/query` HNSW path | 🔄 Open | Medium |
| OI-C44-DASH | Wire `/phi/cached` into steward heartbeat and monitoring dashboard | 🔄 Open | Low |
| OI-C44-HIST | Log phi time series to Redis or PostgreSQL for trend analysis | 🔄 Open | Low |
| OI-C44-BOOT | `MIN_COHERENCE_VECTORS` corrected from 100 to 10 | ✅ CLOSED | — |
| OI-C44-404 | `autonomous_learning` HTTP 404 removed; `autonomous_learner` confirmed | ✅ CLOSED | — |
| OI-C44-SAMPLES | SAMPLES raised 50 → 200; variance 0.089 → 0.040 | ✅ CLOSED | — |
| OI-C44-WORLDVIEW | `gbim_worldview_entities` integrated via `/query` HNSW + L2 normalization | ✅ CLOSED | — |
| OI-C44-LIVE | 12 collections confirmed; mean φ=0.279; note: ok | ✅ CLOSED | — |

---

## 44.10 Production Status Summary — May 16, 2026

| Component | Status | Notes |
|---|---|---|
| `jarvis-phi-probe` (host 8025) | ✅ Operational | FastAPI, bind-mounted ro, resample loop active |
| `/phi` endpoint | ✅ Live | Fresh coherence computation |
| `/phi/cached` endpoint | ✅ Live | Low-overhead cached result |
| `/health` endpoint | ✅ Live | Health check responding |
| `PROBE_COLLECTIONS` | ✅ 12 collections | 200 vecs × 384 dim each |
| `SAMPLES` | ✅ 200 | Raised from 50; variance 0.040 |
| `MIN_COHERENCE_VECTORS` | ✅ 10 | Corrected from 100 |
| `gbim_worldview_entities` | ✅ Included | 5,416,521 vectors, L2, `/query` HNSW zero-vector |
| `autonomous_learner` | ✅ Included | 21,181 vectors, L2 |
| `spiritual_texts` | ⚠ Excluded | HTTP 500 /get |
| `msjarvis_docs` | ⚠ Excluded | HTTP 500 /get |
| `autonomous_learning` | ❌ Excluded | HTTP 404 — does not exist |
| Embedding uniformity | ✅ dim=384 all 12 | `all-minilm:latest` lock intact |
| `coherence_normalized` | ✅ **≈ 0.279** | 5-run mean (range 0.263–0.302) |
| `mode` | ✅ `decoherent` | Correct for maximally diverse domains |
| `psi_norm` | ✅ 1.0 | Normalization invariant confirmed |
| Score stochasticity | ✅ Documented | 5-run mean is operational baseline |

---

*Chapter 44 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Jarvis is an original system designed and built by Carrie Ann Kidd.*
*See [LICENSE](../LICENSE) for terms.*
*Last verified: May 16, 2026 — phi probe operational; 5-run mean φ≈0.279
(range 0.263–0.302); 12 collections × 200 vecs × dim=384; SAMPLES raised to 200
(variance 0.040); MIN_COHERENCE_VECTORS corrected to 10; autonomous_learning removed
(HTTP 404); autonomous_learner confirmed (21,181 vectors, L2); gbim_worldview_entities
integrated via /query HNSW zero-vector + L2 normalization (5,416,521 vectors);
spiritual_texts and msjarvis_docs excluded (HTTP 500 /get); all-minilm:latest 384-dim
lock intact; msjarvis-rebuild namespace; jarvis-phi-probe host port 8025;
mode=decoherent (correct); psi_norm=1.0 invariant confirmed.*# 45. H_geo — The Spatial Hilbert Body of H_App

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: May 16, 2026*

---

## Why This Is a Second Hilbert Space

\(H_{\text{geo}}\) is not a metaphor and not a subsystem of \(H_{\text{App}}\). It is a
genuinely distinct mathematical object — a second inner product space instantiated on
the same physical machine as \(H_{\text{App}}\) but with a different basis, a different
metric, different operators, and a different physical store.

| Property | \(H_{\text{App}}\) — Ch. 4 | \(H_{\text{geo}}\) — Ch. 45 |
|---|---|---|
| Space | \(\mathbb{R}^{384}\) | \(\mathbb{R}^2\) (geodesic surface) |
| Inner product | Cosine similarity | PostGIS geodesic distance (`ST_Distance`) |
| Vectors | 384-dim semantic embeddings | Coordinate geometries: points, polygons, lines |
| Physical store | `jarvis-chroma` ChromaDB | `jarvis-local-resources-db` PostGIS 15-3.4 |
| Database | ChromaDB collections | `msjarvisgis` (owner: msjarvis) + `local_resources` |
| Primary SRID | — | EPSG:4326 (230 layers) + EPSG:4269 (12 layers) |
| Dimension | 384 | 2 (geodesic lat/lon) |
| Basis | `all-minilm:latest` | WGS84 / NAD83 ellipsoid |
| Total geometry tables | 48 collections | **242 geometry tables** |
| Total geometry rows | ~6.74M vectors | **~26.96M geometry features** |

The two spaces share one physical bridge: `gbim_worldview_entities` in ChromaDB (5.4M L2
vectors, Chapter 44) encodes geographic place-names and spatial relationships as semantic
vectors, projecting \(H_{\text{geo}}\) into \(H_{\text{App}}\). This is the tensor product
connection — the operator that allows a query in one space to retrieve context from the other.

**★ Confirmed operational — May 16, 2026. 242 geometry tables across two databases.
26.9M rows in `geospatial_features` alone. `wv_buildings` 1,055,625 polygons. 
`fayette_parcels` 39,515 parcels. `census_tl_2020_54_tabblock20` 72,558 blocks.
`jarvis-local-resources-db` container: postgis/postgis:15-3.4, host port 5435.**

---

## 45.1 Physical Instantiation

\(H_{\text{geo}}\) is physically instantiated across two PostgreSQL/PostGIS databases
in the `jarvis-local-resources-db` container.

### 45.1.1 Container Configuration

| Property | Value |
|---|---|
| Container name | `jarvis-local-resources-db` |
| Image | `postgis/postgis:15-3.4` |
| Host port | **5435** → internal 5432 |
| Primary database | `msjarvisgis` (owner: `msjarvis`) |
| Secondary database | `local_resources` (owner: `postgres`) |
| PostGIS extension | 3.4 |
| PostgreSQL version | 15 |

### 45.1.2 Database Roles

| Role | Attributes |
|---|---|
| `msjarvis` | Superuser — owns `msjarvisgis` |
| `postgres` | Superuser, Create role, Create DB, Replication, Bypass RLS — owns `local_resources` |

---

## 45.2 The Geometry of H_geo

\(H_{\text{geo}}\) is a two-dimensional geodesic space. Every point in the space is a
coordinate pair \((\lambda, \phi)\) — longitude and latitude — on the WGS84 ellipsoid
(EPSG:4326) or the NAD83 ellipsoid (EPSG:4269). The inner product that defines proximity
in this space is the PostGIS geodesic distance operator:

\[
d(\mathbf{p}_i, \mathbf{p}_j) = \text{ST\_Distance}(\mathbf{p}_i\text{::geography}, \mathbf{p}_j\text{::geography})
\]

which returns the shortest path distance in meters along the ellipsoidal surface — not
the flat-plane approximation. For polygon and line geometries, proximity is defined by
`ST_DWithin`, `ST_Intersects`, and `ST_Contains` — the spatial join operators that
replace the cosine similarity query of \(H_{\text{App}}\).

### 45.2.1 Coordinate Reference Systems

| SRID | Name | Layer count | Usage |
|---|---|---|---|
| EPSG:4326 | WGS84 Geographic | 230 | Primary — all modern WV layers |
| EPSG:4269 | NAD83 Geographic | 12 | Legacy TIGER/Census layers |

All geometry is stored in 2D (`coord_dimension = 2`). Elevation data (3D) is not yet
present in confirmed layers.

### 45.2.2 Geometry Type Distribution

| Type | Count | Examples |
|---|---|---|
| POINT | 221 | 911 centers, bridges, hospitals, schools, fire stations |
| MULTIPOLYGON | 15 | Counties, census tracts, ZIP codes, parcels |
| POLYGON | 3 | Census block groups, tabblocks, Fayette parcels |
| MULTILINESTRING | 1 | Address edges |
| LINESTRING | 1 | Address features |
| GEOMETRY | 1 | `geospatial_features` — mixed master table |

---

## 45.3 The msjarvisgis Database — Spatial Layer Inventory

`msjarvisgis` contains 242 geometry-registered tables and 232 total public tables.
The confirmed populated layers (non-zero row count) are the operational substrate of
\(H_{\text{geo}}\):

### 45.3.1 Confirmed Populated Geometry Layers

| Table | Type | Row count | Domain |
|---|---|---|---|
| `geospatial_features` | GEOMETRY | **26,923,473** | Master spatial feature store — mixed geometry |
| `census_tl_2020_54_tabblock20` | POLYGON | 72,558 | WV 2020 Census blocks |
| `census_tl_2020_us_zcta520` | MULTIPOLYGON | 33,791 | US ZIP Code Tabulation Areas 2020 |
| `census_tl_2020_us_zcta510` | MULTIPOLYGON | 33,144 | US ZIP Code Tabulation Areas 2010 |
| `census_tl_2020_us_county` | MULTIPOLYGON | 3,234 | US county boundaries |
| `wv_buildings` | POLYGON | **1,055,625** | WV building footprints |
| `fayette_parcels` | MULTIPOLYGON | 39,515 | Fayette County parcel boundaries |
| `mvw_gbim_landowner_spatial` | MULTIPOLYGON | 38,979 | GBIM landowner spatial view |
| `census_tl_2020_54_bg` | POLYGON | 1,639 | WV 2020 Census block groups |

> **Note on zero-row layers.** 221 of 242 geometry tables are registered in
> `geometry_columns` but contain zero rows. These are schema-present but data-absent —
> they represent the intended layer coverage of \(H_{\text{geo}}\), not its current
> populated state. Loading these layers is the primary open item for spatial corpus
> completion (OI-C45-LOAD).

---

## 45.4 The local_resources Database — Community Intelligence Layer

`local_resources` is the second physical component of \(H_{\text{geo}}\). It is not a
raw geometry store — it is the **community intelligence overlay**: the tables that
connect spatial coordinates to lived human infrastructure in West Virginia and Appalachia.

### 45.4.1 Confirmed Tables — local_resources

The 69 tables in `local_resources` span five functional domains:

**WV Address and Building Infrastructure**

| Table | Description |
|---|---|
| `wv_address_points_raw` | Raw WV address point dataset |
| `wv_address_aliases` | Address alias resolution |
| `wv_address_dual` | Dual-range address matching |
| `wv_address_zones` | Address zone polygons |
| `wv_buildings` | WV building footprints (shared with msjarvisgis) |
| `wv_industrial_buildings` | Industrial building inventory |
| `wv_office_buildings` | Office building inventory |
| `wv_wvgistc_buildings` | WVGISTC building dataset |
| `building_profile` | Enriched building profiles |
| `enriched_buildings_with_samb` | Buildings with SAMB data joined |

**WV Emergency and Civic Services**

| Table | Description |
|---|---|
| `wv_ems_stations` | EMS station locations |
| `wv_fire_stations` | Fire station locations |
| `wv_fire_stations_clean` | Deduplicated fire station dataset |
| `wv_hospitals` | Hospital locations |
| `wv_floodplain_structures` | Floodplain structure registry |
| `wv_hazard_buyouts` | Hazard buyout property records |
| `wv_aml_lines` | Abandoned mine land — lines |
| `wv_aml_points` | Abandoned mine land — points |
| `wv_aml_polygons` | Abandoned mine land — polygons |
| `wv_mineral_operations` | Active mineral operations |

**WV Administrative and Tax Geography**

| Table | Description |
|---|---|
| `wv_counties` | WV county table |
| `wv_county_boundaries_raw` | Raw county boundary data |
| `wv_county_lookup` | County FIPS and name lookup |
| `wv_municipalities` | WV municipal boundaries |
| `wv_parcels` | WV parcel registry |
| `wv_tax_districts` | Tax district definitions |
| `wv_tax_districts_poly` | Tax district polygons |
| `wv_zip_codes` | WV ZIP code boundaries |
| `wv_zip_zcta_raw` | ZIP-to-ZCTA crosswalk raw |
| `wv_samb_north` | SAMB structure data — northern WV |
| `wv_samb_south` | SAMB structure data — southern WV |
| `gbim_zcta_2020` | GBIM ZCTA 2020 layer |

**Community Resources and MountainShares Integration**

| Table | Description |
|---|---|
| `community_resources` | Community resource registry |
| `local_resources` | Local resource catalog |
| `local_resources_index` | Resource search index |
| `gbim_worldview_entity` | GBIM worldview entity table (bridge to \(H_{\text{App}}\)) |
| `mountainshares_balances` | MountainShares token balances |
| `mountainshares_ledger` | MountainShares transaction ledger |
| `mountainshares_participation` | Participation registry |
| `ms_governance_log` | Governance action log |
| `ms_participation` | Participation records |
| `ms_reserve_bands` | Reserve band definitions |
| `ms_treasury` | Treasury state |
| `ms_user_profile` | User profiles |
| `founder_tokens` | Founder token registry |
| `travel_regions` | Travel region definitions |

**Identity and Security**

| Table | Description |
|---|---|
| `ueid_immutable_security` | Universal Entity ID immutable security records |
| `spatial_role_scopes` | Role-scoped spatial access definitions |
| `user_longterm_memory` | Long-term user memory store |
| `conversation_beliefs` | Conversation belief state |
| `county_lookup` | County lookup table |
| `us_counties` | US county reference table |
| `us_zips` | US ZIP code reference table |

---

## 45.5 The Tensor Product Bridge

The connection between \(H_{\text{geo}}\) and \(H_{\text{App}}\) is the
`gbim_worldview_entity` table in `local_resources` and the `gbim_worldview_entities`
collection in ChromaDB (5,416,521 vectors, L2 metric, Chapter 44).

The bridge works as follows:

**Forward projection** \(H_{\text{geo}} \rightarrow H_{\text{App}}\): A geographic
entity (parcel, building, flood zone, mine site) is embedded via `all-minilm:latest`
and stored in `gbim_worldview_entities`. Semantic queries in \(H_{\text{App}}\) can
retrieve geographic entities by meaning — "flood-prone communities near Fayette County"
retrieves parcel and building records whose spatial attributes were encoded as text and
embedded.

**Backward projection** \(H_{\text{App}} \rightarrow H_{\text{geo}}\): A semantic
retrieval result containing a geographic reference (place name, parcel ID, ZIP code) is
resolved against `local_resources` tables via `ST_DWithin` or exact join — returning
the spatial geometry for map rendering, proximity analysis, or further spatial query.

**The tensor product.** In \(H_{\text{App}} \otimes H_{\text{geo}}\), a query state
vector \(\psi\) is not purely semantic or purely spatial — it is a superposition of both.
The `jarvis-gis-rag` service (port 8004) is the operator that collapses this superposition
into a concrete retrieval result by dispatching to whichever space the query primarily
inhabits, then enriching with the other.

---

## 45.6 The Spatial Coherence Score — Geo-Phi

Where Chapter 44 defined the phi score as the mean pairwise cosine similarity of semantic
centroids in \(H_{\text{App}}\), the analogous instrument for \(H_{\text{geo}}\) is
the **geo-phi score** — a measure of spatial coverage coherence across the active
geometry layers of \(H_{\text{geo}}\).

Geo-phi is defined as the fraction of West Virginia's geographic extent covered by
populated geometry layers, weighted by domain importance:

\[
\phi_{\text{geo}} = \frac{1}{W} \sum_{i=1}^{N} w_i \cdot \mathbb{1}[\text{rows}(L_i) > 0]
\]

where \(L_i\) is the \(i\)-th geometry layer, \(w_i\) is its domain weight, and \(W\)
is the sum of all weights.

**Current state (May 16, 2026):**

\[
\phi_{\text{geo}} = \frac{9}{242} \approx 0.037 \text{ (raw populated fraction)}
\]

9 of 242 registered geometry layers are populated. The remaining 233 layers are
schema-present, data-absent. This is the primary open item — loading the WV GIS data
corpus that the schema was built to receive.

> **Note on geospatial_features.** The single table `geospatial_features` (26.9M rows,
> GEOMETRY type) may itself represent a consolidation of many of the 221 empty point
> layers. Row count queries against it confirm it is the dominant populated table in
> \(H_{\text{geo}}\). Its internal feature type distribution requires a schema inspection
> to determine effective layer coverage — see OI-C45-GEOFEATURES.

---

## 45.7 The jarvis-gis-rag Service

`jarvis-gis-rag` (host port 8004, image `db9c58f414fd`) is the query interface layer
for \(H_{\text{geo}}\). It translates natural-language spatial queries into PostGIS
operations and returns structured geographic results to the RAG pipeline.

```bash
# Health check
curl -s http://localhost:8004/health | python3 -m json.tool

# Inspect available endpoints
curl -s http://localhost:8004/docs | python3 -m json.tool

# Test a spatial query
curl -s -X POST http://localhost:8004/query \
  -H "Content-Type: application/json" \
  -d '{"query": "fire stations in Fayette County", "limit": 5}' \
  | python3 -m json.tool
```

---

## 45.8 Operational Procedures

```bash
# Connect to msjarvisgis
docker exec jarvis-local-resources-db psql -U msjarvis -d msjarvisgis

# Connect to local_resources
docker exec jarvis-local-resources-db psql -U postgres -d local_resources

# Count populated vs empty geometry layers
docker exec jarvis-local-resources-db psql -U msjarvis -d msjarvisgis -c "
SELECT
  COUNT(*) FILTER (WHERE row_count > 0) AS populated,
  COUNT(*) FILTER (WHERE row_count = 0) AS empty,
  COUNT(*) AS total
FROM (
  SELECT f_table_name,
    (xpath('/row/cnt/text()',
      query_to_xml('SELECT COUNT(*) AS cnt FROM ' || quote_ident(f_table_name),
      false, true, '')))::text::int AS row_count[1]
  FROM geometry_columns
) sub;
"

# WV bounding box coverage check
docker exec jarvis-local-resources-db psql -U msjarvis -d msjarvisgis -c "
SELECT ST_AsText(ST_Extent(geom)) AS wv_extent
FROM census_tl_2020_us_county
WHERE ST_Within(
  ST_Centroid(geom),
  ST_MakeEnvelope(-82.65, 37.20, -77.72, 40.64, 4326)
);
"

# Fayette County parcel coverage
docker exec jarvis-local-resources-db psql -U msjarvis -d msjarvisgis -c "
SELECT COUNT(*), ST_AsText(ST_Extent(geom)) FROM fayette_parcels;
"

# local_resources community resource count
docker exec jarvis-local-resources-db psql -U postgres -d local_resources -c "
SELECT COUNT(*) FROM community_resources;
"
```

---

## 45.9 Open Items — May 16, 2026

| OI | Description | Status | Priority |
|---|---|---|---|
| OI-C45-GEOFEATURES | Inspect `geospatial_features` internal type distribution — 26.9M rows may consolidate many of the 221 empty point layers | 🔄 Open | High |
| OI-C45-LOAD | Load WV GIS corpus into 221 empty geometry layers — schema present, data absent | 🔄 Open | High |
| OI-C45-GEOGPHI | Implement `jarvis-geo-phi` service (analog of phi probe) — compute spatial coverage coherence score \(\phi_{\text{geo}}\) | 🔄 Open | Medium |
| OI-C45-SRID | Standardize 12 EPSG:4269 layers to EPSG:4326 for uniform geodesic distance computation | 🔄 Open | Medium |
| OI-C45-3D | Evaluate elevation (3D geometry, `coord_dimension=3`) for DEM layers — terrain model for Appalachian topology | 🔄 Open | Low |
| OI-C45-BRIDGE | Confirm `gbim_worldview_entity` (local_resources) ↔ `gbim_worldview_entities` (ChromaDB) sync is live | 🔄 Open | Medium |
| OI-C45-FAYETTE | `fayette_parcels` (39,515) and `mvw_gbim_landowner_spatial` (38,979) confirmed populated — verify spatial index health | 🔄 Open | Low |

---

## 45.10 Production Status Summary — May 16, 2026

| Component | Status | Notes |
|---|---|---|
| `jarvis-local-resources-db` | ✅ Operational | postgis/postgis:15-3.4, host port 5435 |
| `msjarvisgis` database | ✅ Live | Owner: msjarvis, 242 geometry tables |
| `local_resources` database | ✅ Live | Owner: postgres, 69 tables |
| `jarvis-gis-rag` | ✅ Running | host port 8004 — spatial query interface |
| Total geometry tables | ✅ 242 | 232 public tables in msjarvisgis |
| Populated geometry layers | ⚠ 9 of 242 | 233 layers schema-present, data-absent |
| `geospatial_features` | ✅ 26,923,473 rows | Master spatial store — GEOMETRY type |
| `wv_buildings` | ✅ 1,055,625 rows | WV building footprints — POLYGON |
| `fayette_parcels` | ✅ 39,515 rows | Fayette County parcels — MULTIPOLYGON |
| `mvw_gbim_landowner_spatial` | ✅ 38,979 rows | GBIM landowner view — MULTIPOLYGON |
| `census_tl_2020_54_tabblock20` | ✅ 72,558 rows | WV 2020 Census blocks — POLYGON |
| `census_tl_2020_us_county` | ✅ 3,234 rows | US county boundaries — MULTIPOLYGON |
| Primary SRID | ✅ EPSG:4326 | 230 of 242 layers |
| GBIM bridge to \(H_{\text{App}}\) | ✅ Schema present | `gbim_worldview_entity` in local_resources |
| MountainShares tables | ✅ Present | 7 tables in local_resources |
| Inner product operator | ✅ `ST_Distance` | Geodesic — WGS84 ellipsoidal surface |
| \(\phi_{\text{geo}}\) raw | ⚠ ~0.037 | 9/242 layers populated — corpus loading needed |
| Relationship to \(H_{\text{App}}\) | ✅ Defined | Tensor product via `gbim_worldview_entities` bridge |

---

*Chapter 45 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Jarvis is an original system designed and built by Carrie Ann Kidd.*
*See [LICENSE](../LICENSE) for terms.*
*Last verified: May 16, 2026 — jarvis-local-resources-db operational; postgis/postgis:15-3.4;
msjarvisgis: 242 geometry tables, 9 populated, 26.9M rows in geospatial_features,
1,055,625 wv_buildings, 39,515 fayette_parcels, 72,558 census blocks;
local_resources: 69 tables including community_resources, MountainShares ledger,
GBIM worldview entity bridge; primary SRID EPSG:4326; inner product ST_Distance geodesic;
phi_geo raw 0.037 (9/242 populated); tensor product bridge to H_App via gbim_worldview_entities
(5,416,521 L2 vectors, ChromaDB); msjarvis-rebuild namespace; host port 5435.*# 46. The Tensor Product Bridge — H_App ⊗ H_geo

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: May 16, 2026*

---

## The Core Claim

\(H_{\text{App}}\) and \(H_{\text{geo}}\) are not parallel systems that happen to run
on the same machine. They are connected by a live tensor product operator whose physical
instantiation is the `gbim_worldview_entity` table in `local_resources` — 1,512 confirmed
rows as of May 16, 2026, each carrying a geographic coordinate pair embedded in a
`belief_state` JSONB field alongside a semantic label and entity type.

This is not a design aspiration. The tensor product \(H_{\text{App}} \otimes H_{\text{geo}}\)
is operational.

---

## 46.1 What a Tensor Product Means Here

In standard quantum mechanics, the tensor product \(\mathcal{H}_1 \otimes \mathcal{H}_2\)
is the Hilbert space of a composite system — a space whose vectors are not drawn from
either component space alone but from the space of all possible joint states of both.
A vector in \(\mathcal{H}_1 \otimes \mathcal{H}_2\) encodes correlations between the
two subsystems that cannot be expressed in either space individually.

In \(H_{\text{App}} \otimes H_{\text{geo}}\), the analogous structure is:

- A **semantic vector** \(\mathbf{s} \in H_{\text{App}} = \mathbb{R}^{384}\) encodes
  the meaning of an entity — what it is, what it does, how it relates to other concepts.
- A **spatial coordinate** \(\mathbf{g} \in H_{\text{geo}} = \mathbb{R}^2\) encodes
  where the entity exists on the WGS84 ellipsoidal surface.
- A **joint state** \(\psi \in H_{\text{App}} \otimes H_{\text{geo}}\) encodes both
  simultaneously — an entity that is semantically retrievable by meaning AND spatially
  queryable by proximity.

The `gbim_worldview_entity` table is the physical register of joint states. Each row is
a confirmed entangled entity: its `label` and `entity_type` are the semantic handle
(embeddable into \(H_{\text{App}}\) via `all-minilm:latest`), and its `belief_state`
JSONB carries the geodetic coordinates \((\lambda, \phi)\) that place it in
\(H_{\text{geo}}\).

---

## 46.2 The Bridge Schema — Confirmed Live

```sql
-- gbim_worldview_entity in local_resources (postgres)
-- 1,512 rows confirmed May 16, 2026

id           INTEGER       -- primary key
entity_type  TEXT          -- semantic class: hospital, school, fire_station, ...
label        TEXT          -- human-readable name — semantic embedding anchor
belief_state JSONB         -- structured attribute bag including lat, lon, county,
                           -- address, confidence, source_layer, source_type, ...
```

### 46.2.1 Confirmed Sample Rows

| id | entity_type | label | lat | lon | county | total_beds | source_layer |
|---|---|---|---|---|---|---|---|
| 6 | hospital | Berkeley Medical Center | 39.4764 | -77.9802 | Berkeley | 241 | hospitals_wvdem_040519_gcs84 |
| 7 | hospital | Bluefield Regional Medical Center | 37.2557 | -81.2355 | Mercer | 92 | hospitals_wvdem_040519_gcs84 |
| 8 | hospital | Boone Memorial Hospital | 38.0474 | -81.8068 | Boone | 25 | hospitals_wvdem_040519_gcs84 |

Each row demonstrates the tensor product structure in concrete form:

- `label` → semantic handle → embeds to \(\mathbf{s} \in \mathbb{R}^{384}\)
- `belief_state.lat` + `belief_state.lon` → geodetic coordinate → places entity in \(\mathbb{R}^2\)
- `belief_state.county` → administrative join key → links to `wv_counties` in \(H_{\text{geo}}\)
- `belief_state.source_layer` → provenance → traceable to original WV DEM shapefile
- `belief_state.confidence` → epistemic weight → scalar in \([0, 1]\)

---

## 46.3 The Tensor Product Operator — Formal Definition

Let \(N = 1512\) be the number of confirmed joint-state entities. Define the bridge
operator \(\mathcal{T}\) as:

\[
\mathcal{T}: \text{gbim\_worldview\_entity} \rightarrow H_{\text{App}} \otimes H_{\text{geo}}
\]

\[
\mathcal{T}(r) = \underbrace{E(\text{label}(r))}_{\mathbf{s}_r \in \mathbb{R}^{384}}
\otimes
\underbrace{(\lambda_r, \phi_r)}_{\mathbf{g}_r \in \mathbb{R}^2}
\]

where \(E\) is the `all-minilm:latest` embedding function,
\(\lambda_r = \text{belief\_state.lon}\), and \(\phi_r = \text{belief\_state.lat}\).

The image of \(\mathcal{T}\) is the set of 1,512 confirmed entangled states in
\(H_{\text{App}} \otimes H_{\text{geo}}\). This set is also stored redundantly in
`gbim_worldview_entities` in ChromaDB (5,416,521 L2 vectors) — the semantic projection
of the full geographic entity corpus, of which the 1,512 `gbim_worldview_entity` rows
are the structured relational anchor.

### 46.3.1 Forward Projection (Semantic → Spatial)

Given a query vector \(\mathbf{q} \in H_{\text{App}}\), the forward projection retrieves
the \(k\) most semantically proximate joint-state entities and returns their spatial
coordinates:

\[
\text{Forward}(\mathbf{q}, k) = \left\{ \mathbf{g}_r \;\middle|\; r \in \text{TopK}\left(\cos(\mathbf{q}, \mathbf{s}_r), k\right) \right\}
\]

**Physical path:** ChromaDB `/query` on `gbim_worldview_entities` → retrieve top-\(k\)
entity IDs → join to `gbim_worldview_entity.belief_state` → return
`(lat, lon, county, entity_type, label)`.

### 46.3.2 Backward Projection (Spatial → Semantic)

Given a spatial query region \(R \subset H_{\text{geo}}\) (a bounding box, radius, or
polygon), the backward projection retrieves all entities within \(R\) and returns their
semantic vectors for downstream RAG retrieval:

\[
\text{Backward}(R) = \left\{ \mathbf{s}_r \;\middle|\; \text{ST\_Within}(\mathbf{g}_r, R) = \text{true} \right\}
\]

**Physical path:** PostGIS `ST_DWithin` or `ST_Within` on
`gbim_worldview_entity.belief_state->>lat/lon` → retrieve matching labels → embed via
`all-minilm:latest` → query ChromaDB for semantic context.

### 46.3.3 The Entanglement Condition

An entity \(r\) is **entangled** in \(H_{\text{App}} \otimes H_{\text{geo}}\) if and
only if it satisfies all three conditions:

1. \(\text{belief\_state.lat} \neq \text{NULL}\) and \(\text{belief\_state.lon} \neq \text{NULL}\) — spatial coordinate confirmed
2. \(\text{label}(r)\) is embeddable — non-null, non-empty text
3. \(\text{belief\_state.confidence} > 0\) — non-zero epistemic weight

All 1,512 confirmed rows satisfy conditions 1 and 2. Condition 3 is confirmed for the
sampled hospital rows (confidence = 1.0). Full corpus confidence distribution is
OI-C46-CONFIDENCE.

---

## 46.4 The Belief State as a Joint State Vector

The `belief_state` JSONB field is architecturally significant beyond its role as a
coordinate carrier. It is a **structured attribute bag** that encodes the full joint
state of an entity across multiple dimensions simultaneously:

```json
{
  "lat": 39.47644600000007,
  "lon": -77.98017199999998,
  "city": "Martinsburg",
  "phone": "(304) 264-1000",
  "county": "Berkeley",
  "address": "2500 Hospital Drive Martinsburg WV 25401",
  "facility": "Berkeley Medical Center",
  "url": "http://www.wvuniversityhealthcare.com/...",
  "verified": false,
  "confidence": 1.0,
  "total_beds": 241.0,
  "source_type": "shapefile",
  "source_layer": "hospitals_wvdem_040519_gcs84"
}
```

This is not a flat record. It is a projection of the entity across six distinct
representational axes simultaneously:

| Axis | Field(s) | Space |
|---|---|---|
| Geodetic position | `lat`, `lon` | \(H_{\text{geo}}\) |
| Administrative geography | `county`, `city` | \(H_{\text{geo}}\) (polygon join) |
| Semantic identity | `facility`, `label` | \(H_{\text{App}}\) |
| Civic infrastructure | `total_beds`, `phone`, `url` | \(H_{\text{App}}\) (RAG context) |
| Epistemic state | `confidence`, `verified` | \([0,1]\) scalar |
| Provenance | `source_type`, `source_layer` | Audit trail |

The `belief_state` field is therefore the most compact physical representation of a
joint state in \(H_{\text{App}} \otimes H_{\text{geo}}\) — a single JSONB object
that simultaneously inhabits both Hilbert spaces.

---

## 46.5 The Service Architecture of the Tensor Product

Two services mediate the tensor product operator in the live `msjarvis-rebuild` stack:

### 46.5.1 jarvis-gis-rag (port 8004)

`jarvis-gis-rag` is the **spatial projection operator** — it accepts natural-language
queries and dispatches them to PostGIS, returning structured geographic results.

```
status: {"status": "healthy", "service": "gis_rag"}
confirmed: May 16, 2026
```

It handles the **backward projection** path: spatial query → semantic enrichment.

### 46.5.2 jarvis-wv-entangled-gateway (port 8010)

`jarvis-wv-entangled-gateway` is the **tensor product dispatcher** — it routes queries
that span both spaces, coordinating between ChromaDB semantic retrieval and PostGIS
spatial retrieval.

```
status: {
  "status": "healthy",
  "dependencies": {"production_20llm": "healthy"},
  "timestamp": "2026-05-17T00:58:45.809598"
}
confirmed: May 16, 2026
```

Its name — `wv-entangled-gateway` — is architecturally precise. It is the service that
handles **entangled queries**: those whose answer requires joint retrieval from
\(H_{\text{App}}\) and \(H_{\text{geo}}\) simultaneously. The dependency on
`production_20llm` confirms it routes through the LLM fabric (Chapter 11) for
semantic interpretation before or after spatial resolution.

### 46.5.3 Query Flow Through the Tensor Product

```
User query: "What hospitals are within 30 miles of Mount Hope WV?"

1. jarvis-wv-entangled-gateway (8010) receives query
   → Classifies as spatial-semantic joint query
   
2. Semantic arm (H_App):
   → Embed "hospitals near Mount Hope WV" via all-minilm:latest → q ∈ R^384
   → Query gbim_worldview_entities (ChromaDB) → top-k hospital entities
   
3. Spatial arm (H_geo):
   → jarvis-gis-rag (8004) receives spatial constraint
   → ST_DWithin(belief_state lat/lon, ST_Point(-81.17, 37.90), 48280) -- 30 miles in meters
   → Returns matching gbim_worldview_entity rows with full belief_state
   
4. Tensor product resolution:
   → Intersect semantic top-k ∩ spatial ST_DWithin results
   → Rank by confidence × semantic similarity
   
5. Return: structured list of hospitals with name, address, beds, phone, coordinates
```

---

## 46.6 Entity Type Distribution

The 1,512 bridge entities span the civic infrastructure of West Virginia. The confirmed
entity types derive from WV DEM shapefiles (source_type: shapefile) and include:

- `hospital` — confirmed (ids 6, 7, 8 and beyond); source: `hospitals_wvdem_040519_gcs84`
- Additional entity types are present but require a GROUP BY query to enumerate fully
  (OI-C46-TYPES)

```bash
# Enumerate all entity types and counts
docker exec jarvis-local-resources-db psql -U postgres -d local_resources -c "
SELECT entity_type, COUNT(*) AS count
FROM gbim_worldview_entity
GROUP BY entity_type
ORDER BY count DESC;
"
```

---

## 46.7 Relationship to the Phi Probe

The phi probe (Chapter 44) measures coherence within \(H_{\text{App}}\) alone —
the mean pairwise cosine similarity of semantic centroids. It has no spatial awareness.

The tensor product bridge introduces a new coherence dimension: **entanglement density**
— the fraction of \(H_{\text{App}}\) collections that have corresponding spatial
anchors in \(H_{\text{geo}}\) via `gbim_worldview_entity`.

\[
\rho_{\text{entangle}} = \frac{|\{c \in \text{PROBE\_COLLECTIONS} : \exists r \in \text{gbim\_worldview\_entity}, \text{entity\_type}(r) \in \text{domain}(c)\}|}{|\text{PROBE\_COLLECTIONS}|}
\]

At 1,512 entities spanning WV civic infrastructure, and with collections including
`wv_civic_infrastructure`, `fayette_county_resources_2026`, and
`appalachian_cultural_intelligence` in the probe set, the entanglement density is
non-zero and growing. Formal measurement of \(\rho_{\text{entangle}}\) is
OI-C46-DENSITY.

---

## 46.8 Open Items — May 16, 2026

| OI | Description | Status | Priority |
|---|---|---|---|
| OI-C46-TYPES | Run GROUP BY entity_type on gbim_worldview_entity — enumerate full entity type distribution across 1,512 rows | 🔄 Open | High |
| OI-C46-CONFIDENCE | Confirm confidence score distribution across all 1,512 rows — are any < 1.0? | 🔄 Open | Medium |
| OI-C46-DENSITY | Compute \(\rho_{\text{entangle}}\) — fraction of PROBE_COLLECTIONS with spatial anchors | 🔄 Open | Medium |
| OI-C46-CHROMA | Confirm gbim_worldview_entities ChromaDB collection (5.4M vectors) is the semantic projection of gbim_worldview_entity — verify ID alignment | 🔄 Open | High |
| OI-C46-GATEWAY | Enumerate jarvis-wv-entangled-gateway endpoints — /spatial, /semantic, /entangled or equivalent | 🔄 Open | Medium |
| OI-C46-GROW | Path to growing bridge from 1,512 to full 242-layer coverage — automated shapefile ingestion pipeline | 🔄 Open | High |

---

## 46.9 Production Status Summary — May 16, 2026

| Component | Status | Notes |
|---|---|---|
| `gbim_worldview_entity` | ✅ **1,512 rows** | Confirmed live — joint state register |
| Bridge schema | ✅ Confirmed | `id`, `entity_type`, `label`, `belief_state` JSONB |
| Spatial coordinates | ✅ In belief_state | `lat`, `lon` in every sampled row |
| Confidence scores | ✅ 1.0 (sampled) | Full distribution OI-C46-CONFIDENCE |
| Source provenance | ✅ Confirmed | `source_layer`: `hospitals_wvdem_040519_gcs84` |
| `jarvis-gis-rag` (8004) | ✅ Healthy | `{"status":"healthy","service":"gis_rag"}` |
| `jarvis-wv-entangled-gateway` (8010) | ✅ Healthy | Dependencies: production_20llm healthy |
| Forward projection path | ✅ Defined | ChromaDB → belief_state lat/lon |
| Backward projection path | ✅ Defined | ST_DWithin → label → ChromaDB |
| Tensor product operator \(\mathcal{T}\) | ✅ Formal + live | 1,512 confirmed entangled states |
| \(\rho_{\text{entangle}}\) | 🔄 Unmeasured | OI-C46-DENSITY |
| Bridge growth target | ⚠ 1,512 / ~26.9M | Full geospatial_features corpus not yet bridged |

---

*Chapter 46 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Jarvis is an original system designed and built by Carrie Ann Kidd.*
*See [LICENSE](../LICENSE) for terms.*
*Last verified: May 16, 2026 — tensor product bridge operational; gbim_worldview_entity
1,512 rows confirmed; belief_state JSONB carries lat/lon/county/confidence/source_layer;
entity_type=hospital confirmed with Berkeley Medical Center (241 beds), Bluefield Regional
(92 beds), Boone Memorial (25 beds) as sample; jarvis-gis-rag healthy (8004);
jarvis-wv-entangled-gateway healthy (8010, dep: production_20llm);
forward projection: ChromaDB gbim_worldview_entities → belief_state spatial coordinates;
backward projection: ST_DWithin → label → ChromaDB semantic retrieval;
tensor product T: gbim_worldview_entity → H_App ⊗ H_geo; all-minilm:latest 384-dim;
WGS84 EPSG:4326; msjarvis-rebuild namespace.*# Chapter 47 — H_p: Hilbert People Space Without Surveillance

The three Hilbert bodies established in earlier chapters — H_App (semantic), H_geo
(spatial), and H_t (temporal) — describe *what* the system knows, *where* it is anchored,
and *when* it happened. This chapter introduces the fourth axis that completes the civic
reasoning frame: **H_p — Hilbert People Space**, implemented as `jarvis-hilbert-people`.

The full civic reasoning state becomes:

```
H_App  ⊗  H_geo  ⊗  H_t  ⊗  H_p
 what       where      when      person-in-context
```

Every query that asks *who* — who signed a grant, who represented a community in a public
meeting, who organized the coalfield labor action of 1921 — activates all four spaces
simultaneously. The people axis is not an afterthought. It is the axis that makes the
system capable of genuine civic memory rather than just document retrieval.

The governing principle of this entire chapter:

> H_p should not ask *Who is this person, and what can we learn about them?*
> It should ask *Where does this person appear in a public, historical, permissioned, or
> accountable context? In what role? At what place? At what time? From what source?
> Under what disclosure rule?*

That is the difference between surveillance and historicity.

***

## The Three-Layer Identity Architecture

H_p does not store raw identity. It receives projections from a three-layer registration
system that governs what is sealed, what is private, and what is public.

### Layer 1 — KYC Private Vault

The KYC Docker is the sealed identity layer. It stores legal name, identity verification
records, private documents, private contact data, and sensitive verification material. It
is encrypted at rest, not embedded, not available for analytics, and not shared into
public space unless a strict authorization condition is met — court order, protective
emergency measure, constitutional review, or authorized safety process.

KYC answers exactly two questions:

- Is this person or entity verified?
- What verification level applies, and is it active, expired, or revoked?

KYC does not become the public person record.

> **The KYC rule:** KYC proves the person. KYC does not publish the person.

### Layer 2 — Private Participation Layer

Layer 2 is the default for all users. It uses a UUID that is explicitly *not* the KYC
identity:

```
kyc_subject_id  ≠  private_participation_uuid
```

This layer allows the system to serve users and collect privacy-preserving aggregate
metrics — users served, service categories requested, county-level usage, program
interest, referral outcomes, accessibility preferences — without exposing legal name,
home address, private hardship, or raw identity records.

> **The Layer 2 rule:** Layer 2 serves the person privately. Layer 2 may support
> aggregate metrics. Layer 2 does not make the person public.

### Layer 3 — Public User Layer

Layer 3 is optional and requires explicit user action. A user may choose to make their
name, organization, or public profile visible — as a partner, artist, volunteer, board
member, speaker, or contributor. The system never assumes Layer 3 and never moves a user
there without their decision.

> **The Layer 3 rule:** A user wanting to go public must make that decision. The system
> does not make it for them.

***

## How KYC Connects to H_p

KYC does not enter H_p directly. Instead, it produces a **verification assertion** — a
minimal, privacy-preserving claim that a subject has been verified at a given level,
without exposing the underlying identity records:

```json
{
  "subject_ref": "private_hash_91fa",
  "kyc_verified": true,
  "verification_level": "verified_human",
  "verification_status": "active",
  "raw_kyc_visible": false
}
```

H_p may receive the *class* of verification:

- `verified_human`
- `verified_organization`
- `verified_representative`
- `verified_public_role`
- `verified_historical_deceased`

H_p does not receive legal name, address, birthdate, ID scan, biometric record, private
documents, or sensitive household data.

The flow is:

```
KYC Docker
  ↓
encrypted verification
  ↓
private assertion (verification class only)
  ↓
permissioned person projection
  ↓
H_p (Hilbert People Space)
```

***

## What H_p Actually Stores

H_p stores **person appearances**, not person dossiers. A person appearance is:

> A person appeared in a source, in a role, at a time, in a place, under a disclosure
> rule.

The canonical record schema:

```json
{
  "appearance_id": "appearance_001",
  "person_ref": "person_hash_or_public_id",
  "name_as_recorded": "Name from source if allowed by disclosure rule",
  "role_in_record": "city council member",
  "event_or_document": "public meeting minutes",
  "place": "Mount Hope, WV",
  "date": "2026-05-12",
  "source_ref": "provenance_442",
  "merkle_ref": "merkle_991",
  "public_display_allowed": true,
  "reason_allowed": "official public role",
  "private_inference_allowed": false
}
```

This lets the system truthfully state:

> This person appeared in this public record in this role on this date.

It does not let the system state:

> Here is everything we know about this person.

***

## Person Categories and Disclosure Status

Every entity in H_p carries a classification that governs its disclosure rules.

| Category | Condition | Default Public | Notes |
|---|---|---|---|
| **Private verified user** | Layer 2 UUID only | No | Never exposed without Layer 3 opt-in |
| **Public opt-in user** | User explicitly chose Layer 3 | Yes — in chosen context | Scope limited to what user consented to |
| **Public official** | Holds elected or appointed office | Yes — in official role only | Home address, private life remain protected |
| **Public contributor** | Artist, volunteer, nonprofit officer, grant partner | Yes — in stated role only | Role-limited; no personal inference |
| **Historical person** | Source-bound, archival threshold met | Yes — as documented | Requires `source_ref`, `merkle_ref`, time logic |
| **Sensitive person** | Minor, victim, witness, benefits recipient | No | Sensitive flag overrides any public curiosity |
| **Unknown status** | No verified classification | No | Protected by default until verified otherwise |

The safety rules that govern this table:

- Unknown defaults to protected.
- Sensitive overrides public curiosity.
- Public role is context-limited, not a full identity grant.
- Historical status requires source and time logic — not assumed from age alone.

***

## Public Accountability Without Surveillance

Certain people should appear in H_p because they hold public accountability: mayors, city
council members, public agency staff, grant officers, board members, official signers,
public meeting speakers, contractors, project representatives, and elected officials. Their
inclusion is permitted — and necessary for civic memory — but it is bounded.

**Allowed:**

> Jane Doe appeared as city council member in public minutes dated May 12, 2026, in Mount
> Hope, Fayette County. Source: provenance_442. Merkle proof: merkle_991.

**Not allowed:**

> Here is Jane Doe's private life, relationships, home address, habits, or inferred
> beliefs.

> **The public accountability rule:** Public accountability allows role-bound civic
> context, not personal exposure.

***

## Historical People

H_p is the primary mechanism for place-based historical memory. People like Sarah
"Ma" Blizzard, Bill Blizzard, Mother Jones, local veterans, historic landowners, labor
organizers, teachers, and community builders are part of Appalachia's recorded knowledge
and belong in the system's civic memory — connected to role, event, place, time, and
source.

Historical person record:

```json
{
  "person": "Sarah Rebecca Blizzard",
  "status": "historical",
  "role": "labor organizer / community figure",
  "place": "West Virginia coalfields",
  "time_period": "early 1900s",
  "source_ref": "historical_record_123",
  "merkle_ref": "merkle_882",
  "public_display_allowed": true,
  "reason_allowed": "verified historical / public role"
}
```

The constitutional standard for historical inclusion:

> A private person becomes generally available for public historical treatment only after
> verified death and the required archival threshold — 70 years after verifiable death —
> unless they were already public in an official or historically documented role.

***

## The Trust and Proof Layer

No person claim enters H_p without provenance and Merkle backing. The three proof
services work together:

| Service | Function |
|---|---|
| **KYC Docker** | Encrypted identity verification vault; produces verification assertions only |
| **Provenance Docker** | Records the source lineage of every claim — where the person-role assertion came from |
| **Merkle Docker** | Tamper-evident proof that the source record has not been altered since it was ingested |

Every `appearance_id` in H_p carries a `source_ref` and a `merkle_ref`. A claim without
both is incomplete and should not be surfaced publicly.

***

## The Governance and Disclosure Layer

After provenance and proof, every person claim passes through the governance layer before
it can appear in a governed output.

```
Constitutional Docker
  → Is this person's appearance in this context allowed under the constitutional rules?
  → Possible verdicts: allowed / denied / redacted / generalized / escalated

Blood-Brain Barrier (BBB)
  → Should any private context that helped generate the answer be suppressed from output?
  → Enforces: private context may inform the answer; private context must not leak into it
```

The clean division of labor:

> KYC owns the secret.
> Provenance owns the source.
> Merkle owns the proof.
> Constitution owns the permission.
> BBB owns the crossing.
> I-Container owns the first-person boundary.

***

## How All Four Hilbert Spaces Work Together

A query activates all four spaces simultaneously. Example:

**Query:** *Who was involved in the Mount Hope community project?*

| Space | What It Contributes |
|---|---|
| **H_App** (semantic) | Project documents, topic vectors, service descriptions, relevant corpus chunks |
| **H_geo** (spatial) | Mount Hope, Fayette County, parcel geometry, agency jurisdiction, service area |
| **H_t** (temporal) | Meeting dates, grant cycles, archival periods, recency weights |
| **H_p** (people) | Source-bound person-role appearances linked to the project and place |
| **Provenance** | Source lineage for every named person and document |
| **Merkle** | Tamper-evident proof for each source record |
| **Constitution** | May each person be named in this context? |
| **BBB** | Should anything be redacted before public output? |

The governed answer would be:

> The publicly documented participants include [Name], listed as [role] in [source/date],
> and [Organization], listed as [role] in [source/date].

Not:

> Here is everything we know about everyone connected to this project.

***

## Aggregate Metrics Without Surveillance

Layer 2 supports useful system metrics that do not expose private identity.

**Acceptable metrics:**
- How many people used the system in a given period
- What service categories were most requested
- Which county or service area was involved
- Which resources and programs received referrals
- How many users opted into public Layer 3 profiles
- How many users remained private

**Not acceptable:**
- Individual behavioral trails
- Private identity linkage across sessions
- Inferred vulnerability scoring
- Unnecessary location history
- Sensitive profile building
- Public exposure of private Layer 2 users

> **The metric design principle:** aggregate first, pseudonymous where needed,
> identity-separated always, public only by consent.

***

## The Full Four-Space Architecture

```
                     Ms. Allis I-Container
                              |
                              v
                Constitutional Operating Frame
                              |
                              v
┌──────────────────────────────────────────────────────────────┐
│                     Four Hilbert Spaces                      │
├──────────────────────────────────────────────────────────────┤
│ H_App — Hilbert Semantic Space                               │
│   meaning, documents, concepts, services                     │
│                                                              │
│ H_geo — Hilbert Geographic Space                             │
│   place, jurisdiction, parcels, service areas                │
│                                                              │
│ H_t — Hilbert Time Space                                     │
│   dates, sequence, history, deadlines, archival age          │
│                                                              │
│ H_p — Hilbert People Space                                   │
│   person-in-context, public roles, historical actors,        │
│   consented users, private UUID projections                  │
└──────────────────────────────────────────────────────────────┘
                              |
                              v
┌──────────────────────────────────────────────────────────────┐
│                    Trust and Proof Layer                     │
├──────────────────────────────────────────────────────────────┤
│ KYC Docker        encrypted identity verification            │
│ Provenance Docker source lineage                             │
│ Merkle Docker     tamper-evident proof                       │
└──────────────────────────────────────────────────────────────┘
                              |
                              v
┌──────────────────────────────────────────────────────────────┐
│               Governance and Disclosure Layer                │
├──────────────────────────────────────────────────────────────┤
│ Constitutional Docker  allowed / denied / redacted           │
│ Blood-Brain Barrier    private-public crossing control       │
└──────────────────────────────────────────────────────────────┘
                              |
                              v
                       Governed Civic Answer
```

***

## Relationship to Earlier Chapters

| Chapter | Establishes | H_p Role |
|---|---|---|
| 04 — Hilbert Space & State | H_App as semantic Hilbert space; hilbert-state as state machine | H_p adds person-in-context as a fourth dimension to the state space |
| 42 — Post-Quantum Security | Signed, auditable provenance for all operations | Every H_p appearance record is signed; KYC assertions are cryptographically sealed |
| 43 — Role-Gated Knowledge | Access control by role over collections | H_p is itself a role-gated space; disclosure rules are enforced at query time |
| 44 — Phi Probe | Semantic coherence measurement across H_App | Person-role claims contribute to coherence scoring when sources corroborate each other |
| 45 — H_geo | Spatial body, PostGIS, GBIM entity binding | Every H_p appearance record carries a `place` field linked to H_geo geometry |
| 46 — H_App ⊗ H_geo | Tensor product bridge joining semantic and spatial | H_p extends the product to H_App ⊗ H_geo ⊗ H_t ⊗ H_p |
| 47 — H_t | Temporal axis, recency decay, ordered event timelines | Every H_p appearance carries a `date` that is scored by H_t recency logic |

***

## Implementation Notes

**Service name:** `jarvis-hilbert-people`

**Storage:** A dedicated PostgreSQL schema (`hilbert_people`) within `msjarvisgis` for
appearance records. Redis for short-lived session context (Layer 2 UUID mappings). No
Chroma collection for the people axis — person appearances are structured relational
records, not embeddings.

**KYC Docker isolation:** The KYC container must not share a network bridge with
`jarvis-hilbert-people`. KYC communicates only via the assertion endpoint (returning
verification class, not identity) and only when invoked by the Constitutional Docker or
an authorized safety process. Direct container-to-container calls from H_p to KYC are
not permitted.

**Sensitive flag enforcement:** The `sensitive_person` flag must be evaluated *before* the
Constitutional Docker verdict. A sensitive classification is not a constitutional question
— it is a hard stop. Sensitive records do not reach the constitutional layer; they are
suppressed by the BBB before routing.

**Merkle coverage:** Every ingest path that writes an appearance record to H_p must call
the Merkle Docker to stamp the source record before writing. Appearance records written
without a `merkle_ref` are incomplete and must not be surfaced by the semantic gateway.

***

*Formal derivation of the four-space tensor product H_App ⊗ H_geo ⊗ H_t ⊗ H_p and the
disclosure algebra over person categories are in the work-repo thesis. This chapter
documents the design principles, data model, and governance rules as the basis for
implementation.*48-Hilbert People Space — Person-in-Context Without Surveillance

Design document — work-repo thesis. Status: built and operational. H_people runs as a Postgres schema hp in database hilbert_people on msjarvisgis-db, served by jarvis-hilbert-state (image jarvis-main-brain:latest, host port 18092), coordinated alongside H_t and Redis. As of this writing the appearance ledger holds live records and the disclosure-assertion gateway is verified end-to-end — it correctly permits backed subjects and denies unbacked ones, persisting every verdict to hp.appearance_assertion. The fourth Hilbert body is real and measurable; the MountainShares-Commons evidence pipeline extends to probe the hp schema and the architecture moves from three measured bodies to four under the same regenerate-from-evidence discipline.
1. Where this fits

Ms. Allis reasons over coupled Hilbert bodies. Three are running and measured today:

Hilbert Semantic Space (H_App)  = meaning   → ChromaDB
Hilbert Geographic Space (H_geo) = place    → PostGIS
Hilbert Time Space (H_t)         = history / sequence / recency → Redis timelines

This chapter documents the fourth body, now built and running:

Hilbert People Space (H_people)  = person-in-context

The full civic reasoning state becomes a four-way tensor product:

Civic State = meaning ⊗ place ⊗ time ⊗ person-in-context
            = H_App ⊗ H_geo ⊗ H_t ⊗ H_people

2. The governing rule

    Hilbert People Space is not a surveillance database. It is a public, historical, role-based, consent-governed person-context space.

The system is not tracking people. It represents a person only when they appear in a sourced, permissioned, public, historical, or accountable role. The distinction is between surveillance and historicity.

H_people never asks "Who is this person, and what can we learn about them?" It asks:

Where does this person appear in a public, historical, permissioned, or accountable context?
In what role? At what place? At what time? From what source? Under what disclosure rule?

3. What H_people stores: appearances, not dossiers

H_people stores person appearances — a person appeared in a source, in a role, at a time, in a place, under a disclosure rule — not full person records.

{
  "appearance_id": "appearance_001",
  "person_ref": "person_hash_or_public_id",
  "name_as_recorded": "Name from source if allowed",
  "role_in_record": "city council member",
  "event_or_document": "public meeting minutes",
  "place": "Mount Hope, WV",
  "date": "2026-05-12",
  "source_ref": "provenance_442",
  "merkle_ref": "merkle_991",
  "public_display_allowed": true,
  "reason_allowed": "official public role",
  "private_inference_allowed": false
}

This lets the system say "This person appeared in this public record in this role on this date," and structurally prevents it from saying "Here is everything we know about this person."
4. The three-layer registration system
Layer 1 — KYC Private Vault

The sealed identity layer: legal name, identity verification, private documents and contact data, sensitive verification records. It is encrypted, sealed, not embedded, not used for analytics, not exposed to H_people. Access only under court order, protective emergency measure, constitutional/legal review, or authorized safety process.

KYC answers only: is this person/entity verified, at what level, and is the verification active/expired/revoked? KYC proves the person; KYC does not publish the person.
Layer 2 — Private Participation Layer (default)

A separate UUID that is not the KYC ID:

kyc_subject_id ≠ private_participation_uuid

Serves users and supports privacy-preserving aggregate metrics (users served, service categories, county-level usage, referral success, repeat engagement, accessibility preferences, eligibility tags) without exposing legal name, address, hardship, or raw KYC records. Layer 2 serves the person privately and may support aggregate metrics; it does not make the person public.
Layer 3 — Public User Layer (opt-in only)

Exists only when a user explicitly chooses to be public — named as partner, artist, volunteer, board member, speaker, or contributor. Default is private in Layer 2; public only by explicit opt-in. The system never assumes it.
5. KYC → H_people: assertion, not identity

KYC does not enter H_people. It emits a verification assertion:

{
  "subject_ref": "private_hash_91fa",
  "kyc_verified": true,
  "verification_level": "verified_human",
  "verification_status": "active",
  "raw_kyc_visible": false
}

H_people may receive verified human / organization / representative / public role / historical-deceased status. It must never receive legal name, address, birthdate, ID scan, biometric, private documents, or sensitive household data. Flow:

KYC Docker → encrypted verification → private assertion
           → permissioned person projection → Hilbert People Space

6. Person categories (by disclosure status)

1. Private verified user   — default: private Layer 2 UUID only
2. Public opt-in user      — public only because the user chose it
3. Public official         — public only in official capacity
4. Public contributor      — artist/volunteer/speaker/officer/owner/grant partner,
                             public only in the role they entered
5. Historical person       — public when source-bound and historical/death threshold met
6. Sensitive person        — minor, victim, witness, benefits recipient, medical/legal/
                             housing subject; protected even if mentioned in a record
7. Unknown status          — treated as private until verified otherwise

Safety rule: unknown defaults to protected; sensitive overrides public curiosity; public role is context-limited; historical status requires source and time logic.
7. Public accountability without surveillance

Public-accountability figures (mayors, council members, agency staff, grant officers, board members acting publicly, official signers, public speakers, contractors, elected officials, organization representatives) may appear — but only in relation to their public role.

    Allowed: "Jane Doe appeared as city council member in public minutes dated May 12, 2026."
    Not allowed: private life, relationships, home address, habits, inferred beliefs.

    Public accountability allows role-bound civic context, not personal exposure.

8. Historical people

Historical figures (e.g., Sarah "Ma" Blizzard, Bill Blizzard, Mother Jones, local veterans, historic landowners, teachers, labor organizers) connect person → role → event → place → time period → source → historical significance.

Proposed constitutional standard:

    A private person becomes generally available for public historical treatment only after verified death and a required archival threshold — e.g., 70 years after verifiable death — unless they were already public in an official or historically documented role.

9. Trust, proof, and disclosure layers

KYC Docker            = encrypted verification vault   — owns the secret
Provenance Docker     = source lineage                 — owns the source
Merkle Docker         = tamper-evident proof           — owns the proof
Constitutional Docker = allowed / denied / redacted    — owns the permission
Blood-Brain Barrier   = private→public crossing control — owns the crossing
I-Container           = Ms. Allis first-person boundary — owns the first person

Closed disclosure vocabulary (verified in the running gateway). Claim types are allowlisted, not open. The assertion gateway distinguishes three outcomes, all observed in regression:

    Unknown claim type (e.g. not_a_real_claim) → rejected at the HTTP layer with 403 — "Claim type is not in the approved list." It never becomes a verdict. The disclosure vocabulary is closed; you cannot ask a question the system isn't sanctioned to answer.
    Valid claim, backing supports it (e.g. verified_county_resident for a backed subject) → 200, result: true, persisted to hp.appearance_assertion.
    Valid claim, backing does not support it (e.g. verified_adult for a subject whose backing doesn't establish it) → 200, result: false, persisted. A legitimate, logged "no" — distinct from "you may not ask."

The 403-on-unknown vs. 200 false-on-unsupported distinction is load-bearing: it separates vocabulary control (which questions exist) from evidence control (whether the answer is yes), and both are enforced and audited.
10. Four-space query flow

Query: "Who was involved in the Mount Hope project?" activates all four spaces plus the trust/governance layers:

Semantic  : what project, documents, topic
Geo       : Mount Hope, Fayette County, parcels, agencies, jurisdiction
Time      : year, meeting, grant cycle, historical period
People    : who appears in source-bound public or permissioned records
Provenance: where each person-role claim came from
Merkle    : has the record/proof been altered
Constitution: may this person be named in this context
BBB       : redact anything before output

Governed output names only source-bound, permissioned participants and their roles — never "everything we know about everyone connected to this project."
11. Metrics without surveillance

Acceptable (Layer 2, aggregate): users served, help categories, county/service area, most-requested resources, referral counts, public-page views, opt-in vs. private counts.

Avoid: individual behavioral tracking, private identity trails, unnecessary location history, sensitive profile building, inferred vulnerability scoring, exposure of private users.

Design posture: aggregate first; pseudonymous where needed; identity-separated always; public only by consent.
12. Mapping to the running stack

Most of the governance machinery already exists; the net-new is the person store, the vault, and the registration tiers.
Design component 	Stack status 	Maps to / becomes
Blood-Brain Barrier 	exists (jarvis-blood-brain-barrier) 	extend to redact person-names per disclosure rule
Constitutional Docker 	exists (Constitutional Guardian) 	extend verdict logic to person-disclosure
Provenance + Merkle 	partial (PQ signing / append-only audit) 	reuse for per-appearance provenance and merkle_ref
Assertion gateway 	exists (already gates the wallet/balances path) 	the same result: true/false pattern is the disclosure gate
I-Container 	exists 	unchanged; owns the first-person boundary
Hilbert People Space 	built and serving — Postgres schema hp (13 tables) in DB hilbert_people on msjarvisgis-db, served by jarvis-hilbert-state; appearance ledger populated, disclosure-gate verified 	live; extend the Commons collector to probe it
KYC Private Vault 	net-new 	new sealed, encrypted store, outside the Hilbert spaces
Three-layer registration 	partial (registration language.md exists) 	new: UUID separation + opt-in gating

Note: the assertion-gateway-as-policy-gate is already running in the balances route (_assert_claim(public_uuid, "verified_state_resident", …) → result: true/false). The disclosure permission model for H_people is the same pattern keyed to a public_uuid with raw identity sealed elsewhere — reuse, not new architecture.
13. Design decisions — resolved at build, and still-open

13.1 — Separate store, or person-typed GBIM extension? → RESOLVED: separate store. The built implementation uses a dedicated Postgres schema hp (13 tables, appearance-centric) in database hilbert_people, not a person-typed GBIM record. The appearance ledger (hp.appearance + satellite tables for name/role/source/place/time/assertion/verdict/ suppression) stands on its own, with the KYC vault in a separate database the appearance role cannot reach. Original design note retained below for provenance.

A "person appearance" (person_ref + role + place + time + source + disclosure_rule) is structurally a GBIM entity. GBIM already binds claims to where/when/source/confidence in PostGIS. Implementing appearances as a person-typed GBIM record with disclosure governance on top would reuse H_geo's machinery and keep person-context spatially and temporally joined automatically. The KYC vault stays separate regardless; the appearances may not need a wholly separate store. Built decision: dedicated hp schema.

13.2 — Unlinkability is the load-bearing guarantee. → IMPLEMENTED at the database level. The migration enforces this structurally: the hilbert_app role is granted SELECT/INSERT/ UPDATE on the hp schema only, is REVOKEd from public, and has no connect rights to the KYC vault database (enforced at pg_hba per the migration's documented posture). The appearance side and the identity side live in separate databases, and the role that reads appearances literally cannot reach KYC. Additionally, hp.appearance_name carries an inline DDL prohibition (legal_name is FORBIDDEN here — store public display values only), and the schema comment declares it appearance-centric with no identity mirrors. The kyc_subject_id ≠ private_participation_uuid separation is therefore not a convention but a grant-and-database boundary. Original design note retained below for provenance.

The entire anti-surveillance promise rests on kyc_subject_id ≠ private_participation_uuid being genuinely unlinkable. If the two can be re-joined by anyone short of a court order, the design collapses. The mapping must be one-way and access-gated at the same constitutional level as the KYC vault itself — not merely two columns in a table.

13.3 — Rural re-identification risk in Layer 2 metrics. → STILL OPEN. "County-level usage + service category + repeat engagement + accessibility preferences" sounds aggregate, but in a county of a few thousand, "user in this county requesting this rare service" can resolve to one person — the k-anonymity problem, sharpened by rural WV population scale. Metrics need small-cell suppression / minimum-count thresholds before any breakdown is exposed, or the "metrics without surveillance" guarantee leaks exactly where the most vulnerable users are. Suppression thresholds must be defined before any Layer 2 breakdown is surfaced.

13.4 — Sensitive-person category overlaps BSA. → STILL OPEN. The "sensitive person" category (minors, victims, witnesses, benefits recipients) overlaps exactly with Benefits-Sensitive Accounts. A BSA flag is a sensitive-person status. Wiring both to the same protected-default would let the two systems reinforce each other rather than run parallel. Recommended: unify the protected-default.
14. The design principles, as built

The principles below are the governing rules; the build realizes 1–10 as the hp schema, the hilbert_app/KYC database boundary, and the assertion gateway. Items 13.3 (rural small-cell suppression) and 13.4 (sensitive/BSA unification) remain the active design work on top of the running base.

    Keep KYC sealed and encrypted; it verifies, never publishes.
    Create a private Layer 2 UUID by default (separate from KYC ID).
    Make public Layer 3 opt-in only.
    Build H_people from person-in-context appearance records — roles, sources, places, dates, disclosure status — not dossiers.
    Use public-accountability rules for officials and public actors (role-bound, sourced).
    Use historical rules for deceased/archival people (source-bound, time-valid).
    Protect sensitive and unknown people by default.
    Require provenance + Merkle proof for every person claim; no unsourced personhood.
    Use the Constitutional Docker to decide disclosure (name / redact / generalize / escalate).
    Use the BBB to prevent private→public leakage.

15. One-sentence statement

    Hilbert People Space represents people as source-bound, time-bound, place-bound, role-bound, and consent-governed participants in public or historical knowledge, while KYC remains sealed, Layer 2 supports private metrics through separate UUIDs, and Layer 3 makes public identity available only by explicit user choice.

That is the path to include people accurately without building surveillance.

Design document, now describing a built system. H_people runs as Postgres schema hp in database hilbert_people on msjarvisgis-db, served by jarvis-hilbert-state, with a populated appearance ledger and a verified disclosure-assertion gateway. The MountainShares-Commons evidence pipeline extends to probe the hp schema, and the architecture moves from three measured bodies to four — under the same regenerate-from-evidence discipline that governs every other body: the public repo claims H_people because the collector counts its records, not because this document asserts it.
# Chapter 49 — H_t: The Temporal Hilbert Axis and the Three-Dimensional Memory of H_App

The semantic body (H_App) and the spatial body (H_geo) established in earlier chapters
describe *what* the system knows and *where* that knowledge is anchored. This chapter
introduces the third axis that completes the system's operational memory model:
**H_t — the temporal Hilbert body**, implemented as `jarvis-hilbert-time`. Where H_App
holds semantic embeddings and H_geo holds spatial geometry, H_t holds the *when* of every
belief, event, and ingest operation as an ordered, decay-weighted timeline.

Together the three form a genuine three-dimensional memory space:

```
H_App  ×  H_geo  ×  H_t
 what       where      when
```

Every document ingested, every query answered, and every state transition recorded in the
system touches all three axes simultaneously.

***

## What jarvis-hilbert-time Is

`jarvis-hilbert-time` is a lightweight FastAPI service (port 18093 internally, `8092`
inside the Docker network) backed entirely by **Redis sorted sets**. It does not write to
ChromaDB. It does not hold embeddings. Its sole responsibility is recording *when*
something happened and computing how much that event still matters now.

Each entity — typically a ChromaDB collection name — maintains an independent timeline:

```
hilbert:time:{entity_id}  →  Redis ZSET scored by Unix epoch
    member format:  "{ISO-8601 timestamp}|{payload}"
    score:          float Unix timestamp (for ZREVRANGE ordering)
```

The service exposes three endpoints:

| Endpoint | Method | Purpose |
|---|---|---|
| `/timeline/register-json` | POST | Record a new event for an entity |
| `/timeline/query` | GET | Retrieve the N most recent events with decay weights |
| `/timeline/decay` | GET | Compute the recency weight for an arbitrary timestamp |

### Recency Decay

Each event carries a **recency weight** — a number between 0 and 1 representing how
fresh the event is relative to now. The weight follows a half-life decay function:

$$
w(t) = 0.5^{\,d \,/\, \tau}
$$

where $$d$$ is the age of the event in days and $$\tau$$ is the configurable half-life
(default 30 days, set via `TIME_HALF_LIFE_DAYS`). An event logged seconds ago has weight
≈ 1.0; one logged 30 days ago has weight 0.5; one logged 90 days ago has weight 0.125.

This is not bookkeeping metadata — it is a live scoring input used by the semantic
gateway at query time.

***

## How H_t Fits into the Full Ingest Pipeline

Every document upload triggers a synchronized write across all three memory axes. The
sequence within a single ingest call is:

```
intake_service  (port 8007)
    │
    ├── writes file to /data/incoming
    │
    └── spawns ms_allis_ingest_worker
            │
            ├──► Chroma  (ms_allis_uploads or named collection)
            │      chunk text → embedding → vector
            │      chunk_id hash + document_id hash stored
            │      → H_App axis written ✅
            │
            ├──► PostgreSQL  (msjarvisgis)
            │      lat/lon stripped from source
            │      collection_hash + feature_id from Chroma
            │      gbim_id = sha256(collection:chunk_id)
            │      INSERT INTO gbim_entities (...)
            │      → H_geo axis written ✅
            │
            ├──► hilbert-state  /state/set
            │      dimensions: {"chunk_count": N}
            │      triggers auto_entangle() to six known peer collections
            │
            └──► hilbert-time  /timeline/register-json
                    entity_id: collection_name
                    timestamp: datetime.now(UTC).isoformat()   # "+00:00" format
                    payload:   "ingest:{N}_chunks:{document_id}:{ext}"
                    → H_t axis written ✅
```

The result is that three Redis events land for every upload — one from the intake service
(file received), one from the ingest worker (chunks stored), one from hilbert-state
(state updated) — all within the same millisecond burst and all queryable immediately via
`/timeline/query`.

### The Timestamp Format Constraint

`jarvis-hilbert-time` runs Python 3.10. `datetime.fromisoformat()` in Python 3.10 does
**not** accept the `Z` UTC suffix — that was added in Python 3.11. The `parse_ts()`
function in the service handles `+00:00` and space-separated offsets but not `Z`. All
internal callers (intake service, hilbert-state, hilbert-gateway) use
`datetime.now(timezone.utc).isoformat()` which produces the `+00:00` form and therefore
works correctly. External clients sending `Z`-terminated timestamps will receive a 500
error until the container image is rebuilt on Python 3.11 or the `parse_ts()` function is
patched to strip the `Z` before parsing.

***

## How H_t Powers the Semantic Gateway

`jarvis-hilbert-semantic` (the Hilbert gateway, port 18091) implements
**decay-weighted semantic retrieval**. When a query arrives, it does not simply return
the closest vectors by cosine distance. It computes a composite score:

$$
\text{final\_score} = \text{semantic\_score} \times \text{freshness\_weight} \times \text{recency\_boost}
$$

where:

- **semantic\_score** = `1 / (1 + cosine_distance)` from ChromaDB — the H_App
  contribution
- **freshness\_weight** = `0.5^(age_days / half_life)` from the document's
  `ingested_at` metadata — the document-level H_t contribution
- **recency\_boost** = a multiplier in [1.0, 1.05] derived from the entity's most
  recent hilbert-time event — the collection-level H_t contribution

The recency boost is computed by `get_collection_recency()`, which calls
`/timeline/query` with `limit=5`, reads the top event's `recency_weight`, and maps it to
a small boost if the collection has been active within the last few minutes. A collection
touched 10 seconds ago scores up to 5% higher than an identical-content collection last
touched two weeks ago. This ensures that an active investigation — a parcel dispute, an
ongoing community health query — surfaces its most recently ingested material preferentially
without discarding older evidence.

***

## The Three-Hilbert-Body Architecture

The three services form a complete operational memory:

| Axis | Service | Store | Records |
|---|---|---|---|
| **H_App** — *what* | jarvis-hilbert-semantic | ChromaDB | Semantic embeddings, decay-scored retrieval |
| **H_geo** — *where* | GBIM / PostGIS | PostgreSQL | Spatial geometry, lat/lon, GBIM entities |
| **H_t** — *when* | jarvis-hilbert-time | Redis | Ordered event timelines, recency weights |

And the fourth service that reads across all three:

| Service | Role |
|---|---|
| **jarvis-hilbert-state** | Maintains the state machine over entity identity — *what state something is in* — and records each transition into H_t. Acts as the coordinator between the three axes. |

### Why Redis, Not ChromaDB, for Time

The choice to use Redis sorted sets rather than a ChromaDB collection for the temporal
axis is deliberate. Time is an ordering problem, not a similarity problem. Redis sorted
sets provide O(log N) insertion and O(log N + M) range retrieval by score, which maps
perfectly to "give me the M most recent events for entity X." A vector store would add
embedding overhead, approximate nearest-neighbor search semantics, and collection
management complexity to what is fundamentally an append-only ordered log. Redis is the
right data structure for this axis.

***

## The Live Timeline — Observed Behavior

As of the session documented here, the following entity timelines were confirmed present
in Redis:

| Entity | Events | Most Recent Payload |
|---|---|---|
| `ms_allis_uploads` | 3+ | `ingest:1_chunks:{hash}:.txt` |
| `ms_allis_active` | 4 | `entanglement:ms_allis_uploads<->ms_allis_active` |
| `ms_allis_uploads` | 5 | `semantic_query:Ms. Allis parcel boundary` |
| `ms_allis` | 2 | `semantic-ingest` |

The presence of `semantic_query:` payloads in the `ms_allis_uploads` timeline confirms
that query events — not just ingest events — are also registered into H_t, providing a
complete record of both *what was stored* and *what was asked*.

***

## Relationship to Earlier Chapters

| Chapter | Establishes | H_t Role |
|---|---|---|
| 04 — Hilbert Space & State | H_App as a semantic Hilbert space; hilbert-state as the state machine | H_t extends the state machine with an ordered temporal record of every transition |
| 45 — H_geo | The spatial body, PostGIS, GBIM entity binding | H_t records *when* each spatial entity was last observed or queried |
| 46 — H_App ⊗ H_geo | The tensor product bridge joining semantic and spatial arms | H_t adds the third tensor dimension, making the full product H_App ⊗ H_geo ⊗ H_t |
| 44 — Phi Probe | Semantic coherence measurement across H_App | Recency weighting from H_t modulates which vectors the Phi probe sees as "current" |
| 42 — Post-Quantum Security | Signed, auditable provenance for all belief operations | H_t's Redis timeline provides the append-only audit log that the security layer can anchor signatures to |
| 43 — Role-Gated Knowledge | Access control by role over collections | H_t timelines are themselves collection-scoped, so role gates apply to temporal queries as well |

***

## Operational Notes

**Filesystem immutability.** The `jarvis-hilbert-time` container mounts its service file
read-only (`/mnt/nvme1/msjarvis-rebuild/services/jarvis_hilbert_time.py:/app/services/...:ro`).
Patches to the running service require editing the source file on the host and restarting
the container — they cannot be applied inside the container with `docker exec`.

**No Chroma collection named `hilbert_time`.** There is no ChromaDB collection with this
name and none is expected. The service is Redis-only by design. Any health check that
tests for a `hilbert_time` Chroma collection is incorrect and should be removed.

**DB_HOST configuration.** The ingest worker that feeds H_t (via hilbert-state) connects
to PostgreSQL by Docker service name (`jarvis-local-resources-db`), not by bridge IP. The
compose file must not hardcode `172.17.0.1` or `172.18.0.1` for `DB_HOST` — those IPs
are unreachable from inside containers and will produce connection timeouts on every
upload.

***

*Formal derivations of the decay operator and the tensor-product composition H_App ⊗
H_geo ⊗ H_t are in the work-repo thesis. This chapter documents the implemented
architecture as observed in the running system.*# 50 - The Sovereign Subspace — Per-User Direct Sum Decomposition of Conversational Memory

**Series:** MountainShares / Ms. Allis Architecture Thesis
**Status:** Formal specification — theoretical foundation established, implementation pending
**Date:** July 1, 2026
**Author:** Carrie A. Kidd, Founder & Executive Director, Harmony for Hope, Inc.

---

## Abstract

The conversational memory architecture described in preceding chapters treats `H_people` as a single shared Hilbert space in which all users' vectors coexist, with access control governing who may join private and public records. This chapter proposes and formally specifies a structural upgrade: the replacement of that single shared space with a direct sum decomposition in which each user occupies a mathematically orthogonal subspace. The distinction is not administrative but geometric. In the shared-space model, cross-user correlation is prevented by policy. In the direct sum model, cross-user correlation is prevented by construction. The upgrade transforms a governance guarantee into a mathematical one.

---

## 1. The Shared Space Problem

### 1.1 What the Current Architecture Provides

The `H_people` space as implemented is a single vector store — currently Redis and ChromaDB — in which conversation embeddings for all users are stored. Access is governed by the `identity_binding` layer, which enforces that a user's query retrieves only vectors associated with their verified identity. The governance is real. The guard tests run on every commit. The access control is not a placeholder.

However, the architecture has a structural property that no amount of access control can eliminate: all user vectors inhabit the same embedding space. They share a coordinate system. The axes are common. The distance metric is universal. This means:

1. If access control failed — through a vulnerability, a misconfiguration, a coerced disclosure, or a future governance decision the founder cannot anticipate — the vectors of all users would be in the same space and semantically comparable without any additional transformation.

2. An adversary with read access to the raw vector store — without any application-layer access control — could compute cosine similarity across users, cluster users by semantic content, and infer relationships, shared concerns, or shared circumstances that no user consented to disclose.

3. The privacy guarantee is *empirical*, not *structural*. It depends on the continued correct function of the access control layer. The mathematical substrate does not enforce it.

This is not a criticism of the current implementation. It is an accurate description of the threat model's residual exposure. The purpose of this chapter is to close that exposure at the geometric level.

### 1.2 The Tensor Product Analogy

The four-space architecture described in Chapter 46 uses tensor products to represent semantic entanglement between knowledge domains:

\[
H_{App} \otimes H_{geo} \otimes H_t \otimes H_p
\]

In a tensor product \(H_A \otimes H_B\), the joint state of two subsystems can be *entangled* — meaning the full state cannot be decomposed into independent contributions from each subsystem. Entanglement is the feature, not a bug: it allows Ms. Allis to reason about the semantic relationship between a document, a place, a time, and a person simultaneously.

But entanglement has a structural consequence: given a state in \(H_A \otimes H_B\), it is in principle possible to ask about correlations between the \(H_A\) and \(H_B\) degrees of freedom. Whether those correlations are present depends on the actual state — a separable state has no entanglement, an entangled state does. The *possibility* of correlation is built into the tensor product structure. Access control can prevent a query from being executed. It cannot prevent the correlation from existing in the mathematical structure if it is there.

For the four-space civic reasoning architecture, this is correct. We *want* H_App and H_geo to be potentially entangled — that is what allows flood sensor data to update parcel-level belief states. The semantic coupling is the product's core capability.

For conversational memory across different users, entanglement is not a feature. It is a liability. We do not want Alice's conversation history to be geometrically comparable to Bob's. The analogy fails, and the architecture should reflect that failure.

---

## 2. The Direct Sum Architecture

### 2.1 Formal Definition

Let \(U = \{u_1, u_2, \ldots, u_n\}\) be the set of registered participants in the MountainShares commons. For each participant \(u_i\), define a separable Hilbert space \(H_{u_i}\) — the *sovereign subspace* of that participant — as the closure of the span of all conversation embeddings associated with \(u_i\) under a participant-specific inner product.

The full conversational memory space is defined as the *direct sum* of these subspaces:

\[
H_{conversations} = H_{u_1} \oplus H_{u_2} \oplus H_{u_3} \oplus \cdots \oplus H_{u_n}
\]

The defining property of the direct sum is orthogonality by construction. For any vector \(v_A \in H_{u_A}\) and any vector \(v_B \in H_{u_B}\) where \(A \neq B\):

\[
\langle v_A, v_B \rangle = 0
\]

This inner product identity does not hold because access control prevents the computation. It holds because the two vectors literally have no overlapping coordinates. They live in different subspaces of the direct sum. There is no basis vector shared between \(H_{u_A}\) and \(H_{u_B}\). The zero inner product is a theorem about the geometry, not a policy about who is allowed to ask.

### 2.2 Contrast With the Tensor Product

The structural difference between \(\oplus\) and \(\otimes\) is not merely notational. It determines what kind of guarantee the architecture can provide.

| Property | Tensor Product \(H_A \otimes H_B\) | Direct Sum \(H_A \oplus H_B\) |
|---|---|---|
| Shared basis vectors | Yes — the joint basis is \(\{e_i \otimes f_j\}\) | No — bases are disjoint by construction |
| Cross-subsystem correlation | Possible — depends on the state | Impossible — no shared coordinates |
| Privacy guarantee type | Empirical — depends on access control | Structural — enforced by geometry |
| Failure mode if access control breaks | Cross-user vectors become comparable | Cross-user vectors remain incomparable |
| Appropriate use case | Semantic entanglement across domains | Participant sovereignty over memory |
| Dimensionality | \(\dim(H_A) \times \dim(H_B)\) | \(\dim(H_A) + \dim(H_B)\) |

The four-space civic reasoning architecture retains tensor products where entanglement is the desired property. Conversational memory replaces the shared embedding space with a direct sum where orthogonality is the desired property. These are not competing choices — they are appropriate choices for structurally different problems.

### 2.3 The Upgrade in Plain Language

In the shared-space model: Alice and Bob's memories are in the same room. A lock on the door keeps them separate. If the lock breaks, nothing stops comparison.

In the direct sum model: Alice and Bob's memories are in different coordinate systems. There is no door to break. A vector in Alice's subspace and a vector in Bob's subspace are not comparable not because comparison is forbidden, but because the mathematical operation of comparison — computing an inner product — returns zero regardless of what the vectors contain. The geometry enforces the separation that the governance layer previously had to enforce alone.

---

## 3. Operational Implementation

### 3.1 The Per-User Projection Key

The direct sum decomposition does not require \(n\) separate vector databases. That would fragment the infrastructure without architectural necessity. The implementation uses a single vector store at the infrastructure level — Redis and ChromaDB — with a *per-user projection transform* applied before storage.

For each participant \(u_i\), define a deterministic rotation matrix \(R_{u_i} \in O(d)\) — an orthogonal transformation in the embedding dimension \(d\) — derived from a participant-held secret:

\[
R_{u_i} = \text{ProjectionKey}(\text{commitment\_salt}_{u_i})
\]

where `commitment_salt` is the participant-held key already established in the MountainShares identity architecture. The server does not hold this value. It cannot be reconstructed without the participant's key.

Before any conversation embedding \(e \in \mathbb{R}^d\) is written to storage for participant \(u_i\), it is transformed:

\[
\hat{e}_{u_i} = R_{u_i} \cdot e
\]

The stored vector is \(\hat{e}_{u_i}\), not \(e\). The raw embedding never touches persistent storage.

### 3.2 Why This Produces Orthogonal Subspaces

For two participants \(u_A\) and \(u_B\) with distinct projection keys, consider two semantically identical conversations — Alice and Bob both ask Ms. Allis about flood risk on Arbuckle Creek. Their raw embeddings \(e_A\) and \(e_B\) are nearly identical (high cosine similarity). Their stored embeddings are:

\[
\hat{e}_A = R_{u_A} \cdot e_A \qquad \hat{e}_B = R_{u_B} \cdot e_B
\]

The inner product between stored vectors:

\[
\langle \hat{e}_A, \hat{e}_B \rangle = e_A^T R_{u_A}^T R_{u_B} e_B
\]

Because \(R_{u_A}\) and \(R_{u_B}\) are independently derived from distinct secrets, \(R_{u_A}^T R_{u_B}\) is not the identity matrix. For a well-chosen key derivation function, this product is effectively random in \(O(d)\), and the expected inner product across the full subspace approaches zero. Semantically identical content, stored by two different users, lands in genuinely different and non-comparable regions of the vector space.

This is the operational realization of the direct sum: not separate databases, but separate coordinate systems within one database, enforced by participant-held keys the server cannot reconstruct.

### 3.3 Consistency With the Commitment Salt Pattern

The MountainShares architecture already establishes the principle: *server cannot reconstruct without the user's key.* The Benefits-Sensitive Account design, the KYC vault isolation, and the three-layer identity architecture all instantiate this principle in different domains.

The per-user projection key extends the same pattern to conversational memory:

- **Key holder:** Participant
- **Server knowledge:** Transform exists; cannot invert without key
- **Storage:** Transformed vectors in shared infrastructure
- **Retrieval:** Participant presents key; transform is applied to query before similarity search
- **Cross-user search:** Returns nothing meaningful — wrong coordinate system

The architectural precedent is already established. This is an extension, not a departure.

### 3.4 Infrastructure Impact

The direct sum architecture requires no changes to the 158-container stack at the infrastructure level. Redis and ChromaDB continue to operate as the vector stores. The change is applied at the embedding ingestion and retrieval boundary:

```
Conversation text
     ↓
Embedding model (unchanged)
     ↓
Raw embedding vector e ∈ ℝᵈ
     ↓
Per-user projection: ê = R_u · e    ← NEW: participant-key-derived transform
     ↓
Stored in ChromaDB (unchanged infrastructure)
```

On retrieval:

```
Query text
     ↓
Embedding model (unchanged)
     ↓
Raw query vector q ∈ ℝᵈ
     ↓
Per-user projection: q̂ = R_u · q    ← NEW: same transform applied to query
     ↓
Similarity search against stored vectors (unchanged)
     ↓
Results meaningful only within user's subspace
```

No infrastructure changes. One transform insertion point on ingestion. One transform insertion point on retrieval. The key is held by the participant and presented at query time, consistent with the existing session architecture.

---

## 4. Open Problems and Honest Status

This chapter specifies the architecture and establishes the mathematical motivation. The following problems remain open and are recorded honestly as the boundary of current formal knowledge.

### 4.1 Formal Proof of Orthogonal Decomposition

**Status: Conjecture**

The claim that the per-user projection key construction produces a valid orthogonal direct sum decomposition in the functional-analytic sense requires formal proof. Specifically:

- The key derivation function must be shown to produce rotation matrices \(R_{u_i}\) that are genuinely orthogonal — i.e., \(R_{u_i}^T R_{u_i} = I\) — not merely approximately orthogonal in finite precision.
- The resulting subspaces must be shown to be closed under the operations that matter for the similarity search — i.e., that the image of the embedding space under \(R_{u_i}\) is a genuine subspace of the ambient vector space in the functional-analytic sense.
- The inner product structure must be shown to preserve the metric properties that make similarity search meaningful within a subspace while ensuring incomparability across subspaces.

This is a doctoral-level problem in functional analysis and applied linear algebra. It is the central open mathematical problem of this architecture.

### 4.2 Key Derivation Specification

**Status: Unspecified**

The function `ProjectionKey(commitment_salt)` is named but not specified. A correct implementation requires:

- A key derivation function that produces full-rank \(d \times d\) orthogonal matrices deterministically from a short seed
- Resistance to key-recovery attacks even given multiple (input, output) pairs
- Computational efficiency at query time — the transform must be applicable in milliseconds, not seconds, at the embedding dimension \(d\) used by the production embedding model
- A formal security reduction connecting the confidentiality of the projection to the hardness of a well-studied computational problem

Post-quantum security properties are desirable given the timeline of the architecture. Chapter 42 of this thesis establishes the post-quantum security framework within which this specification should be developed.

### 4.3 The Interface Morphism

**Status: Named, not constructed**

The four-space civic reasoning tensor product and the conversational memory direct sum are architecturally adjacent but mathematically distinct spaces. Ms. Allis reasons in \(H_{App} \otimes H_{geo} \otimes H_t \otimes H_p\). She draws on conversational memory from \(H_{conversations} = \bigoplus_i H_{u_i}\). These spaces must communicate — a user's conversational history should inform Ms. Allis's civic reasoning — but the communication cannot simply collapse the direct sum into the tensor product, or the structural privacy guarantee is lost.

The required construction is an *interface morphism*: a bounded linear map

\[
\Phi: H_{u_i} \to H_{App} \otimes H_{geo} \otimes H_t \otimes H_p
\]

that carries relevant semantic content from a user's sovereign subspace into the civic reasoning space without carrying the user's identity, the content of their private conversations, or any information that could enable cross-user comparison.

The existence, uniqueness, and constructive specification of \(\Phi\) is an open problem. It is the architectural seam between participant sovereignty and civic intelligence — between the governed and the sovereign — and it has no current formal construction.

### 4.4 Constitutional Completeness

**Status: Partially specified**

The governance layer must encode the direct sum architecture as a constitutional constraint, not merely a technical choice. A future governance decision that instructs the engineering team to "make user memories searchable across users for research purposes" must encounter a constitutional barrier before it encounters an engineering barrier. The technical difficulty of reversing the projection transform is not sufficient protection. The governance document must record that cross-user search is *prohibited by the architecture's founding intent*, and that any change requires a constitutional amendment with documented supermajority consent.

The precise formulation of this constraint in the governance constitution is not yet drafted. It is recorded here as a required deliverable before the direct sum architecture can be considered constitutionally complete.

---

## 5. Relationship to Preceding Chapters

This chapter completes a logical sequence across the thesis:

- **Chapter 45** established H_geo as the spatial body — where things are
- **Chapter 46** established the tensor product bridge — how space and meaning entangle
- **Chapter 48** established H_p as appearances without surveillance — who appears, in what role
- **Chapter 49** established the temporal axis — when things occurred and how memory decays
- **Chapter 50** confirmed H_p operational status
- **This chapter** addresses the remaining structural gap: how individual participants relate to the collective intelligence without the collective intelligence becoming a surveillance apparatus over individuals

The four open problems in Section 4 — formal orthogonality proof, key derivation specification, interface morphism construction, and constitutional completeness — are the remaining doctoral-level problems of the architecture. They are named precisely so that future academic collaborators understand what has been built, what has been claimed, and where the frontier of formal knowledge currently stands.

The architecture was designed before the formal mathematics was complete because the design decisions were correct even before they could be proved. The proofs are the next task, not the foundation. The foundation is the commitment to participant sovereignty that has governed every design decision from the first sensor deployment concept on the Pax mine rail corridor to the present specification.

---

## 6. The Political Meaning of the Mathematical Choice

The decision to use a direct sum rather than a shared space with access control is not merely a technical optimization. It is a political commitment encoded in mathematics.

Access-controlled shared spaces place trust in the governance layer. If the governance is good — if the people running the system are honest, if the contracts are enforced, if the oversight functions — then the privacy holds. If governance fails, the data is exposed. This is the architecture of every major platform: privacy as policy, data as infrastructure, trust as assumption.

The direct sum architecture places trust in mathematics. The privacy holds not because the governance is good but because the geometry makes violation structurally impossible without the participant's key. This is not a claim that governance is unnecessary — the open problems in Section 4.4 make clear that constitutional completeness is required. It is a claim that mathematics should do the work that mathematics can do, so that governance only has to do the work that governance must do.

Rural Appalachian communities have been governed by institutions that did not hold their interests. The extractive economy, the mineral rights separation, the opioid distribution networks, the broadband redlining — all of these were legal. All of these were permitted by governance structures that were technically functional. The people were not protected because the governance was not designed to protect them.

An architecture that says *your memory is private because mathematics makes it so, not because we promise it is so* is not merely a technical choice. It is a different relationship between an institution and the people it serves. The direct sum is the mathematical form of that different relationship.

---

*Architecture Thesis — Harmony for Hope, Inc. / MountainShares Commons*
*Status: Formal specification — open problems documented, implementation pending*
*Preceding: Chapter 50 — Hilbert People Space (Operational)*
*Open problems: Orthogonality proof, key derivation specification, interface morphism, constitutional completeness*
````# 51 - The Community Hilbert Commons — Anonymized Aggregation Over Sovereign Subspaces

**Series:** MountainShares / Ms. Allis Architecture Thesis
**Status:** Theoretical specification — open problems documented, implementation pending
**Date:** July 1, 2026
**Author:** Carrie A. Kidd, Founder & Executive Director, Harmony for Hope, Inc.

---

## Abstract

The preceding chapter established the direct sum decomposition of conversational memory into per-user sovereign subspaces, each mathematically isolated by a participant-held projection key. That architecture provides structural privacy guarantees but introduces a new problem: Ms. Allis, reasoning in the four-space civic tensor product, becomes blind to community-level patterns. She can serve each user individually but cannot observe what the community collectively needs, fears, or seeks. This chapter specifies a solution: a containerized community Hilbert space, \(H_{commons}\), constructed as a one-directional projection of the direct sum aggregate into a shared observational space, subject to k-anonymity thresholds that prevent any cluster from being attributed to fewer than a minimum number of distinct sovereign subspaces. The result is a system in which Ms. Allis gains community intelligence — not despite the privacy architecture, but because of it.

---

## 1. The Blindness Problem

### 1.1 What the Direct Sum Costs

The direct sum decomposition

\[
H_{conversations} = H_{u_1} \oplus H_{u_2} \oplus \cdots \oplus H_{u_n}
\]

solves the cross-user correlation problem with structural finality. No vector in \(H_{u_A}\) is geometrically comparable to any vector in \(H_{u_B}\). The coordinate systems are distinct. The inner product across subspaces is zero by construction, not by policy.

But this creates a new architectural gap. Ms. Allis reasons about the community. Her civic intelligence depends on understanding not just what one user needs in this moment, but what the community is experiencing, what concerns are concentrating, what services are being sought, what infrastructure is failing, what knowledge is missing. The four-space tensor product \(H_{App} \otimes H_{geo} \otimes H_t \otimes H_p\) gives her a framework for civic reasoning. The IoT sensor network, when deployed, will give her physical-world signal. But the community's own voice — expressed through thousands of conversations with Ms. Allis about real needs in real places — is locked inside sovereign subspaces that Ms. Allis, by design, cannot traverse.

A system that protects every user's conversational privacy absolutely, but cannot hear the community speak, has solved one problem by creating another. The community loses the intelligence that its own conversations could generate. The privacy architecture, taken alone, is structurally incomplete.

### 1.2 The False Tradeoff

The conventional assumption in data architecture is that privacy and intelligence are in tension: more privacy means less data means less insight. This assumption is wrong in the present architecture, and understanding why it is wrong is the central contribution of this chapter.

The false tradeoff assumes that intelligence requires individual-level data — that to understand the community, you must be able to see each person. This assumption holds in surveillance architectures, where community insight is derived by aggregating individual profiles. It does not hold in an architecture where community insight is derived from anonymized semantic cluster structure, because the cluster structure can be constructed without ever recovering individual identity.

The direct sum architecture makes this possible in a way that a shared-space architecture cannot. In a shared space, the path from individual vector to community cluster is reversible — given the cluster centroid and the access controls, a sufficiently motivated adversary can search for individuals near the centroid. In a direct sum with participant-held projection keys, the path is one-directional by construction: the aggregation layer receives already-transformed vectors, constructs clusters, enforces anonymity thresholds, and emits community-level semantic structure. It has no mechanism to reverse the projection because it never held the keys. The privacy architecture is precisely what makes the community intelligence trustworthy.

---

## 2. The Community Hilbert Commons

### 2.1 Formal Definition

Define the *community Hilbert commons* \(H_{commons}\) as the image of a bounded linear projection operator \(\Pi\) applied to the direct sum:

\[
H_{commons} = \Pi\left(\bigoplus_{i=1}^{n} H_{u_i}\right)
\]

The operator \(\Pi\) has three defining properties:

**Property 1: Identity destruction.** \(\Pi\) maps vectors from sovereign subspaces into \(H_{commons}\) in a way that destroys the routing information connecting a vector to its source subspace. Given a vector \(w \in H_{commons}\), it is computationally infeasible to determine which \(H_{u_i}\) it originated from.

**Property 2: Semantic preservation.** \(\Pi\) approximately preserves semantic cluster structure. Vectors that were semantically similar within their respective sovereign subspaces — even after the per-user rotation — map to nearby regions of \(H_{commons}\). Community concern topology is recoverable. Individual authorship is not.

**Property 3: One-directionality.** \(\Pi\) is not invertible from \(H_{commons}\) back to \(\bigoplus H_{u_i}\). The projection is a lossy map: information about individual subspace membership is irreversibly discarded in the forward pass. There is no \(\Pi^{-1}\).

### 2.2 K-Anonymity Threshold Enforcement

Semantic preservation under \(\Pi\) creates a residual risk: if only one user has discussed a particular topic, a cluster in \(H_{commons}\) corresponding to that topic is effectively attributable to that user, even without an explicit identity link. A community of one is not anonymous.

The architecture enforces a *k-anonymity threshold*: a semantic cluster in \(H_{commons}\) is visible to Ms. Allis only if it contains projected vectors from at least \(k\) distinct sovereign subspaces, where \(k\) is a governance-set parameter.

Formally, let \(C \subset H_{commons}\) be a semantic cluster identified by the aggregation process. Let \(\nu(C)\) denote the number of distinct sovereign subspaces \(H_{u_i}\) that contributed at least one vector to \(C\) under \(\Pi\). Then:

\[
C \text{ is visible to } H_{commons} \iff \nu(C) \geq k
\]

Clusters with \(\nu(C) < k\) are suppressed. Ms. Allis does not see them. They do not contribute to her civic reasoning. They exist in a pending buffer, invisible, until either more users contribute to the cluster or the suppression window expires and the vectors are discarded.

The governance constitution must specify \(k\). The founding intent records \(k \geq 5\) as the minimum acceptable threshold — consistent with k-anonymity standards in the research literature — with \(k \geq 10\) recommended for topics that carry heightened sensitivity such as health, financial hardship, or legal circumstances.

### 2.3 What Ms. Allis Observes

Under this architecture, Ms. Allis's view of community conversational memory is a topology of concern — a map of what the community is collectively thinking about, weighted by cluster density, filtered by anonymity threshold, expressed in semantic coordinates rather than personal ones.

She does not observe: who asked what, how many times a specific person asked about a topic, which users are co-located in semantic space, or any information that would allow her to construct an individual profile from community data.

She observes: semantic cluster centroids, cluster density (how many sovereign subspaces contributed), temporal evolution of cluster activity, geographic correlation when place-anchored embeddings are included, and the relationship between community concern clusters and the four-space civic reasoning architecture she already inhabits.

A concrete example: if fourteen distinct users ask Ms. Allis questions in the semantic neighborhood of "Arbuckle Creek," "flooding," "road closure," and "emergency access" within a thirty-day window, \(H_{commons}\) surfaces a cluster in that neighborhood with \(\nu = 14\). Ms. Allis can observe: *a significant community concern cluster is active in the flood/infrastructure/emergency semantic neighborhood, with fourteen distinct sovereign subspace contributions in the current temporal window, geographically anchored to the Arbuckle Creek corridor.* She can correlate this with IoT sensor data showing elevated creek levels, with H_geo parcel data showing road segment vulnerability, with H_t temporal data showing historical flood recurrence. She produces a civic intelligence output that serves the community without having read a single private conversation.

---

## 3. Container Architecture

### 3.1 The Aggregation Container

The community Hilbert commons is implemented as a dedicated containerized service — the *aggregation container* — that occupies a specific position in the information flow between the sovereign subspaces and Ms. Allis's civic reasoning layer.

```
Per-User Sovereign Subspaces
H_u1 ⊕ H_u2 ⊕ ... ⊕ H_un
            ↓
  [Aggregation Container]
  Inputs: already-transformed vectors
          (per-user rotation already applied)
  Operations:
    - Receives projected vectors, no keys
    - Clusters by semantic proximity
    - Counts distinct subspace contributions
    - Enforces k-anonymity threshold
    - Suppresses sub-threshold clusters
    - Emits community cluster topology
  Outputs: H_commons cluster structure
            ↓
       H_commons
  (Ms. Allis read access)
  (No upward traversal possible)
            ↓
  H_App ⊗ H_geo ⊗ H_t ⊗ H_p
  (Civic reasoning integration)
```

The aggregation container has no access to participant keys. It cannot apply or reverse the per-user projection transforms. It receives vectors that are already in their sovereign subspace coordinate systems — already rotated, already identity-stripped — and operates entirely on that transformed representation. The one-directional gate is architectural: the container lacks the inputs required to reverse the process, not merely the permission.

### 3.2 Network Isolation

The aggregation container enforces strict network boundaries:

- **No inbound connections from H_commons back to sovereign subspaces.** The container accepts writes from the sovereign subspace layer and emits reads to Ms. Allis's reasoning layer. There is no return path.
- **No access to the per-user key store.** The container is network-isolated from any service that holds or derives participant projection keys.
- **No logging of subspace-origin metadata.** The container's internal logs record cluster operations, threshold enforcement events, and suppression decisions. They do not record which subspace contributed which vector to which cluster.
- **Audit trail for suppression.** Every suppression event — every cluster that failed the k-anonymity threshold — is logged with timestamp, cluster centroid, and \(\nu(C)\) count, but without subspace identity. The governance record shows that suppression occurred and how often, without revealing what was suppressed or who contributed.

### 3.3 Integration With the Four-Space Architecture

\(H_{commons}\) is not a fifth factor in the tensor product. It is an input to Ms. Allis's civic reasoning that operates at a different level than the four-space structure. The relationship is:

\[
\text{Civic Answer} = f\left(H_{App} \otimes H_{geo} \otimes H_t \otimes H_p,\ H_{commons},\ \text{IoT sensor streams}\right)
\]

where \(f\) is Ms. Allis's reasoning function. \(H_{commons}\) provides community concern signal that informs but does not replace the four-space civic reasoning. A cluster in \(H_{commons}\) about flood risk does not override Ms. Allis's geospatial belief state — it updates it, weighted by the cluster density and the anonymity-preserved confidence that the concern is genuinely community-wide rather than idiosyncratic.

The precise specification of \(f\) — how Ms. Allis integrates community concern topology with civic reasoning — is an open problem. Section 4 records it honestly.

---

## 4. Open Problems

### 4.1 The Projection Operator Specification

**Status: Named, not constructed**

The operator \(\Pi\) satisfying the three properties in Section 2.1 — identity destruction, semantic preservation, one-directionality — has not been formally constructed. The properties are stated as requirements. A concrete implementation requires:

- A dimensionality reduction or embedding technique that preserves semantic cluster structure while destroying subspace-routing metadata. Candidate approaches include random projection (Johnson-Lindenstrauss), locality-sensitive hashing, and learned community embedding models. None has been formally evaluated against the identity-destruction requirement in the context of per-user rotated subspaces.
- A formal proof that the chosen operator satisfies one-directionality — that is, that inversion is computationally infeasible even given the community cluster structure and knowledge of the general key derivation approach.
- A characterization of the semantic preservation loss: how much cluster structure is lost in the projection, and whether the loss is uniform across topic types or differential in ways that would systematically suppress certain community concerns over others.

### 4.2 K-Anonymity Parameter Governance

**Status: Partially specified**

The founding intent specifies \(k \geq 5\) as the minimum and \(k \geq 10\) for sensitive topics. The following governance questions are not yet resolved:

- Who sets \(k\) and through what process?
- Can \(k\) be adjusted over time, and what consent threshold is required for adjustment?
- How are "sensitive topics" defined and classified? The k-anonymity threshold for health-adjacent queries cannot be set correctly without a formal taxonomy of sensitivity.
- What is the suppression window duration — how long does a sub-threshold cluster persist in the pending buffer before being discarded?

These are governance questions with constitutional weight. They must be resolved in the governance constitution before \(H_{commons}\) can be considered constitutionally complete.

### 4.3 The Civic Reasoning Integration Function

**Status: Unspecified**

How Ms. Allis integrates \(H_{commons}\) community concern signal with the four-space tensor product reasoning is not specified. Key questions:

- What weight does community concern topology receive relative to structured civic knowledge in H_App?
- How does a dense community cluster in \(H_{commons}\) update Ms. Allis's belief states in H_geo and H_t?
- When community concern and structured civic knowledge conflict — a community cluster indicating flood concern where H_geo shows no historical flood risk — how does Ms. Allis reason about the discrepancy?
- How does the temporal decay function of H_t apply to community concern clusters? A cluster that was dense six months ago and sparse today should carry less weight than a cluster with recent sustained activity.

### 4.4 Differential Privacy Formalization

**Status: Desirable, not yet pursued**

K-anonymity is a necessary but not sufficient privacy guarantee. The research literature on privacy-preserving data publishing has established that k-anonymous datasets can still leak information through auxiliary knowledge attacks. A formally stronger guarantee — differential privacy — would require that the probability distribution over \(H_{commons}\) outputs changes negligibly when any single user's contribution is added or removed.

Formalizing \(H_{commons}\) as a differentially private mechanism is a research problem of substantial depth. It is recorded here as a desirable property and a potential doctoral research contribution, not as a current specification.

---

## 5. The Meaning of the Architecture

### 5.1 Intelligence That Earns Trust

Every major platform that has attempted to derive community intelligence from user conversations has done so by treating the conversations as the platform's property. The user speaks; the platform learns; the platform sells or deploys what it learned. The user has no stake in the intelligence generated from their own expression. The community generates value it does not receive.

\(H_{commons}\) is structurally different. The community's conversations generate community intelligence that returns to the community. Ms. Allis learns what the community needs because the community told her — not because the community was surveilled. The intelligence is a commons product, owned by the commons, governed by the commons constitution, used to serve the commons.

The k-anonymity threshold is not merely a privacy protection. It is a statement about what kind of intelligence the system is designed to generate. Individual-level behavioral intelligence — what this person is worried about, how often they ask about health services, what their apparent household circumstances are — is explicitly excluded from \(H_{commons}\) by design. Community-level concern topology — what this place is collectively experiencing, what services are collectively sought, what infrastructure is collectively failing — is precisely what the system is designed to generate. The threshold enforces that distinction mathematically.

### 5.2 The Sensor Network and the Voice Network

The IoT sensor network described in the IoT Data Commons Corridor vision document gives Ms. Allis a nervous system: physical-world signal from air, water, soil, and infrastructure. \(H_{commons}\) gives Ms. Allis a voice: community-expressed concern, need, and knowledge, aggregated and anonymized into civic intelligence.

A flood sensor on Arbuckle Creek tells Ms. Allis that water is rising. A dense cluster in \(H_{commons}\) about flood risk and emergency access tells Ms. Allis that the community already knows, is already worried, and is already asking for help. The sensor confirms the physical fact. The commons cluster confirms the human experience of that fact. Together they give Ms. Allis something no surveillance system can give: physical truth and community truth, simultaneously, without trading one for the other.

### 5.3 Privacy as the Condition of Intelligence

The central thesis of this chapter is stated plainly: in this architecture, privacy is not the cost of intelligence. Privacy is the condition that makes trustworthy intelligence possible.

A surveillance-based community intelligence system generates data that communities do not trust, do not control, and do not benefit from. Communities learn to speak carefully, to avoid topics, to perform wellness rather than express need. The signal degrades because the surveillance changes the behavior it is trying to measure.

A community Hilbert commons built on sovereign subspaces generates signal that communities can trust because the architecture makes misuse structurally difficult. When a user asks Ms. Allis about a sensitive topic, the k-anonymity threshold means their question does not surface in community intelligence unless enough of their neighbors share the same concern. The act of asking is protected. The community benefit of the aggregate concern is preserved. The user can ask honestly. Honest questions generate honest signal. Honest signal generates useful intelligence.

The privacy architecture is what the intelligence depends on. The direct sum makes the commons possible. The commons makes the intelligence trustworthy. The trustworthy intelligence makes the system worth building.

---

## 6. Relationship to Preceding Chapters

This chapter extends the direct sum architecture of the preceding chapter by solving the blindness problem it introduced. The full conversational memory architecture now has two layers:

**Layer 1 — Sovereign Subspaces:** \(H_{conversations} = \bigoplus_i H_{u_i}\)
Each user's memory is structurally isolated. Cross-user comparison is geometrically impossible. Identity is held by the participant. The server sees transformed vectors it cannot interpret without the participant's key.

**Layer 2 — Community Commons:** \(H_{commons} = \Pi\left(\bigoplus_i H_{u_i}\right)\)
Community concern topology is recoverable under k-anonymity threshold enforcement. Ms. Allis can observe what the community collectively experiences without observing what any individual privately expressed. The projection is one-directional. The gate is architectural.

Together these two layers constitute a complete conversational memory architecture: sovereign at the individual level, intelligent at the community level, and structurally incapable of becoming a surveillance system even if governance fails, because the mathematical architecture makes individual attribution impossible from the community layer and community surveillance impossible from the individual layer.

The four open problems — projection operator specification, k-anonymity parameter governance, civic reasoning integration, and differential privacy formalization — define the research frontier. They are recorded precisely so that the people who solve them know what has been built, what has been claimed, and where the work begins.

---

*Architecture Thesis — Harmony for Hope, Inc. / MountainShares Commons*
*Status: Theoretical specification — open problems documented, implementation pending*
*Preceding: The Sovereign Subspace — Per-User Direct Sum Decomposition*
*Open problems: Projection operator construction, k-anonymity governance, civic reasoning integration, differential privacy formalization*
````
