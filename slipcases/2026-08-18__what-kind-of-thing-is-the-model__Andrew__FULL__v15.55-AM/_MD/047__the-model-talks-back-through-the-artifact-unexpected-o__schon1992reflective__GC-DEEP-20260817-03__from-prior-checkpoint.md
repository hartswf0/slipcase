ZETTEL

ID:
GC-DEEP-20260817-03

TITLE:
THE MODEL TALKS BACK THROUGH THE ARTIFACT — unexpected output can reorganize the problem before the user reorganizes the prompt.

SOURCE:
Donald A. Schön — “Designing as reflective conversation with the materials of a design situation” — Knowledge-Based Systems 5(1), 1992, 3–14. SOURCE URL: https://doi.org/10.1016/0950-7051(92)90020-G

PASSAGE:
[PARAPHRASE]
Schön analyzes designing as a reflective conversation with the materials of a design situation: designers make moves, encounter consequences, and respond to what the situation gives back rather than simply executing a fully specified prior plan.

RESEARCH OBJECT:
GENERATIVE-OUTPUT-AS-BACKTALK.

LOCAL MOVE:
[[MJ-GC-005]] and [[MJ-GC-029]] are stronger when read as a reflective loop rather than an error-correction loop. The generated artifact does not merely reveal distance from intention; it introduces material consequences the user can notice, reinterpret, and incorporate into the next move.

SOURCE TERMS:
“reflective conversation”
“materials”
“design situation”
“designing”

WHAT BECAME STRANGE:
The generator can participate in design without possessing a human intention if its consequences are sufficiently legible to reorganize the designer’s next move.

QUESTION:
What makes a model-generated deviation capable of “talking back” rather than appearing as noise?

DEEPER QUESTION:
Is co-creation located in shared intention, or can it arise from a recurrent structure in which one actor’s material consequence becomes another actor’s next problem?

MECHANISM:
MOVE
→ MATERIAL CONSEQUENCE
→ NOTICE / FRAME
→ REVISED MOVE
→ new consequence.

FORMAL SHIFT:
FROM: intent → execution → correction.
TO: move → consequence → reframing → move.

SOURCE FORMALISM:
Schön’s source is an account of design activity and reflective conversation; it does not describe diffusion models or prompting.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

INTENT_{t+1} = f(INTENT_t, OUTPUT_t, INTERPRETATION_t).

The target itself is stateful.

TENSION:
Calling every surprising output “back-talk” risks romanticizing arbitrary failure. The user must possess practices for discriminating consequential surprise from irrelevant variation.

MISSING:
Observable criteria for when a surprise produces reframing rather than rejection.

BOUNDARY:
Schön supplies a design-theory analogy, not a claim that the model is a conversational subject in the human sense.

CITATION TRAIL:
[[MJ-GC-005]] → “investigate that more”
[[MJ-GC-029]] → “things that you would never think to do”
→ Schön 1992
→ artifact consequences become material for reframing.

TEST:
Code expert sessions for three responses to unexpected outputs: REJECT, CORRECT, REFRAME. Identify which visible properties predict REFRAME.

PLATFORM:
Design practice / Midjourney interpretation

LINKS:
[[MJ-GC-005]]
[[MJ-GC-029]]
[[GC-DEEP-20260817-01]]

BIBTEX:
@article{schon1992reflective,
  author={Schön, Donald A.},
  title={Designing as Reflective Conversation with the Materials of a Design Situation},
  journal={Knowledge-Based Systems},
  volume={5},
  number={1},
  pages={3--14},
  year={1992},
  doi={10.1016/0950-7051(92)90020-G},
  url={https://doi.org/10.1016/0950-7051(92)90020-G}
}
