# AI Software Engineering Governance Framework v0.2.0

# AI 软件工程治理框架 v0.2.0

> Stable release notes for `v0.2.0`. The release tag identifies the exact published revision.

## What this release changes

`v0.2.0` is a governance simplification release. It keeps the critical controls of `v0.1.9`, but changes the default operating model from broad preloading and preventive paperwork to demand-driven learning, proportional controls, and issue recording.

## Demand-driven governance

- `AI_START_HERE.md` remains the minimal bootstrap; all other knowledge is loaded only when the current task needs it.
- Routers evaluate exclusions and mutually exclusive conditions before inclusions, select the first sufficient route, and stop reading once the action is safely decidable.
- Valid knowledge already present in the current Session may be reused until its facts or authority change.
- Baseline Relearn rebuilds only the affected governance Delta, current task, direct dependencies, and facts needed to resolve an actual conflict.
- Human Project Owners may correct over-reading, over-validation, and unnecessary optional process during execution without waiting for a framework release.

## Proportional controls and review

- Dynamic Role Profiles, Knowledge Manifests, Interaction / Authorization Contracts, Output Contracts, and Worktree controls are instantiated only when their trigger applies or the Human Project Owner adopts them.
- Formal C04 reviews the frozen purpose, scope, core acceptance concerns, exact target, and directly affected evidence. It does not attempt to prove that no issue exists anywhere in the project.
- In-scope acceptance Findings block `PASS`. Other credible issues actually discovered are registered as Feedback and routed to the correct Owner without automatically blocking the current task.
- Human Owners retain the final decision on whether an item is a product problem and whether it should be fixed, deferred, accepted as risk, or rejected.
- Regression Guards are reserved for repeatable, high-impact, durable, machine-checkable problems whose prevention cost is justified.
- Code entering the formal product Baseline must retain risk-proportionate, recoverable Design Intent. Ordinary implementation code may provide As-Is evidence, but it cannot be the sole implicit normative source for state machines, public interface contracts, error semantics, safety constraints, recovery rules, or critical invariants.
- Spikes, emergency fixes, generated code, and Brownfield recovery remain supported through bounded exceptions; formal acceptance restores the required intent without forcing line-by-line design documentation.

## Post-RC clarifications

- Faithful archival of an existing formal review result does not recursively trigger another C04. Source fidelity and reference checks remain required; PASS remains bound to its original exact target.
- Review packages declare exclusions before review. Closure rereviews cover the original closure criteria and directly introduced substantive regressions, not wording preferences.
- Current dynamic facts have one authoritative location, including within the same document. Prose references status instead of maintaining another copy.
- Completion and release use impact-based, risk-proportionate validation and applicable evidence reuse; they do not default to full retesting.

## Context-bounded work and optional multi-agent execution

- Existing leaf/integration work packages can be sized as self-contained work slices, aiming to finish before first context compaction without turning that aim into an acceptance gate or a token ledger.
- `MULTI_AGENT_MODE` defaults to `OFF`. Owners may explicitly select `AUTO_DELEGATE` for independent, bounded tasks; the Root coordinates dependencies, integration and necessary validation.
- Existing permission inheritance, single-writer/worktree isolation, external-session configuration and formal C04 independence remain applicable. A Subagent is not automatically a formal reviewer.
- Projects upgrading from `v0.2.0-rc.1` use the same cumulative-delta upgrade protocol. The new option is not automatically enabled.

## Faster upgrades

The version-agnostic upgrade protocol now uses:

```text
current exact version
+ target exact version
+ cumulative Git delta
+ target upgrade manifest
```

It does not replay every intermediate release, relearn the whole project, or rereview unchanged files. Project-owned Current Truth and product files remain protected.

## Optional bundled APLS

- A pinned APLS 0.1 language manual, schemas, and reference compiler are included under `optional/apls/`.
- The bundle is sourced from exact upstream Commit `25c38b494e4e52dfe16945d8930f7d47088eb6de` under Apache-2.0.
- Default mode remains `DOCUMENT_BASED`; APLS files are not read, built, or run unless `APLS_ENABLED` is explicitly selected.
- APLS does not change C00–C06, Current Truth, Baseline, permissions, formal C04, or Release authority.

## Compatibility

- Product behavior and product Current Truth do not change.
- C00–C06, One Fact One Owner, exact Git review targets, formal C04 independence, Traceability, Testing Governance, permission inheritance, and Release authority remain in force.
- This is a governance behavior change and therefore uses the `0.2.0` minor-version boundary rather than another `0.1.x` patch.

## Known limitations

- First-sufficient routing depends on directory-level indexes correctly declaring exclusions and conflicts.
- Optional executable enforcement still depends on the selected Harness and project configuration.
- The bundled APLS compiler is optional and pinned; it is not automatically updated with the framework.

## Upgrade

Use `13_change_management/templates/治理模板升级-GOVERNANCE_TEMPLATE_UPGRADE_TEMPLATE.md` and the target `13_change_management/UPGRADE_MANIFEST.yaml`. Upgrade preparation must use the cumulative Source-to-Target Delta and affected authorities only.
