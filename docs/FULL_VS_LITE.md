# Full Template vs Lite

The framework supports two adoption profiles. They share the same governance principles; they differ only in how much lifecycle structure is adopted initially.

## Comparison

| Area | Full Template | Lite |
|---|---|---|
| Recommended project type | Long-running, high-risk, regulated, multidisciplinary, brownfield | Small, low-risk, pilot, or evaluation |
| C00-C06 roles | Complete | Complete role boundaries, selectively activated |
| Product/system requirements | Full document set | Existing project documents may be referenced |
| Architecture and ADRs | Full structure | Add when architectural decisions become material |
| Traceability | Included and mechanically validated | Optional until required by risk or acceptance needs |
| Test governance | Full test design and evidence structure | Core testing rules retained; folders added as needed |
| Brownfield migration | Complete migration workflow | Upgrade to Full before broad restructuring |
| Release/operations | Included | Add before governed release or field operation |

## Lite file set

Keep these files at their original paths:

```text
AGENTS.md
AI_START_HERE.md
AI_ENGINEERING_RULES_V2.md
AI_CONVERSATION_ORCHESTRATION_RULES.md
PROJECT_START_PROMPT.md
INDEPENDENT_REVIEW_PROMPT.md
00_project/ai_context/CURRENT_STATE.md
00_project/ai_context/BASELINE_INDEX.md
00_project/ai_context/DECISION_INDEX.md
00_project/ai_context/ACTIVE_TASKS.md
00_project/ai_context/OPEN_QUESTIONS.md
00_project/ai_context/CONVERSATION_MAP.md
00_project/ai_context/ROLE_BRIEFS/*
00_project/governance/AI_CONTEXT_RESET_AND_BASELINE_RELEARN_RULES.md
00_project/governance/AI_TESTING_GOVERNANCE_RULES.md
```

Add `09_quality/traceability/validate_traceability.py` when formal requirement traceability is used.

## Non-negotiable in Lite

Lite may reduce artifacts, but it must not weaken:

- Current Truth and fact ownership;
- accepted requirement and decision authority;
- independent review context;
- human approval boundaries;
- test scope governance;
- context reset and Baseline Relearn;
- Git-based review targets and history.

## Upgrade to Full when

- the project becomes long-running or multidisciplinary;
- safety, data integrity, compliance, or field reliability becomes material;
- product and system requirements need formal traceability;
- multiple teams or suppliers need interface control;
- a brownfield restructuring is planned;
- release, deployment, or operational evidence must be governed.

Lite is not a fork of the governance rules. Stable rules remain in the same root governance documents, preventing Full and Lite from becoming competing Current Truth sources.
