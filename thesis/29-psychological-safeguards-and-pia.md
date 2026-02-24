> **Why this matters for Polymathmatic Geography**
> This chapter formalizes how psychological and mental-health knowledge is integrated into
> Ms. Jarvis to guide interaction patterns, monitor interaction risks, and adapt system behavior
> over time. It supports:
> - **P1 – Every where is entangled** by ensuring that psychological safeguards are woven into
>   the same retrieval, filtering, and memory infrastructure that handles spatial and technical
>   content, not isolated in a separate silo.
> - **P3 – Power has a geometry** by making psychological constraints visible as named services,
>   tagged collections, and explicit endpoints rather than hiding them in opaque model behavior.
> - **P5 – Design is a geographic act** by tailoring psychological guidance to populations and
>   risk types specific to Appalachian communities — rural grief, economic stress, identity
>   disruption — rather than generic global corpora.
> - **P12 – Intelligence with a ZIP code** by grounding psychological RAG retrieval in
>   collections that include place-specific and community-specific mental health materials.
> - **P16 – Power accountable to place** by logging PIA review cycle outputs, recording
>   recommendations and observed patterns, and making this material available for human oversight
>   and community governance review.
>
> As such, this chapter belongs to the **Computational Instrument** tier: it specifies the
> psychological safeguard services, guidance corpus, and PIA review loop that protect
> interaction quality and mental-health alignment in Ms. Jarvis's operation.

---

## Status as of February 2026

| Category | Details |
|---|---|
| **Implemented now** | `jarvis-psychology-services` confirmed running at **127.0.0.1:8019**. Exposes `/psychological_assessment` accepting a query and returning structured fields: `psychological_assessment`, `therapeutic_guidance`, `emotional_support`, `wellbeing_recommendations`, `evidence_based_approaches`. `psychological_rag_domain` confirmed running at **127.0.0.1:9006**. Exposes `/search` and `/add_document` for a curated psychological corpus including therapy, mindfulness, trauma, depression, anxiety, and social-support materials. Dedicated psychological Chroma collections confirmed present in `jarvis-chroma` (**127.0.0.1:8002**). BBB four-filter pipeline (`EthicalFilter`, `SpiritualFilter`, `SafetyMonitor`, `ThreatDetection`) at **0.0.0.0:8016** (confirmed) functions as the primary live gate enforcing interaction safety constraints on every request. `normalize_identity` and `TruthValidator` enforce prohibitions on anthropomorphic claims and identity confusion on every `ultimatechat` response (Chapter 17, Chapter 22). `truthverdict` attached to every `UltimateResponse` with `correct_identity`, `correct_creator`, `relationship_clear` booleans. |
| **Partially implemented / scaffolded** | Classifier and trigger logic for routing requests to the psychological path is **partially heuristic** in the current deployment — topic classifiers and surface-cue detectors are present but not fully rule-documented; routing to `jarvis-psychology-services` is not yet wired into every `ultimatechat` call (Chapter 23). PIA review loop exists as a structured process that **manually samples logs and introspection outputs, producing written recommendations** — it does **not** auto-rewrite configuration, prompts, or filters. Integration of PIA recommendations back into barrier parameters, judge weights, or mode settings requires explicit operator action. Psychological-guidance-specific `consciousnesslayers` entries (e.g. a dedicated `psychological_assessment` layer in `UltimateResponse`) are not yet consistently produced on every call; they appear when `jarvis-psychology-services` is explicitly invoked. |
| **Future work / design intent only** | Automated, scheduled PIA review cycle with machine-readable output format for direct configuration integration. Hard routing of psychologically sensitive requests to `jarvis-psychology-services` based on confirmed classifier output. Automated propagation of PIA recommendations into BBB penalty weights, judge instructions, and global mode policies without manual operator step. Persistent introspective log of PIA cycle inputs, analyses, and recommendations as a first-class Chroma collection. Population- and risk-type-specific retrieval tuning (e.g. rural grief, adolescent caregivers) driving differential guidance retrieval. |

> **Cross-reference:** The BBB pipeline that enforces safety and ethical constraints is described
> in **Chapter 16**. Identity normalization and `TruthValidator` are described in **Chapter 22**.
> The psychological services' relationship to the meaning-oriented track (partially wired into
> `ultimatechat`) is described in **Chapter 23**. For the canonical `ultimatechat` execution
> sequence see **Chapter 17**.

---

# 29. Psychological Safeguards and the PIA Review Loop

This chapter formalizes how psychological and mental-health knowledge is integrated into Ms.
Jarvis to guide interaction patterns, monitor interaction risks, and adapt system behavior over
time. In the current deployment, this is realized through two confirmed running services —
`jarvis-psychology-services` (port **8019**) and `psychological_rag_domain` (port **9006**) —
a curated psychological corpus in `jarvis-chroma`, the BBB pipeline at port **8016** as the
primary live safety gate, and a manual PIA review process that produces recommendations rather
than automated rewrites.

---

## 29.1 Role of Psychological Guidance

In the current deployment, psychological guidance is not treated as an auxiliary feature but as
a core constraint on how the system interacts with people. Its primary functions are threefold.

**Interaction quality.** In the current deployment, `jarvis-psychology-services` (port **8019**)
provides principled reference points for respectful, non-coercive, and supportive exchanges. Its
`/psychological_assessment` endpoint returns `therapeutic_guidance`, `emotional_support`, and
`evidence_based_approaches` structured responses. `psychological_rag_domain` (port **9006**)
provides retrieval of curated materials including therapy, mindfulness, trauma, depression,
anxiety, and social-support content via `/search`.

**Risk awareness.** In the current deployment, `TruthValidator` (applied on every response via
`jarvis-main-brain`, port **8050**) encodes patterns known to be harmful — identity confusion,
anthropomorphic overclaiming, misleading statements about agency and embodiment — and returns
`correct_identity`, `correct_creator`, and `relationship_clear` booleans. The BBB
`EthicalFilter` and `ThreatDetection` sub-filters at port **8016** screen for content violating
ethical or community-safety constraints.

**Self-checking.** In the current deployment, `normalize_identity` applied to every
`ultimatechat` response rewrites outputs that deviate from allowed self-descriptions or blur
human–machine boundaries, before the response is returned to the caller.

---

## 29.2 Organization of the Guidance Corpus

In the current deployment, psychological guidance materials are curated in dedicated collections
within `jarvis-chroma` (**127.0.0.1:8002**, confirmed running) and served via
`psychological_rag_domain` (**127.0.0.1:9006**, confirmed running).

**Corpus content.** In the current deployment, `psychological_rag_domain` holds a curated corpus
on topics including therapy, mindfulness, trauma, depression, anxiety, and social support.
`jarvis-psychology-services` uses this corpus to identify patterns such as anxiety, depression,
stress, grief, and trauma, pulling evidence-based snippets via RAG to generate structured
responses. The corpus is logically distinct from general reference and technical knowledge,
making its normative and clinical role explicit.

**Tagging and retrieval.** The design intends that items will be tagged with theme (e.g.
"trauma-informed care," "addictive dynamics"), population (e.g. adolescents, caregivers, rural
communities), and risk type (e.g. self-harm risk, identity confusion, dependency) to support
targeted retrieval. In the current deployment, tagging is partially implemented; `/search` on
`psychological_rag_domain` supports query-based retrieval, and population- and risk-type-specific
differential retrieval tuning is identified as future work.

---

## 29.3 Use During Live Interactions

In the current deployment, psychological safeguards influence behavior at several points in the
processing pipeline, though routing to the psychological track is not yet fully automated.

**Prompting and constraints.** In the current deployment, when `jarvis-psychology-services` is
explicitly invoked — either directly or via the meaning-oriented path — its outputs augment the
context with psychological constraints. The design intends that requests marked or inferred as
psychologically sensitive will automatically pull relevant guidance into evaluation and generation
modules; in the current deployment, this routing is **partially heuristic** — topic classifiers
and surface-cue detectors are present but not fully documented, and routing is not wired into
every `ultimatechat` call (Chapter 23).

**Style and strategy adjustments.** In the current deployment, when `jarvis-psychology-services`
returns a `psychological_assessment`, it provides `emotional_support` and `wellbeing_recommendations`
fields that can be used to tune response tone, sequencing, and confidence level — particularly
for high-stakes areas involving stress, grief, or crisis. The design intends that detected cues
of distress or crisis will trigger psychologically tuned response templates; in the current
deployment, this triggering is partially heuristic.

**Content filters and safety gates.** In the current deployment, the primary live gate is the
BBB at port **8016**: `EthicalFilter`, `SpiritualFilter`, `SafetyMonitor`, and `ThreatDetection`
screen all inputs and outputs for problematic patterns. `TruthValidator` specifically checks for
anthropomorphic overclaiming and identity confusion on every response. These mechanisms are
active on every `/chat` call regardless of whether the explicit psychological track is invoked.

---

## 29.4 The PIA Review Loop

In the current deployment, the Psychology-Informed Alignment (PIA) review loop exists as a
structured **manual process** that samples logs and introspection outputs, producing written
recommendations — **not auto-rewrites of configuration, prompts, or filters**.

**Inputs and scope.** In the current deployment, PIA review operates by manually sampling recent
interaction logs, `ms_jarvis_memory` entries (Chroma collection, confirmed written after every
`/chat` call; Chapter 17 §17.6), `truthverdict` fields from `UltimateResponse`, BBB
`barrier_stats` counters (total_filtered, total_blocked, pass_rate), and outputs from
`jarvis-psychology-services` and `psychological_rag_domain` health and introspection endpoints.
Automated, scheduled sampling is identified as future work.

**Analysis.** In the current deployment, the PIA review examines recurring patterns in system
behavior — recurring `truthverdict` violations, BBB block-rate trends, identity-confusion
patterns in `TruthValidator` outputs, and underuse of psychological guidance in sensitive
interaction categories. Some classification of patterns is still heuristic; fully automated
pattern-detection is identified as future work.

**Outputs and recommendations.** In the current deployment, the PIA review loop produces
structured **written recommendations** such as "tighten identity phrasing constraints in
crisis-related dialogues," "introduce explicit boundary statements for maternal metaphors," or
"increase invocation of `jarvis-psychology-services` for emerging addictive-behavior discussions."
These are human-interpretable and require explicit operator action to implement — they do not
automatically rewrite BBB parameters, judge instructions, or global mode policies. Machine-
readable output format and automated propagation are identified as future work.

---

## 29.5 Integration with Barriers, Modes, and Judge Components

In the current deployment, PIA recommendations can be applied to several confirmed control
surfaces, but application requires explicit operator action.

**Barrier and filter adjustments.** In the current deployment, BBB `EthicalFilter` and
`ThreatDetection` at port **8016** expose rule sets that can be updated in response to PIA
findings. For example, if the review loop detects drift toward anthropomorphic language, the
corresponding patterns can be given higher penalty weights or additional few-shot exemplars.
In the current deployment, this update process is manual.

**Global mode settings.** The design intends that PIA outputs will modify mode selection
policies — for instance, enforcing more cautious orchestration modes for certain user cohorts or
topics if recent behavior indicates elevated psychological risk. In the current deployment, mode
settings are adjusted by operators following PIA review rather than by automated policy updates.

**Evaluator and judge behavior.** In the current deployment, judge services (7230–7233, confirmed
running) can receive updated instructions reflecting refined psychological guidance — for example,
stronger penalties for overconfident advice in clinical domains. In the current deployment, these
updates are applied manually following PIA recommendations. The design intends that future
configurations will give judges direct access to `psychological_rag_domain` outputs and PIA
summaries as explicit scoring dimensions.

---

## 29.6 Recording, Memory, and Accountability

In the current deployment, psychological safeguards are recorded through several confirmed
mechanisms.

**`ms_jarvis_memory` and interaction logs.** In the current deployment, every `/chat` response
produces a `bg_<ISO8601>` entry in `ms_jarvis_memory` (Chapter 17 §17.6, Chapter 20), with
`truthverdict` fields recording BBB judgments including ethics violations. These entries are the
primary raw material for PIA sampling. BBB `barrier_stats` counters provide aggregate counts of
filter interventions.

**PIA review records.** In the current deployment, each manual PIA review cycle produces a
written record of inputs sampled, patterns observed, and recommendations proposed. The design
intends these records will be written into a dedicated Chroma collection as timestamped
introspective artifacts tagged as psychological-alignment entries. In the current deployment,
these records are maintained as manually produced documents rather than automatically ingested
into Chroma.

**Human oversight and governance.** In the current deployment, PIA review outputs are explicitly
designed for inspection by human reviewers including domain experts, ethicists, and community
governance bodies. This material supports questions such as: "Has the system systematically
improved in handling crisis-adjacent queries?", "Where have psychological safeguards been relaxed
or tightened?", and "Do the recorded mitigations align with declared community norms?" The
design treats psychological risk as a first-class governance concern, on par with technical
reliability and knowledge integrity.

---

## 29.7 Summary

In the current deployment, psychological safeguards are realized through two confirmed running
services — `jarvis-psychology-services` (**127.0.0.1:8019**) and `psychological_rag_domain`
(**127.0.0.1:9006**) — a curated psychological corpus in `jarvis-chroma` (**127.0.0.1:8002**),
the BBB four-filter pipeline at **0.0.0.0:8016** as the primary live safety gate, and
`normalize_identity` plus `TruthValidator` applied to every `ultimatechat` response.

**Two important constraints** must be stated clearly: classifier and trigger logic routing
requests to the psychological track is **partially heuristic** in the current deployment, not
fully automated rule-based classification; and the PIA review loop **produces written
recommendations through a manual sampling process**, not auto-rewrites. Propagation of PIA
recommendations into BBB parameters, judge weights, or mode policies requires explicit operator
action.

The design intends that future work will automate the PIA sampling cycle, produce machine-readable
recommendation outputs for direct configuration integration, fully wire psychological routing into
the `ultimatechat` entrypoint, and persist PIA records as a first-class Chroma collection for
ongoing governance review. For the BBB pipeline that enforces safety constraints see **Chapter 16**.
For the identity constraints enforced alongside psychological safeguards see **Chapter 22**. For
the canonical `ultimatechat` execution sequence see **Chapter 17**.
