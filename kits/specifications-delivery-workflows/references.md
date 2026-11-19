# Specifications & Delivery Workflows references

This kit uses general engineering and product-delivery practices. Check current editions and the applicable organisation's policies before treating any practice as mandatory.

## Reference areas

- **Requirements quality and traceability:** atomic requirements, unique IDs, rationale, source, verification method and change control.
- **Workflow modelling:** explicit actors, states, decisions, exceptions, completion criteria and process ownership.
- **API contracts:** schemas, versioning, authentication, idempotency, error handling, pagination, rate limits and compatibility.
- **Backlog quality:** user outcomes, testable acceptance criteria, dependencies, small increments and definition of ready/done.
- **Software testing:** risk-based coverage, contract tests, boundary tests, failure injection, regression and execution evidence.
- **Delivery planning:** dependency mapping, estimate ranges, uncertainty, milestones, capacity assumptions and change impact.
- **Operational readiness:** observability, ownership, runbooks, escalation, rollback/compensation and support handover.
- **AI-enabled workflow controls:** treat model output as a proposal; validate with deterministic rules and require approval for consequential actions.

## Public starting points

- IREB — requirements engineering resources: https://www.ireb.org/
- OMG — BPMN specifications: https://www.omg.org/bpmn/
- OpenAPI Initiative — API description standard: https://www.openapis.org/
- JSON Schema — schema validation vocabulary: https://json-schema.org/
- ISTQB — testing terminology and syllabus resources: https://www.istqb.org/
- OWASP — API Security Project: https://owasp.org/www-project-api-security/
- GitHub Docs — issues and project planning: https://docs.github.com/

These are starting points, not evidence that a proposed design complies with a standard. Confirm source versions and the actual API vendor's documentation before implementation.

## Review discipline

1. Keep facts, assumptions, proposals, approved decisions and unknowns distinct.
2. Trace requirements to implementation work and tests.
3. Make failure behaviour and side effects explicit.
4. Define a safe way to retry, replay, reconcile and roll back.
5. Record what has actually been verified; never infer execution from a written plan.
