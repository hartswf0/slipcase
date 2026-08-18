ZETTEL

ID:
PROMPT-PRACTICE-DELTA-001

TITLE:
WHEN A PROMPT FAILS, REMOVE WORDS BEFORE ADDING THEM.

SOURCE:
Andreas Zeller & Ralf Hildebrandt — “Simplifying and Isolating Failure-Inducing Input” — IEEE Transactions on Software Engineering 28(2), 2002.

SOURCE URL:
https://doi.org/10.1109/32.988498

FULL TEXT:
https://www.cs.columbia.edu/~junfeng/08fa-e6998/sched/readings/delta-debug-input.pdf

PASSAGE:
[QUOTE]
The algorithm “simplifies the failing test case to a minimal test case that still produces the failure.”

RESEARCH OBJECT:
MINIMAL FAILING PROMPT.

Prompt practice usually reacts to failure by ACCRETION:

bad output
→ add explanation
→ add prohibition
→ add example
→ add exception
→ add another paragraph.

Delta Debugging suggests the inverse operation.

When a prompt reliably produces a failure, first ask:

WHAT IS THE SMALLEST VERSION OF THIS PROMPT THAT STILL PRODUCES THE FAILURE?

LOCAL MOVE:
[[SON-IEC-005]] made prompt craft an iterative search policy rather than a single sentence.

[[SON-IEC-005-A]] made stepping-stone selection consequential.

Delta Debugging adds another operation to that loop:

REDUCTION.

The failure is not merely something to correct.

It can be experimentally compressed until the smallest failure-inducing condition becomes visible.

SOURCE TERMS:
failure-inducing input
minimal test case
simplification
isolation
difference
passing test case
failing test case
1-minimality
successive testing

WHAT BECAME STRANGE:
A long prompt failure may contain almost no useful information precisely because too many variables changed at once.

The valuable artifact may be not the improved prompt but the tiny prompt fragment that still breaks the behavior.

That fragment is simultaneously:

a counterexample
a diagnostic probe
a newly discovered constraint
and a reusable regression test.

The normal instinct—

MAKE THE PROMPT MORE SPECIFIC

—can therefore destroy evidence.

QUESTION:
Can prompt failures be systematically reduced to minimal failure-inducing linguistic fragments?

DEEPER QUESTION:
Is the smallest prompt that reproduces a failure a better unit of specification than the correction written after the failure?

MECHANISM:
Start with:

P_fail

Partition its clauses, examples, adjectives, formatting instructions, context, and constraints.

Repeatedly remove subsets.

If:

MODEL(P_reduced)
still exhibits FAILURE F

continue reducing.

Stop when removing any remaining component causes F to disappear.

The result is a locally minimal failure-inducing prompt.

FORMAL SHIFT:
FROM:

FAILURE
→ ADD CONSTRAINT
→ BIGGER PROMPT

TO:

FAILURE
→ DELETE CONTEXT
→ REEXECUTE
→ PRESERVE FAILURE
→ DELETE AGAIN
→ MINIMAL COUNTEREXAMPLE
→ THEN FORMULATE CONSTRAINT

SOURCE FORMALISM:
[PARAPHRASE]

Zeller and Hildebrandt define ddmin as a procedure that repeatedly tests subsets and complements of a failing configuration until reaching a 1-minimal failing configuration, where removing any individual remaining element makes the failure disappear.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

P = {c₁, c₂, ... cₙ}

where cᵢ are prompt components.

Define:

FAIL(P) = true

Seek P* ⊆ P such that:

FAIL(P*) = true

and for every cᵢ ∈ P*:

FAIL(P* − {cᵢ}) = false.

Then:

P*

is a MINIMAL FAILING PROMPT.

TENSION:
Minimality and informativeness are not identical.

A tiny failure may reveal exactly which words trigger behavior.

But another, larger counterexample might discriminate more strongly between competing explanations.

This places Delta Debugging in productive tension with query-selection methods that maximize information rather than minimize input.

MISSING:
A principled decomposition of natural-language prompts into removable units.

Possible units include:

token
phrase
sentence
example
constraint
role
formatting instruction
context document
tool result
conversation turn.

Prompt behavior is also stochastic, so FAIL cannot always be treated as binary.

BOUNDARY:
Delta Debugging assumes an executable test oracle capable of deciding whether failure persists.

Many generative failures are graded, subjective, stochastic, or only visible after human inspection.

The technique therefore transfers only when FAILURE can be made sufficiently repeatable and legible.

CITATION TRAIL:
[[SON-IEC-005]]
→ iterative prompt search

[[SON-IEC-005-A]]
→ search decisions determine reachable discoveries

→ Zeller & Hildebrandt
→ minimize failure-inducing circumstances
→ MINIMAL FAILING PROMPT
→ corrections can be grounded in isolated causes rather than accumulated prose

TEST:
Choose one prompt from a prompt genealogy that repeatedly produces a recognizable failure.

Freeze:

model
system instructions
temperature
seed where available
tool state.

Decompose the prompt into clauses.

Apply ddmin-style deletion.

For every candidate prompt, run multiple generations and estimate failure frequency.

Stop when no remaining clause can be removed without materially reducing the failure.

Compare:

ORIGINAL PROMPT
MINIMAL FAILING PROMPT
CORRECTED PROMPT.

Ask whether the minimal form exposes a constraint that was obscured in the original correction.

PLATFORM:
IEEE Transactions on Software Engineering

LINKS:
[[SON-IEC-005]]
[[SON-IEC-005-A]]

BIBTEX:
@article{zeller2002simplifying,
  author = {Andreas Zeller and Ralf Hildebrandt},
  title = {Simplifying and Isolating Failure-Inducing Input},
  journal = {IEEE Transactions on Software Engineering},
  volume = {28},
  number = {2},
  pages = {183--200},
  year = {2002},
  doi = {10.1109/32.988498},
  url = {https://doi.org/10.1109/32.988498}
}
