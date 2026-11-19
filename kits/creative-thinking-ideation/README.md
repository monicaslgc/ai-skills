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
| [creative-perspective-lenses](../../skills/creative-perspective-lenses) | Explore a challenge through distinct thinking lenses |
| [creative-room-round-facilitator](../../skills/creative-room-round-facilitator) | Facilitate purposeful, interactive Creative Room rounds |
| [productive-tension-mapper](../../skills/productive-tension-mapper) | Turn competing values and assumptions into useful exploration |
| [analogy-bridge-builder](../../skills/analogy-bridge-builder) | Borrow structural patterns from other domains |
| [constraint-remixer](../../skills/constraint-remixer) | Reframe a challenge by deliberately remixing constraints |
| [creative-convergence](../../skills/creative-convergence) | Find patterns and combinations without premature ranking |
| [concept-developer](../../skills/concept-developer) | Develop a promising idea into a coherent concept brief |
| [concept-evaluator](../../skills/concept-evaluator) | Assess desirability, feasibility and viability while exposing evidence gaps |
| [concept-experiment-designer](../../skills/concept-experiment-designer) | Design a small, ethical experiment to test a critical concept assumption |

## Suggested workflow

1. Start with creative-session for a guided session.
2. Use creative-brief-griller only when the brief needs clarification.
3. Use divergent-ideation to open the solution space.
4. Use idea-bouncer to develop one or more promising ideas through interaction.
5. Return to divergence or reframe the challenge whenever the conversation becomes repetitive.
6. Use perspective lenses and the round facilitator for Creative Room sessions.
7. Use productive-tension-mapper when ideas or values conflict.
8. Use analogy-bridge-builder or constraint-remixer when exploration gets stuck.
9. Use creative-convergence when the idea landscape is broad enough to reveal patterns or combinations.
10. Use concept-developer to turn a user-selected direction into a clear, discussable concept.
11. Return to divergence whenever convergence removes important differences or exposes a weak assumption.
12. Use concept-evaluator when the user is ready to examine a concept's desirability, feasibility and viability.
13. Use concept-experiment-designer when a critical assumption needs a small, ethical test. For operational process improvements, use the Operations Management kit's continuous-improvement-experiment-designer instead.
14. Stop when the user has enough material, or create a session record if a handoff is useful.

The workflow is intentionally non-linear. Do not force every phase into every session.

## Install the whole kit

Clone the repository and copy the skill folders into the skills directory supported by your assistant. Example for Claude Code on macOS/Linux:

```bash
git clone https://github.com/monicaslgc/ai-skills.git
cp -r ai-skills/skills/creative-session ~/.claude/skills/
cp -r ai-skills/skills/creative-brief-griller ~/.claude/skills/
cp -r ai-skills/skills/divergent-ideation ~/.claude/skills/
cp -r ai-skills/skills/idea-bouncer ~/.claude/skills/
cp -r ai-skills/skills/creative-perspective-lenses ~/.claude/skills/
cp -r ai-skills/skills/creative-room-round-facilitator ~/.claude/skills/
cp -r ai-skills/skills/productive-tension-mapper ~/.claude/skills/
cp -r ai-skills/skills/analogy-bridge-builder ~/.claude/skills/
cp -r ai-skills/skills/constraint-remixer ~/.claude/skills/
cp -r ai-skills/skills/creative-convergence ~/.claude/skills/
cp -r ai-skills/skills/concept-developer ~/.claude/skills/
cp -r ai-skills/skills/concept-evaluator ~/.claude/skills/
cp -r ai-skills/skills/concept-experiment-designer ~/.claude/skills/
```

On Windows PowerShell:

```powershell
git clone https://github.com/monicaslgc/ai-skills.git
Copy-Item -Recurse ai-skills\skills\creative-session "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\creative-brief-griller "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\divergent-ideation "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\idea-bouncer "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\creative-perspective-lenses "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\creative-room-round-facilitator "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\productive-tension-mapper "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\analogy-bridge-builder "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\constraint-remixer "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\creative-convergence "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\concept-developer "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\concept-evaluator "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\concept-experiment-designer "$env:USERPROFILE\.claude\skills\"
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
