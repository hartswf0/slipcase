ZETTEL

ID:
PROMPT-PRACTICE-ORACLE-007

TITLE:
CEGIS HAS AN ORACLE; PROMPTING HAS AN ORACLE THAT CAN CHANGE ITS MIND.

SOURCE:
Susmit Jha & Sanjit A. Seshia — “A Theory of Formal Synthesis via Inductive Learning” — 2015/2016.

SOURCE URL:
https://arxiv.org/abs/1505.03953

PASSAGE:
[QUOTE]
OGIS captures synthesizers that “operate by iteratively querying an oracle.”

RESEARCH OBJECT:
MUTATING ORACLE.

The describe → generate → inspect → correct loop resembles formal inductive synthesis only until the HUMAN EVALUATOR changes what counts as correct.

LOCAL MOVE:
[[SON-IEC-005]] treated the human as the subjective evaluator inside iterative generation.

[[SON-IEC-005-C]] showed that history changes later search.

Formal synthesis provides a useful opposition because its oracle operates relative to a specification-learning problem.

Prompt practice can violate that assumption:

the candidate artifact can teach the oracle a distinction.

The evaluator changes while evaluating.

SOURCE TERMS:
formal synthesis
formal specification
oracle-guided inductive synthesis
oracle
candidate programs
examples
counterexamples
memory

WHAT BECAME STRANGE:
In a conventional oracle-guided picture:

candidate
→ oracle judges
→ candidate changes.

In reflective prompting:

candidate
→ human judges
→ HUMAN'S CRITERIA CHANGE
→ candidate changes.

Thus both sides of the relation can update.

The prompt loop is not simply:

LEARN PROGRAM FROM SPECIFICATION.

It may be:

LEARN PROGRAM
WHILE LEARNING SPECIFICATION.

QUESTION:
What theory of synthesis applies when the oracle's judgment function changes because of the candidates it is judging?

DEEPER QUESTION:
Is deferred formalization fundamentally a CO-LEARNING problem in which artifact and specification emerge together?

MECHANISM:
Formal inductive synthesis:

SPECIFICATION
→ oracle interaction
→ candidate
→ counterexample
→ revised candidate.

Reflective prompting:

S_t
→ candidate A_t
→ human encounter
→ S_t+1
→ revised prompt
→ A_t+1.

The evaluation function itself becomes state-dependent.

FORMAL SHIFT:
FROM:

fixed oracle:

O(candidate) → judgment

TO:

stateful oracle:

(O_t, candidate_t)
→ judgment_t
→ O_t+1.

SOURCE FORMALISM:
[PARAPHRASE]

Jha and Seshia formalize OGIS as iterative learning through oracle queries and analyze how kinds of counterexamples and learner memory affect synthesis power.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

FIXED-ORACLE SYNTHESIS:

C_t
→ O
→ e_t
→ C_t+1

where O is invariant.

DEFERRED-FORMALIZATION LOOP:

C_t
→ O_t
→ e_t

and:

O_t+1 =
UPDATE(O_t, C_t, e_t).

Therefore:

candidate state
AND
evaluation state

co-evolve.

TENSION:
Human evaluators can change for uninteresting reasons:

fatigue
novelty seeking
inconsistency
anchoring.

Not every changed criterion is specification discovery.

The challenge is to distinguish LEARNING WHAT MATTERS from preference noise.

MISSING:
A representation of evaluator state.

A taxonomy of oracle change.

A test separating:

previously implicit criterion becoming explicit
new criterion genuinely discovered
criterion merely drifting.

A comparison with coevolutionary and interactive synthesis frameworks.

BOUNDARY:
OGIS and CEGIS as described in the source concern formal inductive synthesis.

The MUTATING ORACLE is [OUR FORMALIZATION], not source machinery.

CITATION TRAIL:
[[SON-IEC-005]]
→ human subjective evaluation inside search

[[SON-IEC-005-C]]
→ history changes subsequent exploration

→ OGIS
→ iterative oracle-guided synthesis
→ oracle treated as source of examples/counterexamples
→ prompt practice differs when evaluator itself updates
→ synthesis becomes candidate/specification co-learning

TEST:
Pre-register a detailed evaluation rubric for a complex generative task.

Run 20 iterative generations.

After every generation record:

existing rubric criteria
newly articulated criterion
removed criterion
reweighted criterion
reason for change.

At the end reconstruct:

O₀
O₁
...
O₂₀.

Then rerun the same generation sequence using only O₀.

If later accepted artifacts require criteria absent from O₀, the process cannot be represented faithfully as optimization against a fixed oracle.

PLATFORM:
arXiv

LINKS:
[[SON-IEC-005]]
[[SON-IEC-005-C]]

BIBTEX:
@misc{jha2015theory,
  author = {Susmit Jha and Sanjit A. Seshia},
  title = {A Theory of Formal Synthesis via Inductive Learning},
  year = {2015},
  eprint = {1505.03953},
  archivePrefix = {arXiv},
  primaryClass = {cs.AI},
  url = {https://arxiv.org/abs/1505.03953}
}
