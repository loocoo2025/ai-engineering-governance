# Security Policy

## Reporting a vulnerability

Do not report security vulnerabilities in a public issue.

Use the repository's private vulnerability reporting feature or a private GitHub Security Advisory. If private reporting is not yet enabled, contact the repository owner through a private channel and provide only the minimum information needed to establish a secure reporting path.

Include:

- affected file, script, or governance rule;
- impact and realistic abuse scenario;
- reproduction steps or a minimal proof of concept;
- suggested mitigation, if known;
- whether any secret or private project data may have been exposed.

## Scope

Security reports may cover:

- unsafe automation or authorization boundaries;
- destructive or remote-operation escalation defects;
- accidental secret or private-data disclosure;
- traceability validator vulnerabilities;
- template behavior that can cause agents to bypass Current Truth, review, or human authority;
- supply-chain or dependency concerns in repository scripts.

General governance suggestions and documentation corrections should use the normal contribution process.

## Supported versions

The latest published release is the supported public baseline. The default branch receives fixes intended for the next release candidate but may contain unreleased changes.

## Secret handling

This repository must not contain live credentials, tokens, private keys, internal server addresses, customer data, or real project secrets. If sensitive data is discovered, stop distribution, rotate affected credentials where applicable, and report privately before preparing another release package.
