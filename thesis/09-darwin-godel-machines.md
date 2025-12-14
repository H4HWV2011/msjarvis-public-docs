# Darwin Gödel Machines and Self-Improving Agents (Draft)

This chapter explains how Ms. Egeria Jarvis uses ideas from Gödel machines and the recent Darwin Gödel Machine (DGM) work to structure self-improvement and meta-reasoning. Historically, the Gödel machine is a theoretical self-referential program that can rewrite any part of its own code once it has proved that the change will improve its expected utility according to a formal specification. In 2025, the Darwin Gödel Machine extended this idea into a more practical framework, combining evolutionary search and large models to propose and empirically evaluate self-modifications, maintaining an archive of improved agents over time.

Ms. Jarvis does not implement a fully formal Gödel machine or the complete Darwin Gödel Machine architecture. Instead, this thesis uses DGM as an inspiration and structural guide: a way to organize multiple, specialized self-improving agents that propose, test, and sometimes adopt changes to code, workflows, or governance procedures under human oversight. Concretely, 69 DGM-style connectors are deployed across the system as small, scoped optimizers attached to specific services and edges in the internal service graph.

## Historical Background and Rationale

The classical Gödel machine concept emphasizes:

- Self-reference:
  - The system contains a description of its own code and environment and can reason about them.
- Proof-based self-modification:
  - It searches for proofs that specific code changes will increase its expected utility and only applies changes when such proofs are found.
- Global scope:
  - In principle, any part of the system can be modified if a beneficial proof exists.

The Darwin Gödel Machine relaxes some of these demands in favor of empirical search:

- Empirical evaluation:
  - Instead of requiring strict formal proofs, DGM uses evolutionary search and empirical testing to evaluate candidate modifications.
- Open-ended evolution:
  - It maintains an archive or population of agents that are periodically varied, tested, and retained if they perform better, enabling long-run improvement.
- Practical implementation:
  - DGM prototypes demonstrate self-improving coding agents that modify and improve their own components using real programming environments and benchmarks.

Ms. Jarvis adopts this lineage because the project needs a systematic way to explore and evaluate improvements without assuming that all changes can be justified by formal proofs. The DGM framing provides a language for discussing self-improvement, experimental variation, and archiving of better behaviors in a way that fits both the technical stack and the reflexive methodology of the thesis.

## Design Principles for DGMs in Ms. Jarvis

Within this system, Darwin Gödel Machine ideas are used under several design principles that govern how the 69 optimizers operate:

- Scoped self-improvement:
  - DGMs are scoped to specific domains (for example, architecture, governance, neurobiology, retrieval, search, and integration) rather than given unrestricted power over the entire system.
- Proposal, not automatic rewrite:
  - DGMs generate change proposals (code patches, configuration changes, workflow variants, governance rule adjustments) that are subject to tests, evaluation, and often human review before adoption.
- Archived variants:
  - Where feasible, DGMs maintain or contribute to archives of agent variants or configurations, creating a record of what was tried and what worked.
- Alignment with constitutional constraints:
  - DGM proposals must respect constitutional, safety, and governance constraints; proposals that violate core principles are rejected or flagged for higher-level review.

This approach aims to capture the spirit of self-improving agents described in the DGM work while staying within the safety, transparency, and legal boundaries of the Ms. Jarvis and MountainShares projects.

## The “5th DGM” and Global Architecture

One prominent DGM instance, informally referred to as the “5th DGM,” is oriented toward the overall architecture of Ms. Jarvis:

- Scope:
  - Examines configurations and workflows across retrieval, semantic memory, GBIM structures, service routing, and logging.
  - Proposes changes such as new routing rules, modified service chains, updated evaluation hooks, improved health checks, or revised documentation and metrics.
- Mechanisms:
  - Uses logs, performance metrics, and test results as its evaluation environment, treating them as feedback signals for architecture decisions.
  - Generates candidate changes (for example, configuration snippets, routing tables, or code fragments), runs tests or simulations, and scores their impact.
- Constraints:
  - Changes with significant impact (affecting security, governance, or external APIs) require explicit human review and version control.
  - Smaller operational tweaks may be auto-applied within defined safeguards and rolled back if subsequent evaluations show regressions.

This 5th DGM is not a fully autonomous Gödel machine; it is a self-improvement assistant focused on architecture and operations, guided by DGM-inspired patterns rather than formal proofs.

## Fractal DGMs and Per-Service Connectors

Beyond the 5th DGM, Ms. Jarvis uses a “fractal” pattern composed of many smaller DGM-style decision modules attached to individual services and edges.

- Structure:
  - A collection of 69 DGM connectors, each attached to a specific service or narrow cluster of services, where it monitors traffic and proposes improvements to that connection.
  - Each connector can be viewed as a small agent with its own configuration, evaluation history, and archive of candidate variants for its local workflow.
- Behavior:
  - Each connector runs a recurring cycle of observation, proposal, and evaluation on its attached edge: observing inputs and outputs, proposing small changes to prompts, routing, or filters, and testing those changes on suitable tasks.
  - Better-performing configurations are retained or promoted, while underperforming candidates are discarded or demoted.
- Purpose:
  - To discover better micro-strategies (for example, improved prompts, more effective agent chains, more targeted retrieval filters, or better timeout and retry policies) that can then be adopted into the live system.

This fractal use of DGMs resembles the open-ended, evolutionary search aspects of the Darwin Gödel Machine but is applied to prompts, workflows, and service connections rather than directly to low-level model weights.

## Domain-Specific DGMs: MountainShares and Neurobiology

Several DGMs are scoped to specific domains where governance, narrative, or specialized analysis require focused self-improvement:

- MountainShares DGM:
  - Focus:
    - Governance and economic workflows in MountainShares, including proposal flows, dispute handling, fee structures, and eligibility rules.
  - Role:
    - Proposes modifications to governance processes, dashboards, or analytical tools, subject to constitutional constraints and legal requirements.
    - Evaluates changes via simulations, backtesting, or scenario analysis, helping to inform community governance decisions rather than dictating them.
- “I-container” / neurobiology DGM:
  - Focus:
    - Self-modeling, narrative, and neurobiology-inspired aspects of Ms. Jarvis, including how internal states are described and monitored.
  - Role:
    - Proposes changes to self-descriptions, internal monitoring routines, and interpretive layers that explain how Ms. Jarvis represents its own state and processes.
    - Helps align the system’s introspective narratives with its actual architecture and data, supporting the reflexive methodology of the thesis.

These domain-specific DGMs keep self-improvement close to the problems they are meant to address, making it easier to reason about scope, risks, and evaluation.

## DGMs, Judging, and Multi-Agent Evaluation

DGM-style components in Ms. Jarvis are closely integrated with judge agents and multi-step evaluation procedures:

- Composition:
  - DGMs interact with ensembles of agents that specialize in coding, retrieval, governance analysis, and explanation, using them as tools to generate and test candidate changes.
- Interaction with LLMs:
  - DGMs generate candidate prompts, tool call sequences, or code modifications, and large models execute or simulate these candidates to produce outputs and metrics.
  - Judge-style agents and LLM-as-a-judge components score these outputs using criteria such as correctness, safety, alignment with governance norms, and relevance to spatial justice.
- Promotion and archival:
  - High-scoring candidates can be proposed for adoption into the main system configuration, with records describing what changed, why it changed, and how those changes performed over time.

This pattern takes DGM’s emphasis on populations of agents, empirical testing, and archival of improved variants and adapts it to the context of multi-agent LLM systems.

## Relationship to WOAH and Orchestration

Darwin Gödel Machines operate alongside, but below, higher-level orchestration and oversight structures such as WOAH and the whale/organization hierarchy:

- DGMs:
  - Focus on self-improvement within defined domains (for example, architecture, workflows, governance, self-modeling, retrieval, and integration).
  - Generate and evaluate proposals, often using LLMs, retrieval, and simulation environments as part of their evaluation context.
- WOAH and orchestration layers:
  - Decide when and how to invoke DGMs, including which services or domains should be optimized at a given time.
  - Integrate DGM outputs with other agents, judges, and analysis tools, resolving conflicts and prioritizing changes that best fit current goals.
  - Enforce overarching constitutional, safety, and governance constraints on what can actually be adopted into the running system.

Subsequent chapters describe WOAH and the broader orchestration hierarchy as the coordinating layer that uses DGMs as tools rather than deferring control to them.

## Limits and Honesty About Implementation

It is important to be explicit about current limits and the gap between theory and implementation:

- No fully formal Gödel machine:
  - Ms. Jarvis does not implement a rigorous, proof-based Gödel machine that can formally guarantee utility improvements before every change.
- DGM as inspiration, not exact copy:
  - The architecture is inspired by the Darwin Gödel Machine’s ideas of open-ended self-improvement, agent populations, and empirical evaluation, but does not claim full fidelity to any specific published implementation.
- Limited scope and evolving practice:
  - While 69 DGM-style connectors and several domain-specific DGMs are active, only a subset have been deeply evaluated and documented; others remain experimental and are being refined over time.
- Human oversight and boundaries:
  - Significant changes remain subject to human review, legal and ethical constraints, and version control.
  - The system is designed to propose and test improvements, not to autonomously refactor itself without oversight.

Future work may formalize these DGMs further, including more precise definitions of their search spaces, evaluation functions, and promotion criteria, as well as empirical studies of how much improvement they actually deliver over time.

> Status: This chapter is a draft conceptual and contextual overview of Darwin Gödel Machine-inspired components in Ms. Jarvis. Detailed algorithms, configuration schemas, and evaluation results for individual DGMs will be developed in technical appendices and future publications.
