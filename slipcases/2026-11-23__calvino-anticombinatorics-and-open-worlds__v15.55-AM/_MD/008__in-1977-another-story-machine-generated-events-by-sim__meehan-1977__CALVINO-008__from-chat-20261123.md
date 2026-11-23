ZETTEL

ID: CALVINO-008

TITLE:
In 1977, another story machine generated events by simulating a world instead of filtering completed plots.

SOURCE:
James R. Meehan — "TALE-SPIN, An Interactive Program that Writes Stories" — IJCAI (1977), pp. 91–97.

PASSAGE:
[PARAPHRASE]
TALE-SPIN generates stories through problem-solving procedures, assertions about the current world, and inferences about event consequences. Characters pursue goals, and their actions change the conditions for subsequent actions.

RESEARCH OBJECT:
A contemporaneous computational genealogy based on world simulation rather than combinatorial elimination.

LOCAL MOVE:
Meehan makes the story an observable trace of characters attempting to solve problems within a simulated environment.

SOURCE TERMS:
"problem solver"; "assertion mechanism";
"inference mechanism"; "goals"; "subgoals";
"problem domains."

WHAT BECAME STRANGE:
The historical contrast need not be Calvino's explicit combinatorics versus today's statistical generation. A substantially different architecture for computer-generated narrative was already documented in the same year as Calvino's Centre Pompidou presentation.

QUESTION:
Why compare contemporary generative AI chiefly with Calvino's anticombinatorics when earlier computational storytelling also explored world simulation and causal inference?

DEEPER QUESTION:
Should the history of AI narrative be organized around different representations of story, rather than successive increases in computational power?

MECHANISM:
An agent has a goal. A solver selects actions or subgoals. Events update world memory. Inferences establish further consequences and possibly new goals.

FORMAL SHIFT:
Character goal
→ world-state representation
→ [problem solving and causal inference]
→ updated world and narrative events.

SOURCE FORMALISM:
Problem solver.
Assertion mechanism.
Inference mechanism.
Stored descriptions of physical and social state.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Goal g
→ action a
→ state update S'
→ inferred consequences E
→ new goals g'

The story is a trace of state transitions, not a surviving member of an explicitly enumerated plot inventory.

TENSION:
TALE-SPIN could generate causally motivated events while producing awkward or uninteresting stories. Causal correctness and literary value remained separate problems.

MISSING:
Evidence of direct exchanges between Meehan and Calvino–Braffort. A controlled comparison of their actual programs.

BOUNDARY:
Contemporaneity does not establish influence. TALE-SPIN's architecture should not be projected backward onto Calvino's work.

CITATION TRAIL:
Meehan (1977).
Meehan, The Metanovel (1976).
Schank and Abelson on scripts and plans.
Dehn (1981).

TEST:
Give TALE-SPIN-style world simulation and Calvino-style filtering identical characters, actions, and starting conditions. Compare what each can produce without adding new representations.

PLATFORM:
[[Alternative Genealogies of AI Story Generation]]

LINKS:
[[CALVINO-003]]
[[CALVINO-005]]
[[CALVINO-009]]
[[CALVINO-016]]

BIBTEX:
@inproceedings{meehan1977talespin,
  author    = {Meehan, James R.},
  title     = {TALE-SPIN, An Interactive Program that Writes Stories},
  booktitle = {Proceedings of the Fifth International Joint Conference on Artificial Intelligence},
  pages     = {91--97},
  year      = {1977},
  url       = {https://ijcai.org/proceedings/1977/17}
}
