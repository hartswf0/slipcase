ZETTEL

ID: CALVINO-006

TITLE:
The machine becomes a character in a story whose algorithm never included it.

SOURCE:
Paul Braffort — "L'ordre dans le crime" — 1997, section 2, description of the additional plot.

PASSAGE:
[PARAPHRASE]
Waldemar's suspicion introduces Skiller and Waldemar himself into the original four-person mystery. Braffort goes further, counting two programs among the resulting eight actants, one of which may be imaginary.

RESEARCH OBJECT:
An expanding narrative ontology that incorporates its own computational machinery.

LOCAL MOVE:
Braffort distinguishes the basic combinatorial plot from an additional plot in which the investigator, his employer, and the programs become implicated in the crime.

SOURCE TERMS:
"intrigue de base"; "intrigue surajoutée";
"actants"; "programmes"; "machination."

WHAT BECAME STRANGE:
The computational model is designed for four people, but the fiction becomes interesting precisely when the machinery constructing the model enters the modeled world.

QUESTION:
Is the failure to include the investigator and programs a limitation of the algorithm, or the device that makes Calvino's story literary?

DEEPER QUESTION:
How can a narrative system represent an observer whose investigation changes the events being investigated?

MECHANISM:
The original crime generates an investigation. The investigation creates new suspicions and actions. Those actions make the investigator a participant in another possible crime.

FORMAL SHIFT:
Four-person crime model
→ investigation
→ [investigator and programs become actants]
→ expanded and recursive narrative model.

SOURCE FORMALISM:
Initial combinatorial specification:
4 characters, 12 actions.

The expanded eight-actant structure is described by Braffort, not implemented as a completed computational model.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

World W0 contains characters A–D.

Model M observes W0.
Observer O executes M.
Events implicate O and M.

W1 = W0 ∪ {O, M, new_events}

The system's representation becomes part of the world it must represent.

TENSION:
Natalie Dehn's later AUTHOR model distinguishes the author from the storyworld. Calvino's fiction destabilizes that distinction by making the investigator's modeling operations part of the story.

MISSING:
An operational account of recursive representation, unreliable observation, and the causal effects of investigation.

BOUNDARY:
Braffort's count of eight actants is a retrospective analysis of the fiction, not evidence of an eight-actant program.

CITATION TRAIL:
Calvino, "The Burning of the Abominable House."
Braffort's working synopsis.
Dehn, "Story Generation After TALE-SPIN" (1981).
Borges, "The Garden of Forking Paths."

TEST:
Build the four-person model, then introduce the investigator's actions as events. Determine whether the original constraints can still describe the expanded narrative without adding a higher-order representational layer.

PLATFORM:
[[Self-Referential Narrative Systems]]

LINKS:
[[CALVINO-003]]
[[CALVINO-009]]
[[CALVINO-014]]

BIBTEX:
@article{braffort1997ordre,
  author  = {Braffort, Paul},
  title   = {L'ordre dans le crime: Une expérience cybernétique avec Italo Calvino},
  journal = {Europe},
  number  = {815},
  month   = mar,
  year    = {1997},
  url     = {https://www.paulbraffort.net/litterature/critique/calvino_crime.html}
}
