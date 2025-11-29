# Darwin Gödel Machines and Self-Improving Agents (Draft)

This chapter explains how Ms. Egeria Jarvis uses ideas from Gödel machines and the recent Darwin Gödel Machine (DGM) work to structure self-improvement and meta-reasoning. Historically, the Gödel machine is a theoretical self-referential program that can rewrite any part of its own code once it has proved that the change will improve its expected utility according to a formal specification. [web:464][web:480] In 2025, the Darwin Gödel Machine extended this idea into a more practical framework, combining evolutionary search and large models to propose and empirically evaluate self-modifications, maintaining an archive of improved agents over time. [web:456][web:457][web:460]

Ms. Jarvis does not implement a fully formal Gödel machine or the complete Darwin Gödel Machine architecture. Instead, this thesis uses DGM as an inspiration and structural guide: a way to organize multiple, specialized self-improving agents that propose, test, and sometimes adopt changes to code, workflows, or governance procedures under human oversight.

## Historical Background and Rationale

The classical Gödel machine concept emphasizes:

- Self-reference: The system contains a complete description of its own code and environment and can reason about them. [web:464][web:480]
- Proof-based self-modification: It searches for proofs that specific code changes will increase its utility, and only applies changes when such proofs are found.
- Global scope: In principle, any part of the system can be modified if a beneficial proof exists.

The Darwin Gödel Machine relaxes some of these demands:

- Empirical evaluation: Instead of requiring strict formal proofs, DGM uses evolutionary search and empirical testing to evaluate candidate modifications. [web:456][web:457][web:482]
- Open-ended evolution: It maintains a population or archive of agents that are periodically varied, tested, and retained if they perform better, supporting long-run improvement. [web:456][web:460]
- Practical implementation: DGM prototypes demonstrate self-improving coding agents that modify and improve their own components using real programming environments and benchmarks. [web:457][web:478][web:483]

Ms. Jarvis adopts this lineage because the project needs a systematic way to explore and evaluate improvements without pretending that all changes can be justified by formal proofs. The DGM framing provides a language for discussing self-improvement, experimental variation, and archiving of better behaviors in a way that fits both the technical stack and the reflexive methodology of the thesis. [web:456][web:477]

## Design Principles for DGMs in Ms. Jarvis

Within this system, Darwin Gödel Machine ideas are used under several design principles:

- Scoped self-improvement: DGMs are scoped to specific domains (architecture, governance, neurobiology, etc.) rather than given unrestricted power over the entire system.
- Proposal, not automatic rewrite: DGMs generate change proposals (code patches, configuration changes, workflow variants, governance rule adjustments) that are subject to tests, evaluation, and often human review before adoption.
- Archived variants: Where feasible, DGMs maintain or contribute to archives of agent variants or configurations, creating a record of what was tried and what worked.
- Alignment with constitutional constraints: DGM proposals must respect constitutional, safety, and governance constraints; proposals that violate core principles are rejected or flagged.

This approach aims to capture the spirit of self-improving agents described in the DGM work while staying within the safety, transparency, and legal boundaries of the Ms. Jarvis and MountainShares projects. [web:456][web:460]

## The “5th DGM” and Global Architecture

One DGM instance, informally referred to as the “5th DGM,” is oriented toward the overall architecture of Ms. Jarvis:

- Scope:
  - Examines configurations and workflows across RAG, ChromaDB, GBIM, service routing, and logging.
  - Proposes changes such as new routing rules, modified service chains, improved health checks, or updated documentation and metrics.
- Mechanisms:
  - Uses logs, performance metrics, and test results as its evaluation environment.
  - Generates candidate changes (e.g., YAML, JSON, or code snippets), runs tests or simulations, and scores their impact.
- Constraints:
  - Changes with significant impact (affecting security, governance, or external APIs) require explicit human review and version control.
  - Smaller operational tweaks may be auto-applied within defined safeguards.

This 5th DGM is not a fully autonomous Gödel machine; it is a self-improvement assistant focused on architecture and operations, guided by DGM-inspired patterns rather than formal proofs. [web:456][web:482]

## Fractal DGM and Many Small DMs

A second pattern is a “fractal” DGM composed of many smaller decision modules (DMs):

- Structure:
  - A set of multiple DM instances (for example, dozens) that explore variations on prompts, tools, and routing strategies for specific tasks.
  - Each DM can be viewed as a small agent with its own configuration and evaluation history.
- Behavior:
  - Candidate DMs are generated, run on shared test suites, and scored.
  - Better-performing DMs are kept or reused; underperformers are discarded or demoted.
- Purpose:
  - To discover better micro-strategies (for example, better prompts, more effective agent chains, or improved retrieval filters) that can then be adopted by Ms. Jarvis.

This fractal DGM resembles the open-ended, evolutionary search aspects of Darwin Gödel Machine, but is applied to agent and workflow configurations rather than low-level model weights. [web:456][web:460]

## Domain-Specific DGMs: MountainShares and Neurobiology

Several DGMs are scoped to specific domains:

- MountainShares DGM:
  - Focus: Governance and economic workflows in MountainShares (proposal flows, dispute handling, fee structures, eligibility rules).
  - Role:
    - Proposes modifications to governance processes, dashboards, or analytical tools, subject to constitutional constraints and legal requirements.
    - Evaluates changes via simulations, backtesting, or scenario analysis, helping to inform community governance decisions rather than dictating them.
- “I-container” / neurobiology DGM:
  - Focus: Self-modeling, narrative, and neurobiology-inspired aspects of Ms. Jarvis.
  - Role:
    - Proposes changes to self-descriptions, internal monitoring, and interpretive layers that explain how Ms. Jarvis sees her own state and processes.
    - Helps align the system’s introspective narratives with its actual architecture and data, supporting the reflexive methodology of the thesis.

These domain-specific DGMs keep self-improvement close to the problems they are meant to address, making it easier to reason about scope, risks, and evaluation.

## Docker DGM Container and LLM-Judge Integration

In the containerized deployment, there is also a DGM-focused Docker service that runs multiple DGM instances connected to the LLM ensemble:

- Composition:
  - Several DGMs operate together inside a single container, each with a distinct role (for example, code improver, workflow tuner, evaluation agent, or governance scenario explorer).
- Interaction with LLMs:
  - DGMs generate candidate prompts, tool call sequences, or code modifications.
  - LLMs execute or simulate these candidates, producing outputs and metrics.
  - Judge-style DGMs and LLM-as-a-judge components score these outputs using criteria such as correctness, safety, alignment with governance norms, or spatial justice relevance. [web:465][web:470]
- Promotion and archival:
  - High-scoring candidates can be proposed for adoption into the main system configuration, with logs and archives documenting what changed and why.

This pattern is directly inspired by DGM’s emphasis on populations of agents, empirical testing, and archival of improved variants, adapted to the context of multi-agent LLM systems. [web:456][web:462][web:468]

## Relationship to WOAH and Orchestration

Darwin Gödel Machines operate alongside, but below, higher-level orchestration and oversight structures such as WOAH and the whale/organization hierarchy:

- DGMs:
  - Focus on self-improvement within defined domains (architecture, workflows, governance, self-modeling).
  - Generate and evaluate proposals, often using LLMs and RAG as part of their environment.
- WOAH and orchestration layers:
  - Decide when and how to invoke DGMs.
  - Integrate DGM outputs with other agents, judges, and analysis tools.
  - Enforce overarching constitutional, safety, and governance constraints on what can actually be adopted.

In subsequent chapters, WOAH and the broader orchestration hierarchy will be described as the coordinating layer that uses DGMs as tools rather than deferring control to them.

## Limits and Honesty About Implementation

It is important to be explicit about current limits:

- No fully formal Gödel machine:
  - Ms. Jarvis does not implement a rigorous, proof-based Gödel machine that can formally guarantee utility improvements before every change. [web:464][web:480]
- DGM as inspiration, not exact copy:
  - The architecture is inspired by the Darwin Gödel Machine’s ideas of open-ended self-improvement, agent populations, and empirical evaluation, but does not claim full fidelity to the published DGM implementations. [web:456][web:457][web:482]
- Human oversight and boundaries:
  - Significant changes remain subject to human review, legal and ethical constraints, and version control.
  - The system is designed to propose and test improvements, not to autonomously refactor itself without oversight.

Future work may formalize these DGMs further, including more precise definitions of their search spaces, evaluation functions, and promotion criteria, as well as empirical studies of how much improvement they actually deliver over time.

> Status: This chapter is a draft conceptual and contextual overview of Darwin Gödel Machine-inspired components in Ms. Jarvis. Detailed algorithms, configuration schemas, and evaluation results for individual DGMs will be developed in technical appendices and future publications.
