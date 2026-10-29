# AI Software Engineering Governance Framework v0.2.1

> Candidate release notes. Publication is pending an independent incremental C04 review; this file does not claim a published release or a review PASS.

## What changes

This patch reduces unnecessary review and validation work while preserving independent acceptance of significant engineering changes.

- Replace unconditional full-validation/full-CI wording with affected-scope validation, necessary regression checks and valid evidence reuse.
- Distinguish ordinary design questioning from formal C04. Finishing a development stage does not automatically create a new formal gate.
- Report S0/S1 findings immediately and stop affected acceptance or progression. A reviewer may finish still-valid independent checks within the frozen scope and existing budget before returning the findings together. Stop when further checks have lost their valid premise or practical value; neither one-finding-per-round nor exhaustive auditing is required.
- Allow one formal review to cover compatible trigger events on the same exact target, with evidence for each applicable acceptance condition. Task hierarchy does not automatically create review-gate hierarchy.
- Clarify the boundary for non-semantic governance maintenance, auxiliary checks and proven equivalent check implementation maintenance. This does not permit in-place changes to locked declarations, registered guard definitions, thresholds, permissions or gate effectiveness.

## Optional industrial engineering profiles

The release includes two project-level attachments previously added to `main` after the v0.2.0 tag:

- `docs/profiles/PLC_ENGINEERING_PROFILE.md`: scan semantics, sequencing, retained data, output arbitration, capacity and field maintainability.
- `docs/profiles/MCU_ENGINEERING_PROFILE.md`: bare-metal/RTOS choices, interrupts, concurrency, resource lifetimes, timing and fault recovery.

Copying or upgrading does not adopt a profile. Projects explicitly select the applicable constraints and load only relevant sections. Existing customized profiles and adoption decisions must be preserved and merged where necessary.

## Controls retained

C00–C06, Current Truth ownership, exact immutable review targets, fresh independent formal review sessions, PASS/CHANGES_REQUESTED, in-scope finding closure verification, applicable traceability and regression guards, permission boundaries and release authorization remain in force. Faithful review-record archival continues to use mechanical checks without recursively triggering C04.

## Upgrade

Use `13_change_management/templates/治理模板升级-GOVERNANCE_TEMPLATE_UPGRADE_TEMPLATE.md` with the exact target tag and `13_change_management/UPGRADE_MANIFEST.yaml`. Compare the cumulative source-to-target delta and merge project-owned facts rather than overwriting them.

This patch changes review execution semantics. Its adoption requires an incremental formal C04; the maintenance exception cannot exempt this upgrade. Unchanged product code, the optional APLS snapshot and unrelated historical evidence do not require a full rereview or retest.

## Known limitations

Equivalent maintenance requires concrete evidence; uncertain changes follow the formal route. Required hardware validation and applicable project acceptance criteria still depend on the adopting project and its target environment. This release does not upgrade or modify product repositories automatically.
