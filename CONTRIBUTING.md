# Contributing

Thank you for improving the AI Software Engineering Governance Framework.

## Report governance issues

Open an issue that identifies:

- the conflicting or unsafe behavior;
- the affected rule or artifact;
- a minimal generic example;
- the expected governance outcome.

Report security-sensitive findings privately according to `SECURITY.md`.

## Propose rule changes

Explain the evidence, the smallest generic correction, affected roles or fact owners, compatibility impact, and how the proposal was reviewed. Do not add a new owner or Current Truth source when an existing owner can hold the fact.

## Submit pull requests

Keep pull requests narrow. Include:

- the governance problem;
- the smallest proposed change;
- files and roles affected;
- validation performed;
- any migration impact for existing adopters.

Run at minimum:

```bash
git diff --check
```

When requirement traceability rules or artifacts change, also run:

```bash
python3 09_quality/traceability/validate_traceability.py
```

## Generic changes only

Never submit credentials, private prompts, customer information, user names, email addresses, local filesystem paths, private repository URLs, server addresses, or real internal project facts. Use explicit placeholders in examples.

Changes learned from a real project must be generalized before they enter this repository.

## Backport philosophy

```text
Real project evidence
→ generic fix
→ independent review
→ template
```

Backport the reusable governance correction, not the originating project's facts, decisions, identifiers, or implementation details.

## License

By submitting a contribution, you agree that it will be licensed under the Apache License 2.0 applicable to this repository.
