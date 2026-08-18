ZETTEL

ID:
PROMPT-PRACTICE-METAMORPHIC-002

TITLE:
WHEN YOU CANNOT SAY WHAT THE RIGHT OUTPUT IS, SAY WHAT MUST REMAIN TRUE WHEN THE PROMPT CHANGES.

SOURCE:
T. Y. Chen, S. C. Cheung & S. M. Yiu — “Metamorphic Testing: A New Approach for Generating Next Test Cases” — HKUST Technical Report HKUST-CS98-01, 1998.

SOURCE URL:
https://arxiv.org/abs/2002.12543

PASSAGE:
[QUOTE]
“The availability of test oracles is pragmatically unattainable in most situations.”

RESEARCH OBJECT:
METAMORPHIC PROMPTING.

The user may be unable to specify the correct artifact.

But the user may still know how two artifacts SHOULD RELATE.

LOCAL MOVE:
[[SON-CONTROL-003]] split generative control into independently manipulable dimensions.

[[SON-PROMPTSEMANTICS-007]] showed that apparently similar linguistic changes may have different operational effects.

Metamorphic testing suggests that a prompt practice should therefore test RELATIONS rather than only outputs.

SOURCE TERMS:
metamorphic testing
test oracle
successful test case
follow-up test case
metamorphic relation
source test case

WHAT BECAME STRANGE:
A specification does not need to say:

THE ANSWER MUST BE X.

It can say:

IF I CHANGE A INTO B,
THEN PROPERTY C MUST REMAIN INVARIANT.

This is especially powerful for generative systems where exact outputs are neither predictable nor desirable.

Examples:

move camera
→ identity remains

translate prompt
→ substantive constraint remains

change season
→ house geometry remains

increase age
→ person identity remains

remove one object
→ unrelated objects remain

reverse chronology
→ causal dependencies update coherently.

The specification lives BETWEEN outputs.

QUESTION:
Can prompt reliability be specified primarily through relations among generations rather than through target generations?

DEEPER QUESTION:
Does natural-language programming need a semantics of TRANSFORMATIONAL INVARIANTS more than a semantics of exact outputs?

MECHANISM:
Begin with a source prompt P.

Apply controlled transformation T:

P' = T(P)

Generate:

O = G(P)
O' = G(P').

Instead of asking whether O or O' is globally correct, evaluate a relation:

R(O, O').

For example:

SAME_IDENTITY(O,O')
SAME_LAYOUT(O,O')
ONLY_COLOR_CHANGED(O,O')
CAUSAL_ORDER_PRESERVED(O,O').

FORMAL SHIFT:
FROM:

PROMPT
→ OUTPUT
→ IS OUTPUT CORRECT?

TO:

PROMPT P
→ OUTPUT O

TRANSFORM(P)
→ P'
→ OUTPUT O'

TEST:

R(O,O') ?

The executable specification becomes a relation over generations.

SOURCE FORMALISM:
[PARAPHRASE]

Metamorphic testing derives follow-up test cases from existing executions and checks necessary relations among their outputs rather than requiring a conventional oracle for every individual result.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

METAMORPHIC PROMPT PROPERTY:

T : P → P'

R : O × O' → {PASS, FAIL}

TEST(P,T,R):

O  = G(P)
O' = G(T(P))

return R(O,O').

Example:

T = CHANGE_CAMERA_ANGLE

R =
IDENTITY(O) = IDENTITY(O')
AND
OBJECT_SET(O) = OBJECT_SET(O').

TENSION:
A relational test can pass while both outputs are bad.

For example:

two generations may preserve identity perfectly while depicting the wrong person.

Metamorphic relations therefore supplement rather than replace all direct evaluation.

MISSING:
A vocabulary of metamorphic relations suitable for:

text
image
video
code
world models
interactive systems
multimodal artifacts.

A method for distinguishing intended change from collateral change.

A way to infer useful metamorphic relations from correction histories.

BOUNDARY:
The source concerns software testing.

Generative media may not have deterministic relations even when behavior is acceptable.

Relations may therefore need tolerances, distributions, or human judgment rather than Boolean equality.

CITATION TRAIL:
[[SON-CONTROL-003]]
→ control consists of separable dimensions

[[SON-PROMPTSEMANTICS-007]]
→ words have model-specific operational effects

→ metamorphic testing
→ correct answer unavailable
→ constrain relations among executions instead
→ PROMPT PRACTICE becomes transformation + invariant + comparison

TEST:
Take one accepted artifact.

Write five transformations that SHOULD alter exactly one dimension.

For each transformation define:

EXPECTED CHANGE
EXPECTED INVARIANT.

Generate paired outputs.

Classify every observed property as:

EXPECTED CHANGE
PRESERVED INVARIANT
COLLATERAL CHANGE
AMBIGUOUS.

Any recurring collateral change becomes a new candidate zettel and a new metamorphic relation.

PLATFORM:
Hong Kong University of Science and Technology / arXiv

LINKS:
[[SON-CONTROL-003]]
[[SON-PROMPTSEMANTICS-007]]

BIBTEX:
@techreport{chen1998metamorphic,
  author = {T. Y. Chen and S. C. Cheung and S. M. Yiu},
  title = {Metamorphic Testing: A New Approach for Generating Next Test Cases},
  institution = {Hong Kong University of Science and Technology},
  number = {HKUST-CS98-01},
  year = {1998},
  url = {https://arxiv.org/abs/2002.12543}
}
