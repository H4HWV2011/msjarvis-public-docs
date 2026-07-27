# Chapter 14. Internal-State Sandbox and Governed Promotion

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: July 27, 2026*

Candidate Trap Demo (July 26, 2026): one row flipped to promotion_state = 'candidate' → public_mv_rows = 0 confirmed

---

## 14.0 How to Read This Chapter (Rural Developer Guide)

This chapter is for anyone building a system where internal reasoning must
stay separate from external consequence until it has passed a series of
explicit, inspectable gates. It shows step by step how candidate states are
formed, held, tested, and either promoted or discarded — and it now has a
live proof of exactly what that boundary means in practice.

Six things to carry forward:

1. **The sandbox is a reasoning workspace, not a decision-maker.** Everything
   that happens inside the sandbox is candidate state. Nothing becomes
   authoritative until it passes the promotion gates.

2. **The Candidate Trap Demo (July 26, 2026) is the live proof of governed
   promotion.** One row in `public.gbim_record` was flipped from
   `promotion_state = 'authorized'` to `promotion_state = 'candidate'`.
   The result was confirmed immediately: `public_mv_rows = 0`. That row
   vanished from the public evidence surface the moment it became a candidate.
   This is not a policy claim — it is a mechanically enforced relational
   constraint, demonstrated live.

3. **Sandbox health and promotion-path health are different checks.** A
   healthy sandbox means internal reasoning can proceed safely. A healthy
   promotion path means candidates can actually move forward through BBB,
   constitutional guardians, and governed optimization cycles. Both need to
   be healthy for a candidate to become an authorized, speakable state.

4. **BBB enforcement is visible in the sandbox health report.** If BBB is
   inactive or unhealthy, no candidate from that sandbox should be promoted.
   This is not a judgment call — it is an operational rule.

5. **No private thoughts, no autonomous authority.** The sandbox holds
   technical candidate states, not feelings or self-modification power. Every
   claim in this chapter maps to a named service, endpoint, or schema field.

6. **Promotion is reversible until it is complete.** A candidate that fails a
   gate stays sandbox-local or is discarded. Nothing is committed until the
   full gate sequence is cleared.

---

## 14.1 Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Allis uses an internal-state sandbox as a
bounded place for reasoning that does not automatically become authority,
memory, or external action. It shows how sandboxed thinking is connected to
gateways, bridges, and promotion paths that are governed rather than
free-running.

It supports:

- **P1 – Every where is entangled** by tying internal deliberation to the
  containers, bridges, and governance services that make place-aware reasoning
  possible.
- **P3 – Power has a geometry** by making the path from sandbox to consequence
  a visible, gated route instead of a hidden leap from model output to action.
- **P5 – Design is a geographic act** by treating sandbox boundaries and
  promotion rules as design decisions that shape how Appalachian contexts are
  interpreted and acted upon.
- **P12 – Intelligence with a ZIP code** by ensuring that internal reasoning
  remains connected to local evidence and governance checks before it can
  affect durable state.
- **P16 – Power accountable to place** by requiring that any move from internal
  speculation to external consequence pass specific gates such as the
  blood–brain barrier (BBB), constitutional guardians, and governed
  optimization cycles.

This chapter belongs to the **Computational Instrument** tier. It specifies
how the internal-state sandbox operates as a candidate reasoning domain and
how promotion out of that domain is governed and bounded.

---

## 14.2 Gate-Constrained Scope

The scope of this chapter is tightly constrained by the governance gates that
already exist in the running system:

- The sandbox is **candidate reasoning**, not final authority.
- Promotion from sandbox must be gated by **governed optimization cycles, BBB,
  constitutional guardians, and bridge behavior**.
- BBB enforcement must be explicit and visible at runtime, not just implied.
- When some dependencies are only partially reachable, the text must
  distinguish **sandbox health** from **full promotion-path health**.
- The chapter must not claim private thoughts, literal consciousness, feelings,
  or autonomous authority beyond the implemented trace and gate mechanisms.

The **Candidate Trap Demo (July 26, 2026)** — one row flipped to
`promotion_state = 'candidate'`, `public_mv_rows = 0` confirmed — is the
chapter's live demonstration that these gate constraints are mechanically
enforced, not merely described. Within these limits, the internal-state sandbox
is documented as a bounded reasoning chamber with verified health reporting,
bridge reachability, and a named operational proof of promotion-boundary
enforcement.

---

## 14.3 What the Internal Sandbox Is

The internal-state sandbox is a **hosted reasoning workspace** inside
Ms. Allis.

It is:

- a containerized service with its own health endpoint;
- a place where candidate internal states are formed and manipulated;
- a domain for reversible, non-committing, high-level reasoning;
- a bridge-connected participant in the broader consciousness and promotion
  pipeline.

It is **not**:

- an autonomous source of authority;
- a store of private thoughts or feelings in a human sense;
- a clinical or therapeutic engine;
- a direct source of external action.

For rural developers, the internal-state sandbox should be understood as
something concrete and inspectable: it has a network address, a health
surface, and a known contract for how candidate reasoning is formed and moved.
The Candidate Trap Demo (July 26, 2026) is the concrete proof of what "not an
autonomous source of authority" means at the relational layer: a row that is
in candidate state produces `public_mv_rows = 0` and cannot back a public
claim until it is promoted to authorized.

---

## 14.4 Sandbox Health and Status

The internal-state sandbox exposes a health and status surface on its host
port.

The status view reports, at minimum:

- basic service health (up or down);
- BBB enforcement status inside the sandbox;
- whether the consciousness bridge is reachable from the sandbox;
- the bridge URL or internal DNS alias;
- the internal network or overlay used to reach the bridge;
- other dependencies such as guardians or judges where relevant.

Because BBB enforcement is visible in sandbox health, any rural developer can:

1. Check whether the sandbox is running at all.
2. Confirm that safety filters and governance hooks are live.
3. Decide whether to treat sandbox reasoning as a valid source of
   **candidate** states.

A status overlay compiled into the running container makes this reporting part
of runtime behavior rather than an aspirational design. The system either
reports these conditions truthfully or it is out of spec.

**Candidate Trap Demo result as a health-surface data point.** The July 26,
2026 demo confirmed that a row flipped to `promotion_state = 'candidate'`
immediately produced `public_mv_rows = 0`. This means the sandbox health
surface is not the only governance layer: the relational layer enforces the
candidate boundary independently of service health reports. A sandbox that
reports healthy while promotion-boundary enforcement is broken would be a
critical governance failure. The Candidate Trap Demo establishes the reference
probe for confirming that the relational enforcement layer is intact: any
auditor can re-run the flip-and-confirm sequence and verify the result.

---

## 14.5 Sandbox as Candidate Reasoning

The internal-state sandbox is explicitly **candidate reasoning**, not final
decision.

Typical activities inside the sandbox include:

- assembling retrieved evidence and contextual signals;
- forming hypotheses and intermediate conclusions;
- comparing alternative interpretations of the same situation;
- staging possible updates or actions as candidates;
- running internal tests or simulations on those candidates.

All of these activities are provisional. They support thinking and exploration,
but they do not, by themselves:

- become durable memory;
- change policy;
- alter external behavior;
- make binding commitments.

The sandbox is the place where Ms. Allis can "try out" reasoning under known
limits, without automatically turning those thoughts into consequences. At the
relational layer, this means that a row in `promotion_state = 'candidate'`
is the precise technical representation of a sandboxed state: it is stored,
visible to governance tooling, but produces `public_mv_rows = 0` — it cannot
reach the public evidence surface until it is promoted. The Candidate Trap Demo
(July 26, 2026) is the operational proof of this equivalence between
"candidate state in the sandbox" and "zero public visibility at the relational
layer."

---

## 14.6 Governing Promotion Out of the Sandbox

Promotion from sandboxed reasoning to higher-authority state is strictly
governed and never automatic.

A candidate state that attempts to leave the sandbox must pass:

- **Governed optimization cycles**, which evaluate proposals and decide whether
  to apply, reject, or roll back;
- **BBB enforcement**, which blocks unsafe, prohibited, or misaligned content
  from crossing into higher tiers;
- **Constitutional guardian checks**, which enforce civic, legal, and design
  constraints;
- **Bridge behavior**, which defines what internal content can be integrated
  into conscious state or other high-authority representations.

Only candidate states that survive these gates are eligible for further
promotion, such as becoming validated internal state, durable memory, or
externally visible output.

### Named Operational Proof — Candidate Trap Demo (July 26, 2026)

This sequence prevents sandboxed reasoning from turning directly into action
or belief just because it exists. The Candidate Trap Demo is the live proof
of what this prevention looks like at the relational layer:
