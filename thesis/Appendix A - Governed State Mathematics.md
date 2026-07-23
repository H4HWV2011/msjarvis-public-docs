# Appendix A — Governed State Mathematics and Verification Discipline (As‑Built)

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 22, 2026*

---

## A.0 Overview

Appendix A defines how Ms. Jarvis’s claims are tied to **verified, running code** after the July 2026 architecture closeout.

It explains what counts as *demonstrated* versus *not‑yet‑demonstrated*, how corpus, memory, and governance paths are tested, and how discrepancies are recorded instead of being smoothed over. It now includes the as‑built AAPCAppE → Chroma → GBIM corpus path, the GBIM promotion contract, live scheduled runners, current /policy/set status, and references to the Hilbert‑time Redis keys and live Chroma collections that were inspected.

This appendix is the **house rule**: if a chapter claims a mechanism is live, it must be able to point back here to the evidence style that supports that claim.

---

## A.1 Demonstrated vs Not‑Yet‑Demonstrated

Every mechanism in the thesis must live in one of two registers:

- **Demonstrated**  
  A claim is *demonstrated* only when a real path has been exercised and confirmed across at least two layers, such as:
  - service or script is running on the expected port or schedule;  
  - endpoint or worker produces live behavior;  
  - database, Chroma, or Redis state shows the expected effect;  
  - logs or test probes confirm the result.

- **Not yet demonstrated**  
  A claim is *not yet demonstrated* when it is:
  - only described architecturally in text;  
  - implemented in code but never exercised end‑to‑end;  
  - visible only in tests or prototypes, not in the live services layer;  
  - dependent on tables, routes, or keys that do not yet exist.

No chapter may quietly promote an architectural idea to “live behavior” without this kind of evidence. Appendix A’s job is to keep that line clear.

---

## A.2 AAPCAppE → Chroma → GBIM Corpus Path

At the corpus level, the as‑built architecture includes a specific Appalachian pipeline:

1. **AAPCAppE scraper (port 8033)**  
   - Service: `jarvis-aaacpe-scraper`  
   - Role: scrapes the internet for **Appalachian linguistic information** and related texts.  
   - Output: corpus chunks ready for vectorization.

2. **Chroma corpus storage (port 8002)**  
   - Service: `jarvis-chroma`  
   - Role: stores vectors and metadata for scraped documents.  
   - Collection: the inspected Chroma collections include the one receiving AAPCAppE output.  
   - Evidence: corpus documents ingested by the scraper appear as records in the configured Chroma collection.

3. **GBIM (Chapter 02) intake path**  
   - GBIM queries Chroma via the standard retrieval pipeline:
     - \(M_{\text{corpus}}\) (corpus embeddings)  
     - \(\rightarrow C_{\text{retrieved}}\) (retrieved candidates)  
     - \(\rightarrow S_{\text{sandbox}}\) (sandbox reasoning over those candidates)  
     - \(\rightarrow F_{\text{candidate}}\) (candidate features passed to GBIM).  
   - This means Appalachian corpus evidence flows from AAPCAppE → Chroma → GBIM, not directly from raw HTTP scraping into spatial governance.

Because this whole path has been exercised, Appendix A treats it as a **demonstrated architecture fact**: AAPCAppE populates Chroma, and GBIM uses Chroma as a corpus‑backed source via the standard M_corpus → C_retrieved → S_sandbox → F_candidate chain.

---

## A.3 The GBIM Promotion Contract (Canonical Example)

GBIM provides the **canonical demonstrated example** of a governed promotion contract in the system.

The contract has three key pieces:

1. **Trigger (guardrail)**  
   - Table: GBIM active‑collection table (for example, `gbim_active_collection`).  
   - Trigger: a BEFORE trigger on insert/update.  
   - Behavior:  
     - checks that the target manifest row is coherence‑approved and in the right status;  
     - rejects activation if `coherence_ok` is false or the build status is wrong;  
     - raises a clear error if the guard is violated.

2. **Evaluator (coherence_ok)**  
   - Coherence evaluator populates a `coherence_ok` flag and related status fields on the manifest row.  
   - It runs as part of the GBIM build/validate pipeline, not as a manual toggle.  
   - Only manifests that pass this evaluation can ever be considered for activation.

3. **Procedure (promote_gbim_collection)**  
   - Single sanctioned procedure, for example `promote_gbim_collection(...)`.  
   - Responsibilities:
     - verify that the manifest is built and `coherence_ok == true`;  
     - set the manifest to `active` status;  
     - update `gbim_active_collection` to point to that manifest;  
     - rely on the trigger to abort if coherence or status is wrong.

This triad—**trigger, evaluator, procedure**—is what Appendx A calls the GBIM promotion contract. It has been run on real manifests, including negative tests (attempting to activate non‑coherent or superseded manifests), so it is treated as **demonstrated**.

---

## A.4 Live Scheduled Runners and the Epistemic Loop

The verification discipline requires that scheduled jobs be named and tied to real scripts. As of July 22, 2026, the following runners are treated as **live**:

1. **`dgm_cycle.sh` (every 30 minutes)**  
   - Status: originally the main periodic DGM governance cycle.  
   - Update: now marked **PAUSED**, replaced by the recurrent epistemic runner (see below).  
   - Lesson: Appendix A keeps this as a historical reference and notes its paused state, rather than pretending it is still active.

2. **`conversation_retention_worker` (hourly)**  
   - Script: `services/hilbert/conversation_retention_worker.py`.  
   - Schedule: runs once per hour.  
   - Role: enforces **conversation retention policies** over per‑user conversational collections (history/private tiers), pruning expired entries and enforcing consent‑based retention.

3. **`identity_promotion.py` (daily at 03:00)**  
   - Script: `services/identity_promotion.py`.  
   - Schedule: `03:00` local time each day.  
   - Role: applies identity‑related promotion rules (for example, moving identities between provisional and confirmed states under policy).

4. **`recurrent_epistemic_runner.py` (@reboot)**  
   - Script: `services/hilbert/recurrent_epistemic_runner.py`.  
   - Launch: configured to start automatically **at system reboot** (inside `crypto-venv`).  
   - Role: orchestrates recurring validation and maintenance, including:
     - invoking Chapter 41 continuous validation;  
     - scheduling or triggering conversation retention;  
     - calling the governed DGM cycle under safeguards;  
     - checking that key services (H_t, Hilbert‑state, BBB, guardian, Chroma, Redis) are live.

Together, these runners form the **as‑built recurrent epistemic loop**: not a single monolithic daemon, but a set of scheduled jobs that keep retention, identity promotion, and governance validation happening regularly.

---

## A.5 Demonstrated vs Not‑Yet‑Demonstrated Sections

Each chapter and appendix is expected to maintain explicit **Demonstrated / Not‑Yet‑Demonstrated** subsections.

The discipline is:

- Move an item to **Demonstrated** only when:
  - the service or script exists;  
  - scheduled or ad‑hoc tests have run;  
  - stores or keys show the effect;  
  - logs or probes can be cited internally.

- Keep an item in **Not‑Yet‑Demonstrated** when:
  - the code exists but has never been exercised;  
  - a test run succeeds only against synthetic, throwaway test harnesses;  
  - routes or scripts have been drafted but not wired into any schedule;  
  - chapter text goes beyond what the evidence actually shows.

Appendix A **retains all Demonstrated / Not‑Yet‑Demonstrated sections** and expects other chapters to mirror this pattern. When a mechanism is promoted or demoted, the change should be recorded here as part of the verification story.

---

## A.6 A.11 /policy/set Discrepancy — Updated Disposition

Earlier, there was a **discrepancy** around a `/policy/set` governance route:

- cron configuration referenced a `/policy/set` path;  
- source inspection initially found **no matching endpoint**, leaving it unclear whether the route was real.

As of the July 22, 2026 gate:

- the `/policy/set` endpoint is now **being built at port 8099**;  
- implementation file: `services/policy_set_service.py`;  
- cron entry remains **commented out** until the endpoint passes end‑to‑end verification.

Appendix A records this as:

- **Discrepancy resolved in design**: the route is now clearly located and given a dedicated service file and port;  
- **Still not fully demonstrated**: it will not be treated as live governance until:
  - the endpoint is reachable on port 8099;  
  - request and response contracts are honored;  
  - policy writes show up correctly in the backing store;  
  - a negative path test (for example, missing authorization) fails closed.

Until those conditions are met, `/policy/set` remains in the **Not‑Yet‑Demonstrated** register, with clear progress notes.

---

## A.7 Live Chroma Collections

Verification at the vector level focuses on **which Chroma collections actually exist and are used** by the live services.

The July 2026 inspection confirmed:

- **AAPCAppE / corpus collections**  
  - one or more collections receiving Appalachian linguistic corpus material from `jarvis-aaacpe-scraper`;  
  - GBIM’s retrieval path reading from these collections via M_corpus → C_retrieved.

- **Per‑user conversation collections**  
  - `conversation_history_user_<slug>`  
  - `conversation_private_user_<slug>`  
  - `conversation_staged_user_<slug>`  
  - Live tests with alpha and beta users confirmed:
    - each user’s writes land in their own collections;  
    - **no cross‑user record leak** between alpha and beta;  
    - legacy shared conversation history remains unused as an authority path.

- **Community Hilbert Commons collection**  
  - Name: `community_hilbert_commons`;  
  - Gateway: on port 8055;  
  - Role: stores **centroid + provenance** records for k‑thresholded, public‑opt‑in community vectors;  
  - Behavior: suppresses under‑threshold groups and does not store user hashes.

Appendix A treats these collection names and behaviors as **demonstrated**: they were scanned and used in the relevant gate tests.

---

## A.8 Redis `hilbert:time:*` Keys and Temporal Verification

Temporal verification relies on concrete inspection of Redis keys whose names begin with `hilbert:time:`.

The July 2026 temporal probes revealed keys such as:

- `hilbert:time:asbuilt_ch49`  
- `hilbert:time:asbuilt_ch49_clean`  
- `hilbert:time:ch04_ch44_probe_...` (several probe keys)  
- `hilbert:time:ch49_test`  
- `hilbert:time:commons_coherence`  
- `hilbert:time:commons_coherence_probe`  
- `hilbert:time:commons_coherence_probe_deleted`  
- `hilbert:time:ingest:blockgroup:540019655001`  
- `hilbert:time:test:naive-fix`  
- `hilbert:time:test:utc-fix`

From these and the health probes, Appendix A elevates the following to **Demonstrated**:

- there is a **live Hilbert‑time service** with named port binding;  
- Redis contains a **family of temporal keys** under `hilbert:time:*`;  
- test and as‑built keys reflect temporal ingestion, commons coherence probes, and specific chapter tests (for example, Ch49);  
- temporal operations can read/write these keys and observe TTL/decay behavior.

More advanced claims about a fully separate `hilbert:ephemeral:*` or `hilbert:staged:*` keyspace, or about perfect time perception, remain **Not‑Yet‑Demonstrated** unless explicitly proven by future gates.

---

## A.9 Identity, Retention, and Loop Scheduling

Identity and retention mechanisms must be tied to **real schedules and workers** rather than being purely declarative.

At this gate, Appendix A records:

- **Identity promotion**  
  - Script `identity_promotion.py` runs daily at 03:00;  
  - It moves identities through promotion stages under configured policies;  
  - The script has been exercised and logs show promotions occurring.

- **Conversation retention**  
  - `conversation_retention_worker` runs hourly;  
  - It enforces per‑user retention and pruning, consistent with consent flags;  
  - Logs and collection sizes verify that pruning is applied over time.

- **Recurrent epistemic runner**  
  - `recurrent_epistemic_runner.py` starts on reboot inside `crypto-venv`;  
  - It coordinates Chapter 41 validation and other checks;  
  - It depends on key services being alive before running heavy tasks.

These runners collectively instantiate the **Recurrent Epistemic Loop** as a concrete scheduling pattern, constrained by what the gate actually reports. Appendix A does **not** treat this as fully autonomous or always‑on; it treats it as a set of **bounded, testable jobs**.

---

## A.10 How to Read Verification Discipline as a Rural Developer

For rural developers operating or auditing this stack, Appendix A can be read as a **practical checklist**:

1. **Is there a live service or worker?**  
   - Check the named port or the scheduled script.

2. **Can you exercise it?**  
   - Call the endpoint or let the job run and see its effect.

3. **Does a store or keyspace confirm the effect?**  
   - Inspect Postgres, Chroma, Redis, or logs.

4. **Is the path governed?**  
   - Look for triggers, evaluators, and procedures (as with GBIM);  
   - Confirm that consent, purpose, and legal‑authority fields are enforced.

5. **Is the chapter honest about status?**  
   - Does it use “Demonstrated” only where this evidence exists?  
   - Does it mark architectural ideas as “Not‑Yet‑Demonstrated” where appropriate?

If the answer to any of these checks is “no,” Appendix A expects the claim to be narrowed, the discrepancy to be logged, or the path to be strengthened until it meets the bar.

---

## A.11 Closing Statement

Appendix A turns **governed state mathematics** into a lived verification discipline.

It fixes the AAPCAppE → Chroma → GBIM path as an evidence‑backed fact, lifts the GBIM promotion contract up as a canonical example of a guarded promotion pipeline, names the live scheduled runners that implement the recurrent epistemic loop, records the current status of `/policy/set`, and anchors temporal and vector claims in real Redis keys and Chroma collections. By insisting on **Demonstrated vs Not‑Yet‑Demonstrated** for every mechanism, it keeps the thesis synchronized with the running system instead of with wishful thinking.

In short, Appendix A is the **ledger of what is actually true in the code and services today**, and the procedure for updating that ledger as the system grows.
