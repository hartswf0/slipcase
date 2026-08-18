ZETTEL

ID:
ZF-20260817-PLAN-AS-RESOURCE-018

TITLE:
The Prompt May Be a Plan Used Inside Action, Not a Script Executed Before It

SOURCE:
Lucy A. Suchman, Human-Machine Reconfigurations: Plans and Situated Actions, 2nd ed., Cambridge University Press, 2006, Chapter 6, “Situated Actions.”
https://www.cambridge.org/core/books/humanmachine-reconfigurations/situated-actions/F4AA82303887FF0875BD656977661875

PASSAGE:
[PARAPHRASE] Suchman situates plans inside ongoing practical activity: they can operate prospectively and retrospectively, but purposeful action cannot simply be identified with execution of an antecedent plan.

RESEARCH OBJECT:
[[ZF-20260817-PROMPT-NOT-UNIT-015]] asked whether the prompt is merely the most visible residue of a longer generative trajectory.

Suchman gives the distinction sharper teeth.

The mistake may not be:

WE STUDIED THE WRONG KIND OF PROMPT.

It may be:

WE MISTOOK A PLAN FOR THE ACTION.

A prompt can matter enormously without containing the creative process.

It can orient activity.
It can establish a direction.
It can become a resource for judging what happens.
It can be revised.
It can later become an account of what the artist claims they were doing.

None of those functions require the subsequent trajectory to be execution of the prompt.

LOCAL MOVE:
Replace:

PROMPT = INSTRUCTION FOR ARTIFACT

with:

PROMPT =
PROSPECTIVE RESOURCE
within
SITUATED GENERATIVE ACTION.

SOURCE TERMS:
plans
situated actions
purposeful action
practical deliberation
ongoing activity
projective account
retrospective account

WHAT BECAME STRANGE:
The same prompt can exist in three temporal roles:

BEFORE:
a projection of what the practitioner thinks they might do.

DURING:
a resource against which unfolding outputs are interpreted.

AFTER:
a compressed retrospective explanation of what happened.

These roles are usually collapsed into one object called “the prompt.”

QUESTION:
When researchers collect the final prompt, are they observing the cause of the work or a retrospective account reconstructed after the work changed?

DEEPER QUESTION:
How much apparent prompt intentionality is produced after generation by narrating a contingent trajectory as though it had been planned from the beginning?

MECHANISM:
INITIAL PLAN
→ SITUATED ACTION
→ UNEXPECTED CONDITIONS
→ LOCAL RESPONSE
→ REVISED PLAN
→ FURTHER ACTION
→ RETROSPECTIVE ACCOUNT.

FORMAL SHIFT:
PLAN
→ EXECUTION

becomes:

PLAN₀
↘
SITUATION₀
→ ACTION₀
→ SITUATION₁
→ PLAN₁
→ ACTION₁
→ ...

The plan participates without determining the sequence.

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

pₜ = articulated prompt/plan at time t
sₜ = encountered generative state
aₜ = situated user action

Then:

aₜ = f(pₜ, sₜ, history)

and:

pₜ₊₁ = g(pₜ, sₜ, aₜ).

Therefore the prompt is itself modified by the consequences of action.

A final prompt pₙ cannot be assumed to represent:

p₀

or to have caused the full trajectory that produced it.

TENSION:
Suchman does not imply that plans are useless.

The inversion is subtler:

plans matter,
but not necessarily because action is their execution.

This leaves two live generative-AI cases:

PROMPT-DOMINANT TASK:
the artifact substantially realizes a stable antecedent specification.

SITUATED TASK:
the specification itself changes through encounters with generated material.

MISSING:
Time-stamped prompt histories showing when the practitioner first articulated each element of the eventual result.

Without this, final prompts can create an illusion of foresight.

BOUNDARY:
Suchman’s analysis concerns purposeful human action and human-machine interaction broadly, not generative image systems.

Applying it to prompting is an analytical extension, not a claimed historical influence.

CITATION TRAIL:
[[ZF-20260817-PROMPT-NOT-UNIT-015]]
→ final prompt may conceal operational history
→ Suchman: plans are resources within situated activity rather than exhaustive prescriptions
→ new distinction: PROMPT-AS-PLAN versus PROMPT-AS-SCRIPT
→ next edge: determine whether final prompts are prospective causes or retrospective rationalizations

TEST:
For 100 completed generative artworks, preserve:

initial brief
every intermediate prompt
every generated candidate
every user operation
final prompt
post-hoc artist explanation.

For each feature visible in the final artwork, identify the first moment it became:

INTENDED
ARTICULATED
GENERATED
NOTICED
RETAINED.

If many important features are generated before they are articulated, the final prompt is partly retrospective rather than fully prospective.

PLATFORM:
situated action
human-machine interaction
generative workflows

LINKS:
[[ZF-20260817-PROMPT-NOT-UNIT-015]]
[[PROMPT-AS-PLAN]]
[[SITUATED-GENERATION]]
[[GENERATIVE-TRAJECTORY]]
[[RETROSPECTIVE-INTENTIONALITY]]

BIBTEX:
@book{suchman2006reconfigurations,
  author={Suchman, Lucy A.},
  title={Human-Machine Reconfigurations: Plans and Situated Actions},
  edition={2},
  publisher={Cambridge University Press},
  year={2006},
  url={https://www.cambridge.org/core/books/humanmachine-reconfigurations/situated-actions/F4AA82303887FF0875BD656977661875}
}
