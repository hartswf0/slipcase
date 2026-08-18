ZETTEL

ID:
THEORY-1992-SCHON

TITLE:
Design intentions can evolve during the design process

SOURCE:
Donald A. Schön, "Designing as Reflective Conversation with the Materials of a Design Situation," Knowledge-Based Systems 5(1), 1992.

SOURCE URL:
https://doi.org/10.1016/0950-7051(92)90020-G

PASSAGE:
[PARAPHRASE]
Schön identifies the evolution of design intentions during designing and emphasizes reflective interaction with the consequences of design moves.

RESEARCH OBJECT:
[PARAPHRASE]
INTENTION CAN BE A VARIABLE OF THE PROCESS RATHER THAN A FIXED INPUT.

LOCAL MOVE:
Pressure [[MARTINA-2022-003]]: a correction may change the intention rather than merely improve expression of an unchanged intention.

SOURCE TERMS:
"reflective conversation"; "design intentions"; "consequences"; "moves"

WHAT BECAME STRANGE:
Fidelity to a later intention cannot automatically be used as evidence of an identical earlier intention.

QUESTION:
When Martina retains an unexpected model feature, has she recognized, discovered, or formed a preference?

DEEPER QUESTION:
Can a methodology distinguish intention evolution from increasing articulation?

MECHANISM:
Design moves create consequences; the designer appreciates consequences; subsequent moves and intentions evolve.

FORMAL SHIFT:
INTENTION_t -> MOVE -> CONSEQUENCES -> APPRAISAL -> INTENTION_t+1.

SOURCE FORMALISM:
[PARAPHRASE]
The source presents design as reflective conversation and includes evolution of intentions among phenomena a computational account must reproduce.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
I_{t+1}=UPDATE(I_t, perceived consequences of move_t).

TENSION:
Not every prompt revision signals changed intention; some are error correction under a stable goal.

MISSING:
Fine-grained longitudinal coding of retained unexpected features.

BOUNDARY:
Schön studies design, not generative AI.

CITATION TRAIL:
[[MARTINA-2022-003]] -> Schön 1992 -> intention as changing state -> recognition/formation distinction.

TEST:
Code every post-output revision as correspondence correction, criterion discovery, or criterion formation using pre-registered evidence.

PLATFORM:
Design cognition; reflective practice

LINKS:
[[MARTINA-2022-001]]
[[MARTINA-2022-003]]
[[MARTINA-2022-024]]

BIBTEX:
@article{schon1992reflective,
  author={Sch{\"o}n, Donald A.},
  title={Designing as Reflective Conversation with the Materials of a Design Situation},
  journal={Knowledge-Based Systems},
  year={1992},
  volume={5},
  number={1},
  pages={3--14},
  doi={10.1016/0950-7051(92)90020-G}
}
