# NOC Operator Patterns

Sanitized, reusable engineering patterns for Network Operations tooling.

This repository contains generic examples derived from real operational engineering work without publishing production credentials, customer-sensitive evidence, internal endpoints, or proprietary runbook details.

## Included patterns

- wrapped operator cards;
- incident correlation;
- evidence normalization;
- status vocabulary;
- human-first terminal output;
- read-only-first control patterns.

## Design rule

```text
machine evidence
      |
      v
normalize
      |
      v
correlate
      |
      v
render for the operator
      |
      v
next safe action
```

## Status vocabulary

```text
[ OK ]   confirmed healthy / expected
[WARN]   degraded, contradictory, or needs attention
[FAIL]   confirmed fault
[INFO]   context
[????]   unknown / not yet validated
```

## Safety

These examples are intentionally generic. They do not include production hostnames, customer identifiers, secrets, internal API endpoints, or privileged execution paths.
