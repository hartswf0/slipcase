ZETTEL

ID:
PROGRAMROLE-001

TITLE:
An acceptable programming language explicitly places programs inside the domain of data.

SOURCE:
Neil D. Jones — “A Swiss Pocket Knife for Computability” — 2013 — §2.1, reformulating Rogers’ acceptable programming systems.

PASSAGE:
[PARAPHRASE]
Jones specifies separate sets of programs and data but requires the program set to be a subset of the data domain. A universal program receives another program as an ordinary argument, and the S-m-n property transforms a program together with data into a new program.

RESEARCH OBJECT:
PROGRAM ≠ NON-DATA.

Formal computability theory deliberately requires programs to be representable as data.

LOCAL MOVE:
The parent seeks a semantic discriminator between program and ordinary causal input.

Rogers-style acceptability begins by making the carrier sets overlap.

SOURCE TERMS:
programs
data
semantic function
universal program
S-m-n
acceptable programming language

WHAT BECAME STRANGE:
The foundational architecture does not protect the code/data boundary.

It requires permeability.

QUESTION:
If every program is data but not every datum is a program, what specifies membership in the program subset?

DEEPER QUESTION:
Is PROGRAM ROLE produced by a parser/semantic map selecting some data objects for interpretation rather than by a fundamentally different representation type?

MECHANISM:
p ∈ Pgms ⊆ D

and universal program:

univ(p,d)
→ behaves as p(d).

Specializer:

s₁¹(p,s)
→ new program p_s.

FORMAL SHIFT:
<PROGRAM AS DISTINCT SUBSTANCE>
→ <PROGRAM AS SPECIALLY INTERPRETABLE DATA>

SOURCE FORMALISM:
Jones writes:

    Pgms ⊆ D

with semantic mappings:

    [[p]]ⁿ : Dⁿ ⇀ D

and a universal-program property satisfying:

    [[p]](d) = [[univ]](p,d).

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Potential distinction:

    ProgramRole(d,I)
        iff
    d ∈ DomainProgram(I)

rather than:

    Program(d)

as an intrinsic material predicate.

TENSION:
The formalism still posits a distinguished subset Pgms.

It has not eliminated programhood; it has made the criterion of membership the next problem.

MISSING:
What formally characterizes Pgms apart from being the domain on which the semantic map is defined?

BOUNDARY:
Programs are data with a privileged interpretive relation.

The privilege itself remains unexplained by the carrier representation.

CITATION TRAIL:
[[UPTAKE-003]]
→ program versus ordinary input
→ Rogers/Jones acceptable programming systems
→ Pgms ⊆ D
→ interpretability rather than substance becomes candidate boundary.

TEST:
Choose a Lisp-like data universe containing both valid program ASTs and arbitrary lists.

Identify the exact predicate and interpretive machinery that separates:

    d ∈ Pgms

from:

    d ∈ D \ Pgms.

Then test whether that predicate can itself be changed at runtime.

PLATFORM:
[[description-becomes-operation]]

LINKS:
[[UPTAKE-003]]
[[programs-as-data]]
[[acceptable-programming-system]]
[[program-role]]

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
