ZETTEL

ID:
NLC-001

TITLE:
By 1980 researchers were not merely issuing English commands to computers; they were constructing named subroutines in English.

SOURCE:
Alan W. Biermann and Bruce W. Ballard — “Toward Natural Language Computation I” — 1980 — pp. 71–73.

PASSAGE:
[PARAPHRASE]
The Natural Language Computer allows users to type English commands and watch them execute on displayed data. Correctly executed command sequences can be named and reused as subroutines. The paper explicitly discusses programming constructs including conditionals, repetition, and procedure definition.

RESEARCH OBJECT:
The genealogy moves beyond SHRDLU.

Natural-language PROGRAM CONSTRUCTION, not merely natural-language command execution, predates LLMs.

LOCAL MOVE:
NLC lets a user create a new imperative verb by specifying its procedure body through English commands.

SOURCE TERMS:
Natural Language Computer
programming
subroutine
define
if
repeat
procedure
imperative

WHAT BECAME STRANGE:
The historical novelty claim weakens again.

By 1980 the literature already contained:

NATURAL LANGUAGE
→ PROCEDURE DEFINITION
→ REUSABLE COMPUTATION.

QUESTION:
What remains genuinely distinctive about prompt programming if both English command execution and English procedure definition predate neural language models?

DEEPER QUESTION:
Is the LLM transition fundamentally from HAND-SPECIFIED SEMANTIC COVERAGE to LEARNED OPEN-ENDED SEMANTIC GENERALIZATION?

MECHANISM:
English commands
→ scanner
→ parser
→ flow-of-control semantics
→ sentence semantics
→ matrix operations.

For procedure construction:

English command sequence
→ name sequence as new imperative
→ stored subroutine
→ later English invocation
→ procedure execution.

FORMAL SHIFT:
<NATURAL-LANGUAGE COMMAND>
→ <REUSABLE PROCEDURE>
→ [NAMING / ABSTRACTION]
→ <EXPANDED NATURAL-LANGUAGE PROGRAMMING VOCABULARY>

SOURCE FORMALISM:
The paper presents explicit modules:

SCANNER
→ PARSER
→ FLOW-OF-CONTROL SEMANTICS
↔ SENTENCE SEMANTICS
→ MATRIX COMPUTER.

It describes user-defined imperatives and programming constructs including “if,” “repeat,” and procedure definition.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

NLC already supports something like:

    Define(name, [u₁,...,uₙ])
        → Procedure(name)

and later:

    Interpret(name(args))
        → Execute(Procedure(name), args).

TENSION:
NLC sharply restricts vocabulary, semantic domain, and syntactic form; the user must work inside a matrix-oriented microworld and begin sentences with imperative verbs.

MISSING:
A comparative measure of semantic breadth and adaptation between:

NLC
SHRDLU
semantic parsers
instruction-tuned LLMs.

BOUNDARY:
LLMs are not the origin of natural-language programming.

Their novelty must be located elsewhere.

CITATION TRAIL:
[[MINIMUM-024]]
→ Winograd / SHRDLU
→ Ballard and Biermann NLC
→ natural-language subroutines and flow control
→ learned versus hand-engineered semantic coverage.

TEST:
Give NLC-like and LLM-based systems tasks requiring:

new verb definition
procedure reuse
conditional control
reference resolution
out-of-domain vocabulary
paraphrase.

Record exactly where NLC’s hand-specified language boundary appears and where the learned model continues.

PLATFORM:
[[generative-collapse]]

LINKS:
[[MINIMUM-024]]
[[natural-language-programming]]
[[NLC]]
[[prompt-genealogy]]

BIBTEX:
@article{BiermannBallard1980,
  author  = {Biermann, Alan W. and Ballard, Bruce W.},
  title   = {Toward Natural Language Computation I},
  journal = {American Journal of Computational Linguistics},
  volume  = {6},
  number  = {2},
  pages   = {71--86},
  year    = {1980}
}
