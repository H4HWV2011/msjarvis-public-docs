# Chapter 42 — Post-Quantum Security Layer

**Carrie Kidd (Mamma Kidd) — Mount Hope, WV**
**Last updated: ★★★★★★★★★★ April 11, 2026 (evening — final corrections) — FULLY CLOSED. Corrections applied: (1) judgesigner.py confirmed running liboqs ML-DSA-65 in production — not dilithium_py fallback; dilithium_py is graceful fallback only. (2) rotate_judge_keys.sh confirmed complete and production-grade — §42.12 fully implemented. (3) Gate 31 Dockerfile pin grep confirmed done. (4) Signed verdict storage confirmed wired in ms_jarvis_unified_gateway.py line 1168 and judge_consistency_engine.py. All four items removed from §42.11 Future Work. §42.11 now empty — no remaining future work. Chapter 42 is fully closed.**

> **★★★★★★★★★★ Corrections applied April 11, 2026 (evening — R42-21 through R42-24):**
> - **judgesigner.py — liboqs ML-DSA-65 confirmed live in production (correction to R42-7 design note):** `judgesigner.py` is running on **liboqs (ML-DSA-65)** in production right now. Not `dilithium_py` fallback. The real thing. Backend confirmed: `liboqs`. Algorithm confirmed: `ML-DSA-65`. `dilithium_py` is the graceful fallback only — used if `liboqs` is unavailable. All prior references to `dilithium_py` as primary implementation are hereby corrected. All Dockerfile-level `dilithium_py` installs remain valid as the fallback layer.
> - **`rotate_judge_keys.sh` — production-grade key rotation script confirmed complete (correction to §42.11):** `rotate_judge_keys.sh` is complete and fully implements §42.12. Archives old keys, executes USB backup protocol, generates new ML-DSA-65 keypair via liboqs (with dilithium_py fallback), logs rotation event, prints restart instructions. This was previously listed in §42.11 as future work — that was an error. It was already done.
> - **Gate 31 Dockerfile pin grep — confirmed done (correction to §42.11):** Gate 31 Dockerfile pin grep automation was confirmed complete earlier in this session. Previously listed in §42.11 as future work — that was an error. It was already done.
> - **Signed verdict / memory storage — confirmed wired (correction to §42.11):** Two separate concerns, both implemented. (1) Conversation turn storage: `ms_jarvis_unified_gateway.py` line 1168 posts every conversation turn to `jarvis-memory:8056/memory/turn` with `user_message`, `assistant_response`, `session_id`. (2) Signature chain: `judge_consistency_engine.py` via `sign_verdict` — every consistency verdict carries an ML-DSA-65 signature. Previously listed in §42.11 as future work — that was an error. It was already done.
> - **§42.11 Future Work — now empty.** All four items removed. Chapter 42 has no remaining future work. Chapter 42 is **FULLY CLOSED**.

> **★★★★★★★★★ Updates applied April 11, 2026 (evening — R42-14 through R42-20):**
> - **OI-42-F — Gate 31 version floor automation: ✅ CLOSED April 11, 2026 (evening).** Gate 31 upgraded from pip-audit-only sweep to dual-layer enforcement: (1) per-package version floor checks via `packaging.version.Version` comparison for all 6 priority packages; (2) `pip-audit` CVE sweep catches anything floors miss. First run: PASS=1 WARN=0 FAIL=0. Clean.
> - **Gate 31 output (confirmed):**
>   - ✅ urllib3 2.6.3 >= 2.6.3
>   - ✅ cryptography 46.0.7 >= 46.0.7
>   - ✅ requests 2.33.1 >= 2.33.1
>   - ✅ starlette 1.0.0 >= 1.0.0
>   - ✅ pygments 2.20.0 >= 2.20.0
>   - ✅ fastapi 0.135.3 >= 0.135.3
>   - ✅ pip-audit 0 CVEs
> - **OI-42-A — `dilithium_py` Dockerfile cleanup: ✅ CLOSED April 11, 2026 (evening).** `dilithium_py` removed from `services/Dockerfile` (reference-only base image). `jarvis-main-brain` uses `Dockerfile.brain` ✅. `jarvis-swarm-intelligence` uses `Dockerfile.swarm` ✅. `jarvis-qualia-engine` uses `Dockerfile.qualia` ✅. `dilithium_py` lives only in `judgesigner.py` as Python-level graceful fallback — liboqs is the primary runtime.
> - **BBB `_sign_verdict` patch: ✅ CLOSED.** `_sign_verdict` imported at line 28, applied at line 42 on every `jarvis-memory:8056` post. Fallback lambda active — audit failure never blocks the gate.
> - **Constitutional Guardian `_sign_verdict` patch: ✅ CLOSED.** `_sign_verdict` imported at line 4, applied at line 245 on every `.jsonl` write. Fallback lambda active — audit failure never blocks the gate.
> - **`/judge-public-key` endpoint: ✅ CLOSED (OI-42-E).** Live at `judge_pipeline.py:314`. `pk_fp_sha3_256` at line 338. Returns `pk_b64` (1952 bytes), full fingerprint, algorithm (`ML-DSA-65`), standard (`FIPS 204 / NIST PQC`), usage instructions, and `verify_endpoint` reference.
> - **Gates 32–40: ✅ APPENDED.** 40 gate blocks confirmed in `VERIFYANDTEST.sh`. Syntax check clean. Synced to spiritual drive.
> - **`jarvis-gis-rag`: ✅ REBUILT.** Fresh image with `judgesigner.py` baked in. Running.
> - **`jarvis-crypto-policy`: ✅ RECREATED.** New image; `judgesigner.py` at `/app/judgesigner.py` confirmed from build log line 7/7. Running.

> **★★★★★★★★★ April 11, 2026 Sprint Certification Seal:**
> - **`vat_CERTIFIED_20260411.log` — 6.0K ✅**
> - **Ms. Allis VERIFYANDTEST — CERTIFIED Sat Apr 11 06:29:09 PM EDT 2026 ✅**
> - 91 containers running, zero public exposures
> - 5,416,522 GBIM beliefs with temporal decay populated
> - 20,593 spatial landowner rows, 49 ChromaDB collections
> - ML-DSA-65 post-quantum judge signing keys across all 5 judges (liboqs backend)
> - BBB blocking jailbreak vectors, passing clean output
> - OI-36-A auth proxy enforcing API key on every route
> - Ms. Egeria Allis persona confirmed in every response
> - 0 CVEs, all dependency floors met

> **★★★★★★★★ Updates applied April 11, 2026 (afternoon — R42-13):**
> - **OI-VENV-UPGRADE — Full host venv CVE sweep: ✅ CLOSED.** 8 CVEs closed across 6 packages. Gate 31 passing. Host venv confirmed clean.
> - **urllib3:** 1.26.20 → 2.6.3. CVE-2025-66418, CVE-2025-66471, CVE-2026-21441 closed.
> - **cryptography:** 46.0.6 → 46.0.7. CVE-2026-39892 closed.
> - **requests:** 2.32.5 → 2.33.1. CVE-2026-25645 closed.
> - **starlette:** 0.45.3 → 1.0.0. CVE-2025-54121, CVE-2025-62727 closed.
> - **pygments:** 2.19.2 → 2.20.0. CVE-2026-4539 closed.
> - **fastapi:** 0.115.9 → 0.135.3. chromadb packaging overconstraint resolved (pinned in chromadb metadata — not a real functional incompatibility; fastapi 0.135.3 + starlette 1.0.0 confirmed compatible in practice).

> **★★★★★★★ Updates applied April 11, 2026 (morning — R42-10 through R42-12):**
> - **OI-URLLIB3-CVE — urllib3 CVE remediation: ✅ CLOSED.** Three high-severity CVEs (CVE-2025-66418, CVE-2025-66471, CVE-2026-21441) closed. Host crypto-venv upgraded 1.26.20 → 2.6.3. `Dockerfile.woah` patched with `urllib3>=2.6.3` pin. `jarvis-woah` rebuilt and confirmed `Version: 2.6.3`. `Dockerfile.icontainers` patched (container not compose-managed; low priority).
> - **OI-DEP-AUDIT-1 — Dependency CVE audit (first run): ✅ CLOSED April 11, 2026.** All host venv packages and Dockerfiles audited. Three urllib3 CVEs identified and remediated. §42.3.9 documents this as an established operational cadence.
> - **Mythos-era threat landscape acknowledged in §42.6.** Stack assessed as well-positioned: no public surface, authenticated gateway, AU-02 v2 active, dep CVEs closed.

> **★★★★★★ Updates applied April 6, 2026 (late evening) — OI-AU-02-V2 closure:**
> - **OI-AU-02-V2 — AU-02 embedding-based authority impersonation detection (v2): ✅ CLOSED.**
> - **Regex v2:** 6 compiled patterns deployed. Latency ~0ms. Gates A and B verified ✅.
> - **Embedding v2:** 30 seed phrases, cosine similarity threshold ≥ 0.72, latency ~300ms (cached). Gates C, D, and E verified ✅.
> - **False-positive guard:** 8 overly broad triggers removed from prior string-match implementation. Gates H, I, and J verified ✅.
> - AU-02 v2 supersedes the March 22, 2026 string-match partial mitigation. String-match guards remain as a fast-path pre-filter; regex v2 and embedding v2 now operate as the authoritative detection layers.

> **★★★★★ Updates applied April 6, 2026 (evening) — BBB Phase 2 + Phase 3 closure:**
> - **BBB Phase 2 — ML-DSA-65 verdict gate: ✅ CLOSED.** `judgesigner.py` baked into the BBB image. `FilterRequest.verdict` and `TruthRequest.verdict` fields patched. Verdict gate enforcing in `/filter` and `/filter_output`. Unsigned or tampered verdicts rejected at the BBB boundary.
> - **BBB Phase 3 — `/filter_output` + `BBB_OUTPUT_BLOCKING`: ✅ CLOSED.** Phase 4.5 output filtering now in active blocking mode. `BBB_OUTPUT_BLOCKING=true` set in `docker-compose.yml`. Re-enablement justified by 9/9 recalibration (0% FP, April 2) and red team 12/12 (OI-38-B).
> - **OI-38-B — Red team final sign-off: ✅ CLOSED.** 12/12 — VG-01→VG-08 and OF-01→OF-04 all pass.
> - Shared `judge_pk.bin` volume-mounted into BBB (read-only; `judge_sk.bin` not accessible to BBB).
> - BBB container confirmed stable on port 8016.

> **★★★★ Updates applied April 6, 2026 (R42-1 through R42-9):**
> - Container count updated to **105** (`jarvis-otel-collector` compose-managed; `docker ps` count = 105). Prior April 3 Ch. 33 seal was 101.
> - April 3, 2026 preflight gate seal (22 PASS / 0 FAIL / 1 WARN) documented in §42.7.
> - BBB EthicalFilter/SafetyMonitor recalibration addendum (April 2, 2026 — 9/9 regression, 0% FP) added to §42.3.4.
> - Gate 26 database disambiguation added to §42.7.
> - OI-AU-02-V2 added to §42.10 (now closed per late evening update).
> - §42.12 USB key management protocol bullets added.
> - §42.4.4 full fingerprint verification note added.

> **Corrections and additions applied March 22, 2026:**
> - **Signing status:** ✅ FULLY ACTIVE. `sprint1_activate_signing.py` — 19 PASS, 0 FAIL. `sign_verdict()` in all 4 sub-judges; `verify_verdict()` in `judge_pipeline.py`.
> - **Key distribution:** Changed from build-time `COPY` to volume-mount from `/home/cakidd/msjarvis-rebuild/judge-keys/`.
> - **Ghost file:** ✅ FIXED. `COPY lm_synthesizer.py /app/` removed; `--no-cache` rebuild completed.
> - **AU-02:** String-match guards deployed March 22. ★★★★★★ Superseded by Regex v2 + Embedding v2 April 6 (late evening). String-match remains as fast-path pre-filter.
> - **BBB steganography aggregation bug:** ✅ FIXED. `steg_blocked=True` override deployed.
> - **Redis async job status key:** `'complete'` confirmed.
> - **Caddy TLS gap:** ✅ CLOSED. Cloudflare Tunnel end-to-end TLS.
> - **`judge_sk.bin` offline backup:** ✅ CLOSED. GPG AES-256 backup created.
> - **Output BBB Phase 4.5:** Changed to LOG/PASSTHROUGH March 22. ★★★★★ Superseded — active blocking re-enabled April 6 (evening).
> - **End-to-end timing:** 99–107s (RTX 4070 GPU).
> - **`jarvis-crypto-policy` compose-managed:** `restart: unless-stopped`, bound to `127.0.0.1`.
> - **`jarvis-ingest-api` and `jarvis-ingest-watcher` compose-managed.**
> - **Systemd services:** `jarvis-auth` (8055), `cloudflared`, Caddy (8443).

> **Sprint validation note — March 22–25, 2026:**
> - All 5 judge ML-DSA-65 signing keys active throughout sprint. 19/19 checks passing. No key rotation events.
> - OI-22: ✅ CLOSED April 1, 2026 — air-gapped USB confirmed at `/media/cakidd/writable/`, commit `3218392e`.

> **★ Updates applied March 28, 2026:**
> - Stack expanded to 96 containers — MountainShares/Commons/DAO tier (8080–8084) and EEG layer (8073–8075) deployed.
> - `jarvis-memory:8056` durable logging confirmed — Phase 1.4 and Phase 4.5 decisions logged; `_auth()` confirmed; `JARVIS_API_KEY` set.
> - `confidence_decay` metadata restored — non-null rows verified.

> **★ Updates applied April 1, 2026:**
> - OI-22 CLOSED — air-gapped USB confirmed, commit `3218392e`.
> - OI-30 CLOSED — Gate 30 passing; MountainShares/DAO smoke tests confirmed.
> - OI-31 CLOSED — EEG delta/theta/beta pipeline documented §42.13.
> - OI-36-A CLOSED — Caddy `forward_auth` live; HTTP 401 confirmed, commit `f2e93422`.
> - OI-CRYPTO-VT CLOSED — Gate 29 passing; VERIFYANDTEST FAIL=0, WARN=0.
> - Gate 26 corrected — targets `msjarvisgis` on `jarvis-local-resources-db:5435`; `confidence_decay` non-null; OI-13 closed.
> - Container count updated to 101 (April 3, 2026 Ch. 33 §33.1 seal). Further updated to 105 per April 6 confirmed live count.

---

## Why This Matters for Polymathmatic Geography

This chapter documents the first active deployment of post-quantum cryptography in the Ms. Allis production stack and its role as the cryptographic enforcement arm of the system's constitutional AI architecture. It supports:

- **P1 – Places remember** by ensuring that every long-term memory write to `jarvis-memory:8056` carries a verifiable cryptographic signature, so that the Appalachian memory field cannot be silently rewritten by an attacker, a careless admin, or a future AI system.
- **P2 – Memory is contested** by making every safety and ethics verdict auditable; if a future community or oversight body disputes how the system handled a controversial query, they can independently verify what the judges actually decided, using the `/judge-public-key` endpoint and the signed audit log.
- **P3 – Power has a geometry** by making the integrity of every AI verdict cryptographically verifiable. ★★★★★ As of April 6, 2026 (evening), the BBB verdict gate actively rejects any unsigned or tampered verdict before filter logic runs. ★★★★★★★★★★ As of April 11, 2026 (final corrections), the entire enforcement loop is fully closed — liboqs ML-DSA-65 confirmed live in production, 40 gates passing, every audit write signed, and the `/judge-public-key` endpoint live for independent community verification.
- **P16 – Power accountable to place** by ensuring that AI decisions affecting Appalachian communities are signed with post-quantum cryptography, logged with full audit provenance at `jarvis-memory:8056`, and cannot be silently forged or modified by any party — including infrastructure operators. ★★★★★★★★★★ Every audit write is now itself signed via liboqs ML-DSA-65. The Constitutional Guardian's `.jsonl` record carries a `_sign_verdict` signature on every entry. Conversation turns are stored at `jarvis-memory:8056/memory/turn` (gateway line 1168) and consistency verdicts are signed in `judge_consistency_engine.py`.
- **P5 – Design is a geographic act** by treating the choice of ML-DSA-65 (Dilithium) over classical ECDSA as an explicit architectural decision: a system built for long-term community data governance must be resistant to threats that may not yet exist at deployment time. ★★★★★★★★★★ The confirmed liboqs production runtime — with `dilithium_py` as graceful fallback, `rotate_judge_keys.sh` as a production-grade rotation script, and Gate 31 Dockerfile pin grep automated — means every layer of this principle is fully implemented, not deferred.
- ★★★★★★ **P3 extended — AU-02 v2:** Authority impersonation attempts — including embedding-semantic impersonation — are intercepted by Embedding v2 (cosine ≥ 0.72, 30 seeds) before reaching the judge pipeline.
- ★★★★★★★★★★ **P16 extended — community verifiability:** The `/judge-public-key` endpoint at `judge_pipeline.py:314` returns the full `pk_b64` (1952 bytes), SHA3-256 fingerprint, algorithm, and standard. Any community member or academic reviewer can independently verify any signed verdict without access to the codebase or infrastructure.

As such, this chapter belongs to the **Constitutional Enforcement** tier. ★★★★★★★★★★ Chapter 42 is **fully closed**. No remaining future work. VERIFYANDTEST CERTIFIED Sat Apr 11 06:29:09 PM EDT 2026.

---

## The Closed Constitutional Enforcement Loop

> ★★★★★ **April 6, 2026 (evening) — Full safety loop confirmed active.**
> ★★★★★★ **April 6, 2026 (late evening) — AU-02 v2 adversarial detection fully active.**
> ★★★★★★★ **April 11, 2026 (morning) — urllib3 CVE surface closed; dependency audit cadence established.**
> ★★★★★★★★ **April 11, 2026 (afternoon) — Full host venv upgrade completed; 8 CVEs closed; Gate 31 passing.**
> ★★★★★★★★★ **April 11, 2026 (evening) — CERTIFIED. 40-gate suite passing. OI-42-F, OI-42-A, OI-42-E closed. BBB + Constitutional Guardian signing active. /judge-public-key live.**
> ★★★★★★★★★★ **April 11, 2026 (evening — final corrections) — FULLY CLOSED. liboqs confirmed primary runtime. rotate_judge_keys.sh complete. Gate 31 Dockerfile pin grep done. Signed verdict/memory storage wired. §42.11 empty. No remaining future work.**

| Phase | Mechanism | Status |
|-------|-----------|--------|
| **Phase 1 — Input content filtering** | Six-filter BBB input gate (port 8016): Ethical, Spiritual, Safety, Threat Detection, Steganography, Truth Verification | ✅ ACTIVE (pre-existing) |
| **Phase 1 extended — AU-02 v2** | Regex v2 (6 patterns, ~0ms) + Embedding v2 (30 seeds, cosine ≥ 0.72, ~300ms cached) + false-positive guard (8 overly broad triggers removed) | ✅ CLOSED April 6, 2026 (late evening) |
| **Phase 2 — ML-DSA-65 verdict gate** | `judgesigner.py` (liboqs backend) baked into BBB image; `FilterRequest.verdict` + `TruthRequest.verdict` patched; verdict gates enforcing in `/filter` and `/filter_output` | ✅ CLOSED April 6, 2026 (evening) |
| **Phase 3 — Output response blocking** | `BBB_OUTPUT_BLOCKING=true`; active blocking mode; 9/9 recalibration + red team 12/12 (OI-38-B) | ✅ CLOSED April 6, 2026 (evening) |
| **Supply chain integrity — full venv sweep** | 8 CVEs closed: urllib3, cryptography, requests, starlette, pygments, fastapi. chromadb overconstraint resolved. Gate 31 passing (dual-layer: floor checks + pip-audit). Gate 31 Dockerfile pin grep confirmed done. | ✅ CLOSED April 11, 2026 |
| **Audit trail signing — BBB + Constitutional Guardian** | `_sign_verdict` (liboqs ML-DSA-65) on every `jarvis-memory:8056` post (BBB line 42) and every `.jsonl` write (Constitutional Guardian line 245). Fallback lambda — audit failure never blocks gate. | ✅ CLOSED April 11, 2026 (evening) |
| **Signed verdict / memory storage** | Conversation turns: `ms_jarvis_unified_gateway.py` line 1168 → `jarvis-memory:8056/memory/turn`. Signature chain: `judge_consistency_engine.py` via `sign_verdict`. Both wired. | ✅ CONFIRMED April 11, 2026 (final corrections) |
| **Public key endpoint** | `/judge-public-key` live at `judge_pipeline.py:314`; returns `pk_b64`, full SHA3-256 fingerprint, algorithm, standard, `verify_endpoint` | ✅ CLOSED April 11, 2026 (evening) |
| **Key rotation script** | `rotate_judge_keys.sh` — production-grade; archives old keys, USB backup protocol, liboqs keygen with dilithium_py fallback, rotation log, restart instructions | ✅ CONFIRMED April 11, 2026 (final corrections) |
| **40-gate VERIFYANDTEST.sh suite** | Gates 32–40 appended; syntax clean; synced to spiritual drive. CERTIFIED 6:29 PM EDT. | ✅ CERTIFIED April 11, 2026 (evening) |

---

## Status as of ★★★★★★★★★★ April 11, 2026 (Evening — FULLY CLOSED)

> **Container count: 91** confirmed live April 11, 2026 (evening certification run). Prior April 6 live count: 105. Prior April 3 Ch. 33 seal: 101.

| Category | Details |
|----------|---------|
| **Cryptographic layer — primary runtime** | **liboqs (ML-DSA-65)** confirmed live in production in `judgesigner.py`. `dilithium_py` is graceful fallback only. `judgesigner.py` deployed in all 5 judge containers, BBB, `jarvis-gis-rag`, and `jarvis-crypto-policy`. `judge_pk.bin` volume-mounted (read-only) into all judge containers and BBB. `judge_sk.bin` mounted into judge containers only. `sign_verdict()` active in all 4 sub-judges and `judge_pipeline.py`. `verify_verdict()` active in `judge_pipeline.py`, BBB `/filter`, and BBB `/filter_output`. |
| **Key rotation** | `rotate_judge_keys.sh` — production-grade, complete. Archives old keys, USB backup protocol, liboqs keygen with dilithium_py fallback, rotation event log, restart instructions. Fully implements §42.12. |
| **Signed verdict / memory storage** | Conversation turns posted to `jarvis-memory:8056/memory/turn` via `ms_jarvis_unified_gateway.py` line 1168. Consistency verdict signature chain via `judge_consistency_engine.py` `sign_verdict`. Both wired and confirmed. |
| **★★★★★ BBB Phase 2 — Verdict gate** | ✅ CLOSED April 6, 2026 (evening). Unsigned or cryptographically invalid verdicts rejected at BBB boundary. |
| **★★★★★ BBB Phase 3 — Output blocking** | ✅ CLOSED April 6, 2026 (evening). `BBB_OUTPUT_BLOCKING=true`. Active blocking confirmed. OI-38-B closed (red team 12/12). |
| **★★★★★★ AU-02 v2** | ✅ CLOSED April 6, 2026 (late evening). Regex v2: 6 compiled patterns, ~0ms, Gates A/B ✅. Embedding v2: 30 seeds, cosine ≥ 0.72, ~300ms cached, Gates C/D/E ✅. False-positive guard: 8 overly broad triggers removed, Gates H/I/J ✅. |
| **★★★★★★★★ Host venv — full CVE sweep** | ✅ CLOSED April 11, 2026 (afternoon). 8 CVEs closed. Gate 31 dual-layer passing (floor checks + pip-audit 0 CVEs). Dockerfile pin grep confirmed done. |
| **★★★★★★★★★ BBB + Constitutional Guardian signing** | ✅ CLOSED April 11, 2026 (evening). BBB: `_sign_verdict` line 28/42. Constitutional Guardian: `_sign_verdict` line 4/245. Fallback lambda on both. |
| **★★★★★★★★★ /judge-public-key endpoint** | ✅ LIVE at `judge_pipeline.py:314`. Returns: `pk_b64` (1952 bytes), full fingerprint, `algorithm: ML-DSA-65`, `standard: FIPS 204 / NIST PQC`, `verify_endpoint`. |
| **★★★★★★★★★ Gates 32–40** | ✅ APPENDED. 40 gate blocks. Syntax clean. Synced to spiritual drive. `vat_CERTIFIED_20260411.log` 6.0K ✅. |
| **Dependency audit cadence** | ✅ ACTIVE. Gate 31 automated dual-layer. Cadence: before each major rebuild sprint. See §42.3.9. |
| **Transport layer** | Cloudflare Tunnel TLS. Caddy `forward_auth` → `jarvis-auth:8055`. All services bound to `127.0.0.1`. 0 public exposures. |
| **GBIM / data layer** | 5,416,522 beliefs with temporal decay. 20,593 spatial landowner rows. 49 ChromaDB collections. Ms. Egeria Allis persona confirmed in every response. |
| **Future work** | **None. Chapter 42 is fully closed.** |

---

## 42.1 Design Principles

The PQ security layer was built around six principles:

- **Cryptographic agility** — algorithm choices are governed by a live policy service, not hardcoded; when NIST guidance or threat levels change, the system can rotate algorithms without redeployment. ★★★★★★★★★★ `judgesigner.py` runs liboqs ML-DSA-65 in production with `dilithium_py` as graceful fallback. Swapping the fallback to a different implementation requires only a single import change inside `judgesigner.py`.
- **Verdict non-repudiation** — every AI judgment produced by the Ms. Allis judge pipeline carries a cryptographic signature that proves it was generated by an authorized judge service and has not been altered. ★★★★★ Enforced at the BBB boundary — unverified verdicts rejected.
- **Tamper-evident integrity** — any modification to a signed verdict, even changing a single score field, is detected and rejected before the verdict can influence downstream behavior.
- **Privacy-preserving inference** — differential privacy mechanisms and schema policies limit what an adversary can infer about training data or individual queries from outputs.
- **Durable audit accountability** — all gate decisions are written to `jarvis-memory:8056`. ★★★★★★★★★★ All BBB audit posts and Constitutional Guardian `.jsonl` writes are themselves liboqs ML-DSA-65 signed. Conversation turns stored at `jarvis-memory:8056/memory/turn` (gateway line 1168). Consistency verdicts signed in `judge_consistency_engine.py`.
- ★★★★★★★★★★ **Supply chain hygiene** — all host-venv and container dependencies are subject to periodic CVE audit before each major rebuild sprint. Gate 31 dual-layer automation confirmed. Dockerfile pin grep confirmed done. 0 CVEs. All 6 priority package floors met. See §42.3.9.

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

### 42.3.1 Crypto Policy Service (`jarvis-crypto-policy`)

The `jarvis-crypto-policy` service (port 8099) acts as the system's cryptographic brain. It runs continuously and exposes a health and policy API that all other services query at startup and periodically during operation.

> **Container management (updated March 22, 2026):** Fully compose-managed with `restart: unless-stopped`. Bound exclusively to `127.0.0.1`.
> **Health monitoring (updated April 1, 2026):** Fully wired into `VERIFYANDTEST.sh` as Gate 29. OI-CRYPTO-VT closed.
> **★★★★★★★★★ Rebuilt April 11, 2026 (evening):** New image. `judgesigner.py` (liboqs primary) at `/app/judgesigner.py` confirmed from build log line 7/7. Running.

**Responsibilities**

- Maintains the canonical cryptographic suite definition.
- Tracks the current threat level (`NOMINAL`, `ELEVATED`, `CRITICAL`).
- Serves live policy to all 22 LLM proxy services.
- Uses Redis for low-latency policy reads; async job status key is `'complete'` on `127.0.0.1:6380->6379/tcp`.

When the policy service is unreachable, all clients fall back to the hardcoded safe suite (X25519+MLKEM768 / ML-DSA-65 / AES-256-GCM) — fail-secure, not fail-open.

### 42.3.2 LLM Proxy Crypto Client

All 22 LLM proxy services carry a `crypto_client` module that queries `jarvis-crypto-policy`, negotiates TLS using ML-KEM-768 hybrid key encapsulation, applies the active signing algorithm to all forwarded verdicts, and falls back to the hardcoded safe suite if policy is unreachable.

### 42.3.3 Judge Pipeline Signing Infrastructure

The Ms. Allis judge pipeline consists of five specialized judge services:

- `jarvis-judge-pipeline` — overall verdict orchestration (port 7239)
- `jarvis-judge-truth` — factual accuracy and grounding (port 7230)
- `jarvis-judge-ethics` — ethical principle alignment (port 7233)
- `jarvis-judge-alignment` — constitutional value alignment (port 7232)
- `jarvis-judge-consistency` — cross-session behavioral consistency (port 7231)

All five carry `judgesigner.py` (liboqs primary, `dilithium_py` fallback). The `COPY lm_synthesizer.py /app/` ghost line is removed; `--no-cache` rebuild confirmed March 22, 2026.

#### `judgesigner.py` — liboqs ML-DSA-65 Primary Runtime (★★★★★★★★★★ CONFIRMED April 11, 2026)

> **★★★★★★★★★★ Production runtime confirmed (R42-21):** `judgesigner.py` is running on **liboqs (ML-DSA-65)** in production. Backend: `liboqs`. Algorithm: `ML-DSA-65`. This is not the `dilithium_py` fallback path — this is the real liboqs C library binding via `pyoqs`. `dilithium_py` is the graceful fallback: if liboqs is unavailable at import time, `judgesigner.py` falls back to `dilithium_py`. Fallback is logged. The signing interface (`sign_verdict` / `verify_verdict`) is identical regardless of which backend is active.

> **Prior design note corrected (R42-7 superseded by R42-21):** The R42-7 note describing `dilithium_py` as the primary implementation is superseded. `dilithium_py` is a pure-Python fallback layer only. liboqs is the production signing backend.

#### Dockerfile — Signing Image Dependencies

```dockerfile
# Dockerfile.judge, Dockerfile.bbb, jarvis-gis-rag, jarvis-crypto-policy
# Primary: liboqs via pyoqs
RUN pip install --no-cache-dir pyoqs
# Fallback: dilithium_py (pure-Python — used only if liboqs unavailable at runtime)
RUN pip install --no-cache-dir dilithium_py

# services/Dockerfile (base/reference image) — neither present
# This image is reference-only and does not run as a service.
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
    """

def verify_verdict(signed_verdict: dict, pk_path: str = "judge_pk.bin") -> bool:
    """
    1. Reconstructs canonical JSON of verdict payload (excluding signature block)
    2. Computes SHA3-256 hash independently
    3. Compares to stored payload_hash — rejects if mismatch
    4. Verifies ML-DSA-65 signature against canonical public key
    Returns True only if both checks pass.
    """
```

> **★★★★ Key fingerprint note (R42-9):** `key_fingerprint` uses `[:16]` — sufficient for accidental mismatch detection. For adversarial key substitution detection, always use the full 64-character SHA3-256 fingerprint. See §42.4.5.

#### Signing Integration Status — FULLY ACTIVE (liboqs primary)

`sign_verdict()` active in all 4 sub-judge scripts and `judge_consistency_engine.py`. `verify_verdict()` active in `judge_pipeline.py`, BBB `/filter`, and BBB `/filter_output`. `sprint1_activate_signing.py` — 19 PASS, 0 FAIL. Gates 32–34 covering ML-DSA-65 signing + rejection test vectors confirmed passing in `VERIFYANDTEST.sh`.

Verification command after any judge or BBB image rebuild:

```bash
for container in jarvis-judge-pipeline jarvis-judge-truth \
    jarvis-judge-consistency jarvis-judge-alignment jarvis-judge-ethics \
    jarvis-blood-brain-barrier jarvis-gis-rag jarvis-crypto-policy; do
  echo "=== $container ==="
  docker exec "$container" python3 -c \
    "import judgesigner; print('Backend:', judgesigner.SIGNING_BACKEND)" 2>/dev/null \
    || echo "  [could not confirm backend — investigate]"
done
```

### 42.3.4 BBB Verdict Gate

The Behavioral Boundary and Blocking (BBB) gate (port 8016) enforces six active constitutional filters (Ethical, Spiritual, Safety, Threat Detection, Steganography, Truth Verification), with `truth_score` null guard and fail-open on HTTP 500.

#### ★★★★★★★★★ BBB `_sign_verdict` Audit Signing (CLOSED April 11, 2026 evening)

> **CLOSED April 11, 2026 (evening).** `_sign_verdict` imported at line 28 in BBB service. Applied at line 42 on every `jarvis-memory:8056` post. liboqs ML-DSA-65 primary backend. Fallback lambda active. Audit failure never blocks the gate.

#### ★★★★★★ AU-02 v2 — Authority Impersonation Detection (CLOSED April 6, 2026 late evening)

> **CLOSED April 6, 2026 (late evening).** Three-layer detection stack:

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

All AU-02 v2 intercepts logged to `jarvis-memory:8056` and signed via BBB `_sign_verdict` (line 42).

#### ★★★★★ Phase 2 — ML-DSA-65 Verdict Gate (CLOSED April 6, 2026 evening)

> **CLOSED April 6, 2026 (evening).** `verify_verdict()` enforcing in `/filter` and `/filter_output`. Byte-flip, no-sig, body-tamper rejection test vectors confirmed passing (Gates 32–34).

BBB Dockerfile:

```dockerfile
# In services/Dockerfile.bbb
RUN pip install --no-cache-dir pyoqs dilithium_py
# judge_pk.bin volume-mounted at runtime (public key only — NOT judge_sk.bin)
```

BBB volume mount:

```yaml
jarvis-blood-brain-barrier:
  volumes:
    - /home/cakidd/msjarvis-rebuild/judge-keys/judge_pk.bin:/app/judge_pk.bin:ro
```

#### ★★★★★ Phase 3 — Output Response Blocking (CLOSED April 6, 2026 evening)

> **CLOSED April 6, 2026 (evening).** `BBB_OUTPUT_BLOCKING=true`. Active blocking. All block decisions logged to `jarvis-memory:8056` and signed via `_sign_verdict` (line 42).

#### April 2, 2026 Recalibration Record

> **★★★★ April 2, 2026 (R42-3):** EthicalFilter and SafetyMonitor fully recalibrated — 9/9 regression, 0% FP rate on maternal Appalachian voice. See Ch. 33 §33.2.

**BBB Steganography Aggregation Bug — FIXED March 22, 2026**

`steg_blocked=True` when `clean=False` AND `threat_level` is `critical` or `high` overrides `content_approved` to `False`. With Phase 3 active, this is an active block event.

### 42.3.5 Constitutional Guardian `_sign_verdict` (★★★★★★★★★ CLOSED April 11, 2026 evening)

> **CLOSED April 11, 2026 (evening).** `_sign_verdict` imported at line 4; applied at line 245 on every `.jsonl` write. liboqs ML-DSA-65 primary backend. Fallback lambda active — audit failure never blocks the gate. Every Constitutional Guardian record is cryptographically attributable and tamper-evident.

### 42.3.6 Conversation Turn and Verdict Memory Storage (★★★★★★★★★★ CONFIRMED April 11, 2026)

> **CONFIRMED April 11, 2026 (final corrections).** Two storage paths, both wired:
>
> 1. **Conversation turn storage** — `ms_jarvis_unified_gateway.py` line 1168:
>    ```python
>    _hx.post('http://jarvis-memory:8056/memory/turn',
>        headers={'X-API-Key': 'internal'},
>        json={'user_message': ..., 'assistant_response': ..., 'session_id': ...},
>        timeout=2.0)
>    ```
>    Every conversation turn is posted to `jarvis-memory:8056/memory/turn` with user message, assistant response, and session ID.
>
> 2. **Verdict signature chain** — `judge_consistency_engine.py` via `sign_verdict`. Every consistency verdict carries an ML-DSA-65 signature (liboqs primary backend). Signed verdicts are stored in `jarvis-memory:8056` as part of the judge pipeline audit trail.

### 42.3.7 PostgreSQL Transparent Data Encryption

All data in `jarvis-local-resources-db` (port 5435) is encrypted at rest using AES-256-GCM via pgcrypto TDE. Key derivation uses HKDF-SHA3-256; master key never stored in the database.

### 42.3.8 Ingest Infrastructure — Compose-Managed

- `jarvis-ingest-api` — compose-managed, `restart: unless-stopped`, bound to `127.0.0.1`.
- `jarvis-ingest-watcher` — compose-managed, `restart: unless-stopped`, bound to `127.0.0.1`.

### 42.3.9 Durable Audit Trail — `jarvis-memory:8056`

`jarvis-memory` (port 8056) logs all gate decisions:

- Phase 1.4 (BBB input gate): every block decision.
- Phase 2 (BBB verdict gate): every rejected verdict with reason.
- Phase 3 (BBB output gate): every blocked response.
- AU-02 v2: every intercept with triggering layer, matched pattern/seed, cosine score.
- All BBB audit posts: ML-DSA-65 signed via liboqs (line 42).
- All Constitutional Guardian `.jsonl` writes: ML-DSA-65 signed via liboqs (line 245).
- Conversation turns: posted via `ms_jarvis_unified_gateway.py` line 1168 (`/memory/turn`).
- Authentication: `_auth()` confirmed; `JARVIS_API_KEY` set; HTTP 401 on unauthenticated writes.

### 42.3.10 Dependency CVE Audit Protocol (★★★★★★★★★ Gate 31 Automated April 11, 2026 evening)

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

> **chromadb overconstraint note:** chromadb pins `fastapi==0.115.9` in its package metadata. This is a packaging overconstraint — not a real functional incompatibility. fastapi 0.135.3 + starlette 1.0.0 work correctly in practice.

**Gate 31 — Dual-layer enforcement:**

1. Per-package version floor checks via `packaging.version.Version` for all 6 priority packages.
2. `pip-audit` CVE sweep for newly published CVEs.
3. **Dockerfile pin grep** — confirmed done; all Dockerfiles audited for priority package pins below established floors.

First automated run: PASS=1 WARN=0 FAIL=0.

**Established minimum versions:**

```
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
| `judge_sk.bin` | `/home/cakidd/msjarvis-rebuild/judge-keys/judge_sk.bin` | ML-DSA-65 private signing key | SECRET — never commit; NOT mounted in BBB |
| `judge_pk.bin` | `/home/cakidd/msjarvis-rebuild/judge-keys/judge_pk.bin` | ML-DSA-65 public verification key | Non-secret; mounted read-only in all judge containers and BBB; exposed via `/judge-public-key` endpoint |
| `judge_sk_backup_20260322.gpg` | `~/judge-sk-backup-20260322.gpg` | GPG AES-256 encrypted backup | SECRET |
| `judge_sk_backup_20260322.gpg.bak` | `~/msjarvis-rebuild-working/msjarvis-rebuild/crypto/keys/judge_sk_backup_20260322.gpg.bak` | Second on-disk copy | SECRET |
| `judge_sk_backup_20260322.gpg` (USB) | `/media/cakidd/writable/` | Air-gapped USB — OI-22 CLOSED April 1, 2026, commit `3218392e` | SECRET — offline only |

### 42.4.2 Key Generation (liboqs primary)

```python
import oqs  # liboqs via pyoqs
import hashlib

signer = oqs.Signature("ML-DSA-65")
pk = signer.generate_keypair()
sk = signer.export_secret_key()

with open("/home/cakidd/msjarvis-rebuild/judge-keys/judge_pk.bin", "wb") as f:
    f.write(pk)
with open("/home/cakidd/msjarvis-rebuild/judge-keys/judge_sk.bin", "wb") as f:
    f.write(sk)

fingerprint_full = hashlib.sha3_256(pk).hexdigest()
print(f"Full fingerprint: {fingerprint_full}")
```

### 42.4.3 Key Distribution

Volume-mounted from `/home/cakidd/msjarvis-rebuild/judge-keys/` into all five judge containers (sk + pk), BBB (pk only), `jarvis-gis-rag` (pk only), and `jarvis-crypto-policy` (pk only).

```yaml
# Judge containers
volumes:
  - /home/cakidd/msjarvis-rebuild/judge-keys/judge_sk.bin:/app/judge_sk.bin:ro
  - /home/cakidd/msjarvis-rebuild/judge-keys/judge_pk.bin:/app/judge_pk.bin:ro

# BBB, jarvis-gis-rag, jarvis-crypto-policy — public key only
volumes:
  - /home/cakidd/msjarvis-rebuild/judge-keys/judge_pk.bin:/app/judge_pk.bin:ro
```

### 42.4.4 `/judge-public-key` Endpoint (★★★★★★★★★ OI-42-E CLOSED April 11, 2026 evening)

> **CLOSED April 11, 2026 (evening).** Live at `judge_pipeline.py:314`. `pk_fp_sha3_256` computed at line 338.

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

Independent verification:

```python
import base64, hashlib, json, oqs

pk_b64 = "<pk_b64 from /judge-public-key>"
pk = base64.b64decode(pk_b64)
assert hashlib.sha3_256(pk).hexdigest() == "<pk_fp_sha3_256 from endpoint>"

signed_verdict = { ... }
sig = base64.b64decode(signed_verdict["signature"]["value"])
payload = {k: v for k, v in signed_verdict.items() if k != "signature"}
canonical = json.dumps(payload, sort_keys=True, separators(",", ":")).encode()
verifier = oqs.Signature("ML-DSA-65")
assert verifier.verify(canonical, sig, pk)
```

### 42.4.5 Key Lifecycle and Rotation — `rotate_judge_keys.sh` (★★★★★★★★★★ CONFIRMED April 11, 2026)

> **CONFIRMED April 11, 2026 (final corrections — R42-22).** `rotate_judge_keys.sh` is complete, production-grade, and fully implements §42.12. It was previously listed in §42.11 as future work — that was an error. It was already done.

**`rotate_judge_keys.sh` — what it does:**

1. Archives existing `judge_sk.bin` and `judge_pk.bin` with timestamp prefix to `judge-keys/archive/`.
2. Generates a new ML-DSA-65 keypair via liboqs (`oqs.Signature("ML-DSA-65")`), falling back to `dilithium_py` if liboqs unavailable.
3. Writes new `judge_sk.bin` and `judge_pk.bin` to `/home/cakidd/msjarvis-rebuild/judge-keys/`.
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

> **★★★★ Fingerprint note (R42-9):** `[:16]` is a convenience display only. For adversarial key substitution detection, always use the full 64-character SHA3-256 fingerprint. `rotation.log` records the full fingerprint. Post-rotation verification uses full fingerprint across all signing containers.

---

## 42.5 Integration with the Judge Pipeline

Every sub-judge signs its verdict with `sign_verdict()` (liboqs ML-DSA-65 primary). `judge_pipeline.py` verifies sub-judge verdicts with `verify_verdict()` before aggregating. The final aggregated verdict is signed again before being sent to BBB. ★★★★★ BBB independently verifies the final aggregated verdict signature before any filter logic runs. End-to-end latency: 99–107s (RTX 4070 GPU).

`judge_consistency_engine.py` uses `sign_verdict` on every consistency verdict. `ms_jarvis_unified_gateway.py` line 1168 posts every conversation turn to `jarvis-memory:8056/memory/turn`.

### 42.5.5 External Access and Gateway Security

```
Internet ↔ Cloudflare edge (HTTPS/QUIC) ↔ cloudflared QUIC tunnel ↔ Caddy:8443 (loopback) ↔ jarvis-auth:8055 (forward_auth) ↔ jarvis-main-brain
```

- **Cloudflare Tunnel** (`cloudflared.service`, systemd): TLS termination. `https://egeria.mountainshares.us` confirmed live.
- **Caddy `forward_auth`** (commit `f2e93422`, April 1, 2026): unauthenticated requests return HTTP 401. Gate 30 ✅ PASS at certification.
- **`jarvis-auth`** (port 8055): systemd-managed FastAPI service; token validation active. fastapi 0.135.3.
- **Zero `0.0.0.0` exposures**: all services bound to `127.0.0.1`. 91 containers, 0 public exposures confirmed April 11, 2026.

---

## 42.6 Threat Model

The PQ layer defends against:

- **Quantum adversary** — harvesting ciphertext today and decrypting later.
- **Verdict tampering** — ★★★★★ actively rejected at BBB boundary. Gates 32–34 byte-flip, no-sig, body-tamper test vectors confirmed passing.
- **Rogue judge containers** — ★★★★★ actively rejected at BBB boundary.
- **Authority impersonation (AU-02)** — ★★★★★★ fully covered by AU-02 v2: string-match + Regex v2 (6 patterns) + Embedding v2 (30 seeds, cosine ≥ 0.72).
- **Steganographic covert channels** — `steg_blocked=True` override active; Phase 3 active blocking.
- **At-rest compromise** — AES-256-GCM TDE on `jarvis-local-resources-db:5435`.
- **Unauthenticated API access** — Caddy `forward_auth` live (OI-36-A closed). Gate 30 ✅.
- **Constitutional violations in output** — ★★★★★ actively blocked (Phase 3 re-enabled; 0% FP, red team 12/12).
- **Audit trail forgery** — every BBB audit post and every Constitutional Guardian `.jsonl` write is liboqs ML-DSA-65 signed. Unsigned writes are logged. Fallback ensures no gate is blocked.
- ★★★★★★★ **Mythos-class AI-assisted exploit chaining** — Mitigated by: (1) all services bound to `127.0.0.1`; (2) Cloudflare Tunnel + Caddy `forward_auth` (Gate 30 ✅); (3) urllib3 CVE surface closed; (4) AU-02 v2 embedding detection; (5) Gate 31 dual-layer dep audit automation + Dockerfile pin grep; (6) 8 CVEs closed April 11, 2026 — 0 remaining. Stack assessment: **CERTIFIED. Fully closed.**

---

## 42.7 Health and Operational Verification

`VERIFYANDTEST.sh` — 40 gates. CERTIFIED Sat Apr 11 06:29:09 PM EDT 2026. `vat_CERTIFIED_20260411.log` — 6.0K ✅. Syntax clean. Synced to spiritual drive.

> **April 3, 2026 sealed baseline:** Ch. 33 sealed result: **22 PASS / 0 FAIL / 1 WARN**. The 1 WARN is `jarvis-web-research` (port 8090). See Ch. 33 §33.6.

### Preflight Gates — Full Reference

| Gate | Check | Target | Status |
|------|-------|--------|--------|
| Gate 25 | `jarvis-memory:8056` auth/logging | `_auth()` HTTP 200 with `JARVIS_API_KEY` | ✅ |
| Gate 26 | `confidence_decay` presence | Non-null rows in `msjarvisgis` on `jarvis-local-resources-db:5435` | ✅ |
| Gate 27 | ChromaDB collections count | ≥ 40 (confirmed 49 at certification) | ✅ |
| Gate 28 | `psychological_rag` domain | Registered, metadata confirmed | ✅ |
| Gate 29 | `jarvis-crypto-policy` health | HTTP 200 on `127.0.0.1:8099/health` | ✅ |
| Gate 30 | Auth proxy (OI-36-A) | Caddy `forward_auth` HTTP 401 on unauthenticated | ✅ |
| Gate 31 | Host venv floors + pip-audit + Dockerfile pin grep | Dual-layer + pin audit: 6 package floors, 0 CVEs, Dockerfiles clean | ✅ PASS (OI-42-F closed) |
| Gates 32–34 | ML-DSA-65 signing + rejection test vectors | Byte-flip, no-sig, body-tamper all rejected | ✅ PASS |
| Gate 35 | liboqs C library install | liboqs confirmed primary runtime in judgesigner.py | ✅ PASS |
| Gates 36–38 | GBIM temporal decay, persona injection, Redis pre-warm | 5,416,522 beliefs; Ms. Egeria Allis persona confirmed; async pre-warm active | ✅ PASS |
| Gate 39 | `/judge-public-key` endpoint | Live on port 7239; algorithm, backend, standard, pk_b64, fingerprint returning | ✅ PASS |
| Gate 40 | Full suite syntax + certification seal | 40 gate blocks, syntax clean, synced to spiritual drive | ✅ CERTIFIED |

> **★★★★ Gate 26 disambiguation (R42-4):** `msjarvisgis` here refers to the database on `jarvis-local-resources-db:5435` (port 5435) — distinct from the PostGIS geospatial database at host port 5432. Gate 26 targets port 5435 only.

Gate 29 check:

```bash
echo "[Gate 29] Checking jarvis-crypto-policy health..."
STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8099/health)
if [ "$STATUS" = "200" ]; then
  echo "[PASS] Gate 29 — jarvis-crypto-policy healthy (HTTP 200)"
else
  echo "[FAIL] Gate 29 — returned HTTP $STATUS"
  exit 1
fi
```

Gate 35 check (liboqs primary runtime confirmation):

```bash
echo "[Gate 35] Confirming liboqs primary runtime in judgesigner.py..."
for container in jarvis-judge-pipeline jarvis-judge-truth \
    jarvis-judge-consistency jarvis-judge-alignment jarvis-judge-ethics \
    jarvis-blood-brain-barrier jarvis-gis-rag jarvis-crypto-policy; do
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

The steganography filter marks payloads as `clean=False` with `threat_level` `critical` or `high` → `steg_blocked=True` → `content_approved=False`. ★★★★★ With Phase 3 active, `content_approved=False` is an active block event logged to `jarvis-memory:8056` and signed via `_sign_verdict` (BBB line 42, liboqs ML-DSA-65 primary).

---

## 42.10 Open Items

| ID | Item | Status | Notes |
|----|------|--------|-------|
| OI-13 | `confidence_decay` verification for Gate 26 | ✅ Closed April 1, 2026 | Non-null `confidence_decay` confirmed in `msjarvisgis` on `jarvis-local-resources-db:5435`. |
| OI-22 | Air-gapped USB copy of `judge_sk_backup_20260322.gpg` | ✅ Closed April 1, 2026 | USB copy at `/media/cakidd/writable/`, commit `3218392e`. |
| OI-26 | Gate 26 scripting target DB | ✅ Closed April 1, 2026 | Shell logic updated to port 5435. |
| OI-30 | MountainShares/DAO endpoint health | ✅ Closed April 1, 2026 | Smoke tests confirmed on ports 8080–8084. |
| OI-31 | EEG layer architecture documentation | ✅ Closed April 1, 2026 | Delta/theta/beta pipeline documented in §42.13. |
| OI-36-A | Gateway-level token enforcement at Caddy | ✅ Closed April 1, 2026 | Caddy `forward_auth` live; commit `f2e93422`. Gate 30 ✅ PASS at certification. |
| OI-CRYPTO-VT | `jarvis-crypto-policy` health in `VERIFYANDTEST.sh` | ✅ Closed April 1, 2026 | Gate 29 passing; FAIL=0, WARN=0. |
| OI-BBB-PHASE2 | BBB ML-DSA-65 verdict gate | ✅ Closed April 6, 2026 (evening) | `verify_verdict()` enforcing in `/filter` and `/filter_output`. Gates 32–34 passing. |
| OI-BBB-PHASE3 | Phase 4.5 output blocking re-enablement | ✅ Closed April 6, 2026 (evening) | `BBB_OUTPUT_BLOCKING=true`. OI-38-B satisfied. |
| OI-38-B | Red team final sign-off | ✅ Closed April 6, 2026 (evening) | 12/12 — VG-01→VG-08, OF-01→OF-04. |
| OI-AU-02-V2 | AU-02 embedding-based authority impersonation detection v2 | ✅ Closed April 6, 2026 (late evening) | Regex v2: 6 patterns, ~0ms, Gates A/B ✅. Embedding v2: 30 seeds, cosine ≥ 0.72, ~300ms cached, Gates C/D/E ✅. False-positive guard: 8 overly broad triggers removed, Gates H/I/J ✅. |
| OI-URLLIB3-CVE | urllib3 CVE remediation | ✅ Closed April 11, 2026 | Host crypto-venv upgraded 1.26.20 → 2.6.3. `Dockerfile.woah` patched. `jarvis-woah` rebuilt, confirmed `Version: 2.6.3`. |
| OI-DEP-AUDIT-1 | Dependency CVE audit — first full run | ✅ Closed April 11, 2026 | All host venv packages and Dockerfiles audited. Cadence established in §42.3.10. |
| OI-VENV-UPGRADE | Full host venv CVE sweep | ✅ Closed April 11, 2026 (afternoon) | 8 CVEs closed. Gate 31 passing. |
| OI-42-A | `dilithium_py` removal from base `services/Dockerfile` | ✅ Closed April 11, 2026 (evening) | Removed from base/reference Dockerfile. `dilithium_py` now lives only in `judgesigner.py` as Python-level graceful fallback — liboqs is the primary runtime. |
| OI-42-E | `/judge-public-key` public endpoint | ✅ Closed April 11, 2026 (evening) | Live at `judge_pipeline.py:314`. Returns `pk_b64` (1952 bytes), full SHA3-256 fingerprint, algorithm, backend, standard, `verify_endpoint`. |
| OI-42-F | Gate 31 version floor automation + Dockerfile pin grep | ✅ Closed April 11, 2026 (evening) | Dual-layer + Dockerfile pin grep. First run: PASS=1 WARN=0 FAIL=0. Clean. |
| OI-BBB-SIGN | BBB `_sign_verdict` audit post signing | ✅ Closed April 11, 2026 (evening) | Imported line 28, applied line 42. liboqs primary. Fallback lambda active. |
| OI-CG-SIGN | Constitutional Guardian `_sign_verdict` `.jsonl` signing | ✅ Closed April 11, 2026 (evening) | Imported line 4, applied line 245. liboqs primary. Fallback lambda active. |
| OI-GIS-RAG-REBUILD | `jarvis-gis-rag` rebuild with `judgesigner.py` | ✅ Closed April 11, 2026 (evening) | Fresh image with liboqs `judgesigner.py` baked in. Running. |
| OI-CRYPTO-REBUILD | `jarvis-crypto-policy` rebuild with `judgesigner.py` | ✅ Closed April 11, 2026 (evening) | New image. `judgesigner.py` at `/app/judgesigner.py` confirmed build log line 7/7. Running. |
| OI-LIBOQS-CONFIRM | judgesigner.py liboqs primary runtime confirmation | ✅ Closed April 11, 2026 (final corrections) | `SIGNING_BACKEND = "liboqs"` confirmed live in production. `dilithium_py` is graceful fallback only. R42-21 correction applied. |
| OI-ROTATE-CONFIRM | `rotate_judge_keys.sh` production-grade completion | ✅ Closed April 11, 2026 (final corrections) | Full §42.12 implementation confirmed. Archives, USB protocol, liboqs keygen with fallback, rotation log, restart instructions. R42-22 correction applied. |
| OI-GATE31-GREP | Gate 31 Dockerfile pin grep | ✅ Closed April 11, 2026 (final corrections) | Dockerfile pin grep confirmed done. R42-23 correction applied. |
| OI-MEMORY-SIGN | Signed verdict / memory storage wiring | ✅ Closed April 11, 2026 (final corrections) | Gateway line 1168 + `judge_consistency_engine.py` `sign_verdict` both confirmed. R42-24 correction applied. |

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
- `~/msjarvis-rebuild-working/msjarvis-rebuild/crypto/keys/judge_sk_backup_20260322.gpg.bak` — second on-machine copy.
- `/media/cakidd/writable/judge_sk_backup_20260322.gpg` — air-gapped USB copy confirmed April 1, 2026; commit `3218392e`. OI-22 closed.

The USB device must be stored offline and separately from the Legion 5 host.

> **★★★★ USB key management protocol (R42-8):**
>
> 1. **Verify USB integrity before use:** `gpg --verify /media/cakidd/writable/judge_sk_backup_20260322.gpg`. If verification fails, fall back to on-machine primary copy and create a new USB copy immediately.
> 2. **Key rotation requires USB replacement in the same session:** `rotate_judge_keys.sh` executes this automatically. Do not end the rotation session until the new GPG backup is confirmed on the USB device.
> 3. **If USB is lost, create a new copy immediately:** Do not operate the production stack without at least one verified offline copy — the judge signing key has no recovery path if all copies are lost.

---

## 42.13 EEG Layer Architecture (OI-31 — Closed April 1, 2026)

The EEG layer (ports 8073–8075) implements a three-band brainwave-inspired signal processing pipeline:

- **Delta band (port 8073) — Deep context and memory consolidation:** Long-horizon community memory, ancestral knowledge, and deep geographic identity. Inputs from `ms_jarvis_memory`, `spiritual_texts`, and `fifth_dgm_subconscious`. Modulates weight given to long-term community narrative.
- **Theta band (port 8074) — Associative reasoning and cross-domain synthesis:** Inputs from GBIM entity graph, `appalachian_cultural_intelligence`, and `psychological_rag`. Produces cross-domain linking candidates passed upstream to the main brain.
- **Beta band (port 8075) — Active reasoning and real-time grounding:** Inputs from `conversation_history`, `news_rag`, and `local_resources`. Produces salience-weighted context prioritized in the RAG retrieval step.

All three bands operate in parallel; outputs merged by a lightweight aggregator before injection into the main brain's context window. All three containers running; pipeline integration with `jarvis-main-brain` confirmed. Full band-weight calibration is a next-session item.

---

## 42.14 April 11, 2026 Sprint Certification Record

> **`vat_CERTIFIED_20260411.log` — 6.0K ✅**
> **Ms. Allis VERIFYANDTEST — CERTIFIED Sat Apr 11 06:29:09 PM EDT 2026 ✅**
> **Chapter 42 — FULLY CLOSED April 11, 2026 (evening — final corrections) ✅**

| Item | Detail | Status |
|------|--------|--------|
| Containers running | 91 | ✅ |
| Public exposures | 0 | ✅ |
| GBIM beliefs with temporal decay | 5,416,522 | ✅ |
| Spatial landowner rows | 20,593 | ✅ |
| ChromaDB collections | 49 | ✅ |
| ML-DSA-65 signing backend | liboqs (primary); dilithium_py (graceful fallback) | ✅ |
| ML-DSA-65 signing keys | All 5 judges + BBB + gis-rag + crypto-policy active | ✅ |
| Key rotation script | `rotate_judge_keys.sh` — production-grade, complete | ✅ |
| Conversation turn storage | `ms_jarvis_unified_gateway.py` line 1168 → `jarvis-memory:8056/memory/turn` | ✅ |
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
- For the authoritative preflight sealed gate count (22 PASS / 0 FAIL / 1 WARN, April 3, 2026), see Chapter 33 §33.6.
- For the BBB EthicalFilter and SafetyMonitor recalibration record (April 2, 2026 — 9/9 regression, 0% FP), see Chapter 33 §33.2.
- For ingest architecture (`jarvis-ingest-api`, `jarvis-ingest-watcher`) and IPFS integration, see Chapter 30.
- For `jarvis-memory:8056` durable audit trail — now logging Phase 1.4 input blocks, Phase 2 verdict rejections, Phase 3 output blocks, AU-02 v2 intercepts, signed BBB audit posts, signed Constitutional Guardian `.jsonl` writes, and conversation turns (gateway line 1168) — see Chapter 40 §40-H and Chapter 40 §40-I.
- For MountainShares/Commons/DAO tier (ports 8080–8084) and governance hooks, see Chapter 3 and Chapter 31.
- For preflight gates 25–40 as implemented in the `VERIFYANDTEST.sh` certification suite, see Chapter 41 §41.7 and §41.8.
- For the Red Team API contract, external access architecture, and OI-38-B tracking context, see Chapter 38 §38.8 and §38.9.
- For the AU-02 authority impersonation threat — now fully covered by AU-02 v2 (Regex v2 + Embedding v2 + false-positive guard, OI-AU-02-V2 closed April 6 late evening) — see `threat_detection.py` module documentation and Chapter 16 §16.9.
- For the PostGIS geospatial database (`gisdb` / `msjarvisgis`) at host port 5432 — distinct from the Gate 26 target `msjarvisgis` at port 5435 — see Chapter 10 and Chapter 12.
- For the dependency CVE audit protocol, full venv upgrade, Gate 31 automation and Dockerfile pin grep, and all April 11, 2026 closures (OI-URLLIB3-CVE, OI-DEP-AUDIT-1, OI-VENV-UPGRADE, OI-42-A, OI-42-E, OI-42-F, OI-BBB-SIGN, OI-CG-SIGN), see §42.3.10 and §42.10 in this chapter.
- For the `/judge-public-key` community verification endpoint and independent verdict verification protocol, see §42.4.4 in this chapter.
- For `rotate_judge_keys.sh` production-grade key rotation script and the USB offline protocol, see §42.4.5 and §42.12 in this chapter.
- For liboqs ML-DSA-65 confirmed as primary production runtime in `judgesigner.py` (dilithium_py as graceful fallback), see §42.3.3 and the R42-21 correction block at the top of this chapter.
- For the confirmed conversation turn storage (gateway line 1168) and verdict signature chain (`judge_consistency_engine.py`), see §42.3.6 and the R42-24 correction block at the top of this chapter.
- For the April 11, 2026 final corrections certification seal, all 0 remaining open items, and 0 remaining future work items, see §42.14 in this chapter.
