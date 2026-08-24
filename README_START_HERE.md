# Start Here

This is the operator entry point for adopting the AI Software Engineering Governance Framework in a project.

For a five-minute overview, read [README.md](README.md). For execution details, use [docs/QUICK_START.md](docs/QUICK_START.md).

## Choose an adoption profile

### Full Template

Use the complete repository when the project is long-running, safety- or quality-sensitive, multidisciplinary, brownfield, or requires formal traceability and release evidence.

1. Copy or extract the complete template.
2. Replace project placeholders.
3. Initialize or verify Git.
4. Configure `00_project/ai_context/CURRENT_STATE.md`.
5. Start the agent with `PROJECT_START_PROMPT.md`.

### Lite

Use the Lite file set for small or low-risk projects that need governance without the full lifecycle directory tree. The exact file list and upgrade triggers are in [docs/FULL_VS_LITE.md](docs/FULL_VS_LITE.md).

Lite keeps the same non-negotiable principles:

- Current Truth;
- One Fact, One Owner;
- Role != Model != Harness;
- independent C04 review;
- explicit human authority boundaries;
- Baseline Relearn after context/model/harness replacement.

## Mandatory first agent read

Ask the active agent to read, in order:

1. `AI_START_HERE.md`;
2. `AI_ENGINEERING_RULES_V2.md`;
3. `AI_CONVERSATION_ORCHESTRATION_RULES.md`;
4. `00_project/ai_context/CURRENT_STATE.md`;
5. the active role brief under `00_project/ai_context/ROLE_BRIEFS/`.

For a new project, begin with C00/C01. For an existing project, follow `AI_LEGACY_PROJECT_STANDARDIZATION_GUIDE.md` and inventory the project before moving or rewriting files.

Important decisions must be written to their formal fact owner. Chat history is not a durable project truth source.
