ZETTEL

ID:
Z-OPLANG-MELT02-06

TITLE:
Negative specification can steer without ever becoming explicit specification.

SOURCE:
Michael Polanyi — The Tacit Dimension — University of Chicago Press reissue, 2009; originally published 1966.

SOURCE URL:
https://press.uchicago.edu/ucp/books/book/chicago/T/bo6035368.html

PASSAGE:
[QUOTE]
“we can know more than we can tell”

RESEARCH OBJECT:
<TACIT STEERING>.

Our earlier “negative specification” zettel assumed that repeated rejection progressively externalizes the evaluator’s criterion.

Polanyi opens a more difficult possibility:

successful discrimination may persist without the criterion becoming articulable.

LOCAL MOVE:
Polanyi uses tacit knowledge to challenge accounts of knowledge that equate possession with explicit statement.

SOURCE TERMS:
“tacit”
“know”
“tell”
“tradition”
“practices”
“implied values”
“prejudgments”

WHAT BECAME STRANGE:
“No, not that” may not be a primitive stage on the way to a fully expressible rule.

It may itself be the form in which some knowledge remains available.

Then:

<rejection>
does not necessarily
[extract hidden specification].

It may simply allow an external process to be steered by a discriminatory competence that never becomes propositionally explicit.

QUESTION:
Can a generative system be reliably directed by human judgment whose operative criterion never becomes articulable?

DEEPER QUESTION:
If a model learns to anticipate a person’s selections more accurately than that person can explain them, where does the specification reside?

MECHANISM:
<human>
possesses <discriminatory competence>.

<candidate>
[elicits]
<accept / reject / comparison>.

Feedback
[changes]
<future candidate distribution>.

Yet:

<explicit criterion>

may remain absent.

Interaction improves without articulation necessarily increasing.

FORMAL SHIFT:
<TACIT CRITERION>
→ <FAILURE>
→ [ARTICULATE]
→ <EXPLICIT SPECIFICATION>

becomes:

<TACIT DISCRIMINATION>
→ [SELECT / REJECT]
→ <ADAPTIVE STEERING>
→ [SELECT / REJECT]
→ ...

with no required terminal explicit rule.

SOURCE FORMALISM:
NONE.

Polanyi’s claim concerns tacit knowing, not generative systems.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

J(x) = human discriminatory judgment over candidate x.

Assume no known explicit function C such that the human can state:

J(x) = C(x).

A learning system may nevertheless approximate:

J_hat(x)

from repeated selections.

Then steering can converge while articulation remains low.

This creates three distinct quantities:

D = discrimination ability
A = articulation ability
P = predictive learnability of judgments

The field currently assumes too readily that D → A.

TENSION:
Polanyi’s philosophical claim does not prove that tacit criteria are formally irreducible.

A sufficiently rich model might infer regularities from behavior that the person cannot verbalize.

But inferred predictability is not obviously equivalent to the person’s own theory or reason.

MISSING:
The distinction between:
- stable tacit criterion,
- momentary preference,
- post-hoc rationalization,
- learned behavioral mimicry,
- genuine articulation.

BOUNDARY:
The source does not establish that aesthetic judgment is permanently ineffable.

It pressures the assumption that successful iterative refinement necessarily culminates in explicit specification.

CITATION TRAIL:
Polanyi — tacit knowing.
Ryle — knowing how.
Schön — reflection-in-action.
Preference elicitation.
Interactive evolutionary computation.
Reward modeling from human preferences.

TEST:
Ask participants to iteratively select among generated alternatives while preventing explanatory feedback.

Separately collect their explicit verbal criteria.

Train a model only on selections.

Then test:
A. prediction of future choices,
B. transfer to novel cases,
C. participant ability to explain choices,
D. agreement between inferred predictors and stated rules.

If A/B rise while C remains low, the process is better described as tacit steering than specification extraction.

PLATFORM:
[[Deferred Formalization]]

LINKS:
[[Negative Specification]]
[[Tacit Criterion]]
[[Judgment as Operation]]

BIBTEX:
@book{polanyi2009tacit,
  author = {Polanyi, Michael},
  title = {The Tacit Dimension},
  publisher = {University of Chicago Press},
  year = {2009},
  note = {Originally published 1966; reissue with foreword by Amartya Sen}
}
