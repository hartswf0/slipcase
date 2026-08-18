ZETTEL

ID:
RETENTION-005-Y-E

TITLE:
A creative assistant need not infer what the artist wants; it can preserve the artist’s capacity to decide later.

SOURCE:
Yuqing Du, Stas Tiomkin, Emre Kiciman, Daniel Polani, Pieter Abbeel, and Anca Dragan — “AvE: Assistance via Empowerment” — NeurIPS 2020.

PASSAGE:
[PARAPHRASE]
AvE challenges assistance that begins by inferring a user goal and instead proposes increasing the human’s ability to control the environment, preserving autonomy across multiple possible later goals.

RESEARCH OBJECT:
OPTION-PRESERVING CREATIVE ASSISTANCE.

LOCAL MOVE:
When intention is ambiguous, do not necessarily guess it; preserve future human action capacity.

SOURCE TERMS:
assistance
empowerment
autonomy
goal ambiguity
goal misspecification
control

WHAT BECAME STRANGE:
The smartest assistant may be the one that commits least aggressively on the artist’s behalf.

QUESTION:
Should generative creative systems optimize for preserving future artistic options rather than predicting the final desired image?

DEEPER QUESTION:
Could creative assistance reverse from GENERATE WHAT I THINK YOU MEAN to KEEP OPEN THE DIFFERENCES YOU MAY LATER CARE ABOUT?

MECHANISM:
goal-inference assistant guesses ĝ and collapses alternatives; empowerment assistant preserves/increases controllable futures so artist resolves goal later.

FORMAL SHIFT:
<ASSIST BY PREDICTING INTENT> → <ASSIST BY PRESERVING FUTURE AGENCY>

SOURCE FORMALISM:
AvE augments reinforcement learning with a human-empowerment objective rather than a single inferred human goal.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
Choose system intervention maximizing HumanEmpowerment(s_{t+1}) subject to explicit constraints, not only similarity to inferred goal.

TENSION:
Pure option preservation can prevent useful commitment; creative work eventually closes branches.

MISSING:
A policy deciding when assistant should PRESERVE, PROPOSE, COMMIT—and who controls transition.

BOUNDARY:
Autonomy is not leaving every possibility open forever; it is preserving meaningful options until commitment is warranted.

CITATION TRAIL:
[[RETENTION-005-N-A]] + [[RETENTION-005-Y]] → delegated freedom → AvE → preserve options rather than infer goal.

TEST:
Compare auto-completing assistant with option-preserving assistant on evolving targets; measure ability to reach later-formed intentions without restarting.

PLATFORM:
[[class-is-not-a-path]]

LINKS:
[[RETENTION-005-N-A]]
[[RETENTION-005-Y]]
[[assistance-via-empowerment]]
[[option-preservation]]
[[creative-autonomy]]

BIBTEX:
NONE
