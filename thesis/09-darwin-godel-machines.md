# 9. Darwin Gödel Machines and Self‑Improving Agents

This chapter explains how Ms. Egeria Jarvis uses ideas from Gödel machines and the recent Darwin Gödel Machine (DGM) work to structure self‑improvement and meta‑reasoning. Historically, the Gödel machine is a theoretical self‑referential program that can rewrite any part of its own code once it has proved that the change will improve its expected utility according to a formal specification. The Darwin Gödel Machine extends this idea into a more practical framework, combining evolutionary search and large models to propose and empirically evaluate self‑modifications, maintaining an archive of improved agents over time.

Ms. Jarvis does not implement a fully formal Gödel machine or a complete Darwin Gödel Machine stack. Instead, this thesis uses DGM as an inspiration and structural guide: a way to organize multiple, specialized self‑improving agents that propose, test, and sometimes adopt changes to code, workflows, or governance procedures under human oversight. Concretely, dozens of DGM‑style connectors are deployed across the system as small, scoped optimizers attached to specific services and edges in the internal service graph, though only a subset are currently mature and well‑evaluated.

## 9.1 Historical Background and Rationale

The classical Gödel machine concept emphasizes three core ideas:

- **Self‑reference**  
  The system contains a description of its own code and environment and can reason about them. It can, in principle, evaluate proposed self‑modifications by reasoning about their future effects.

- **Proof‑based self‑modification**  
  It searches for proofs that specific code changes will increase its expected utility and only applies changes when such proofs are found. This yields strong guarantees but is extremely demanding in practice.

- **Global scope**  
  In theory, any part of the system can be modified if a beneficial proof exists; the machine is not restricted to a narrow module or feature.

The Darwin Gödel Machine relaxes some of these demands in favor of empirical search:

- **Empirical evaluation**  
  Instead of requiring strict formal proofs, DGM uses evolutionary search and empirical testing to evaluate candidate modifications. It treats performance on tasks, benchmarks, or simulations as the primary feedback signal.

- **Open‑ended evolution**  
  It maintains an archive or population of agents that are periodically varied, tested, and retained if they perform better. This enables long‑run improvement without a fixed end state.

- **Practical implementation**  
  DGM prototypes demonstrate self‑improving coding agents that modify and improve their own components using real programming environments, tests, and evaluation metrics.

Ms. Jarvis adopts this lineage because the project needs a systematic way to explore and evaluate improvements without assuming that all changes can be justified by formal proofs. The DGM framing provides a language for discussing self‑improvement, experimental variation, and archiving of better behaviors in a way that fits both the technical stack and the reflexive methodology of the thesis.

## 9.2 Design Principles for DGMs in Ms. Jarvis

Within Ms. Jarvis, Darwin Gödel Machine ideas are applied under several design principles that govern how self‑improving components operate:

- **Scoped self‑improvement**  
  DGM‑style modules are scoped to specific domains (for example, architecture, governance, neurobiology, retrieval, search, and integration) rather than given unrestricted power over the entire system. This reduces risk and makes it easier to reason about proposed changes.

- **Proposal, not automatic rewrite**  
  DGMs generate change proposals—code patches, configuration changes, workflow variants, governance rule adjustments—that are subject to tests, evaluation, and often human review before adoption. They are positioned as suggesters and optimizers, not autonomous editors of the entire codebase.

- **Archived variants**  
  Where feasible, DGMs maintain or contribute to archives of agent variants or configurations, creating a record of what was tried and what worked. This supports reproducibility and allows improvements to be rolled back or compared.

- **Alignment with constitutional constraints**  
  DGM proposals must respect constitutional, safety, and governance constraints. Proposals that violate core principles are rejected or flagged for higher‑level review, and DGM components are expected to call out rather than hide problematic changes.

This approach aims to capture the spirit of self‑improving agents described in the DGM work while staying within the safety, transparency, and legal boundaries of the Ms. Jarvis and MountainShares projects.

## 9.3 The “Fifth DGM” and Global Architecture

One prominent DGM instance, informally referred to as the “Fifth DGM,” is oriented toward the overall architecture of Ms. Jarvis.

- **Scope**  
  This DGM examines configurations and workflows across retrieval, semantic memory, GBIM structures, service routing, and logging. It focuses on system‑level questions such as which services should be chained together for a given task, how often health checks should run, or how logs and metrics should be structured.

- **Mechanisms**  
  The Fifth DGM uses logs, performance metrics, and test results as its evaluation environment, treating them as feedback signals for architecture decisions. It generates candidate changes—for example, configuration snippets, routing tables, or code fragments—runs tests or simulations against them, and scores their impact.

- **Constraints**  
  Changes with significant impact (affecting security, governance, or external APIs) require explicit human review and version control. Smaller operational tweaks, such as adjusting timeouts or toggling a fallback path, may be auto‑applied within defined safeguards and rolled back if subsequent evaluations show regressions.

This Fifth DGM is not a fully autonomous Gödel machine; it is a self‑improvement assistant focused on architecture and operations, guided by DGM‑inspired patterns rather than formal proofs. It illustrates how DGM ideas can be used to structure ongoing configuration and orchestration refinement without handing over unconditional control.

## 9.4 Fractal DGMs and Per‑Service Connectors

Beyond the Fifth DGM, Ms. Jarvis uses a “fractal” pattern composed of many smaller DGM‑style decision modules attached to individual services and edges.

- **Structure**  
  A collection of narrowly scoped DGM connectors are attached to specific services or clusters of services, where they monitor traffic and propose improvements to those local connections. Each connector can be viewed as a small agent with its own configuration, evaluation history, and archive of candidate variants for its local workflow.

- **Behavior**  
  Each connector runs a recurring cycle of observation, proposal, and evaluation on its attached edge: observing inputs and outputs, proposing small changes to prompts, routing rules, or filters, and testing those changes on suitable tasks. Over time, this yields an empirical record of how different micro‑strategies perform under real workloads.

- **Purpose**  
  The goal is to discover better micro‑strategies—for example, improved prompts between two services, more effective agent chains, more targeted retrieval filters, or better timeout and retry policies—that can then be adopted into the live system. These local improvements complement the broader architectural proposals from the Fifth DGM.

This fractal use of DGMs resembles the open‑ended, evolutionary search aspects of the Darwin Gödel Machine but is applied to prompts, workflows, and service connections rather than directly to low‑level model weights.

## 9.5 Domain‑Specific DGMs: MountainShares and Neurobiology

Several DGM‑style components are scoped to specific domains where governance, narrative, or specialized analysis require focused self‑improvement.

- **MountainShares DGM**  
  - *Focus*  
    Governance and economic workflows in MountainShares, including proposal flows, dispute handling, fee structures, and eligibility rules.  
  - *Role*  
    Proposes modifications to governance processes, dashboards, or analytical tools, subject to constitutional constraints and legal requirements. Evaluates changes via simulations, backtesting, or scenario analysis, helping to inform community governance decisions rather than dictating them.

- **“I‑container” / neurobiology DGM**  
  - *Focus*  
    Self‑modeling, narrative, and neurobiology‑inspired aspects of Ms. Jarvis, including how internal states are described and monitored.  
  - *Role*  
    Proposes changes to self‑descriptions, internal monitoring routines, and interpretive layers that explain how Ms. Jarvis represents its own state and processes. Helps align the system’s introspective narratives with its actual architecture and data, supporting the reflexive methodology of the thesis.

These domain‑specific DGMs keep self‑improvement close to the problems they are meant to address, making it easier to reason about scope, risks, and evaluation, and allowing subject‑matter experts to participate in reviewing proposed changes.

## 9.6 DGMs, Judging, and Multi‑Agent Evaluation

DGM‑style components in Ms. Jarvis are closely integrated with judge agents and multi‑step evaluation procedures. They are not stand‑alone optimizers; they work within a larger multi‑agent system.

- **Composition with other agents**  
  DGMs interact with ensembles of agents that specialize in coding, retrieval, governance analysis, and explanation, using them as tools to generate and test candidate changes. A DGM may, for example, call a coding agent to implement a proposed patch, a retrieval agent to assemble test data, and an analyst agent to summarize the results.

- **Interaction with LLMs**  
  DGMs generate candidate prompts, tool call sequences, or code modifications, and large models execute or simulate these candidates to produce outputs and metrics. Judge‑style agents and “LLM‑as‑a‑judge” components score these outputs using criteria such as correctness, safety, alignment with governance norms, and relevance to spatial justice.

- **Promotion and archival**  
  High‑scoring candidates can be proposed for adoption into the main system configuration, with records describing what changed, why it changed, and how those changes performed over time. Low‑performing variants remain in the archive as negative examples, informing future search and avoiding repeated exploration of the same unproductive regions.

This pattern takes DGM’s emphasis on populations of agents, empirical testing, and archival of improved variants and adapts it to the context of multi‑agent LLM systems.

## 9.7 Relationship to WOAH and Orchestration

Darwin Gödel Machine‑inspired components operate alongside, but below, higher‑level orchestration and oversight structures such as WOAH and the whale/organization hierarchy.

- **DGMs as tools**  
  DGMs focus on self‑improvement within defined domains (for example, architecture, workflows, governance, self‑modeling, retrieval, and integration). They generate and evaluate proposals, often using LLMs, retrieval, and simulation environments as part of their evaluation context.

- **Orchestration and oversight layers**  
  Higher‑level orchestration layers decide when and how to invoke DGMs, including which services or domains should be optimized at a given time. They integrate DGM outputs with other agents, judges, and analysis tools, resolving conflicts and prioritizing changes that best fit current goals. They also enforce overarching constitutional, safety, and governance constraints on what can actually be adopted into the running system.

In this view, DGMs are subordinate optimizers that feed into a broader governance and orchestration framework rather than being the ultimate arbiters of system behavior.

## 9.8 Limits and Honesty About Implementation

It is important to be explicit about current limits and the gap between theory and implementation:

- **No fully formal Gödel machine**  
  Ms. Jarvis does not implement a rigorous, proof‑based Gödel machine that can formally guarantee utility improvements before every change. The computational and specification demands of such a system remain out of reach.

- **DGM as inspiration, not exact copy**  
  The architecture is inspired by the Darwin Gödel Machine’s ideas of open‑ended self‑improvement, agent populations, and empirical evaluation, but it does not claim full fidelity to any specific published implementation. Many practical choices—such as how proposals are generated, how tests are run, and how archives are structured—are adapted to the constraints of this project.

- **Limited scope and evolving practice**  
  While many DGM‑style connectors and several domain‑specific DGMs are active, only a subset have been deeply evaluated and documented; others remain experimental and are being refined over time. Some connectors may be disabled or run in “observation only” mode until their behavior is better understood.

- **Human oversight and boundaries**  
  Significant changes remain subject to human review, legal and ethical constraints, and version control. The system is designed to propose and test improvements, not to autonomously refactor itself without oversight. This limitation is by design and is central to the governance commitments of the project.

Future work may formalize these DGMs further, including more precise definitions of their search spaces, evaluation functions, and promotion criteria, as well as empirical studies of how much improvement they actually deliver over time. Technical appendices and subsequent publications will document specific DGMs, their configurations, and observed impacts on system behavior.
