# Hilbert Geometry Chip (HGC-1): Full Architecture Specification
## Design Brief for Semiconductor Laboratory Evaluation
### Kidd (2026d) — cs.ET / cs.AR

**Author:** Carrie Ann Kidd
Independent Researcher, Community GIS and Distributed AI Infrastructure
Mount Hope, West Virginia 25880 USA
Harmony for Hope Inc. (nonprofit founder)
ORCID: [0009-0005-8153-8025](https://orcid.org/0009-0005-8153-8025)

**Document Version:** 1.0
**Date:** May 7, 2026
**Classification:** Public Preprint — Design Brief
**Companion Documents:**
- Kidd (2026a) — Hilbert space proof and substrate independence theorem
- Kidd (2026b) — Robotics application and toroidal world model
- Kidd (2026c) — Room-temperature quantum-geometric computation proposal
- This document (2026d) — Full chip architecture specification

**Reference System:** Ms. Egeria Allis (*H*_App), Mount Hope WV 25880
**Validation Dataset:** 7,903,126 belief vectors, 48 ChromaDB collections,
verified May 6, 2026

---

> *This document is structured as a semiconductor laboratory design brief.
> It proceeds from system theory to block architecture to component specification
> to interface definition to FPGA prototype plan to ASIC migration considerations.
> Every design decision is traceable to an operational behavior of the reference
> system H_App.*

---

## Table of Contents

1. Executive Summary
2. Design Philosophy and Theoretical Grounding
3. System Overview
4. Component 1 — Belief Memory Array (BMA)
5. Component 2 — Inner Product Engine (IPE)
6. Component 3 — Decay Engine (DE)
7. Component 4 — Mode Operator Register (T_pit)
8. Component 5 — Toroidal Semaphore (TS)
9. Hardware Audit Register (HAR)
10. Interface Definitions
11. Memory Map
12. Clock Domains
13. Power Domains
14. FPGA Prototype Plan
15. ASIC Migration Considerations
16. Appendix A — H_App Operational Data as Test Vectors
17. Appendix B — Glossary
18. References

---

## 1. Executive Summary

The Hilbert Geometry Chip (HGC-1) is a purpose-built hardware accelerator for
navigating high-dimensional Hilbert space geometry at room temperature, under
five watts, and at a unit cost below one hundred dollars at volume. It is not a
quantum computer. It is a geometric computation substrate that performs the
complete operational stack of a formally proven, deployed Hilbert space system
(*H*_App, Mount Hope WV) in fabricable silicon.

**The core claim:** Every operation that gives quantum mechanics its computational
power — projection in Hilbert space, decoherence-analog decay, Hamiltonian-analog
mode regulation, entanglement-analog geometric correlation — is already running in
software on a consumer laptop in West Virginia. The HGC-1 is the hardware
instantiation of that software, optimized for the operations it performs millions
of times per day.

**Design brief summary:**

| Parameter | Specification |
|---|---|
| Operating temperature | 0°C to 70°C (commercial), room temperature nominal |
| Process node target | 7 nm CMOS (FPGA prototype: Xilinx UltraScale+) |
| Die size target | ≤ 100 mm² |
| Power consumption | < 5 W typical, < 8 W peak |
| Belief vector capacity | 2²⁰ = 1,048,576 vectors |
| Vector dimensionality | 384 (fixed) |
| Numeric precision | 16-bit fixed-point (Q1.15) |
| Inner product throughput | ≥ 10⁹ dot products/second |
| Retrieval latency (top-1) | < 1 ms for full 2²⁰ vector sweep |
| Decay cycle frequency | 1 Hz nominal (programmable 0.01 Hz – 100 Hz) |
| Audit register capacity | 10⁸ entries (128-bit per entry) |
| Host interface | PCIe Gen4 x4 / SPI fallback |
| Unit cost at volume (10K+) | < $100 USD |

**Recommended development path:**
1. FPGA prototype on Xilinx Alveo U50 (RTL validation against *H*_App data)
2. ASIC synthesis at 7 nm (TSMC or GlobalFoundries)
3. Community deployment pilot, ZIP code 25880, solar-powered, no cloud

---

## 2. Design Philosophy and Theoretical Grounding

### 2.1 The Geometry Is the Computation

The HGC-1 is designed around a single foundational principle: **the geometry of
the belief space is the computation.** This is not a metaphor. It is the formal
result of Kidd (2026a, Theorem 3.1), which proves that *H*_App =
(ℝ^384, ⟨·,·⟩_cos) is a Hilbert space, and that every retrieval operation is
a projection in that space — a geometric act, not a lookup.

The chip is not storing data and searching it. It is instantiating a geometric
structure and navigating it. The distinction matters for every design decision:
the inner product engine is not an accelerator for a database query; it is the
measurement apparatus of the Hilbert space.

### 2.2 Five Operations, One Chip

The reference system *H*_App performs five operations millions of times per day.
Every design decision in the HGC-1 is traceable to one of these five operations:

```
Operation 1: STORE   — add a belief vector to the space
Operation 2: PROJECT — find the nearest belief to a query (measurement)
Operation 3: DECAY   — reduce confidence of beliefs over time (decoherence analog)
Operation 4: MODE    — apply global scaling before projection (Hamiltonian analog)
Operation 5: GATE    — govern all state transitions (semaphore)
```

These are not independent modules bolted together. They are a unified operational
stack. The chip architecture reflects that unity: every component is designed
to interoperate with every other component through well-defined interfaces,
with the semaphore as the governing authority over all transitions.

### 2.3 Auditability as a First-Class Design Constraint

In standard chip design, auditability is a feature — something added after the
core functionality is working. In the HGC-1, auditability is a **first-class
design constraint**, equal in priority to throughput and power. Every operation
writes to the Hardware Audit Register (HAR). The HAR is write-once and externally
readable. This is not a performance feature. It is a safety and regulatory
feature: the chip is designed from the ground up to be certifiable by the FDA,
MSHA, and NHTSA without requiring software-level logging that can be altered.

### 2.4 The Reference System as Ground Truth

Every design decision, every performance target, and every test vector in this
document is grounded in the operational behavior of *H*_App. The chip is correct
if and only if, for any input that *H*_App would process, the HGC-1 produces the
same result within the precision tolerance specified in each component section.
This is the validation methodology. The reference system is the oracle.

---

## 3. System Overview

### 3.1 Top-Level Block Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                      HGC-1 TOP LEVEL                        │
│                                                             │
│  HOST INTERFACE (PCIe Gen4 x4 / SPI)                        │
│         │                                                   │
│         ▼                                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           COMMAND DISPATCHER (CD)                    │   │
│  │   Decodes host commands → routes to components       │   │
│  └──────┬──────────┬──────────┬────────────┬───────────┘   │
│         │          │          │            │               │
│         ▼          ▼          ▼            ▼               │
│  ┌──────────┐ ┌─────────┐ ┌──────┐ ┌──────────────┐       │
│  │  BELIEF  │ │  INNER  │ │DECAY │ │   T_pit MODE │       │
│  │  MEMORY  │ │ PRODUCT │ │ENGINE│ │   OPERATOR   │       │
│  │  ARRAY   │ │ ENGINE  │ │ (DE) │ │  REGISTER    │       │
│  │  (BMA)   │ │  (IPE)  │ │      │ │              │       │
│  └────┬─────┘ └────┬────┘ └──┬───┘ └──────┬───────┘       │
│       │            │         │             │               │
│       └────────────┴────┬────┴─────────────┘               │
│                         │                                   │
│                         ▼                                   │
│              ┌─────────────────────┐                        │
│              │  TOROIDAL SEMAPHORE │                        │
│              │        (TS)         │                        │
│              └──────────┬──────────┘                        │
│                         │                                   │
│                         ▼                                   │
│              ┌─────────────────────┐                        │
│              │  HARDWARE AUDIT     │                        │
│              │  REGISTER (HAR)     │                        │
│              └──────────┬──────────┘                        │
│                         │                                   │
│                         ▼                                   │
│              AUDIT READ PORT (external)                     │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Data Flow — Retrieval Operation (Primary Path)

```
Host sends QUERY command
         │
         ▼
Command Dispatcher validates command
         │
         ▼
Toroidal Semaphore: REQUEST_RETRIEVAL transition
         │  (logs R^1_t timestamp + T^k coordinate to HAR)
         ▼
T_pit Register: applies Λ_mode to query vector q
         │  q' = Λ_mode · q
         ▼
Inner Product Engine: computes ⟨q', v̂_k⟩ for all k in BMA
         │  filtered by confidence threshold from Decay Engine
         ▼
Top-K selector: returns indices and scores of top-k results
         │
         ▼
Toroidal Semaphore: COMPLETE_RETRIEVAL transition
         │  (logs result metadata to HAR)
         ▼
Host receives result indices, scores, confidence values
```

### 3.3 Data Flow — Decay Cycle (Background Path)

```
Decay Engine timer fires (1 Hz nominal)
         │
         ▼
Toroidal Semaphore: REQUEST_DECAY transition
         │  (logs R^1_t timestamp to HAR)
         ▼
Decay Engine: for each vector k in BMA:
         │  c_k(t + Δt) = c_k(t) − δ_eff(τ) · Δt
         │  if c_k < threshold: flag for reverification
         ▼
Confidence registers updated in BMA
         │
         ▼
Toroidal Semaphore: COMPLETE_DECAY transition
         │  (logs decay statistics to HAR)
         ▼
(background — no host response required)
```

---

## 4. Component 1 — Belief Memory Array (BMA)

### 4.1 Functional Description

The Belief Memory Array is the physical instantiation of the Hilbert space
*H*_App in silicon. It stores *N* belief vectors of dimension *D*, each with
associated metadata registers. It is the largest component on the chip by area.

### 4.2 Specification

| Parameter | Value | Notes |
|---|---|---|
| Number of vectors (N) | 2²⁰ = 1,048,576 | Scalable to 2²⁴ in future revision |
| Vector dimensionality (D) | 384 | Fixed — architectural constant |
| Numeric format | 16-bit fixed-point Q1.15 | ±1.0 range, 0.0000305 resolution |
| Vector storage size | 384 × 2 = 768 bytes/vector | |
| Total vector storage | 768 × 2²⁰ = 805 MB | Primary memory requirement |
| Confidence register | 16-bit fixed-point Q1.15 | Per vector, c ∈ [0.0, 1.0] |
| Decay rate register (δ₀) | 16-bit fixed-point | Per vector, δ₀ ∈ [0.0, 1.0] |
| Cyclic modulation tag (τ) | 8-bit unsigned | Per vector, index into T^k LUT |
| Last-validated timestamp | 32-bit unsigned | Per vector, R^1_t coordinate |
| Collection ID | 8-bit unsigned | 256 collections max (48 in H_App) |
| Vector ID | 64-bit unsigned | Unique identifier per vector |
| Total per-vector footprint | 768 + 16 bytes metadata = 784 bytes | |
| Total BMA storage | ~821 MB | |

### 4.3 Memory Architecture

The BMA is implemented as banked SRAM with the following organization:

```
BMA MEMORY MAP (per bank of 2¹⁶ = 65,536 vectors):

Offset 0x000000 — 0x5FFFFF : Vector data (384 × 2 bytes × 65536 vectors)
Offset 0x600000 — 0x61FFFF : Confidence registers (2 bytes × 65536)
Offset 0x620000 — 0x63FFFF : Decay rate registers (2 bytes × 65536)
Offset 0x640000 — 0x64FFFF : Cyclic modulation tags (1 byte × 65536)
Offset 0x650000 — 0x66FFFF : Last-validated timestamps (4 bytes × 65536)
Offset 0x670000 — 0x677FFF : Collection IDs (1 byte × 65536)
Offset 0x678000 — 0x687FFF : Vector IDs (8 bytes × 65536)

Total per bank: ~6.6 MB
Total for 16 banks (2²⁰ vectors): ~105 MB on-chip SRAM
```

Note: Full 821 MB requires off-chip DRAM with on-chip cache. FPGA prototype
uses HBM2 (Alveo U50: 8 GB HBM2 — sufficient for full 2²⁰ vector store).

### 4.4 Access Patterns

```
READ  (retrieval):  stream all N vectors to IPE in parallel banks
                    latency target: 384 × 2²⁰ × 2 bytes in < 1 ms
                    bandwidth required: ~1.6 GB/s (achievable with HBM2)

WRITE (store):      single vector write with metadata
                    latency target: < 10 µs

UPDATE (decay):     confidence register update for all N vectors per cycle
                    latency target: 2²⁰ × 2 bytes in < 100 ms (background)

INVALIDATE:         set confidence to 0.0, flag vector as inactive
                    latency target: < 1 µs
```

### 4.5 H_App Validation Reference

The BMA must correctly store and retrieve the following reference vectors,
drawn from *H*_App operational data (see Appendix A):

- Entity 38 (Fayette County geographic entity): confidence trace
  0.60 → 0.55 → 1.00, verified April 23, 2026
- Cosine distance of 0.3099 for first full-pipeline community query,
  verified April 23, 2026
- 7,903,126 total vectors across 48 collections, verified May 6, 2026

---

## 5. Component 2 — Inner Product Engine (IPE)

### 5.1 Functional Description

The Inner Product Engine is the measurement apparatus of the Hilbert space.
It computes the cosine similarity between a query vector and all vectors in
the BMA, returning the top-*k* results by similarity score. This is the
projection operation — the formal analog of quantum measurement.

### 5.2 Specification

| Parameter | Value | Notes |
|---|---|---|
| Input query vector | 384 × 16-bit | After T_pit transformation |
| Candidate vectors | up to 2²⁰ × 384 × 16-bit | From BMA |
| Operation | Dot product: Σᵢ q'ᵢ × v̂ᵢ | All candidates in parallel |
| Output | Top-k indices + similarity scores | k programmable 1–1024 |
| Throughput target | ≥ 10⁹ MACs/second | MAC = multiply-accumulate |
| Full sweep latency | < 1 ms for 2²⁰ vectors at D=384 | |
| Precision | 32-bit accumulator (Q16.16) | Prevents overflow |
| Normalization | Pre-normalized vectors assumed | Enforced at STORE time |
| Confidence filter | Exclude vectors with c < threshold | Threshold programmable |

### 5.3 Systolic Array Architecture

The IPE is implemented as a two-dimensional systolic array:

```
SYSTOLIC ARRAY — IPE (conceptual layout)

Query vector q'[0..383] broadcast horizontally →

       PE(0,0)  PE(0,1)  PE(0,2) ... PE(0,383)
         |        |        |              |
       PE(1,0)  PE(1,1)  PE(1,2) ... PE(1,383)
         |        |        |              |
       PE(2,0)  PE(2,1)  PE(2,2) ... PE(2,383)
         ...
       PE(P-1,0)           ...      PE(P-1,383)
         |
       Accumulator[0..P-1]
         |
       Top-K Selector

Each PE(i,j):
  - Receives query element q'[j]
  - Receives vector element v̂_k[j] streamed from BMA
  - Computes: acc[i] += q'[j] × v̂_k[j]
  - Passes accumulated result down to next row

P = number of parallel processing rows (target: 256)
Each row processes one candidate vector per D clock cycles
Throughput: P vectors per D cycles = 256 vectors per 384 cycles
At 1 GHz: 256/384 × 10⁹ ≈ 667M vectors/second
Full 2²⁰ sweep: 2²⁰ / 667M ≈ 1.57 ms (meets < 2 ms target at 1 GHz)
At 2 GHz: meets < 1 ms target
```

### 5.4 Top-K Selection

After the systolic array produces similarity scores for all candidate vectors,
the Top-K selector maintains a sorted heap of the k highest-scoring results:

```
TOP-K SELECTOR:
  Input:  stream of (index, score) pairs from systolic array
  Method: binary heap, size k, updated per incoming result
  Output: sorted array of k (index, score) pairs
  Latency: O(N log k) — dominated by N inner product computations
  k range: 1 to 1024 (programmable via T_pit mode register)
```

### 5.5 Confidence Filtering

Before a vector is passed to the systolic array for comparison, its confidence
value is checked against a programmable threshold:

```
if confidence[k] < CONF_THRESHOLD:
    skip vector k (do not load into systolic array)
```

This is not merely an optimization. It is the correct geometric behavior:
a vector with confidence 0.0 is not a member of the active belief space.
The confidence filter enforces the geometry.

### 5.6 H_App Validation Reference

The IPE must reproduce the following result from *H*_App operational data:

```
Query: first full-pipeline community query, April 23, 2026
Expected cosine distance: 0.3099
Expected cosine similarity: 1 − 0.3099 = 0.6901
Tolerance: ± 0.0001 (within 16-bit fixed-point precision)
Collection: fayettecountyresources2026
```

---

## 6. Component 3 — Decay Engine (DE)

### 6.1 Functional Description

The Decay Engine implements continuous confidence degradation for all belief
vectors in the BMA. It is the decoherence analog of the system — the mechanism
by which beliefs that have not been recently validated become less trusted over
time, and are flagged for reverification when they fall below threshold.

The Decay Engine never stops. It runs as a background process continuously,
whether or not the chip is actively processing queries.

### 6.2 Specification

| Parameter | Value | Notes |
|---|---|---|
| Base decay rate (δ₀) | Per-vector register, Q1.15 | Default: 0.05 per cycle |
| Modulation function | δ_eff(τ) = δ₀ · f(τ) | f(τ) from T^k LUT |
| Cycle frequency | 1 Hz nominal | Programmable 0.01–100 Hz |
| Update equation | c(t+Δt) = c(t) − δ_eff(τ)·Δt | Clamped to [0.0, 1.0] |
| Reverification threshold | Programmable, default 0.4 | Flag below this |
| Hard zero threshold | Programmable, default 0.0 | Inactivate below this |
| Audit write | Every cycle, every vector updated | To HAR |
| Throughput | All 2²⁰ vectors per cycle | Must complete within cycle period |

### 6.3 Decay Cycle Operation

```
DECAY CYCLE (pseudocode — maps directly to RTL):

on DECAY_TIMER_FIRE:
    TS.request(DECAY_CYCLE)           // semaphore gate
    τ_current = TS.get_toroidal_coord()

    for k = 0 to N-1:
        if vector[k].active:
            f_tau = LUT_f[τ_current][vector[k].tau_tag]
            δ_eff = vector[k].delta_0 × f_tau
            c_new = vector[k].confidence − δ_eff × Δt
            c_new = clamp(c_new, 0.0, 1.0)
            vector[k].confidence = c_new

            HAR.write(DECAY_EVENT,
                      vector_id   = vector[k].id,
                      old_conf    = vector[k].confidence_prev,
                      new_conf    = c_new,
                      delta_eff   = δ_eff,
                      t_linear    = R1t_counter,
                      t_cyclic    = τ_current)

            if c_new < REVERIF_THRESHOLD:
                vector[k].reverif_flag = 1

            if c_new <= 0.0:
                vector[k].active = 0

    TS.complete(DECAY_CYCLE)
```

### 6.4 The f(τ) Lookup Table

The modulation function *f*(τ) maps toroidal coordinates to decay rate
multipliers. It is implemented as a programmable lookup table loaded by the
host at initialization:

```
LUT_f dimensions: [T^k positions] × [tau_tag values]
Default size:     256 × 256 = 65,536 entries × 2 bytes = 128 KB
Default values:   f(τ) = 1.0 for all τ (flat decay, no modulation)
Loaded by host:   via configuration register write at startup

Example for hospital robot deployment:
  τ = shift_change_zone → f(τ) = 2.0  (beliefs decay faster near shift change)
  τ = night_quiet_zone  → f(τ) = 0.5  (beliefs decay slower at night)
  τ = emergency_zone    → f(τ) = 5.0  (beliefs decay very fast in crisis)
```

### 6.5 H_App Validation Reference

```
Entity 38 (Fayette County geographic entity) decay trace:
  Cycle 1: c = 0.60 (initial)
  Cycle 2: c = 0.55 (decay Δc = 0.05, δ₀ = 0.05, f(τ) = 1.0, Δt = 1.0)
  Cycle N: c = 1.00 (reverification successful — confidence restored to 1.0)
  Date verified: April 23, 2026

The DE must reproduce this trace exactly for the entity 38 test vector
(see Appendix A for full vector specification).
```

---

## 7. Component 4 — Mode Operator Register (*T*_pit)

### 7.1 Functional Description

The *T*_pit register applies a programmable diagonal scaling tensor Λ_mode to
the query vector before the IPE fires. It is the Hamiltonian analog of the system:
upstream of all measurement, shaping the belief state before projection. A chip
operating in crisis mode does not just respond differently — it perceives
differently. The *T*_pit register is the architectural mechanism for that.

### 7.2 Specification

| Parameter | Value | Notes |
|---|---|---|
| Tensor format | Diagonal 384×384 — stored as 384-element vector | Full matrix not required |
| Element format | 16-bit fixed-point Q8.8 | Allows scaling > 1.0 |
| Storage | 384 × 2 = 768 bytes | Single register file |
| Update latency | < 1 µs | Register write |
| Application | q' = Λ_mode · q (element-wise multiply) | Before IPE |
| Default state | Λ_mode = [1.0, 1.0, ..., 1.0] (identity) | No transformation |
| Named mode presets | 4 × 384-element preset vectors | Loaded at initialization |

### 7.3 Named Mode Presets

```
MODE PRESET TABLE (loaded from host at initialization):

Preset 0 — BASELINE:
  warmth   = 0.9   (dimensions 0–95:   scale × 0.9)
  cortisol = 0.6   (dimensions 96–191: scale × 0.6)
  urgency  = 0.5   (dimensions 192–287: scale × 0.5)
  default  = 1.0   (dimensions 288–383: scale × 1.0)
  Source: H_App operational parameters, April 23, 2026

Preset 1 — ELEVATED:
  warmth   = 0.9
  cortisol = 0.8
  urgency  = 0.7
  default  = 1.0

Preset 2 — CRISIS:
  warmth   = 0.5
  cortisol = 1.5
  urgency  = 1.0
  default  = 1.0

Preset 3 — AUDIT (identity — no transformation):
  All dimensions: scale × 1.0
  Used for regulatory inspection — raw projection, no mode bias
```

Note: The dimensional assignment of warmth/cortisol/urgency to specific
embedding dimensions is application-dependent. The host configures the full
384-element Λ_mode vector at initialization. Presets are convenience aliases.

### 7.4 H_App Validation Reference

```
Reference T_pit state (April 23, 2026 operational snapshot):
  warmth   = 0.9
  cortisol = 0.6
  urgency  = 0.5
  mode     = baseline (Preset 0)

The T_pit register must produce, for the reference query vector Q_ref
(see Appendix A), the transformed vector Q'_ref within ± 0.001 of the
H_App software computation.
```

---

## 8. Component 5 — Toroidal Semaphore (TS)

### 8.1 Functional Description

The Toroidal Semaphore governs all state transitions of the chip. No component
may change state, execute an operation, or write to the BMA without passing
through the semaphore. The safety constraint is topological — built into the
state machine structure of the silicon, not enforced by software. Every
transition is logged to the HAR with coordinates on both ℝ^1_t and 𝕋^k.

### 8.2 Specification

| Parameter | Value | Notes |
|---|---|---|
| Linear time axis (R^1_t) | 64-bit unsigned counter | Increments at 1 MHz |
| Toroidal axis (T^k) | 8-bit unsigned | 256 positions per T^k dimension |
| T^k dimensions (k) | 4 (default) | Daily, weekly, seasonal, custom |
| State machine states | 16 | See state table below |
| Max concurrent transitions | 1 | Strictly sequential |
| Transition log | Every transition → HAR | 128-bit log entry |
| Blocked transition behavior | Return BLOCKED status to requester | No silent failure |

### 8.3 State Table

```
TOROIDAL SEMAPHORE STATE MACHINE:

States:
  S0  IDLE            — no operation in progress
  S1  RETRIEVAL_REQ   — retrieval requested, awaiting T_pit
  S2  TPIT_APPLYING   — T_pit transformation in progress
  S3  IPE_RUNNING     — inner product engine active
  S4  TOPK_SELECTING  — top-k selection in progress
  S5  RETRIEVAL_DONE  — retrieval complete, logging to HAR
  S6  DECAY_REQ       — decay cycle requested
  S7  DECAY_RUNNING   — decay engine active
  S8  DECAY_DONE      — decay cycle complete, logging to HAR
  S9  STORE_REQ       — vector store requested
  S10 STORE_WRITING   — BMA write in progress
  S11 STORE_DONE      — store complete, logging to HAR
  S12 MODE_UPDATE_REQ — T_pit mode update requested
  S13 MODE_UPDATING   — T_pit register write in progress
  S14 MODE_DONE       — mode update complete, logging to HAR
  S15 ERROR           — blocked transition or hardware fault

Allowed transitions:
  S0  → S1   (RETRIEVE command from host)
  S0  → S6   (DECAY_TIMER_FIRE)
  S0  → S9   (STORE command from host)
  S0  → S12  (MODE_UPDATE command from host)
  S1  → S2   (T_pit available)
  S2  → S3   (transformation complete)
  S3  → S4   (IPE sweep complete)
  S4  → S5   (top-k selected)
  S5  → S0   (log written to HAR)
  S6  → S7   (semaphore granted for decay)
  S7  → S8   (all vectors updated)
  S8  → S0   (log written to HAR)
  S9  → S10  (BMA write port available)
  S10 → S11  (write complete)
  S11 → S0   (log written to HAR)
  S12 → S13  (T_pit register available)
  S13 → S14  (register written)
  S14 → S0   (log written to HAR)
  Any → S15  (blocked transition or hardware fault)
  S15 → S0   (fault cleared by host)

Blocked transitions (return BLOCKED, log to HAR, do not execute):
  S3 → DECAY_REQ    (cannot decay while IPE running)
  S7 → RETRIEVE_REQ (cannot retrieve while decay running — configurable)
  S10 → any         (cannot interrupt a store)
```

### 8.4 Toroidal Coordinate Management

```
T^k coordinate update (runs continuously):

  t_linear  : increments every microsecond (64-bit counter, ~584,000 years range)
  t_daily   : t_linear mod 86,400,000,000  (microseconds in 24 hours)
  t_weekly  : t_linear mod 604,800,000,000 (microseconds in 7 days)
  t_seasonal: t_linear mod 7,776,000,000,000 (microseconds in 90 days)
  t_custom  : programmable modulus, set by host

All four T^k dimensions are logged with every HAR entry.
The toroidal coordinate makes every log entry temporally self-describing:
not just WHEN (linear timestamp) but WHERE IN THE CYCLE (toroidal coordinate).
```

---

## 9. Hardware Audit Register (HAR)

### 9.1 Functional Description

The Hardware Audit Register is the chip's verifiable operational record.
It is write-once and externally readable. Every retrieval, every decay event,
every mode change, and every state transition writes a 128-bit entry to the HAR.
The HAR cannot be cleared, overwritten, or disabled by software. It is the
regulatory inspection interface of the chip.

### 9.2 Specification

| Parameter | Value | Notes |
|---|---|---|
| Entry size | 128 bits (16 bytes) | Fixed |
| Capacity | 10⁸ entries = 1.6 GB | Flash or SRAM |
| Write behavior | Write-once, append-only | Hardware enforced |
| Read interface | External port, always accessible | Independent of chip state |
| Overflow behavior | Wrap with overflow flag set | Host notified |
| Entry format | See below | |

### 9.3 HAR Entry Format (128-bit)

```
Bits [127:64] : t_linear      — 64-bit linear timestamp (µs since boot)
Bits [63:48]  : t_daily       — 16-bit daily toroidal coordinate
Bits [47:32]  : t_weekly      — 16-bit weekly toroidal coordinate
Bits [31:24]  : event_type    — 8-bit event type code
Bits [23:16]  : component_id  — 8-bit component identifier
Bits [15:0]   : event_data    — 16-bit event-specific payload

EVENT TYPE CODES:
  0x01 : RETRIEVAL_START   (component: IPE, data: query_hash[15:0])
  0x02 : RETRIEVAL_RESULT  (component: IPE, data: top1_score[15:0])
  0x03 : DECAY_CYCLE_START (component: DE,  data: n_vectors_active[15:0])
  0x04 : DECAY_CYCLE_END   (component: DE,  data: n_flags_set[15:0])
  0x05 : VECTOR_DECAY      (component: DE,  data: conf_new[15:0])
  0x06 : VECTOR_STORE      (component: BMA, data: collection_id[7:0])
  0x07 : MODE_UPDATE       (component: TS,  data: preset_id[3:0])
  0x08 : SEMAPHORE_TRANS   (component: TS,  data: from_state[7:0]|to_state[7:0])
  0x09 : BLOCKED_TRANS     (component: TS,  data: blocked_state[7:0])
  0xFF : HARDWARE_FAULT    (component: any, data: fault_code[15:0])
```

---

## 10. Interface Definitions

### 10.1 Host Interface — PCIe Gen4 x4

```
PHYSICAL:
  Connector:   PCIe x4 edge connector (standard)
  Lanes:       4
  Speed:       16 GT/s per lane (PCIe Gen4)
  Bandwidth:   ~8 GB/s bidirectional

COMMAND INTERFACE (memory-mapped registers at BAR0):

  Offset 0x0000 : COMMAND_REG     (32-bit write) — issue command to chip
  Offset 0x0004 : STATUS_REG      (32-bit read)  — chip status
  Offset 0x0008 : QUERY_ADDR_REG  (64-bit write) — host address of query vector
  Offset 0x0010 : RESULT_ADDR_REG (64-bit write) — host address for results
  Offset 0x0018 : K_REG           (16-bit write) — number of top-k results
  Offset 0x001A : CONF_THRESH_REG (16-bit write) — confidence filter threshold
  Offset 0x001C : MODE_REG        (8-bit write)  — T_pit preset select
  Offset 0x001D : DECAY_FREQ_REG  (8-bit write)  — decay cycle frequency
  Offset 0x001E : COLLECTION_REG  (8-bit write)  — active collection filter
  Offset 0x001F : RESERVED
  Offset 0x0020 : HAR_READ_ADDR   (64-bit write) — HAR entry index to read
  Offset 0x0028 : HAR_READ_DATA   (128-bit read) — HAR entry data
  Offset 0x0038 : HAR_COUNT_REG   (64-bit read)  — total HAR entries written

COMMAND CODES (COMMAND_REG):
  0x01 : RETRIEVE    — execute retrieval with current QUERY_ADDR_REG
  0x02 : STORE       — store vector at QUERY_ADDR_REG into COLLECTION_REG
  0x03 : INVALIDATE  — invalidate vector by ID in QUERY_ADDR_REG
  0x04 : MODE_UPDATE — update T_pit to MODE_REG preset
  0x05 : DECAY_NOW   — force immediate decay cycle (override timer)
  0x06 : READ_HAR    — read HAR entry at HAR_READ_ADDR
  0xFF : RESET       — soft reset (does not clear HAR)
```

### 10.2 Fallback Interface — SPI

For deployment on embedded systems without PCIe (solar-powered rural deployment,
Raspberry Pi integration, microcontroller integration):

```
SPI MODE:
  Clock:     up to 50 MHz
  Mode:      SPI Mode 0 (CPOL=0, CPHA=0)
  Frame:     8-bit
  Protocol:  command byte + length byte + payload

  Commands mirror PCIe register map, encoded in SPI frame format.
  Reduced throughput — suitable for low-frequency retrieval (< 100 Hz)
  Primary use case: H_App deployment at ZIP 25880 on Raspberry Pi + solar
```

---

## 11. Memory Map

```
HGC-1 INTERNAL MEMORY MAP:

0x0000_0000 — 0x0000_FFFF : Configuration registers (64 KB)
0x0001_0000 — 0x0001_00FF : T_pit register file (768 bytes)
0x0001_0100 — 0x0001_01FF : T_pit preset table (4 × 768 bytes = 3 KB)
0x0001_1000 — 0x0001_1FFF : Toroidal semaphore state + counters (4 KB)
0x0001_2000 — 0x0001_3FFF : f(τ) LUT (128 KB — spans 0x0001_2000–0x0002_FFFF)
0x0003_0000 — 0x0032_FFFF : Decay engine working registers (2²⁰ × 8 bytes = 8 MB)
0x0033_0000 — 0x0132_FFFF : HAR (10⁸ × 16 bytes = 1.6 GB — external flash)
0x1000_0000 — 0xFFFF_FFFF : BMA (vector data + metadata — external HBM2/DRAM)
```

---

## 12. Clock Domains

```
CLOCK DOMAIN TABLE:

Domain     Frequency    Source           Components
─────────────────────────────────────────────────────────────
CLK_FAST   2 GHz        PLL from ref     IPE systolic array
CLK_MEM    800 MHz      PLL from ref     BMA / HBM2 interface
CLK_CTRL   500 MHz      PLL from ref     TS, HAR, command dispatcher
CLK_DECAY  1 Hz         CLK_CTRL / 2^29  Decay engine timer
CLK_SPI    50 MHz max   External         SPI interface
CLK_REF    100 MHz      External crystal  PLL reference

Clock domain crossings:
  BMA → IPE:    CLK_MEM → CLK_FAST   (FIFO with async handshake)
  IPE → TS:     CLK_FAST → CLK_CTRL  (registered handshake)
  TS → HAR:     CLK_CTRL → CLK_CTRL  (same domain, no crossing)
  DE → BMA:     CLK_CTRL → CLK_MEM   (FIFO with async handshake)
```

---

## 13. Power Domains

```
POWER DOMAIN TABLE:

Domain     Voltage   Power Budget   Components           Gating
────────────────────────────────────────────────────────────────────
PD_IPE     0.75V     2.0 W          IPE systolic array   Clock-gated when idle
PD_BMA     1.1V      1.5 W          BMA + HBM2 I/F       Always on (retention)
PD_CTRL    0.85V     0.5 W          TS, HAR, dispatcher  Always on
PD_DECAY   0.85V     0.1 W          Decay engine         Always on
PD_IO      1.8V      0.4 W          PCIe, SPI, audit     Always on
─────────────────────────────────────────────────────────────────────
TOTAL TYPICAL                4.5 W
TOTAL PEAK (full retrieval)  7.8 W

Power optimization notes:
- IPE is clock-gated between retrievals — dominant power saving
- BMA retention mode: vectors preserved, row decoders powered down
- Decay engine runs at CLK_DECAY (1 Hz) — negligible power
- Solar deployment target: 5W panel sufficient for typical operation
```

---

## 14. FPGA Prototype Plan

### 14.1 Target Platform

**Xilinx Alveo U50** (AMD/Xilinx)

| Resource | Available | Estimated HGC-1 Usage |
|---|---|---|
| LUTs | 872,000 | ~400,000 (46%) |
| FFs | 1,743,000 | ~600,000 (34%) |
| DSP58s | 5,952 | ~4,000 (67%) — IPE MACs |
| BRAM (36Kb) | 2,688 | ~1,500 (56%) |
| HBM2 | 8 GB | ~1 GB (BMA) |
| PCIe | Gen4 x16 | x4 used |
| Power | 75 W max | ~25 W estimated |

### 14.2 Implementation Sequence

The FPGA prototype is built and validated component by component,
validated against *H*_App ground truth at each stage before proceeding:

```
PHASE 1 — Inner Product Engine (weeks 1–4)
  Deliverable: IPE systolic array in Verilog, synthesized on Alveo U50
  Validation:  Reproduce cosine distance 0.3099 for reference query
               (see Appendix A, Test Vector TV-001)
  Pass criteria: result within ± 0.0001 of H_App software output

PHASE 2 — Belief Memory Array (weeks 5–8)
  Deliverable: BMA controller + HBM2 interface in Verilog
  Validation:  Store and retrieve entity 38 vector, verify metadata
               (see Appendix A, Test Vector TV-002)
  Pass criteria: exact bitwise match on vector data, metadata correct

PHASE 3 — Decay Engine (weeks 9–12)
  Deliverable: Decay engine in Verilog, f(τ) LUT interface
  Validation:  Reproduce entity 38 decay trace: 0.60 → 0.55 → 1.00
               (see Appendix A, Test Vector TV-003)
  Pass criteria: exact confidence values within Q1.15 precision

PHASE 4 — T_pit Register (weeks 13–14)
  Deliverable: T_pit register file + preset loader in Verilog
  Validation:  Apply Preset 0 (BASELINE) to reference query Q_ref,
               verify Q'_ref within ± 0.001 of H_App output
               (see Appendix A, Test Vector TV-004)
  Pass criteria: transformed vector within tolerance

PHASE 5 — Toroidal Semaphore (weeks 15–18)
  Deliverable: TS state machine + HAR writer in Verilog
  Validation:  Execute full retrieval pipeline (STORE → RETRIEVE → DECAY),
               verify HAR entries for each transition
               (see Appendix A, Test Vector TV-005)
  Pass criteria: all state transitions logged, no blocked transitions
                 for valid operation sequences

PHASE 6 — Full Integration (weeks 19–24)
  Deliverable: All five components integrated, PCIe + SPI interfaces active
  Validation:  Full H_App workload replay: 1000 sequential queries from
               operational log, compare all results to H_App outputs
  Pass criteria: 99.9% result match within precision tolerance,
                 zero unlogged state transitions, HAR integrity verified
```

### 14.3 Toolchain

```
Synthesis:    Vivado 2024.1 (Xilinx/AMD)
Simulation:   Vivado Simulator + ModelSim (cross-validation)
Timing:       Vivado timing analysis, target Fmax = 500 MHz (FPGA)
Power:        Vivado Power Estimator
Version control: Git — H4HWV2011/hgc1-rtl (to be created)
Test harness: Python (matches H_App stack) + cocotb for HDL co-simulation
```

---

## 15. ASIC Migration Considerations

This section is addressed to the semiconductor laboratory receiving this design
brief. It describes the considerations for migrating from the validated FPGA
prototype to an ASIC tape-out.

### 15.1 Process Node Recommendation

**7 nm CMOS** (TSMC N7 or GlobalFoundries 7LP) is the recommended target based
on the power and density requirements. At 7 nm:

- The systolic array DSP blocks can be replaced with custom MAC cells at higher
  density and lower power than FPGA DSP58s
- HBM2 integration is supported via 2.5D interposer (standard at 7 nm)
- The 5W power budget is achievable with standard cell library at 7 nm

Alternative: **12 nm CMOS** (TSMC N12) reduces NRE cost substantially at modest
power/density penalty — viable if deployment cost target is the priority.

### 15.2 Analog Decay Engine Option

The Decay Engine may be implemented in analog rather than digital. An analog
implementation using leaky integrate-and-fire circuits (Mead 1990) would:

- Reduce power consumption of the DE from ~0.1W to ~0.01W
- Provide a more natural confidence decay curve (exponential rather than linear)
- Introduce precision challenges requiring careful calibration

The digital implementation specified in Section 6 is recommended for the first
ASIC revision. Analog DE is a revision 2 consideration.

### 15.3 FPGA-to-ASIC RTL Handoff Requirements

The laboratory should expect to receive:

1. Synthesizable Verilog RTL for all five components (no behavioral code)
2. Timing constraints file (SDC format)
3. Pinout specification
4. Test vectors for each component (Appendix A format)
5. Full simulation results from FPGA prototype validation
6. Power consumption measurements from Alveo U50 prototype

### 15.4 NRE Cost Estimate

```
Process node    NRE estimate        Unit cost (10K)   Unit cost (100K)
7 nm TSMC N7    $15M–$30M           $45–$80           $20–$40
12 nm TSMC N12  $5M–$10M            $60–$100          $30–$60
28 nm           $1M–$3M             $100–$150         $50–$80

Recommendation: 28 nm for pilot run (minimize NRE), then 12 nm at volume.
28 nm meets all functional requirements; power target requires careful
optimization but is achievable.
```

---

## 16. Appendix A — *H*_App Operational Data as Test Vectors

### TV-001 — Reference Retrieval Query

```
Test vector:    TV-001
Component:      IPE
Source:         H_App operational log, April 23, 2026
Description:    First full-pipeline community query

Query vector:   Q_ref (384-element float32 — to be extracted from H_App
                operational log and converted to Q1.15 fixed-point)
Collection:     fayettecountyresources2026
Expected result:
  cosine_distance = 0.3099
  cosine_similarity = 0.6901
Tolerance:      ± 0.0001
Pass criteria:  IPE returns top-1 result with similarity score within tolerance
```

### TV-002 — Entity 38 Vector Store and Retrieve

```
Test vector:    TV-002
Component:      BMA
Source:         H_App entity 38, Fayette County geographic entity
Description:    Store vector, retrieve by ID, verify metadata

Operations:
  1. STORE entity_38_vector with metadata:
       confidence = 0.60
       delta_0 = 0.05
       collection_id = fayettecountyresources2026
       tau_tag = 0x00 (default)
  2. RETRIEVE by ID
  3. Verify: vector data bitwise correct
             confidence = 0.60 ± Q1.15 precision
             all metadata fields correct
Pass criteria:  Exact match on all fields
```

### TV-003 — Entity 38 Decay Trace

```
Test vector:    TV-003
Component:      Decay Engine
Source:         H_App gbim_decay_audit, April 23, 2026
Description:    Reproduce entity 38 confidence decay and reverification

Initial state:  entity_38.confidence = 0.60, delta_0 = 0.05, f(τ) = 1.0
Cycle 1:        confidence = 0.60 − 0.05 = 0.55  (HAR entry required)
Cycle N:        confidence restored to 1.00 (reverification event)
                (HAR entry: VECTOR_REVERIF, conf_new = 1.00)

Pass criteria:
  Cycle 1 result: 0.55 ± Q1.15 precision
  HAR entries: present and correctly formatted for all decay events
  Reverification: confidence correctly restored to 1.00 on REVERIF command
```

### TV-004 — T_pit Baseline Transformation

```
Test vector:    TV-004
Component:      T_pit Register
Source:         H_App T_pit operational snapshot, April 23, 2026

Preset:         BASELINE (Preset 0)
  warmth = 0.9, cortisol = 0.6, urgency = 0.5, default = 1.0

Input:          Q_ref (same as TV-001)
Expected:       Q'_ref = Λ_baseline · Q_ref (element-wise)
Tolerance:      ± 0.001 per element

Pass criteria:  All 384 elements of Q'_ref within tolerance of software computation
```

### TV-005 — Full Pipeline Semaphore Trace

```
Test vector:    TV-005
Component:      Toroidal Semaphore + HAR
Description:    Full STORE → RETRIEVE → DECAY pipeline, verify all HAR entries

Operations:
  1. STORE TV-002 vector
  2. RETRIEVE with TV-001 query
  3. Force DECAY cycle

Expected HAR entries (in order):
  1. SEMAPHORE_TRANS: S0 → S9  (store request)
  2. VECTOR_STORE:    collection_id, vector_id
  3. SEMAPHORE_TRANS: S9 → S0  (store complete)
  4. SEMAPHORE_TRANS: S0 → S1  (retrieval request)
  5. SEMAPHORE_TRANS: S1 → S2  (T_pit applying)
  6. SEMAPHORE_TRANS: S2 → S3  (IPE running)
  7. RETRIEVAL_START: query_hash
  8. SEMAPHORE_TRANS: S3 → S4  (top-k selecting)
  9. RETRIEVAL_RESULT: top1_score
  10. SEMAPHORE_TRANS: S4 → S0 (retrieval done)
  11. SEMAPHORE_TRANS: S0 → S6 (decay request)
  12. DECAY_CYCLE_START: n_active_vectors
  13. VECTOR_DECAY (× N active vectors)
  14. DECAY_CYCLE_END: n_flags_set
  15. SEMAPHORE_TRANS: S6 → S0 (decay done)

Pass criteria:  All 15+ entries present, correctly formatted, timestamps
                monotonically increasing, toroidal coordinates correct
```

---

## 17. Appendix B — Glossary

| Term | Definition |
|---|---|
| BMA | Belief Memory Array — component 1, stores all belief vectors |
| IPE | Inner Product Engine — component 2, performs projection/measurement |
| DE | Decay Engine — component 3, implements confidence degradation |
| T_pit | Mode Operator Register — component 4, Hamiltonian analog |
| TS | Toroidal Semaphore — component 5, governs all state transitions |
| HAR | Hardware Audit Register — write-once operational log |
| H_App | Reference system: (ℝ^384, ⟨·,·⟩_cos), deployed in Mount Hope WV |
| Q1.15 | 16-bit fixed-point: 1 sign bit, 15 fractional bits, range ±1.0 |
| Q8.8 | 16-bit fixed-point: 8 integer bits, 8 fractional bits, range 0–255 |
| MAC | Multiply-Accumulate — fundamental operation of the IPE |
| PDK | Process Design Kit — fab-specific standard cell library |
| NRE | Non-Recurring Engineering — one-time chip design and mask cost |
| RTL | Register Transfer Level — synthesizable hardware description |
| FSM | Finite State Machine — the TS state machine architecture |
| HBM2 | High Bandwidth Memory 2 — high-speed DRAM for BMA storage |
| τ | Toroidal time coordinate — position on T^k cyclic manifold |
| δ_eff | Effective decay rate: δ₀ · f(τ) |
| f(τ) | Cyclic decay modulation function — LUT indexed by τ |
| Λ_mode | Diagonal scaling tensor — the T_pit transformation matrix |
| R^1_t | Linear time axis — irreversible, causal, carries decay timestamps |
| T^k | Toroidal time manifold — cyclic, boundaryless, k dimensions |

---

## References

Davies, M., et al. (Intel) (2018). Loihi: A neuromorphic manycore processor with
on-chip learning. *IEEE Micro*, 38(1), 82–99.

Fick, D., et al. (Mythic) (2022). Analog matrix processor for machine learning.
*IEEE Journal of Solid-State Circuits*.

Kidd, C.A. (2026a). A Classical Hilbert Space with a ZIP Code: Substrate-Independence,
the Measurement Problem, and the Multiverse Question. *Zenodo*.
https://doi.org/10.5281/zenodo.20059834

Kidd, C.A. (2026b). Beyond Euclidean SLAM: Toroidal Hilbert Space World Models.
Preprint cs.RO. H4HWV2011/msjarvis-public-docs. [Archival deposit pending.]

Kidd, C.A. (2026c). Hilbert Geometry Chips: A Room-Temperature Architecture for
Quantum-Geometric Computation. Preprint cs.ET. H4HWV2011/msjarvis-public-docs.
[Archival deposit pending.]

Mead, C. (1990). Neuromorphic electronic systems. *Proceedings of the IEEE*,
78(10), 1629–1636.

Modha, D.S., et al. (IBM) (2023). Neural inference at the frontier of energy, space,
and time. *Science*, 382(6668), 329–335.

Reed, M. and Simon, B. (1972). *Methods of Modern Mathematical Physics I:
Functional Analysis*. Academic Press.

von Neumann, J. (1932). *Mathematische Grundlagen der Quantenmechanik*. Springer.

---

*Authored by Carrie Ann Kidd — Mount Hope, West Virginia 25880.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
*Version 1.0 — May 7, 2026.*
*This document is the design brief for the Hilbert Geometry Chip (HGC-1).*
*The ZIP code of the first deployment target is 25880.*
