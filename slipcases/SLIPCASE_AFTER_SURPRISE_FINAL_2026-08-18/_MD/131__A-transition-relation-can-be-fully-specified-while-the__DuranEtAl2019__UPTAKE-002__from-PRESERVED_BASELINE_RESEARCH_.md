ZETTEL

ID:
UPTAKE-002

TITLE:
A transition relation can be fully specified while the choice of which transition to take remains a separate programmable object.

SOURCE:
Francisco Durán, Steven Eker, Santiago Escobar, Narciso Martí-Oliet, José Meseguer, Rubén Rubio, and Carolyn Talcott — “Programming and Symbolic Computation in Maude” — 2019 — §§1.1, 4.

PASSAGE:
[PARAPHRASE]
Maude rewrite theories specify potentially nondeterministic local transformations. Because many rules may be applicable and many transition sequences may be possible, Maude provides a separate strategy language for controlling which rule applications are pursued toward a goal.

RESEARCH OBJECT:
TRANSITION SEMANTICS and EXECUTION STRATEGY split.

LOCAL MOVE:
The rule system determines what transitions are possible.

A second program-like object determines which possibilities are selected.

SOURCE TERMS:
rewrite theory
rule
transition
nondeterminism
strategy
goal
rule application

WHAT BECAME STRANGE:
The parent asks whether uptake is sufficiently specified.

But “specified” itself divides:

WHAT MAY HAPPEN?
versus
WHICH POSSIBLE PATH WILL BE TAKEN?

QUESTION:
Could cultural rules be formally precise as a possibility relation while remaining radically underdetermined at the level of strategy selection?

DEEPER QUESTION:
Is the more informative cultural/computational comparison:

NORMS : STRATEGY
rather than
CULTURAL RULES : MACHINE INSTRUCTIONS?

MECHANISM:
rewrite theory R
→ set of locally permitted transitions

    Succ_R(γ)

strategy π
→ selects/orders admissible rule applications

    π(R,γ)

→ one trajectory or restricted family of trajectories.

FORMAL SHIFT:
<TRANSITION RELATION>
+
<CONTROL STRATEGY>
→ <EXECUTION PATH>

SOURCE FORMALISM:
A Maude program can be a rewrite theory:

    R = (Σ,E,R)

whose rewrite rules specify local transitions.

The strategy language separately controls rule application in nondeterministic systems.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Separate:

    Δ : Γ → P(Γ)

from:

    π : History(Γ) × Δ → P(Γ)

Then:

    Δ

defines possibility,

while:

    π

defines control over possibility.

TENSION:
Many conventional programming languages bake evaluation strategy into their semantics, making Δ and π appear to be one mechanism.

MISSING:
A cross-domain taxonomy separating:

RULE
CONSTRAINT
POLICY
STRATEGY
SCHEDULER
HEURISTIC.

BOUNDARY:
Underdetermination of next action does not imply absence of operational specification.

It may indicate that transition rules and control policy occupy different levels.

CITATION TRAIL:
[[MINIMUM-028]]
→ specified uptake
→ Maude nondeterministic rewrite theory
→ strategy language
→ rule / strategy separation.

[[MINIMUM-025]]
→ probabilistic or relational cultural transition
→ missing selection mechanism
→ strategy as new coordinate.

TEST:
Take one nondeterministic rewrite theory R.

Execute it under two strategies:

π₁
π₂.

Hold R and initial state fixed.

If outcomes differ, classify which explanatory work belongs to R and which belongs to π.

Then attempt the same decomposition for one ethnographic rule system.

PLATFORM:
[[description-becomes-operation]]

LINKS:
[[MINIMUM-028]]
[[MINIMUM-025]]
[[transition-vs-strategy]]
[[nondeterminism]]
[[cultural-strategy]]

BIBTEX:
@article{DuranEtAl2019,
  author  = {Dur{\'a}n, Francisco and Eker, Steven and Escobar, Santiago and Mart{\'i}-Oliet, Narciso and Meseguer, Jos{\'e} and Rubio, Rub{\'e}n and Talcott, Carolyn},
  title   = {Programming and Symbolic Computation in Maude},
  journal = {arXiv preprint arXiv:1910.08416},
  year    = {2019}
}
