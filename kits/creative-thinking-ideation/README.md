# Creative Thinking & Ideation kit

A universal, tool-free set of skills for exploring challenges, generating possibilities and developing ideas through collaborative thinking or a simulated Creative Room.

## Modes

- **Creative Partner:** the AI works directly with the user through natural back-and-forth.
- **Creative Room:** the AI uses distinct thinking lenses—Visionary, Strategist, Artist, Inventor, Challenger and Synthesizer—to introduce varied perspectives. These are reasoning perspectives, not separate agents or real people.

## Skills

| Skill | Use it to |
|---|---|
| [creative-session](../../skills/creative-session) | Orchestrate a complete session in either mode |
| [creative-brief-griller](../../skills/creative-brief-griller) | Clarify the challenge and challenge solution-loaded briefs |
| [divergent-ideation](../../skills/divergent-ideation) | Generate distinct directions without premature evaluation |
| [idea-bouncer](../../skills/idea-bouncer) | Develop ideas through iterative back-and-forth |

## Suggested workflow

1. Start with creative-session for a guided session.
2. Use creative-brief-griller only when the brief needs clarification.
3. Use divergent-ideation to open the solution space.
4. Use idea-bouncer to develop one or more promising ideas through interaction.
5. Return to divergence or reframe the challenge whenever the conversation becomes repetitive.
6. Stop when the user has enough material, or create a session record if a handoff is useful.

The workflow is intentionally non-linear. Do not force every phase into every session.

## Install the whole kit

Clone the repository and copy the skill folders into the skills directory supported by your assistant. Example for Claude Code on macOS/Linux:

```bash
git clone https://github.com/monicaslgc/ai-skills.git
cp -r ai-skills/skills/creative-session ~/.claude/skills/
cp -r ai-skills/skills/creative-brief-griller ~/.claude/skills/
cp -r ai-skills/skills/divergent-ideation ~/.claude/skills/
cp -r ai-skills/skills/idea-bouncer ~/.claude/skills/
```

On Windows PowerShell:

```powershell
git clone https://github.com/monicaslgc/ai-skills.git
Copy-Item -Recurse ai-skills\skills\creative-session "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\creative-brief-griller "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\divergent-ideation "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\idea-bouncer "$env:USERPROFILE\.claude\skills\"
```

Other assistants use their documented skills directory. Each skill folder contains SKILL.md and USER_STORY.md.

## Examples

- "Run a Creative Partner session to rethink how people organise personal projects."
- "Open a Creative Room and explore unusual directions for a community workshop."
- "I have a rough idea. Bounce it around with me; don't evaluate it yet."
- "Generate several radically different approaches, then let me choose one to develop."

## Scope and limitations

These skills are instructions for an AI model, not a persistent multi-agent runtime. Creative Room lenses are simulated within the current model interaction. Session continuity across chats requires the user to retain and provide the session record. No external tools, APIs or proprietary methods are required.

All examples should use fictional or approved information. Do not include confidential employer, client or personal data.

See examples.md, references.md and evaluation.md.
