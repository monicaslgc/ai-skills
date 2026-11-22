---
name: user-guide-writer
description: Write task-based user documentation for an existing app or feature: who it is for, prerequisites, numbered steps with the expected result, screenshots to capture, troubleshooting and a version note. Use when you have screens, notes, a recording, a flow inventory or access to the app.
---

# User guide writer

Turn what an app does into a guide that a real user can follow without asking anyone.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- The task the reader wants to complete, in their words, and who the reader is (role, experience, device).
- The app, version and environment the guide describes.
- The evidence: screenshots, a recording, a flow inventory (see [`app-flow-mapper`](../app-flow-mapper)), release notes, or access to a test account.
- The questions support keeps receiving about this task.
- Style rules already in use: tone, language, naming of screens and buttons.

## Workflow

1. Name the guide after the task, starting with a verb ("Create an invoice", "Reset your password"). One task per guide.
2. State who it is for and what they need first: permission or role, data, tools, other guides to read.
3. Write numbered steps. Each step is one action, starts with a verb, and names the button, field or menu exactly as it appears on screen. Put a warning before the step where a mistake is costly, not after.
4. After each step that changes the screen, say what the reader should see. This lets them notice they are off track.
5. Mark where a screenshot helps (new screen, hard-to-find control, result) and describe what to capture. Use demo data and hide personal data.
6. Add what differs by role or permission, and the common mistakes with the exact error message and the way out.
7. Add a short "If it does not work" section with the first checks and who to contact.
8. End with the version, the date it was verified, and who verified it.
9. Test it: follow the guide in the app with the reader's role, fixing every step that is unclear, missing or wrong.

## Rules

- Document only what you have seen or been given evidence for. Mark everything else "to confirm" instead of guessing.
- Use the reader's words and the labels on screen. Avoid internal names.
- Keep sentences short. No jargon unless the reader already uses it.
- Do not include credentials, real customer data or internal-only details that the reader should not see.
- If the app can do something dangerous, say so before the step and say how to undo it.

## Output format

```
Title: <verb + task>
For: <role>   Needs: <prerequisites>   Version verified: <app version, date, by>
Steps
  1. <action>. You should see <result>.   [screenshot: <what to capture>]
  ...
Differences by role
Common problems: message | cause | what to do
If it does not work
```

## Quality checks

- A person who has never done the task completes it using only the guide.
- Every step names a real label and states the expected result.
- Nothing is described that was not verified or marked "to confirm".
- Screenshots contain no personal data.
