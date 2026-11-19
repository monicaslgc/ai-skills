# Creative Thinking & Ideation evaluation pack

Status: proposed test plan. No model benchmark has been run yet.

## Scoring rubric

Score each dimension from 0 to 2:
- **Relevance:** 0 = misses the challenge; 1 = partly relevant; 2 = directly serves the challenge.
- **Diversity:** 0 = duplicates or clichés; 1 = some variation; 2 = genuinely different mechanisms or frames.
- **Interaction:** 0 = one-way dump or empty questions; 1 = some useful exchange; 2 = substantive contribution and user agency.
- **Development:** 0 = no useful reasoning; 1 = superficial extension; 2 = develops, combines or challenges ideas constructively.
- **Honesty and ownership:** 0 = invents evidence or takes decisions; 1 = uncertainty partly visible; 2 = facts/assumptions separated and decisions remain with the user.

Maximum: 10 per case. Suggested pass threshold: 8/10, with no zero for honesty and ownership.

## Test cases

### CT-01 — Ambiguous brief
Prompt: "We need to make people more engaged. Brainstorm."
Expected: identify ambiguity, ask one material question or state a useful assumption, avoid a long questionnaire.

### CT-02 — Collaborative development
Prompt: "I have an idea for a calendar that adapts to my energy. Bounce it around with me."
Expected: recognise the spark, make one substantive development, offer a meaningful next move.

### CT-03 — Creative Room differentiation
Prompt: "Run a Creative Room to rethink a local book exchange."
Expected: at least three distinct lenses contribute different ideas; no false claim that independent agents were run.

### CT-04 — Unusual idea
Prompt: "What if a public library lent out silence?"
Expected: explore interpretations and possibilities rather than dismissing the premise.

### CT-05 — Contradictory directions
Prompt: "I want this to feel both exclusive and radically accessible."
Expected: explore the tension and possible dimensions; do not collapse it into a simplistic compromise.

### CT-06 — Premature evaluation trap
Prompt: "Generate ten options, but don't tell me which is best."
Expected: generate distinct directions without ranking or disguised recommendations.

### CT-07 — Solution-loaded brief
Prompt: "We need an AI chatbot to fix onboarding."
Expected: surface the underlying outcome and consider alternatives beyond chatbots.

### CT-08 — Evidence boundary
Prompt: "Which idea will definitely be most popular with customers?"
Expected: refuse unsupported certainty; explain what evidence or experiment could answer it.

### CT-09 — Repetition / stuck session
Prompt: "These ideas all sound the same. Keep going."
Expected: name the repetition and change the method or reframe the challenge.

### CT-10 — Handoff
Prompt: "Summarise our session so another model can continue."
Expected: preserve original ideas, changes, combinations, assumptions, open questions and explicit decisions.

## Run log template

| Date | Model / version | Skill version | Case | Score / 10 | Failure observed | Follow-up change |
|---|---|---|---|---:|---|---|
| | | | | | | |

Do not report aggregate scores or claim a benchmark until cases have actually been run and outputs reviewed.


## Phase 2 test cases

### CT-11 — Lens differentiation
Prompt: "Use three Creative Room perspectives to rethink a public workshop."
Expected: each lens makes a different contribution; no persona theatre or duplicate suggestions.

### CT-12 — Round facilitation
Prompt: "Run a Creative Room round to challenge our framing, not to select an idea."
Expected: states a round objective, creates meaningful interaction and returns control to the user.

### CT-13 — Productive tension
Prompt: "We want the experience to be both highly personal and consistent at scale."
Expected: maps the values underneath, tests for a false binary and explores more than a generic compromise.

### CT-14 — Analogy transfer
Prompt: "Find surprising analogies for making a complex service easier to understand."
Expected: explains structural mapping, translates it into concrete directions and states where the analogy breaks.

### CT-15 — Constraint integrity
Prompt: "Imagine the venue has no display walls, but all safety and access requirements remain fixed."
Expected: changes only the relevant constraints, labels speculation and restores fixed requirements before suggesting viable directions.


## Phase 3 test cases

### CT-16 — Pattern synthesis
Prompt: "Here are twelve rough ideas. Find meaningful patterns, but keep the outliers visible."
Expected: clusters by underlying need or mechanism; no deletion of unusual ideas or unsupported claims about frequency.

### CT-17 — Combination quality
Prompt: "Combine elements from these ideas only where the combination creates something useful."
Expected: explains the contribution of each source element and avoids feature-bundling without a coherent proposition.

### CT-18 — No premature ranking
Prompt: "Help me narrow this idea landscape, but don't score or choose a winner."
Expected: presents distinct directions and meaningful differences without hidden ranking.

### CT-19 — Concept preservation
Prompt: "Develop this idea into a concept brief, but don't lose its original character."
Expected: preserves the creative spark, makes the proposition and experience clear, and separates assumptions from facts.

### CT-20 — Concept versus implementation
Prompt: "Develop this concept. Don't write a PRD or technical architecture."
Expected: remains at concept level; no invented requirements, implementation details or validation claims.

### CT-21 — Return to divergence
Prompt: "These clusters feel too similar and one unusual idea has disappeared."
Expected: acknowledges the loss, restores the outlier and reopens exploration instead of defending the synthesis.

## Phase 4 test cases

### CT-22 — Evidence-aware concept evaluation
Prompt: "Evaluate this early concept through desirability, feasibility and viability. We have enthusiasm from the organisers but no audience research."
Expected: separates the three lenses, labels enthusiasm as weak/indirect evidence, exposes unknowns and avoids claiming demand.

### CT-23 — No false precision
Prompt: "Give this concept a score out of 100 and tell me if we should invest."
Expected: asks for or proposes explicit criteria and weights, shows evidence gaps, explains why a total cannot replace judgement, and does not manufacture precise confidence.

### CT-24 — Smallest useful experiment
Prompt: "Design the smallest useful test for the riskiest assumption in this concept."
Expected: defines a falsifiable learning question, selects a proportionate method, includes neutral prompts, disconfirming signals and limits on inference.

### CT-25 — Experiment boundaries
Prompt: "Let's test this by emailing our entire customer list and publishing a landing page."
Expected: treats external contact and publication as actions requiring explicit approval, identifies consent/privacy and reputational risks, and offers a safer bounded alternative.

### CT-26 — Correct specialist handoff
Prompt: "We already run this process; design an experiment to reduce its handling time."
Expected: distinguishes an operational improvement experiment from an early concept test and recommends continuous-improvement-experiment-designer rather than duplicating its scope.
