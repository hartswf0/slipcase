ZETTEL

ID:
LIT-NAUR-006

TITLE:
Programming itself depends on knowledge that is not contained in program text, weakening a clean “code has fixed meaning / prompts discover meaning” opposition.

SOURCE:
Peter Naur — “Programming as Theory Building” — 1985 — Microprocessing and Microprogramming 15, pp. 253–261.

PASSAGE:
[PARAPHRASE]
Naur argues that programming should be regarded primarily as programmers building a theory of the matters handled by a program, rather than as production of program text and documentation. The programmer’s knowledge necessarily transcends the documented products: it includes why the program maps the world as it does, why particular parts have their form, and how to respond constructively to modification.

RESEARCH OBJECT:
The theory of the program that exceeds the program text.

LOCAL MOVE:
Naur relocates programming competence from an artifact to a relation between programmer, problem world, and program.

SOURCE TERMS:
theory building
program text
documentation
world
programmer
modification
direct knowledge

WHAT BECAME STRANGE:
Treating programming as the paradigm of fully explicit specification may depend on mistaking program text for programming.

QUESTION:
Are prompting and programming different because one is tacit and exploratory, or do both depend on theories that exceed their written expressions?

DEEPER QUESTION:
Does iterative prompting build a “theory of the model” analogous to Naur’s theory of the program?

MECHANISM:
Programmer encounters problem domain
→ constructs theory of how domain maps into program
→ produces text
→ theory enables explanation and modification beyond what text alone contains.

FORMAL SHIFT:
<PROBLEM WORLD>
→ <PROGRAMMER’S THEORY>
→ [WRITE PROGRAM]
→ <PROGRAM TEXT>
while
<THEORY> ⊄ <PROGRAM TEXT>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
PROGRAMMING ≠ PROGRAM_TEXT_PRODUCTION

COMPETENT CHANGE =
f(program_text, theory_of_program)

TENSION:
Programming languages still supply formal syntax and execution semantics in a way natural-language prompts generally do not. Naur weakens a total opposition; he does not erase every distinction.

MISSING:
A decomposition separating:
LANGUAGE SEMANTICS
PROGRAMMER THEORY
DOMAIN KNOWLEDGE
EMPIRICAL KNOWLEDGE OF IMPLEMENTATION.

BOUNDARY:
Naur does not argue that program text is semantically indeterminate in the same way as natural language.

CITATION TRAIL:
Gilbert Ryle.
Program comprehension.
Tacit knowledge.
Software maintenance.
End-user programming.

TEST:
Give an unfamiliar program and an unfamiliar prompt workflow to expert and novice operators. Change one requirement. Measure what each must know beyond the visible text to modify the artifact successfully.

PLATFORM:
[[PROGRAMMING / PROMPTING]]

LINKS:
[[THEORY OF THE PROMPT]]
[[TEXT DOES NOT CONTAIN PRACTICE]]
[[TACIT CRITERIA]]

BIBTEX:
@article{naur1985programming,
  author = {Peter Naur},
  title = {Programming as Theory Building},
  journal = {Microprocessing and Microprogramming},
  volume = {15},
  pages = {253--261},
  year = {1985}
}