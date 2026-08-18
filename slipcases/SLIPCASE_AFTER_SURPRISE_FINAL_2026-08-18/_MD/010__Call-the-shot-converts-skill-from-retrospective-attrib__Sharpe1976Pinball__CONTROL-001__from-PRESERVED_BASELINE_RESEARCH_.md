ZETTEL

ID:
CONTROL-001

TITLE:
“Call the shot” converts skill from retrospective attribution into a prospective falsifiable claim.

SOURCE:
Roger Sharpe’s 1976 New York City pinball testimony, as reconstructed in later interviews and University of Wisconsin alumni history.

PASSAGE:
[PARAPHRASE]
Sharpe’s demonstration of pinball skill involved announcing intended shots and then attempting them before the City Council. Later accounts emphasize his practice of calling trajectories in advance and his understanding of the game’s geometry and sequences.

RESEARCH OBJECT:
PROSPECTIVE SPECIFICATION is stronger evidence of control than retrospective selection.

LOCAL MOVE:
The essay’s “call the shot” test can be formalized without making it a complete theory of authorship.

SOURCE TERMS:
call the shot
skill
geometry
sequence
control
trajectory

WHAT BECAME STRANGE:
After an outcome occurs, a maker can always redescribe an attractive accident as intended.

A prospective prediction closes that loophole partially by exposing intention before the system resolves uncertainty.

QUESTION:
What exactly does successful shot-calling measure:
prediction,
control,
skill,
causal intervention,
or calibration?

DEEPER QUESTION:
How many successful counterfactual interventions are required before we can infer robust control rather than luck?

MECHANISM:
maker announces target property y*
→ acts through interface a
→ stochastic/physical system evolves
→ outcome y
→ compare y to y*
→ repeat under nearby conditions.

FORMAL SHIFT:
<RETROSPECTIVE CLAIM OF INTENTION>
→ [PRECOMMIT TARGET]
→ <FALSIFIABLE CONTROL CLAIM>
→ [SYSTEM RESPONSE]
→ <SUCCESS / FAILURE>

SOURCE FORMALISM:
NONE.

The pinball episode is a practical demonstration, not a statistical test of causal control.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

A minimal control experiment:

    declare target τ before action

    do(a)

    observe Y

    success = [Y ∈ τ].

Stronger evidence requires repeated interventions:

    P(Y ∈ τ | do(a_targeted))
        >
    P(Y ∈ τ | baseline).

TENSION:
One spectacular successful called shot can still occur by chance.

Sharpe’s historical demonstration was rhetorically persuasive without being a controlled experiment.

MISSING:
A statistical/control-theoretic version of “call the shot” suitable for generative interfaces.

BOUNDARY:
Prospective success provides evidence of control.

It does not by itself establish artistic authorship, creativity, or legal protectability.

CITATION TRAIL:
[[UPTAKE-003]]
→ counterfactual control
→ Roger Sharpe called shots
→ prospective intervention
→ control as falsifiable difference-making.

TEST:
For a generative system, define 20 nearby transformations in advance:

preserve A
change B to specified target B*
hold C within tolerance.

Record success before selection or curation.

Compare against blind sampling and post hoc cherry-picking.

PLATFORM:
[[class-is-not-a-path]]

LINKS:
[[UPTAKE-003]]
[[counterfactual-control]]
[[pinball]]
[[prospective-test]]

BIBTEX:
@misc{Sharpe1976Pinball,
  author = {Sharpe, Roger},
  title  = {Testimony concerning New York City's pinball ban},
  year   = {1976},
  note   = {Historical event; primary transcript still to be located}
}
