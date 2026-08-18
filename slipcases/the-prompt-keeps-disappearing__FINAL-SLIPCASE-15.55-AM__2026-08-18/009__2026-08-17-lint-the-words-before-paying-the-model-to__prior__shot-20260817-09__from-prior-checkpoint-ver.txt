ZETTEL

ID:
SHOT-20260817-09

TITLE:
2026-08-17 — Lint the words before paying the model to build the world.

SOURCE:
Chengyi Yang, Pengzhen Li, Jiayin Qi, Aimin Zhou, Ji Wu, Ji Liu — “SCMAPR: Self-Correcting Multi-Agent Prompt Refinement for Complex-Scenario Text-to-Video Generation” — arXiv:2604.05489v4 — 2026-04 — consulted 2026-08-17.
SOURCE URL: https://arxiv.org/abs/2604.05489

PASSAGE:
[QUOTE]
“structured semantic verification that triggers conditional revision when violations are detected.”

RESEARCH OBJECT:
PROMPT STATIC ANALYSIS.

LOCAL MOVE:
[[MJ-2022-013-A]] found PRODUCTIVE MISMATCH:

the generated artifact can become useful because it differs from what was imagined.

But not every mismatch is productive.

[[SHOT-20260817-03]] gives generated objects schemas.

[[SHOT-20260817-07]] allows failures to rewrite later instructions.

SCMAPR moves error detection even earlier:

before generation.

The prompt itself becomes an inspectable intermediate artifact.

SOURCE TERMS:
“scenario routing”
“prompt refinement”
“semantic verification”
“conditional revision”
“violations”
“rewriting”

WHAT BECAME STRANGE:
The expensive generated artifact may not need to exist before some failures become detectable.

A prompt can be wrong before the model ever sees the world it is supposed to make.

QUESTION:
Which classes of generative failure can be detected directly in the specification?

DEEPER QUESTION:
Can prompt practice develop static analysis analogous to programming languages:

type errors
missing dependencies
contradictory constraints
unbound entities
impossible temporal order
underspecified persistence?

MECHANISM:
Raw request arrives.

Scenario is classified.

Relevant specification policy is selected.

Prompt is rewritten.

Verifier evaluates the rewritten specification.

Detected violation triggers another rewrite.

Only validated instruction proceeds to generation.

FORMAL SHIFT:
DESCRIBE
→ GENERATE
→ INSPECT FAILURE
→ CORRECT

becomes

DESCRIBE
→ COMPILE SPECIFICATION
→ LINT
→ CORRECT
→ GENERATE

SOURCE FORMALISM:
[PARAPHRASE]

SCMAPR uses specialized stages for scenario routing, prompt refinement, semantic verification, and conditional revision before the final generation request proceeds.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

PROMPT LINTER:

ENTITIES:
all referenced entities declared?

IDENTITY:
persistence requirements explicit?

RELATIONS:
spatial relations noncontradictory?

TIME:
event order satisfiable?

CAMERA:
camera state compatible with described action?

STATE:
what persists after each operation?

BOUNDARY:
what must not change?

If violation:
REWRITE.

If internally valid:
EXECUTE.

TENSION:
[[MJ-2022-013-A]] warns against eliminating every mismatch because unexpected difference can produce insight.

Therefore prompt linting should catch:

CONTRADICTION

without eliminating:

INTERPRETIVE OPENNESS.

A specification can be rigorous about invariants while leaving chosen regions underdetermined.

MISSING:
A distinction between:

ERROR
AMBIGUITY
OPEN PARAMETER
CREATIVE FREEDOM.

Most prompt checkers risk treating all four as deficiencies.

BOUNDARY:
SCMAPR concerns complex text-to-video generation.

The static-analysis interpretation and generalized lint categories are [OUR FORMALIZATION — NOT SOURCE SYNTAX].

CITATION TRAIL:
[[MJ-2022-013-A]]
→ mismatch can be productive
→ [[SHOT-20260817-03]]
→ structure becomes explicit
→ SCMAPR 2026
→ specification receives semantic verifier
→ [[SHOT-20260817-07]]
→ execution failures can later update the verifier's rules
→ prompt practice becomes compile-lint-execute-revise

TEST:
Beginning 2026-08-17, collect failed prompts from:

image generation
video generation
3D world generation
software generation
agent workflows.

For each failure ask:

Could the failure have been detected from the specification alone?

If yes, derive a lint rule.

Classify each rule as:

CONTRADICTION
MISSING STATE
MISSING ENTITY
INVALID DEPENDENCY
UNBOUND REFERENCE
ACCIDENTAL AMBIGUITY.

Do not lint intentional underdetermination.

PLATFORM:
Text-to-video
Generative media
Agent prompting
Prompt refinement

LINKS:
[[MJ-2022-013-A]]
[[SHOT-20260817-03]]
[[SHOT-20260817-07]]
[[SHOT-20260817-08]]

BIBTEX:
@misc{yang2026scmapr,
  title={SCMAPR: Self-Correcting Multi-Agent Prompt Refinement for Complex-Scenario Text-to-Video Generation},
  author={Yang, Chengyi and Li, Pengzhen and Qi, Jiayin and Zhou, Aimin and Wu, Ji and Liu, Ji},
  year={2026},
  eprint={2604.05489},
  archivePrefix={arXiv}
}
