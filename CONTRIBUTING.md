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
