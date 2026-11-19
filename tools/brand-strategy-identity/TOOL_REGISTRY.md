# Brand Strategy & Identity — Tool Catalogue

This is a provider-neutral design catalogue, not an executable tool server. **No brand-specific integrations are implemented or connected by this kit.** A skill may only call a tool when the runtime actually provides it. Otherwise, it must say so and offer a manual alternative.

The schemas supplied here are reference input/output contracts for selected operations. They do not implement the operations.

| Tool | Purpose | Class | Side effect | Approval | Schema status |
|---|---|---|---|---|---|
| `web_search` | Search public sources | data | none | no | Not defined |
| `image_search` | Find visual references | data | none | no | Not defined |
| `brand_website_analyzer` | Extract public site messaging and visible brand patterns | data | none | no | Not defined |
| `competitor_research` | Compare competitors from public evidence | data | none | no | [Input schema](schemas/competitor_research.input.schema.json) |
| `audience_evidence_analyzer` | Synthesise supplied research and analytics | data | none | no | Not defined |
| `trademark_search` | Query selected trademark registers | data | none | no; preliminary only | Covered as an option in [naming validation](schemas/naming_validation.input.schema.json) |
| `domain_availability_check` | Check domain status | data | none | no; status can change | Covered as an option in [naming validation](schemas/naming_validation.input.schema.json) |
| `social_handle_check` | Check public handle status | data | none | no; status can change | Covered as an option in [naming validation](schemas/naming_validation.input.schema.json) |
| `moodboard_builder` | Assemble references and annotations | action | creates draft | yes if shared externally | Not defined |
| `image_generation` | Generate original visual explorations | action | creates draft assets | yes before adoption/publication | Not defined |
| `colour_palette_generator` | Produce palette candidates and contrast data | action | creates draft | no for draft; yes for approval | Not defined |
| `generate_naming_matrix` | Save candidate names and evaluation | action | writes project data | yes if shared or finalised | Not defined |
| `create_brand_brief` | Create/update project brief | action | writes project data | yes for external sharing | Not defined |
| `generate_brand_guidelines` | Generate draft guideline document | action | writes file | yes before distribution | Not defined |
| `request_stakeholder_feedback` | Send feedback request | action | sends communication | yes | Not defined |
| `create_approval_request` | Request formal approval | action | sends communication | yes | [Input schema](schemas/approval_request.input.schema.json) |
| `save_brand_decision` | Record approved decision/version | action | writes project data | yes | [Input schema](schemas/save_decision.input.schema.json) |
| `update_project_status` | Update workflow state | action | writes project data | yes when status implies approval | Not defined |
| `export_brand_document` | Export artefact | action | creates file | yes before external distribution | Not defined |

## Shared handoff contract

[Project handoff output schema](schemas/project_handoff.output.schema.json) defines a common stage result. It is a data contract only; the orchestrator skill does not itself create persistent state or invoke other skills unless the host agent runtime supports that behaviour.

## Contract rules

Before implementing a tool, define its stable name, purpose, typed input/output schema, error behaviour, authentication scope, rate limits and side-effect classification. Use JSON Schema and reject unknown properties. Outputs should include provenance, timestamp, query/filters and limitations. Never expose secrets. Use idempotency keys for writes. Tool errors must be explicit; never replace an error with a guessed result. A tool description must explain when not to use it.

## Implementation order

1. Start with read-only research tools and clear provenance.
2. Add naming checks with jurisdiction, class, query and timestamp; results are preliminary, never legal clearance.
3. Add project-document writes with versioning and idempotency.
4. Add approval requests and decision records with attributable human approvals.
5. Add publishing/export integrations only after permissions, audit logs and rollback behaviour are tested.
