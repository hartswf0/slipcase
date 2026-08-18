ZETTEL

ID:
PROGRAMROLE-002

TITLE:
Kleene’s recursion theorem permits an explicit interchange of program and data roles.

SOURCE:
Neil D. Jones — “A Swiss Pocket Knife for Computability” — 2013 — §2.2, applying Kleene’s Second Recursion Theorem.

PASSAGE:
[PARAPHRASE]
Jones gives an application of Kleene’s theorem in which a constructed program receives another program q as input and behaves as q would behave when given the constructed program itself as data. Jones explicitly describes this as interchanging the roles of programs and data.

RESEARCH OBJECT:
The PROGRAM / INPUT polarity can be reversed inside a single computability-theoretic construction.

LOCAL MOVE:
The parent sought the property making representation r control receiver I.

The recursion theorem produces a case where r alternates between:

THING EXECUTED
and
THING SUPPLIED TO ANOTHER PROGRAM.

SOURCE TERMS:
program
data
universal program
self-reference
fixpoint
Second Recursion Theorem

WHAT BECAME STRANGE:
Even PROGRAM ROLE and RECEIVER ROLE can circulate.

A program can be passed as data to a universal interpreter whose selected program then receives the first program as data.

QUESTION:
Can a sharp program/input distinction survive universal interpretation and reflection?

DEEPER QUESTION:
Would the correct invariant be not the ROLE of an artifact but the existence of a typed INTERPRETATION EDGE between artifacts?

MECHANISM:
Jones considers:

    p(q,d) = univ(d,q)

and obtains a fixpoint p* satisfying:

    [[p*]](q)
      =
    [[q]](p*).

Thus:
q begins as input to p*
but becomes the executed program,
while p* becomes q’s input.

FORMAL SHIFT:
<PROGRAM p* , INPUT q>
→ [UNIVERSAL INTERPRETATION]
→ <PROGRAM q , INPUT p*>

SOURCE FORMALISM:
Jones derives:

    ∀q ∈ Pgms .
    [[p*]](q) = [[q]](p*).

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Represent execution as an edge:

    Executes(I, code, data)

rather than unary labels:

    Program(code)
    Data(data).

The same node may occupy either endpoint in different edges.

TENSION:
This construction depends on an acceptable programming system with universal interpretation and recursion-theoretic machinery.

Ordinary application architectures may impose much stricter role separation.

MISSING:
Which weaker computational systems permit role interchange without full universal self-interpretation?

BOUNDARY:
The program/data distinction is relational under universal computation.

This does not imply every data object can occupy program role in every interpreter.

CITATION TRAIL:
[[UPTAKE-003]]
→ program-role discriminator
→ Kleene SRT
→ Jones application interchanging program/data roles
→ execution as relation between representations.

[[REFLECT-002]]
→ represented semantics
→ self-reference
→ roles circulate across meta-levels.

TEST:
Implement the equation:

    [[p*]](q) = [[q]](p*)

in a self-interpreting language.

Draw the execution graph without labeling any node permanently PROGRAM or DATA.

Label only edges and argument positions.

PLATFORM:
[[description-becomes-operation]]

LINKS:
[[UPTAKE-003]]
[[REFLECT-002]]
[[program-data-role-interchange]]
[[kleene-second-recursion-theorem]]

BIBTEX:
@article{Jones2013PocketKnife,
  author  = {Jones, Neil D.},
  title   = {A Swiss Pocket Knife for Computability},
  journal = {Electronic Proceedings in Theoretical Computer Science},
  volume  = {129},
  pages   = {1--17},
  year    = {2013},
  doi     = {10.4204/EPTCS.129.1}
}
