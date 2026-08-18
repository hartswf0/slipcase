ZETTEL

ID:
PROMPT-PRACTICE-PROPERTY-008

TITLE:
AN INVARIANT SHOULD NOT JUST BE WRITTEN DOWN; IT SHOULD KNOW HOW TO ATTACK THE PROGRAM.

SOURCE:
Koen Claessen & John Hughes — “QuickCheck: A Lightweight Tool for Random Testing of Haskell Programs” — ICFP 2000.

SOURCE URL:
https://doi.org/10.1145/351240.351266

PASSAGE:
[QUOTE]
QuickCheck “aids the Haskell programmer in formulating and testing properties of programs.”

RESEARCH OBJECT:
GENERATIVE INVARIANT.

A prompt rule becomes much stronger when it can produce its own family of attempted violations.

LOCAL MOVE:
[[SON-IEC-005-A]] showed that search must explore surprising stepping stones.

[[SON-CONTROL-003]] split vague “control” into separately testable dimensions.

Property-based testing suggests a corresponding transformation for prompt practice:

DO NOT ONLY SAVE:

“the character must remain the same.”

Save a procedure capable of generating many situations in which character persistence could fail.

SOURCE TERMS:
property
random testing
test case
generator
counterexample
specification

WHAT BECAME STRANGE:
A static invariant is passive prose.

A generative invariant contains:

a claim
+
a space of perturbations
+
an evaluator.

It is therefore capable of attacking every future implementation.

Example:

PROPERTY:
HOUSE_IDENTITY_PERSISTS.

GENERATOR:
randomly vary

weather
camera
time
occupants
lighting
distance
season.

TEST:
identity remains invariant.

One sentence has become an experimental machine.

QUESTION:
Should every accepted prompt constraint be compiled into a generator of adversarial cases?

DEEPER QUESTION:
Could a prompt repository become executable scholarship in which claims continuously manufacture attempts to falsify themselves?

MECHANISM:
Property-based testing separates:

PROPERTY

from

EXAMPLES.

A generator supplies many values satisfying the input domain.

The property is checked repeatedly.

When a counterexample appears, it becomes evidence against the implementation or the property.

FORMAL SHIFT:
FROM:

INVARIANT:
“X should remain stable.”

TO:

PROPERTY P(x)

+
GENERATOR G → {x₁,x₂,...}

+
CHECK:

∀x generated,
P(x).

For generative systems:

TRANSFORMATION GENERATOR
→ prompt variants
→ generations
→ invariant evaluator.

SOURCE FORMALISM:
[PARAPHRASE]

QuickCheck represents properties as executable Haskell expressions and automatically evaluates them across generated test inputs.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

PROMPT PROPERTY:

PROP =
{
  invariant I,
  perturbation generator G,
  evaluator E
}

For pᵢ ~ G(P):

oᵢ = MODEL(pᵢ)

FAIL if:

E(I,oᵢ) = false.

A zettel TEST can therefore become:

TEST GENERATOR

rather than one manually described experiment.

TENSION:
Random generation is not automatically useful exploration.

A badly designed generator can produce thousands of easy cases and never touch the boundary where the system fails.

This creates a direct bridge to:

[[PROMPT-PRACTICE-DISAGREEMENT-003]]

which prefers informative cases,

and:

[[PROMPT-PRACTICE-DELTA-001]]

which minimizes discovered failures.

MISSING:
Generators for natural-language variations that preserve intended semantics.

Evaluators for aesthetic, causal, spatial, and narrative invariants.

A distinction between valid perturbations and transformations that accidentally change the requirement itself.

BOUNDARY:
QuickCheck tests conventional executable programs against explicitly encoded properties.

Prompt properties often depend on stochastic model behavior and human judgment.

The transfer therefore requires probabilistic or graded property evaluation.

CITATION TRAIL:
[[SON-IEC-005-A]]
→ exploration over candidate space

[[SON-CONTROL-003]]
→ control dimensions become separable

→ QuickCheck
→ properties generate test cases
→ accepted prompt constraints become executable adversaries
→ FORAGE TEST becomes a recursion engine rather than terminal question

TEST:
Take ten accepted invariants from an existing prompt workflow.

For each create:

PROPERTY
PERTURBATION GENERATOR
EVALUATOR.

Run at least 30 automatically varied cases per property.

Every failure becomes:

counterexample
→ shrink
→ new zettel
→ revised property
→ regenerated tests.

The successful end state is not:

NO FAILURES.

It is:

EVERY PROPERTY CAN CONTINUE PRODUCING NEW ATTEMPTS TO BREAK IT.

PLATFORM:
ACM ICFP

LINKS:
[[SON-IEC-005-A]]
[[SON-CONTROL-003]]

BIBTEX:
@inproceedings{claessen2000quickcheck,
  author = {Koen Claessen and John Hughes},
  title = {QuickCheck: A Lightweight Tool for Random Testing of Haskell Programs},
  booktitle = {Proceedings of the Fifth ACM SIGPLAN International Conference on Functional Programming},
  pages = {268--279},
  year = {2000},
  doi = {10.1145/351240.351266},
  url = {https://doi.org/10.1145/351240.351266}
}
