# Career kit

Skills for job applications built from one honest master CV: tailoring, cover letters, interview stories and confidentiality-safe wording.

## Skills in this kit

| Skill | Use it to |
|---|---|
| [`job-posting-scorer`](../../skills/job-posting-scorer) | Rank job postings with transparent, rules-based scoring |
| [`cv-tailoring-from-master`](../../skills/cv-tailoring-from-master) | Tailor a master CV to a job posting without inventing anything |
| [`cover-letter-writer`](../../skills/cover-letter-writer) | Write a short, specific, natural cover letter |
| [`achievement-story-builder`](../../skills/achievement-story-builder) | Turn work achievements into interview-ready STAR stories |
| [`confidentiality-safe-wording`](../../skills/confidentiality-safe-wording) | Describe confidential work publicly without revealing names or secrets |

## Suggested order

1. Rank postings with `job-posting-scorer`.
2. Write safe, accurate descriptions with `confidentiality-safe-wording`.
3. Tailor with `cv-tailoring-from-master` and write the letter with `cover-letter-writer`.
4. Prepare with `achievement-story-builder`.

## Install the whole kit

```bash
git clone https://github.com/monicaslgc/ai-skills.git
cp -r ai-skills/skills/job-posting-scorer ~/.claude/skills/
cp -r ai-skills/skills/cv-tailoring-from-master ~/.claude/skills/
cp -r ai-skills/skills/cover-letter-writer ~/.claude/skills/
cp -r ai-skills/skills/achievement-story-builder ~/.claude/skills/
cp -r ai-skills/skills/confidentiality-safe-wording ~/.claude/skills/
```

On Windows PowerShell:

```powershell
git clone https://github.com/monicaslgc/ai-skills.git
Copy-Item -Recurse ai-skills\skills\job-posting-scorer "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\cv-tailoring-from-master "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\cover-letter-writer "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\achievement-story-builder "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\confidentiality-safe-wording "$env:USERPROFILE\.claude\skills\"
```

These skills need no tools or servers. Each skill folder has a `USER_STORY.md` with a scenario and an example prompt.

All examples are invented. Do not paste real personal data, credentials or confidential contract text into a chat you do not control.
