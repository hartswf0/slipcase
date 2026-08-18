ZETTEL

ID:
REFLECT-003

TITLE:
Self-reference does not require a syntactic reflection primitive: Kleene’s theorem constructs it from specialization.

SOURCE:
Neil D. Jones — “A Swiss Pocket Knife for Computability” — 2013 — §§2.1–2.3, reconstructing Kleene’s Second Recursion Theorem.

PASSAGE:
[PARAPHRASE]
For any suitable two-argument program p, Kleene’s theorem constructs a one-argument program p* whose behavior is the same as p when p is given p*’s own program text as its first argument. Jones emphasizes that the construction predates computers and can be understood operationally as program transformation and self-reference.

RESEARCH OBJECT:
REFLECTION need not begin with a language feature named reflection.

It can emerge extensionally from universal programmability plus specialization machinery.

LOCAL MOVE:
The parent asked whether computational meta-change remains bounded by a pre-existing reflective interface.

Kleene shows a more primitive phenomenon:
program self-reference can be constructed without explicit reflective syntax.

SOURCE TERMS:
Second Recursion Theorem
fixpoint
self-application
program text
specialization
reflection

WHAT BECAME STRANGE:
A language may lack:
`eval`
quotation operators
reflection APIs
self-modifying commands

and still support programs whose behavior depends on their own representation.

QUESTION:
Which reflective phenomena require explicit reflective syntax, and which follow automatically from acceptable programmability?

DEEPER QUESTION:
Is reflection an optional language feature or a latent consequence of representable programs plus universal interpretation/specialization?

MECHANISM:
given p(q,d)

construct p*

such that:

    [[p*]](d)
      =
    [[p]](p*,d).

The program’s own representation is fed back into the computation.

FORMAL SHIFT:
<PROGRAM EXTERNAL TO ITS OWN INPUT>
→ [FIXPOINT CONSTRUCTION]
→ <PROGRAM WITH ACCESS TO OWN REPRESENTATION THROUGH BEHAVIORAL EQUIVALENCE>

SOURCE FORMALISM:
Jones states Kleene’s theorem as:

    ∀p ∈ Pgms
    ∃p* ∈ Pgms
    ∀d ∈ D :
    [[p]](p*,d) = [[p*]](d).

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Reflection can be split:

    EXPLICIT REFLECTION:
      language contains primitives exposing representation.

    EXTENSIONAL REFLECTION:
      there exists p* whose behavior is equivalent to receiving its own representation.

TENSION:
The theorem guarantees semantic existence/construction under acceptable-programming assumptions, not convenient introspective access to arbitrary runtime structure.

MISSING:
Which forms of semantic self-modification require more than Kleene-style self-reference?

BOUNDARY:
The absence of explicit reflection syntax does not establish non-reflexivity at the level of computability.

CITATION TRAIL:
[[REFLECT-002]]
→ reflective rewriting logic
→ Kleene SRT
→ reflection without explicit meta-level syntax
→ distinguish self-reference from semantic self-modification.

[[METASTABLE-001]]
→ rules of rule-change
→ latent reflection
→ search for what additional machinery changes semantics rather than merely references code.

TEST:
Construct:
A. a quine,
B. a program that recognizes its own text,
C. a program that changes its own semantics.

Determine which are supplied by Kleene’s theorem alone and which require additional interpreter authority.

PLATFORM:
[[description-becomes-operation]]

LINKS:
[[REFLECT-002]]
[[METASTABLE-001]]
[[kleene-second-recursion-theorem]]
[[latent-reflection]]

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
