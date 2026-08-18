ZETTEL

ID:
OPS-20260817-006

TITLE:
The most powerful way to tell the model what you want may be to define how failure is scored.

SOURCE:
DSPy — current documentation accessed August 17, 2026.
https://dspy.ai/

PASSAGE:
[QUOTE]
“Compile your program against a metric.”

RESEARCH OBJECT:
THE METRIC BECOMES AN INDIRECT INSTRUCTION GENERATOR.

LOCAL MOVE:
[[MJ-MARTINA-004]] described Martina accumulating prompt lessons manually through trial and error.

DSPy separates the task specification from the exact prompt wording and provides optimizers that modify prompts against examples and a scoring function.

The programmer can increasingly call the shot by defining success rather than composing every sentence that causes it.

SOURCE TERMS:
“structured signatures”
“program”
“metric”
“optimizers”
“compile”
“prompts automatically”

WHAT BECAME STRANGE:
Prompt authorship can move one level upward.

Instead of:

WRITE THE RIGHT WORDS

the operation becomes:

DEFINE THE TASK
DEFINE EXAMPLES
DEFINE WHAT COUNTS AS BETTER
SEARCH FOR WORDS THAT SATISFY IT.

QUESTION:
Does the metric become a higher-order prompt?

DEEPER QUESTION:
If an optimizer writes the actual instructions, is the human programmer's true expressive act the definition of the evaluation function?

MECHANISM:
DSPy exposes structured signatures for tasks, modules controlling execution strategy, and optimizers that compile programs against metrics using examples and scoring functions.

FORMAL SHIFT:
FROM:
HUMAN
→ PROMPT
→ OUTPUT

TO:
HUMAN
→ TASK_SIGNATURE
→ METRIC
→ EXAMPLES
→ OPTIMIZER
→ PROMPT*
→ OUTPUT.

SOURCE FORMALISM:
DSPy documentation describes:

Signature
→ Module
→ execution

and:

examples
+ scoring function
+ optimizer
→ compiled program / tuned prompts.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

P* =
argmax_P
SCORE(
  RUN(P, DATA)
)

Human “shot calling” moves from specifying P directly to specifying SCORE.

TENSION:
A metric only calls the intended shot if it actually captures the intended goal.

Optimization can make a system better at the metric while worse at unmeasured properties.

MISSING:
Cases where optimized prompts reveal specification errors in the metric rather than prompt errors.

BOUNDARY:
DSPy does not eliminate prompts. It changes who or what selects their concrete wording and how that wording is evaluated.

CITATION TRAIL:
[[MJ-MARTINA-004]]
→ accumulate prompt improvements manually
→ DSPy automates prompt selection against a metric
→ successful behavior becomes optimization target
→ prompt text becomes compiled artifact
→ pursue the evaluator as the new site of authorship.

TEST:
Choose one prompt from the current Zettel-forage practice.

Create a dataset of desired and undesired outputs.

Write a metric for:
schema fidelity,
novelty,
citation validity,
recursive openness.

Allow an optimizer to rewrite the underlying prompt.

Inspect every change.

Ask whether the optimized prompt teaches something new about the latent specification that the original prose failed to state.

PLATFORM:
DSPy

LINKS:
[[MJ-MARTINA-004]]
[[MJ-MARTINA-014-A-A]]
[[MJ-MARTINA-013-A]]

BIBTEX:
@misc{dspy2026docs,
  author = {{DSPy Project}},
  title = {DSPy: Program, Don't Prompt},
  year = {2026},
  url = {https://dspy.ai/}
}
