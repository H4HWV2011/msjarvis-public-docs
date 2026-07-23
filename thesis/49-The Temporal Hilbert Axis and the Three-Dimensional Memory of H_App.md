# 49. The Temporal Hilbert Axis and the Three-Tier Memory of \(H_{\mathrm{App}}\)

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 22, 2026*

---

## 49.1 What This Chapter Is Allowed to Claim

Within this gate, Chapter 49 may be rewritten as an **as‑built temporal Hilbert axis chapter**.

It may claim that:

- \(H_{t}\) is **live** with three connected tiers: **ephemeral**, **staged**, and **historical**;  
- ephemeral and staged temporal states are **Redis‑backed**, visible and round‑trippable via the temporal health probe;  
- historical temporal memory is backed by the **`public.temporal_historical_memory`** Postgres table;  
- **staged promotion observes a hysteresis window**, so events are not promoted prematurely;  
- **historical admission requires retention consent, coherence, and promotion readiness**;  
- **raw, unreviewed temporal traces are suppressed** and not auto‑promoted;  
- temporal decay is represented by a **bounded half‑life weighting**.

It must **not** claim:

- perfect time perception;  
- a complete historical archive of all events;  
- unconsented historical retention;  
- automatic promotion of raw traces;  
- clinical, legal, or universal safety guarantees.

The chapter stays inside these proven boundaries.

---

## 49.2 Plain‑Language Purpose for Rural Developers

For rural operators, this chapter answers:

> “How does Ms. Jarvis remember ‘when things happened’ without turning every moment into permanent history?”

This chapter explains, step by step:

- how the temporal axis \(H_{t}\) is implemented in three tiers;  
- how Redis and Postgres divide **short‑term vs historical** time;  
- how **hysteresis**, **consent**, and **coherence** control promotion;  
- how **decay/half‑life** keeps historical memory bounded.

It describes **how time works in practice** for this system, not how time should work in theory.

---

## 49.3 Three Tiers of Temporal Memory

The as‑built temporal system uses three tiers:

- **Ephemeral**: very short‑lived temporal state in Redis;  
- **Staged**: medium‑lived state in Redis waiting for review;  
- **Historical**: admitted temporal events in Postgres.

Each tier has its own **Redis prefix or table**:

- `hilbert:ephemeral:` for ephemeral;  
- `hilbert:staged:` for staged;  
- `public.temporal_historical_memory` for historical.

The temporal health probe shows that:

- keys with these prefixes exist;  
- ephemeral and staged keys can be written and read;  
- the historical table exists with the expected schema, even though its current row count is zero on this deployment.

---

## 49.4 Ephemeral Temporal State (Redis)

**Ephemeral** temporal state is the first tier.

The probe shows an ephemeral example:

- tier: `ephemeral`;  
- `storage_key`: `hilbert:ephemeral:9c65d5…`;  
- `age_seconds`: about 5;  
- `promotion_ready`: `false`;  
- `retention_consent`: `false`;  
- `coherence_ok`: `false`;  
- `verdict`: `PERMIT`;  
- `reason`: `"ephemeral_temporal_state_permitted"`.

In plain terms:

- very fresh, system‑role events can be **temporarily stored** in Redis;  
- they are allowed as ephemeral state for **`request_purpose: "temporal_memory"`**;  
- they are **not yet candidates** for durable history (promotion_ready is false, no consent).

TTL checks show a non‑zero time‑to‑live (for example, 3600 seconds), meaning:

- ephemeral events **expire automatically** from Redis if nothing else happens.

This tier is how the system thinks in the short term without committing to history.

---

## 49.5 Staged Temporal State (Redis)

**Staged** temporal state is the second tier.

The probe shows a staged example:

- tier: `staged`;  
- `storage_key`: `hilbert:staged:d187f5…`;  
- `age_seconds`: about 3600;  
- `promotion_ready`: `false`;  
- `retention_consent`: `false`;  
- `coherence_ok`: `false`;  
- `verdict`: `PERMIT`;  
- `reason`: `"staged_temporal_state_permitted"`.

There is also a **premature** staged example:

- `age_seconds`: 2;  
- `tier`: `staged`;  
- `verdict`: `REVIEW`;  
- `reason`: `"hysteresis_window_not_satisfied"`.

This shows that:

- staged events live in Redis under `hilbert:staged:`;  
- they represent **candidates under observation**, not yet committed history;  
- if an event is **too fresh** (inside the hysteresis window), the system returns `REVIEW` rather than promoting it.

For rural developers: staged events are **“waiting room” events**—the system is watching them, but has not decided to write them into history.

---

## 49.6 Historical Temporal State (Postgres)

**Historical** temporal memory is the third tier, stored in Postgres.

The probe shows:

- `historical_table`: `public.temporal_historical_memory`;  
- `exists.stdout`: `t` (table exists);  
- `columns.stdout` listing:

  - `id:bigint`  
  - `entity_id:text`  
  - `event_id:text`  
  - `event_type:text`  
  - `payload:jsonb`  
  - `truth_score:double precision`  
  - `provenance_hash:text`  
  - `admitted_at:timestamp with time zone`  
  - `valid_from:timestamp with time zone`  
  - `valid_to:timestamp with time zone`  
  - `superseded_at:timestamp with time zone`  
  - `superseded_by:text`  

- `count.stdout`: `"0"` (no rows yet on this deployment).

A historical example in the probe uses:

- tier: `historical`;  
- `verdict`: `PERMIT`;  
- `reason`: `"historical_temporal_state_permitted"`;  
- `record_id`: `httime_18b58182…`;  
- `storage_key`: `"public.temporal_historical_memory"`;  
- `age_seconds`: 3600;  
- `coherence_ok`: `true`;  
- `retention_consent`: `true`;  
- `promotion_ready`: `true`.

This combination shows **how** a historical event would be admitted:

- the event meets the gates (consent, coherence, promotion_ready);  
- it is written to the Postgres table with **truth score and provenance**;  
- later supersession can be tracked via `valid_from/valid_to` and `superseded_*` columns.

Even though the current row count is zero, the **table and contract exist and are tested**.

---

## 49.7 Hysteresis: Waiting Before Promotion

The probe constants include:

- `hysteresis_seconds`: `60.0`.

This means:

- the system requires a **minimum age** (here, 60 seconds) before an event can be treated as a serious candidate for historical promotion.

The “premature” case in the probe shows:

- `age_seconds`: 2.0;  
- `tier`: `staged`;  
- `promotion_ready`: `false`;  
- `verdict`: `REVIEW`;  
- `reason`: `"hysteresis_window_not_satisfied"`.

So if an event is **too recent**, the temporal gate refuses to commit it and returns a “review” verdict instead.

For rural operators, hysteresis is the system’s way of saying:

> “Let’s wait a little before writing this into history, in case it changes or turns out to be noise.”

---

## 49.8 Consent, Coherence, and Promotion Readiness

Historical admission is **not just about age**. The probe shows three distinct gate failures:

1. **Low coherence**  
   - `coherence_ok`: `false`;  
   - `retention_consent`: `true`;  
   - `promotion_ready`: `true`;  
   - `tier`: `historical`;  
   - `verdict`: `REVIEW`;  
   - `reason`: `"historical_coherence_required"`.

   The system says: “Even with consent and readiness, you can’t write incoherent temporal state into history.”

2. **No retention consent**  
   - `coherence_ok`: `true`;  
   - `retention_consent`: `false`;  
   - `promotion_ready`: `true`;  
   - `verdict`: `SUPPRESS`;  
   - `reason`: `"historical_retention_consent_required"`.

   Here coherence is fine, but there is **no consent to retain**, so the event is suppressed from historical memory.

3. **Raw, unreviewed trace**  
   - `coherence_ok`: `true`;  
   - `retention_consent`: `true`;  
   - `promotion_ready`: `true`;  
   - `verdict`: `SUPPRESS`;  
   - `reason`: `"forbidden_metadata:raw_unreviewed_trace"`.

   Even with consent and coherence, **raw unreviewed traces** are forbidden as historical entries.

These cases show that historical promotion requires:

- age outside the hysteresis window;  
- `coherence_ok == true`;  
- `retention_consent == true`;  
- no forbidden metadata;  
- `promotion_ready == true`.

Only then does the system return `verdict: "PERMIT"` for the historical tier.

---

## 49.9 Temporal Decay and Half‑Life Weighting

The probe includes `decay_weight` in each projection, and constants:

- `half_life_days`: `30.0`.

This describes a **half‑life decay model**:

- the longer ago an event occurred (`age_seconds`), the **smaller its weight** becomes;  
- `decay_weight` represents this decayed influence in the temporal axis.

Examples from the probe:

- ephemeral event at 5 seconds: `decay_weight ≈ 0.99999866`;  
- historical event at 3600 seconds: `decay_weight ≈ 0.99903776`.

The numbers are close to 1 for short times, but will gradually **drop over days** according to the half‑life.

For rural developers, half‑life weighting means:

- older events **still exist** in history, but their influence in time‑sensitive reasoning is **bounded and fades**;  
- temporal memory doesn’t treat every event as equally fresh forever.

---

## 49.10 Redis and Postgres Health

The probe confirms that:

- Redis read/write operations for `hilbert:ephemeral:` and `hilbert:staged:` keys return `OK`;  
- TTLs are set (for example, 3600 seconds);  
- lists of existing keys include:

  - `hilbert:ephemeral:9c65d5…`;  
  - `hilbert:staged:d187f5…`;  
  - multiple `hilbert:time:*` keys for probes and tests.

- Postgres reports:

  - `public.temporal_historical_memory` **exists**;  
  - the columns match the temporal contract;  
  - current count is `"0"`.

This shows that the temporal axis has:

- **live Redis support** for ephemeral and staged tiers;  
- a **live Postgres table** ready for historical admission.

---

## 49.11 Three‑Tier Temporal Flow for Rural Developers

The as‑built temporal axis can be pictured as this flow:

1. **Ephemeral tier (Redis, `hilbert:ephemeral:`)**  
   - Very fresh events;  
   - System role;  
   - Not ready for promotion;  
   - No retention consent yet;  
   - Allowed only as short‑term state.

2. **Staged tier (Redis, `hilbert:staged:`)**  
   - Events under observation;  
   - Must satisfy **hysteresis_seconds** (60s) before serious consideration;  
   - Still not historical;  
   - May be reviewed or dropped.

3. **Historical tier (Postgres, `public.temporal_historical_memory`)**  
   - Events that pass:

     - age/hysteresis;  
     - coherence;  
     - retention consent;  
     - promotion readiness;  
     - metadata checks (no forbidden raw traces).

   - Stored with truth score, provenance hash, validity interval, and supersession fields.

The system moves events **forward through tiers only when gates pass**, and may stop or suppress them at any point.

---

## 49.12 What This Chapter Does Not Claim

To stay within the gate:

- It does **not** claim that the system perceives time perfectly or detects every event;  
- It does **not** claim that `public.temporal_historical_memory` contains a complete archive;  
- It does **not** claim that any event can be retained without consent;  
- It does **not** claim that raw traces are automatically refined and promoted;  
- It does **not** claim temporal behavior as a clinical or legal safety guarantee.

It only claims:

- a **bounded temporal axis \(H_{t}\)** with three tiers;  
- **Redis‑backed ephemeral and staged states**;  
- a **Postgres‑backed historical table**;  
- **hysteresis, consent, coherence, and promotion gates**;  
- **half‑life decay weighting**.

---

## 49.13 Closing Statement

Chapter 49, at this closure, presents **the temporal Hilbert axis as it is actually built and tested**.

Time in Ms. Jarvis is handled through a three‑tier system: ephemeral and staged temporal states in Redis, and gated historical memory in Postgres. Promotion from “now” to “history” respects hysteresis, coherence, and retention consent, suppresses raw traces, and weights older events with a half‑life model. This gives rural developers a concrete, inspectable picture of how the system remembers **when things happened**—enough to provide continuity and context, but bounded so that not every trace becomes permanent history.
