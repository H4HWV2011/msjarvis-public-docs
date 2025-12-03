# 33. Language Model Ensemble and Judge Systems in Live Operation

This chapter describes how multiple language models and evaluation components are used together during ongoing activity. The focus is on how different models are assigned roles, how their outputs are compared and scored, and how these judgments feed back into barrier, container, and control layers.

## 32.1 Roles of the Core Models

Several models are used with distinct primary roles:

- Task execution:
  - One or more models focus on generating answers, plans, or narratives, given structured context from retrieval, containers, and coordination.
- Structural transformation:
  - Some models are used mainly for tasks such as summarization, classification, or schema alignment, translating between formats.
- Evaluation and critique:
  - Others act as evaluators or assistants to the judge components, helping to check clarity, consistency, or adherence to constraints.

Separating these roles helps keep responsibilities clearer and makes it easier to study behavior.

## 32.2 Judge Components and Evaluation Criteria

Judge components assess candidate outputs along multiple dimensions:

- Criteria:
  - Typical dimensions include helpfulness, factual support, safety, alignment with policies, and appropriateness of style for the intended audience.
- Inputs:
  - Judges receive the candidate output, relevant context from memory and containers, and explicit instructions about what to check.
- Outputs:
  - They produce scores, labels, and short explanations indicating where an output succeeds or falls short.

These evaluations are used both for real-time decisions and for later analysis.

## 32.3 Ensemble Patterns

The system uses ensemble patterns to combine strengths of different models and judges:

- Multiple candidates:
  - For some tasks, several models or prompt variants may be asked to produce candidate outputs, which are then compared.
- Comparative evaluation:
  - Judge components can rank or choose between candidates, rather than scoring each in isolation.
- Aggregation:
  - Simple aggregation rules, such as preferring outputs that satisfy safety and support thresholds while performing well on task-specific metrics, guide the final selection.

This approach reduces reliance on any single model or judgment.

## 32.4 Use in Live Cycles

Ensemble and judge mechanisms are integrated into live processes described in earlier chapters:

- Web research:
  - When incorporating new external material, evaluators check for basic support, internal consistency, and compliance with source policies before write-back.
- Heartbeat and narratives:
  - Scheduled narratives, especially those prepared for external platforms, pass through judge checks focused on safety, tone, and clarity.
- Psychological review:
  - In the PIA loop, evaluators apply criteria derived from psychological guidance, flagging responses or patterns that may require attention.

These uses tie evaluation closely to the rhythms of ongoing activity.

## 32.5 Interaction with Barrier and Truth-Related Signals

Judge outputs interact with the barrier and support-related signals:

- Entry decisions:
  - For certain classes of content, especially from external sources, evaluations contribute to decisions about whether material is admitted beyond quarantine.
- Support levels:
  - Evaluator scores can influence how strongly new statements are treated, affecting their labels as well-supported, weakly supported, or conflicting.
- Policy feedback:
  - Aggregate evaluations over time can suggest adjustments to barrier policies or to the thresholds used for promotion within containers.

This makes evaluation part of the overall protection and filtering strategy.

## 32.6 Influence on Containers, Memory, and Optimizers

Evaluation signals are used by other architectural layers:

- Container paths:
  - Scores and labels from judges are stored alongside records and can influence which items are kept, how they are grouped, and whether they are considered for deep retention.
- Long-term memory:
  - Stable evaluation patterns, such as recurring weaknesses or strengths in certain tasks, can be written into long-term entries describing model behavior.
- Optimization components:
  - Per-service optimizers use evaluation feedback as part of their metrics when testing proposed changes to prompts, workflows, or configurations.

This integration ensures that evaluation is not a one-off filter but part of a continuous improvement loop.

## 32.7 Summary

The language model ensemble and judge systems provide a layered evaluation capability that supports live operation. By assigning different roles to models, combining their outputs, and feeding evaluation results into barrier, container, memory, and optimization layers, the system can better manage quality, safety, and alignment across a wide range of tasks.
