---
name: user-story-writer
description: Write clear user stories with scenarios and testable acceptance criteria for a skill, feature, tool or automation. Use when asked to write a user story, describe who something is for, define acceptance criteria, or document what a skill or feature should do from the user's point of view. Trigger phrases - "write a user story for", "who is this for", "acceptance criteria for", "add a USER_STORY.md".
---

# User Story Writer

Turn a skill, feature or automation into a short user story that someone else can read, agree with and test. Write from the user's side: the outcome they want, not how it is built.

## Inputs to collect

Read the thing being described (a `SKILL.md`, a README, a feature request or the user's description). Ask only for what you cannot infer:
- Who the typical user is.
- The problem or outcome they care about.
- A realistic situation where they would use it.
- Any limits (what it must not do, what needs approval).

## Workflow

1. **Name the user** by role and situation, not by a person ("a home-server owner", not a real name).
2. **State the want** as an outcome the user can recognise ("to see why a service keeps restarting"), not as a feature ("a log parser").
3. **State the benefit** in "so that" form: the real reason it matters.
4. **Write one concrete scenario** in two or three sentences using invented, generic details.
5. **Write 3-6 acceptance criteria.** Each one must be observable and checkable by someone who did not write it. Include at least one about safety or approval when the thing can change anything, and one about what happens when information is missing.
6. **Add one example prompt** or input the user could try.
7. **Check it:**
   - No criterion is vague ("works well", "is fast").
   - No criterion describes implementation.
   - No real names, addresses, credentials or employer details appear.

## Output format

Save as `USER_STORY.md` next to the thing it describes:

```
# User story: <name>

## Story
**As** <who>,
**I want** <outcome>,
**so that** <benefit>.

## Scenario
<two or three sentences>

## Acceptance criteria
- [ ] <observable, checkable statement>

## Try it
> <example prompt or input>
```

## Safety

- Use invented or generic details. Never copy real people, companies, hostnames, tokens or private data into a story.
- Do not promise behaviour the thing does not have. If the source is unclear, mark the criterion as an open question instead of guessing.
- Do not change the skill or feature being described; only write about it.
