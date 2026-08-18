ZETTEL

ID:
RETENTION-005-D

TITLE:
“Re-rolling the dice” collapses two technically different iterative practices: blind resampling and closed-loop steering.

SOURCE:
U.S. Copyright Office — Copyright and Artificial Intelligence, Part 2: Copyrightability — January 2025 — pp. 20–21. The Office concludes that repeated prompt revision normally produces additional outputs for selection without changing the user's degree of control, while elsewhere emphasizing that control rather than mere predictability is the relevant issue.

PASSAGE:
[PARAPHRASE]
The Office characterizes repeated prompt revision as functionally similar to repeated sampling. Yet its own broader test asks whether a human can constrain or channel processing, leaving open the possibility that some iterative interfaces may support materially different forms of feedback control.

RESEARCH OBJECT:
ITERATION HAS AT LEAST TWO CAUSAL FORMS.

LOCAL MOVE:
RETENTION-005 asks whether repeated selection accumulates into authorship.

The prior classification:

ITERATE = RE-ROLL

must be split.

SOURCE TERMS:
revising prompts
control
selection
randomness
predictability
constrain
channel

WHAT BECAME STRANGE:
Two users can each make 100 generations.

USER A:
presses regenerate 100 times.

USER B:
after each output identifies one specific deviation, changes one control variable, tests whether the deviation moves, and preserves all other targeted properties.

The raw iteration count is identical.

The causal structure is not.

QUESTION:
What evidence would make iterative prompting legally distinguishable from repeated random sampling?

DEEPER QUESTION:
Could feedback control itself constitute a form of expressive execution even when no individual prompt uniquely specifies the final image?

MECHANISM:
BLIND SEARCH:

    p constant
    y_t ~ G(p,z_t)
    choose best y.

CLOSED-LOOP STEERING:

    y_t ~ G(p_t,z_t)
    e_t = Target - Observe(y_t)
    p_{t+1} = π(p_t,e_t)
    repeat.

FORMAL SHIFT:
<ITERATION COUNT>
→ {
    <RESAMPLING>,
    <FEEDBACK CONTROL>
  }

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Evidence of steering exists when targeted interventions systematically change intended variables:

    E[d(f(y_{t+1}), f*) | targeted Δp_t]
        <
    E[d(f(y_t), f*)]

while protected invariants remain stable.

TENSION:
Even sophisticated feedback may operate only by shifting probabilities rather than determining exact expressive form.

Copyright law may still require more than measurable causal influence.

MISSING:
A legal threshold translating quantitative feature control into “authorship” rather than mere influence.

BOUNDARY:
“Repeated prompting” is not a sufficiently fine-grained causal category.

Neither large N nor small N establishes control.

CITATION TRAIL:
[[RETENTION-005]]
→ repeated selection
→ USCO re-roll analysis
→ USCO simultaneously treats control as central
→ distinguish search from closed-loop steering
→ require trajectory evidence.

TEST:
Predeclare five target edits and five invariants.

For each prompt revision record:

intended change
actual change
unintended collateral change.

Compare against an equal-number random-resampling baseline.

If targeted revision produces significantly stronger conditional control, the re-roll model is incomplete.

PLATFORM:
[[class-is-not-a-path]]

LINKS:
[[RETENTION-005]]
[[feedback-control]]
[[re-rolling-dice]]
[[iteration]]
[[control-topology]]

BIBTEX:
@techreport{USCO2025Copyrightability,
  author      = {{U.S. Copyright Office}},
  title       = {Copyright and Artificial Intelligence, Part 2: Copyrightability},
  institution = {U.S. Copyright Office},
  year        = {2025}
}
