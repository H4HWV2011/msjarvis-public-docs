# 10. WOAH: Weighted Optimization Algorithm Hierarchy

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 10, 2026*

---

## Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Allis coordinates many specialized agents as a
**population**, rather than relying on a single model, and how that coordination is
constrained by spatial-justice goals.

It supports:

- **P1 – Every where is entangled** by treating governance, spatial, and narrative agents
  as a coupled population whose influence is jointly optimized, not siloed.
- **P3 – Power has a geometry** by shaping how optimization pressure flows through the
  service graph, deciding which agents' outputs are amplified or muted for particular
  places and tasks.
- **P5 – Design is a geographic act** by making orchestration weights and routing
  strategies first-class design choices that affect how West Virginia is seen and served.
- **P12 – Intelligence with a ZIP code** by privileging agents and retrieval paths that
  are explicitly grounded in Appalachian data and institutions.
- **P16 – Power accountable to place** by keeping WOAH as a glass-box service that can
  expose how different agents were weighted in producing an answer.

This chapter belongs to the **Computational Instrument** tier: it specifies a
WOA-inspired orchestration layer that coordinates Ms. Allis's multi-agent "mind" in
service of Quantarithmia's justice-oriented instruments.

WOAH operates at **Phase 2.5 of the 9-phase `ultimatechat` pipeline** (see Ch. 11
§11.4), but in the revised architecture its influence no longer stops at routing and
identity weighting alone. WOAH now also helps shape how the **internal-state sandbox**
runs, how heavily certain evaluative dimensions are emphasized, and how candidate
reasoning states are prepared for possible promotion.

> Figure 10.1. WOAH as a WOA-inspired orchestration service in Ms. Allis, weighting
> multiple agents and feeding those weights into the consciousness, routing, and sandbox
> governance stack with Appalachian, place-aware priorities.

---

## WOAH: Weighted Optimization Algorithm Hierarchy

This chapter describes WOAH (Weighted Optimization Algorithm Hierarchy) as used in Ms.
Egeria Allis. WOAH is inspired by the Whale Optimization Algorithm (WOA), a
population-based metaheuristic that models humpback whale hunting with exploration and
exploitation phases, but it is not a textbook WOA implementation.

In this system, WOAH is a set of concrete services that evaluate and weight multiple
agents, including LLMs, DGMs, RAG paths, and related evaluators, and feed those weights
into the consciousness and orchestration layers, helping coordinate many minds rather
than optimizing a single numeric function. WOAH should therefore be understood as a
**WOA-inspired orchestration pattern implemented as a service layer**, with practical
scoring and weighting logic, rather than as a fully formal WOA with provable convergence
guarantees.

The key revision in this chapter is that WOAH is now described as influencing
**sandbox behavior operationally**. Weighted optimization decisions are executed first
inside the internal-state sandbox, informed by neurobiological, affective, and qualia
signals, and are then subjected to BBB, constitutional, and DGM gating before they are
allowed to alter persistent state. WOAH does not directly rewrite durable memory,
identity, or code merely because it has produced a high score.

---

## Deployment Status

WOAH remains a live and meaningful part of the architecture. It continues to function as
an active orchestration and identity-weighting layer tied to the broader consciousness
stack, the Fifth DGM, the pituitary governor, and the service graph documented elsewhere
in the thesis.

Two roles remain important:

- **`allis-woah`** as the qualia-net internal WOAH node.
- **`nbb_woah_algorithms`** as the full scoring and population-dynamics service.

The chapter no longer treats WOAH as important only because it is deployed. It is now
important because its weighting outputs participate in the governed transition between
**sandboxed reasoning** and **admissible persistent effect**.

---

## Classical Whale Optimization Algorithm

The original Whale Optimization Algorithm (WOA) is a population-based optimization
method that models humpback whales' bubble-net hunting behavior.

Key features of WOA include:

- **Population and best agent** — a set of candidate solutions explores a search space,
  and the current best candidate guides others.
- **Encircling prey** — agents update their positions relative to the best solution using
  coefficients that shrink over time, balancing exploration and exploitation.
- **Spiral and bubble-net search** — a spiral equation models bubble-net feeding,
  allowing candidate solutions to move around the best in a shrinking spiral trajectory.

WOAH in Ms. Allis borrows the ideas of populations, encircling, and weighted movement
toward better candidates, but adapts them to agent orchestration rather than direct
numeric parameter search.

---

## WOAH in Ms. Allis: Conceptual Role

In Ms. Allis, WOAH refers to a hierarchy of weighting and evaluation processes that sit
between low-level agents and higher-level consciousness or orchestration.

Its familiar functions remain:

- **Multiple agents as "whales"** — different LLMs, DGMs, RAG paths, and analysis
  services act as candidate "whales," each producing outputs or evaluations over the same
  query or memory item.
- **Weighted evaluation** — WOAH services analyze those outputs and assign weights or
  scores indicating how much influence each agent should have for a given task, user, or
  place.
- **Hierarchical integration** — these weights are fed into consciousness coordinators,
  qualia engines, and judge layers that combine agent outputs into a final response.

The chapter now adds a further role: **WOAH influences sandbox behavior before
promotion**. Its weights may shape whether a sandbox cycle is required to consult WOAH
explicitly (`require_woah`), how many internal reasoning steps may be taken
(`max_steps`), how strict promotion thresholds are set for candidate states, and which
evaluation dimensions are emphasized during review.

In this sense WOAH is not merely a downstream scorer. It becomes part of the operational
governance of sandboxed reasoning.

---

## WOAH and the Internal-State Sandbox

The internal-state sandbox is the protected domain in which provisional reasoning can
occur without immediate production consequence. Retrieved context, model-generated
hypotheses, affective cues, EEG-linked signals, spatial relations, identity traces, and
qualia-linked interpretations can interact there as candidate internal states.

WOAH now helps shape this sandbox operationally.

A simplified control pattern is:

\[
\text{context} \rightarrow \text{WOAH weighting} \rightarrow \text{sandbox parameterization} \rightarrow \text{candidate reasoning state}
\]

This means WOAH-derived weights may influence, for example:

- whether WOAH participation is mandatory for a given internal reasoning cycle
  (`require_woah`);
- the allowed depth or breadth of deliberation inside the sandbox (`max_steps`);
- how strongly the evaluation regime emphasizes identity continuity, place-based
  salience, governance sensitivity, evidentiary sufficiency, or novelty;
- how conservative the later promotion thresholds will be when a candidate state seeks to
  leave the sandbox.

These are not direct writes to persistent memory. They are **sandbox-control effects**.
WOAH affects how the candidate state is formed and evaluated, not whether it is
automatically accepted.

---

## The WOAH Algorithms Service

The central production-grade WOAH component remains the **WOAH algorithms service**,
which computes weighting outputs over content and metadata and maintains a WOA-inspired
population of internal weight vectors.

Its scoring axes continue to include dimensions such as:

- `hierarchical_weight`
- `self_relevance`
- `temporal_importance`
- `novelty`
- `stability`
- `composite_weight`
- `identity_type`
- `weight_category`

Those outputs remain useful for identity and routing, but the current architecture now
treats them as relevant to sandbox governance as well.

A high-weight structural governance narrative, for example, may lead the system to:

- require explicit WOAH participation before the sandbox may attempt promotion;
- allow more internal steps so the candidate state is evaluated under richer context;
- increase scrutiny at the promotion boundary because the candidate, if later admitted,
  would have greater identity or governance consequence;
- emphasize evidentiary and constitutional review more strongly than novelty.

Conversely, low-weight or obviously transient material may be handled with lighter
sandbox parameters and stricter limits on persistence.

---

## WOA-Inspired Population Dynamics

WOAH maintains an internal population of weight vectors updated in a WOA-inspired way.
This lets the system accumulate policy tendencies over time rather than treating each
decision as wholly isolated.

The population remains useful for interpretability and orchestration, but the revised
architecture also links it to **sandbox governance**. As the population evolves, it can
shift how the system balances exploration and caution in the internal-state sandbox.

For example, a population trend toward strong identity weighting may lead the sandbox to:

- increase review intensity for autobiographical or governance-sensitive content;
- raise the bar for promotion into durable memory;
- preserve more provenance and justification metadata during candidate formation;
- keep certain high-salience states provisional for longer before they can be considered
  promotable.

This makes WOAH part of the system’s **epistemic control loop**, not merely a scoring
service for finished outputs.

---

## WOAH in the Consciousness and Orchestration Stack

WOAH occupies an intermediate layer in the Ms. Allis architecture, operating at
**Phase 2.5 of the 9-phase `ultimatechat` pipeline**.

**Upstream layers** still include user input, RAG paths, GIS and Hilbert-state services,
qualia and neurobiological signals, and governance-linked context.

**WOAH layer** functions now include:

- determining how important a memory or narrative may be for identity;
- distinguishing structural from episodic salience;
- feeding weighted context into consciousness and routing services;
- influencing sandbox parameters such as `require_woah`, `max_steps`, and evaluation
  emphasis;
- helping determine how cautious later promotion review should be.

**Downstream layers** include the Fifth DGM, BBB and constitutional review, the
consciousness bridge, and persistence-bearing memory layers.

The essential revision is this: **optimization decisions affecting persistent state are
not immediate**. WOAH may shape weighting, routing, or sandbox behavior, but if the
resulting candidate state could affect durable memory, identity continuity, action, or
external consequence, that state still moves through the internal-state sandbox and then
through DGM-style promotion gates before it becomes validated, experiential, or
persistent.

WOAH influences the path. It does not self-authorize the outcome.

---

## From WOAH Weight to Governed Promotion

The architecture now requires clearer language for how WOAH relates to state change.

A useful simplified chain is:

\[
S_{\mathrm{input}} \rightarrow S_{\mathrm{weighted}} \rightarrow S_{\mathrm{sandbox}} \rightarrow S_{\mathrm{candidate}} \xrightarrow{G_{\mathrm{BBB}} ,\, G_{\mathrm{constitutional}} ,\, G_{\mathrm{DGM}}} S_{\mathrm{validated}}
\]

and only thereafter, where permitted:

\[
S_{\mathrm{validated}} \rightarrow S_{\mathrm{experience}} \rightarrow S_{\mathrm{memory}}
\]

This makes explicit that a WOAH score is not itself a promotion event. It is one factor
in shaping the candidate state and the conditions under which that state may later be
reviewed.

WOAH may alter:

- the candidate’s evaluation priority;
- the depth of sandbox reasoning;
- the strictness of promotion thresholds;
- the relative emphasis of evidence, coherence, identity, geography, privacy, and
  constitutional constraint.

But the authority change occurs only at the **governed promotion boundary**.

---

## Thresholds and Hysteresis

A revised WOAH chapter must also prevent the mistaken impression that optimization modes
should switch instantly at one threshold.

If WOAH weights influenced sandbox behavior using only a single decision boundary, the
system could oscillate rapidly when a score hovered near that boundary. To avoid this,
the architecture should use **threshold bands** and **hysteresis**.

Let:

\[
\theta_{\mathrm{enter}}
\]

be the threshold for entering a heightened optimization or promotion-sensitive mode, and

\[
\theta_{\mathrm{exit}}
\]

be the threshold for leaving it, with:

\[
\theta_{\mathrm{exit}} < \theta_{\mathrm{enter}}
\]

Then a state or mode can be governed as follows:

- it enters a stricter or more WOAH-sensitive review mode only when the relevant score
  rises above \(\theta_{\mathrm{enter}}\);
- it remains in that mode until the score falls below \(\theta_{\mathrm{exit}}\).

This prevents rapid flapping near one boundary.

Operationally, this matters for:

- switching `require_woah` on or off;
- increasing or decreasing `max_steps`;
- toggling elevated promotion scrutiny for identity-bearing or governance-bearing
  content;
- changing how strongly the sandbox emphasizes locality, autobiographical relevance, or
  constitutional review.

The result is a more stable optimization regime. WOAH-guided governance changes occur
decisively, not nervously.

---

## WOAH and Non-Immediate Persistence

The chapter must be explicit that optimization pressure does not equal immediate
persistence.

A candidate conclusion formed under WOAH influence remains provisional while inside the
sandbox. Even when WOAH assigns strong structural weight, that does not by itself turn a
state into durable memory, identity content, or action-bearing belief.

Instead, the architecture requires:

1. weighted formation inside the sandbox;
2. candidate-state assessment under evidence, coherence, privacy, constitutional, and
   operational review;
3. DGM-style gating at the promotion boundary;
4. only then, selective admission into validated, experiential, or memory-bearing state.

This keeps WOAH aligned with the broader constitutional architecture of Ms. Allis.
Optimization remains governed, rather than self-justifying.

---

## Relationship to Classical WOA and Limitations

The relationship between WOAH and classical WOA remains honest but partial.

**Conceptual borrowing** includes:

- maintaining a population of candidates;
- moving candidates toward a current best vector;
- balancing exploitation with limited exploration.

**Implementation reality** is still more practical than formal:

- WOAH is a service-layer orchestration mechanism, not a mathematically complete optimizer;
- its semantic identity scoring remains heuristic and operational rather than proof-based;
- its population dynamics are useful for interpretability and policy shaping, but do not
  establish convergence guarantees;
- its outputs influence sandbox parameterization and evaluation emphasis, but do not
  bypass governance gates.

This thesis therefore presents WOAH as a **WOA-inspired orchestration and governance
instrument**, not as a complete formal optimization theory.

---

## WOAH as a Computational Instrument for Place-Accountable Intelligence

From a Polymathmatic Geography perspective, WOAH functions as a computational instrument
that connects algorithmic behavior to specific places and communities.

It does so by:

- privileging Appalachian and governance-linked content in its weighting logic;
- shaping which narratives receive stronger internal attention;
- exposing those weighting tendencies as an inspectable, glass-box process;
- influencing how sandbox reasoning is parameterized for place-sensitive or
  identity-sensitive content;
- participating in a governed transition regime rather than an automatic persistence
  regime.

This is especially important because WOAH now affects not only what the system values,
but how the system **deliberates before committing**. It therefore becomes part of the
geographic politics of internal cognition, not only the ranking of outputs.

WOAH belongs in the **Computational Instrument** tier because it is a first-class
orchestration layer whose weights shape information flow, evaluative attention, and the
conditions under which candidate states are even considered for promotion.

---

## Closing Statement

WOAH in Ms. Allis is no longer adequately described as only a routing and identity
weighting service. It is a WOA-inspired orchestration layer that now also influences
**sandbox behavior operationally**, including whether WOAH consultation is required, how
many internal reasoning steps may occur, which evaluative dimensions are emphasized, and
how strict later promotion thresholds become.

Its role remains governed rather than sovereign. Weighted optimization decisions that may
affect durable memory, identity, or action do not take effect immediately. They move
through the internal-state sandbox, then through BBB, constitutional, and DGM gates,
before any candidate state may become validated or persistent.

Threshold bands and hysteresis are therefore essential. They prevent optimization modes
from oscillating rapidly near a single boundary and ensure that WOAH-guided governance
changes remain stable, reviewable, and answerable to the larger constitutional design of
Ms. Allis.
