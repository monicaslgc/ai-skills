# Contributing

Thanks for helping. Skills here are small and single-purpose.

## Add a skill

1. Create `skills/<skill-name>/SKILL.md` (lowercase, hyphens; the folder name must equal `name:`).
2. Start with frontmatter:

   ```markdown
   ---
   name: your-skill
   description: When to use it, with a few example trigger phrases.
   ---
   ```
3. Add `skills/<skill-name>/USER_STORY.md` (who it is for, scenario, acceptance criteria, an example prompt).
4. Keep the body to a workflow, tool choices and safety rules. Prefer read-only first and require confirmation for anything destructive.
5. Never include real IPs, hostnames, emails, tokens or personal data. Use placeholders like `<host>`.
6. Add a row to the table in the README, and an example prompt if it helps.
7. Run the validator:

   ```bash
   python scripts/validate.py
   ```

## Pull requests

One skill per PR. Explain what problem it solves and how you tested it.

## Confidentiality

Apply the textbook test: a skill must be explainable from public standards or common professional practice. Do not turn a company's internal policy, procedure, template, threshold, pricing or contract structure into a skill, even with the names removed. Only contribute material you have the right to share. Do not include information from an employer, client or supplier (names, figures, contract terms, internal procedures, documents or source code), and do not include real personal data. Describe methods in general terms and use invented examples.

## Licensing of contributions

By submitting a pull request you confirm that you wrote the contribution or have the right to share it, and that you license it under this repository's MIT License. You keep the copyright in your own contribution.
