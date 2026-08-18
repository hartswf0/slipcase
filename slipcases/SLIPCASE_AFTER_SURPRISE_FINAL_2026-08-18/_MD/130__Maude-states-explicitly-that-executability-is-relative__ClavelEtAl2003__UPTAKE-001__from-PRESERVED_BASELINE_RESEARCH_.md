ZETTEL

ID:
UPTAKE-001

TITLE:
Maude states explicitly that executability is relative: the same formal statement can be non-executable at one level and executable at another.

SOURCE:
Manuel Clavel, Francisco Durán, Steven Eker, Patrick Lincoln, Narciso Martí-Oliet, José Meseguer, and Carolyn Talcott — “The Maude 2.0 System” — 2003 — §2 and §3.5.

PASSAGE:
[PARAPHRASE]
Maude distinguishes fully executable, partially executable, and non-executable theories and statements. The authors then say that executability is relative: statements marked non-executable at the object level can still be represented and operated upon at the metalevel, where strategies may guide their execution.

RESEARCH OBJECT:
EXECUTABLE is not an intrinsic unary property of a statement even inside a rigorously formal programming/specification language.

LOCAL MOVE:
Maude parameterizes executability by:

LEVEL
+
INTERPRETIVE MACHINERY
+
STRATEGY.

SOURCE TERMS:
executable
nonexec
admissible
metalevel
reflection
strategy
META-LEVEL

WHAT BECAME STRANGE:
The parent distinction:

specified uptake
versus
underspecified uptake

is still too binary.

A description may be insufficiently executable under one interpreter regime while becoming executable when moved to another level and supplied with control information.

QUESTION:
Should executability be typed as a relation among expression, interpreter level, and strategy?

DEEPER QUESTION:
What is the minimum additional information required to turn a declarative specification into an executable one without changing its object-level assertions?

MECHANISM:
statement r
→ object-level executability test
→ NONEXEC

then:

represent r as metalevel data
→ supply metalevel machinery
→ supply strategy
→ guided metalevel execution.

FORMAL SHIFT:
<NONEXECUTABLE OBJECT-LEVEL DESCRIPTION>
→ [REIFICATION + STRATEGY]
→ <EXECUTABLE META-LEVEL OBJECT>

SOURCE FORMALISM:
Maude supports a `nonexec` attribute.

The source distinguishes fully, partially, and non-executable theories and explicitly characterizes executability as relative to metalevel interpretation and strategy.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Replace:

    Executable(e)

with:

    Executable(e | I, level, strategy).

Then it is possible that:

    ¬Executable(e | I_object, L0, ∅)

while:

    Executable(reify(e) | I_meta, L1, π).

TENSION:
Metalevel execution may perform reasoning ABOUT the represented statement rather than reproduce the same operational role the statement would have had as direct executable code.

MISSING:
A precise equivalence criterion between:
object-level execution
and
metalevel guided execution.

BOUNDARY:
Even within a formal language, executable versus non-executable may depend on interpretive regime rather than textual form alone.

CITATION TRAIL:
[[MINIMUM-028]]
→ “specified uptake”
→ Maude executable/nonexec distinction
→ “executability is a relative matter”
→ strategy- and level-relative execution.

TEST:
Take one Maude statement marked `nonexec`.

Attempt:

A. ordinary object-level execution
B. metalevel representation with no strategy
C. metalevel representation with an explicit strategy.

Identify exactly which new coordinate turns failure into a realizable computation.

PLATFORM:
[[description-becomes-operation]]

LINKS:
[[MINIMUM-028]]
[[relative-executability]]
[[specified-uptake]]
[[strategy]]
[[reflection]]

BIBTEX:
@inproceedings{ClavelEtAl2003,
  author    = {Clavel, Manuel and Dur{\'a}n, Francisco and Eker, Steven and Lincoln, Patrick and Mart{\'i}-Oliet, Narciso and Meseguer, Jos{\'e} and Talcott, Carolyn},
  title     = {The Maude 2.0 System},
  booktitle = {Rewriting Techniques and Applications},
  series    = {Lecture Notes in Computer Science},
  volume    = {2706},
  pages     = {76--87},
  publisher = {Springer},
  year      = {2003},
  doi       = {10.1007/3-540-44881-0_7}
}
