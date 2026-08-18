ZETTEL

ID:
PROMPT-PRACTICE-DISAGREEMENT-003

TITLE:
THE BEST NEXT PROMPT MAY BE THE ONE MOST LIKELY TO MAKE YOUR EXPLANATIONS DISAGREE.

SOURCE:
H. S. Seung, M. Opper & H. Sompolinsky — “Query by Committee” — Proceedings of the Fifth Annual ACM Workshop on Computational Learning Theory, 1992.

SOURCE URL:
https://doi.org/10.1145/130385.130417

PASSAGE:
[QUOTE]
“The next query is chosen according to the principle of maximal disagreement.”

RESEARCH OBJECT:
DIAGNOSTIC PROMPT.

A prompt can be written not to obtain the desired artifact but to discriminate between competing explanations of why previous artifacts behaved as they did.

LOCAL MOVE:
[[SON-IEC-005]] made prompts part of a search policy.

[[SON-IEC-005-A]] showed that choosing the apparent closest step can be deceptive.

Query by Committee changes the objective of the NEXT PROMPT:

do not ask for the most promising output.

Ask for the experiment whose possible outputs most sharply divide your current theories.

SOURCE TERMS:
query
committee
maximal disagreement
information gain
version space
hypothesis
learner
teacher

WHAT BECAME STRANGE:
Suppose an image keeps losing a character when the camera moves.

Possible explanations:

H₁:
the prompt under-specifies persistence.

H₂:
the model cannot reliably preserve object identity.

H₃:
the word “behind” causes occlusion bias.

H₄:
context has become too long.

H₅:
the seed produces unstable composition.

The ordinary prompt writer chooses another wording hoping it works.

The experimental prompt writer chooses the next prompt according to:

WHICH PROMPT WOULD MAKE H₁…H₅ PREDICT DIFFERENT OUTCOMES?

Failure becomes hypothesis discrimination.

QUESTION:
Can prompt iteration be made dramatically more efficient by selecting the next prompt for information gain rather than artifact quality?

DEEPER QUESTION:
Should a mature prompt language contain a distinct class of prompts whose purpose is epistemic rather than productive?

MECHANISM:
Maintain a set of live explanations:

H = {h₁,h₂,...hₙ}.

For candidate probe q, estimate:

h₁(q)
h₂(q)
...
hₙ(q).

Prefer q where predicted outcomes disagree maximally.

Run q.

Observe result.

Eliminate explanations inconsistent with the observation.

FORMAL SHIFT:
FROM:

CURRENT OUTPUT
→ WRITE BETTER PROMPT
→ BETTER OUTPUT?

TO:

CURRENT FAILURE
→ ENUMERATE EXPLANATIONS
→ DESIGN DISCRIMINATING PROMPT
→ OBSERVE
→ KILL EXPLANATIONS
→ ONLY THEN REVISE PRODUCTION PROMPT

SOURCE FORMALISM:
[PARAPHRASE]

Query-by-committee methods maintain multiple hypotheses consistent with observed examples and preferentially query cases on which those hypotheses disagree.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

H = {h₁,...,hₙ}

and candidate prompt q.

Define:

DISAGREEMENT(q)
=
D(
 h₁(q),
 h₂(q),
 ...
 hₙ(q)
).

Choose:

q* = argmax_q DISAGREEMENT(q).

Then:

OBSERVE(G(q*))

and update H.

TENSION:
The smallest reproducible failure is not necessarily the most informative failure.

[[PROMPT-PRACTICE-DELTA-001]] prefers reduction.

Query by Committee prefers discrimination.

The two operations therefore answer different questions:

DELTA:
What is minimally sufficient to reproduce this behavior?

DISAGREEMENT:
Which experiment best tells us which explanation is true?

MISSING:
A practical way to generate explicit competing hypotheses during prompt work.

A disagreement metric for hypotheses expressed in natural language.

A mechanism for preventing the same model being tested from also manufacturing conveniently self-confirming hypotheses.

BOUNDARY:
Query by Committee is a supervised-learning method with a formal hypothesis space and teacher-provided labels.

Prompt debugging rarely has such a clean hypothesis class.

The transfer is therefore methodological, not a claim that prompt iteration literally implements the algorithm.

CITATION TRAIL:
[[SON-IEC-005]]
→ prompting as iterative search

[[SON-IEC-005-A]]
→ search direction can be deceptive

→ Query by Committee
→ choose queries for maximal disagreement
→ prompt becomes diagnostic experiment
→ CORRECTION follows model discrimination rather than guesswork

TEST:
For one stubborn prompt failure:

1. Write at least four mutually discriminable explanations.
2. For each explanation predict the outcome of five possible probe prompts.
3. Select the probe with the greatest predicted disagreement.
4. Execute it.
5. Eliminate contradicted explanations.
6. Repeat until one or two hypotheses survive.

Compare generations spent against ordinary trial-and-error repair.

PLATFORM:
ACM COLT

LINKS:
[[SON-IEC-005]]
[[SON-IEC-005-A]]

BIBTEX:
@inproceedings{seung1992query,
  author = {H. S. Seung and M. Opper and H. Sompolinsky},
  title = {Query by Committee},
  booktitle = {Proceedings of the Fifth Annual ACM Workshop on Computational Learning Theory},
  pages = {287--294},
  year = {1992},
  doi = {10.1145/130385.130417},
  url = {https://doi.org/10.1145/130385.130417}
}
