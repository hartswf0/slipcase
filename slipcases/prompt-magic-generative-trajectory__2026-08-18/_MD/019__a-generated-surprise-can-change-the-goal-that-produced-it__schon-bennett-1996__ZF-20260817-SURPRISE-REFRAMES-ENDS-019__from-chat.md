ZETTEL

ID:
ZF-20260817-SURPRISE-REFRAMES-ENDS-019

TITLE:
A Generated Surprise Can Change the Goal That Produced It

SOURCE:
Donald A. Schön and John Bennett, “Reflective Conversation with Materials,” in Terry Winograd, ed., Bringing Design to Software, 1996.
https://hci.stanford.edu/publications/bds/9-schon.html

PASSAGE:
[PARAPHRASE] Schön describes designers making moves, encountering consequences they did not intend, and revising their understanding while continuing to work. He explicitly notes that reframing can interactively redefine both means and ends.

RESEARCH OBJECT:
[[ZF-20260817-PROMPT-NOT-UNIT-015]] allowed intention to change during a generative session.

Schön makes the mutation stronger.

The output need not merely show the artist a better WAY to reach the same goal.

It can change the GOAL.

This matters because many theories of prompting assume a hidden stable target:

human has intention I
→ tries expressions
→ eventually finds output approximating I.

But reflective practice permits:

I₀
→ action
→ surprising result
→ reinterpretation
→ I₁.

The destination is partly produced by traveling.

LOCAL MOVE:
Replace:

ITERATION =
error correction toward fixed target

with:

ITERATION =
conversation in which outputs can redefine both means and ends.

SOURCE TERMS:
reflection in action
surprise
knowing in action
experiment
move
consequences
reframing
means
ends

WHAT BECAME STRANGE:
A “failure” can be the event that reveals what the work should become.

If the practitioner could have perfectly specified the final artifact before beginning, the most important generative discovery might never occur.

The underspecification condemned as lack of control may be the condition that allows the problem itself to move.

QUESTION:
How often does a generative output solve the user’s stated problem, and how often does it cause the user to replace that problem with another one?

DEEPER QUESTION:
If the end of a creative process is partly constituted by events inside the process, where can artistic intention be located without projecting the endpoint backward in time?

MECHANISM:
INTENTION₀
→ MOVE
→ RESULT
→ SURPRISE
→ ATTENTION
→ REFRAME
→ INTENTION₁
→ NEW MOVE.

The generative artifact participates in reformulating the task.

FORMAL SHIFT:
OPTIMIZATION:

find x maximizing J₀(x)

becomes:

REFLECTIVE SEARCH:

generate xₜ
→ encounter xₜ
→ transform Jₜ
→ generate under Jₜ₊₁.

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Ordinary target model:

x* = argmax_x J(x)

with fixed J.

Reflective generative model:

xₜ ~ G(aₜ)

Jₜ₊₁ = R(Jₜ, xₜ, surpriseₜ)

aₜ₊₁ = π(Jₜ₊₁, xₜ).

Thus:

THE EVALUATION FUNCTION ITSELF CHANGES.

The artist is not merely searching a possibility space.

The criteria defining valuable possibilities are being reconstructed during search.

TENSION:
One interpretation:

This is genuine reflective design.

Another:

The practitioner is merely rationalizing whatever attractive accident the model happened to produce.

Both create changing goals.

The difference is whether the practitioner can demonstrate discriminating, cumulative transformation rather than passive acceptance.

MISSING:
Operational criteria separating:

REFRAMING
from
POST-HOC RATIONALIZATION.

Both can produce a story in which the final result seems meaningful.

BOUNDARY:
Schön’s account concerns skilled design practice and does not establish that every generative interaction counts as reflection-in-action.

Surprise alone is insufficient.

The practitioner must respond to surprise in a way that restructures subsequent doing.

CITATION TRAIL:
[[ZF-20260817-PROMPT-NOT-UNIT-015]]
[[ZF-20260817-DOCUMENTARY-MODE-012]]
→ generative trajectory allows intention to change
→ Schön: surprise can provoke reflection during action
→ reframing can transform both means and ends
→ new object: MODEL OUTPUT AS PROBLEM-REFRAMING EVENT
→ next edge: discriminate reflective revision from opportunistic rationalization

TEST:
Before each generation, require practitioners to state:

CURRENT GOAL
CURRENT CONSTRAINTS
EXPECTED FAILURE
SUCCESS CRITERIA.

After each generation, record whether any of those changed and why.

Blind independent coders classify changes as:

ERROR CORRECTION
MEANS REVISION
END REVISION
UNRELATED DRIFT
POST-HOC JUSTIFICATION.

Compare experts and novices.

If experts exhibit coherent end-revision triggered by interpretable surprises, generative skill includes reframing rather than mere target pursuit.

PLATFORM:
design practice
generative AI
iterative creative systems

LINKS:
[[ZF-20260817-PROMPT-NOT-UNIT-015]]
[[ZF-20260817-DOCUMENTARY-MODE-012]]
[[REFLECTION-IN-ACTION]]
[[GENERATIVE-SURPRISE]]
[[ENDOGENOUS-GOALS]]
[[DEFERRED-FORMALIZATION]]

BIBTEX:
@incollection{schon1996reflective,
  author={Schön, Donald A. and Bennett, John},
  title={Reflective Conversation with Materials},
  booktitle={Bringing Design to Software},
  editor={Winograd, Terry},
  year={1996},
  pages={171--189},
  doi={10.1145/229868.230044},
  url={https://hci.stanford.edu/publications/bds/9-schon.html}
}
