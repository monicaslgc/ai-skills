# How skills work, and how to build one

A skill is a folder with a Markdown file (`SKILL.md`) that teaches an AI agent how to do one job well. It is not code and it is not a prompt you paste each time. The agent finds it, reads it when it is relevant and follows it.

## How an agent uses a skill

1. **Discovery.** At the start of a session the agent reads only the `name` and `description` of every installed skill. This is cheap, so you can have hundreds installed.
2. **Matching.** When your request fits a description, the agent loads that skill's full `SKILL.md` into its context. The description is the only thing used to decide, so it does most of the work.
3. **Following.** The agent follows the workflow, asks for missing inputs and produces the output format the skill defines.
4. **Extras on demand.** A skill can point to other files in its folder (templates, checklists, examples). The agent opens them only when a step needs them.

```
skills/
  sop-writer/
    SKILL.md        <- required: frontmatter + instructions
    USER_STORY.md   <- in this repo: who, scenario, acceptance, example prompt
    templates/      <- optional extra files the skill refers to
```

Skills differ from the alternatives:

| | Skill | Pasted prompt | Tool / MCP server |
|---|---|---|---|
| Loaded | When relevant | Every time you paste it | When called |
| Contains | Method and judgement | A one-off request | An action (read a file, call an API) |
| Needs code | No | No | Yes |

A skill can say which tools to use, but it does not provide them. Say so in the skill and in the README's tool requirements.

## Anatomy of a good `SKILL.md`

```markdown
---
name: sop-writer
description: Write a standard operating procedure (SOP). Use when documenting how a task is done, handing work over, or making a process repeatable.
---

# Sop writer

One sentence on the job and the result.

## Inputs to collect
## Workflow
## Output format
## Safety rules
```

**Frontmatter**
- `name`: lowercase, hyphens, identical to the folder name.
- `description`: what it does and when to use it, with a few trigger phrases a person would really type. Write it for the agent, not for a catalogue.

**Body**
- Inputs to collect: what to ask for, and to mark gaps as unknown instead of guessing.
- Workflow: numbered steps, each one action, starting with a verb.
- Output format: a skeleton the agent fills in, so results are consistent.
- Safety rules: read-only first, confirm before anything that changes or sends, no secrets.

## Building one, step by step

1. **Pick one job.** If the description needs "and" twice, split it into two skills. Small skills are easier to trigger, test and reuse.
2. **Write a real example first.** Do the job once by hand, or with the agent, and note the steps that made the result good. The skill is that method written down.
3. **Write the description.** Name the job, then "Use when ..." with two or three trigger situations. Test it by asking: would a stranger's request match this wording?
4. **Write the workflow.** Order the steps as you did them. Add what to do when input is missing or a step fails.
5. **Define the output.** Show the exact sections or table the result should have.
6. **Add the guardrails.** Mark steps that change things, spend money, send messages or touch personal data, and require confirmation. Never ask for passwords or keys.
7. **Write `USER_STORY.md`.** Who it is for, a short scenario, acceptance criteria and a prompt to try. The acceptance criteria are your test.
8. **Test it.** Run the example prompt in a fresh session. Check that the skill triggers, that the steps are followed and that the acceptance criteria hold. Then try a vague request and a request that should not trigger it.
9. **Register and validate.** Put it in exactly one kit, add it to the README, then run the checks below.

## Writing tips

- Short and specific beats long and general. Every line should change what the agent does.
- Explain the reason for a rule once. Agents follow rules better when they know why.
- Prefer a checklist the agent can verify over a vague instruction such as "be thorough".
- Do not put facts that go stale (prices, version numbers) in the skill. Point to where to check them.
- Keep the body under roughly 150 lines. Move long reference material into a separate file the skill links to.

## Common mistakes

| Mistake | Fix |
|---|---|
| Vague description ("helps with documents") | Name the document and the trigger situations |
| Skill never triggers | Add the words people really use to the description |
| Skill triggers too often | Narrow the description, state what it is not for |
| One skill that does five jobs | Split it, and chain them in a workflow |
| Invents facts when input is missing | Add an "if unknown, say so and ask" rule |
| Real names, IPs or company internals included | Use placeholders and invented examples |

## Validating in this repository

```bash
python scripts/validate.py            # structure, user story, README and kit listing, no secrets
python scripts/check_tools.py         # tools named in skills exist and are documented
python scripts/check_workflows.py     # workflow chains refer to real skills
python scripts/check_private_terms.py # no private terms in tracked files
```

The same checks run on every push in GitHub Actions. They check structure, not quality, so always run your example prompt too. See [CONTRIBUTING.md](../CONTRIBUTING.md) for the pull request rules and the confidentiality test.

## Chaining skills

One skill does one job. To deliver something bigger, chain skills in a workflow with a person approving at each gate. See [`workflows/`](../workflows/README.md) and the [skill ecosystem map](skill-ecosystem/README.md).
