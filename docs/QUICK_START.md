# Quick Start

## Prerequisites

- Git;
- a coding agent or harness that can read and edit repository files;
- Python 3 only when running the provided traceability validator.

No specific model vendor is required.

## Full Template setup

1. Copy or extract the complete release archive into the target project root.
2. If the target is an existing project, do not overwrite conflicting files. Follow `AI_LEGACY_PROJECT_STANDARDIZATION_GUIDE.md` first.
3. Replace `{{PROJECT_NAME}}`, dates, gates, and other placeholders relevant to the project.
4. Configure the current stage, authorization, `AUTONOMY_MODE`, model/harness slots, `AUTHORIZED_UNTIL`, and `PREAUTHORIZED_GATES` in `00_project/ai_context/CURRENT_STATE.md`.
5. Initialize Git if needed and create a stable anchor before implementation.
6. Give the active agent `PROJECT_START_PROMPT.md`.
7. For a new project, start with C00/C01 and establish product requirements before architecture or implementation.

## Lite setup

Copy the Lite file set documented in `docs/FULL_VS_LITE.md`. Keep the original paths for all selected files so cross-references and fact ownership remain valid.

At minimum:

1. configure `CURRENT_STATE.md`;
2. establish current decisions and baseline references;
3. create an active task;
4. select the active C00-C06 role;
5. require a fresh independent C04 session for review;
6. use Baseline Relearn when switching model, harness, or long-running context.

## Five-minute verification

- The agent can state the current role, stage, authorization, and next task.
- Every dynamic fact has one owner file.
- The current model/harness routing exists only in `CURRENT_STATE.md`.
- The review target is an exact Git target.
- C04 cannot modify the reviewed object or close its own Finding.
- Human approval boundaries are explicit.

If any answer is unclear, remain in C00 and resolve governance state before implementation.
