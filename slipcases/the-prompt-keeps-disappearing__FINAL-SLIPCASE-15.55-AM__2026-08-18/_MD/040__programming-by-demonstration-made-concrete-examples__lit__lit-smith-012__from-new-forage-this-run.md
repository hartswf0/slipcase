ZETTEL

ID:
LIT-SMITH-012

TITLE:
Programming by demonstration made concrete examples part of specification decades before prompt iteration.

SOURCE:
David Canfield Smith — “Pygmalion: An Executable Electronic Blackboard” — 1993 retrospective chapter on the 1975 Pygmalion system — in Watch What I Do: Programming by Demonstration.
SOURCE URL: https://acypher.com/wwid/Chapters/01Pygmalion.html

PASSAGE:
[PARAPHRASE]
Smith describes Pygmalion as changing the process of programming from specifying an abstract computation in a programming language to demonstrating concrete cases to the machine. He identifies the 1975 system as an early implementation of programming by demonstration and describes its use of icons and concrete manipulation.

RESEARCH OBJECT:
CONCRETE DEMONSTRATION AS A SPECIFICATION MEDIUM.

LOCAL MOVE:
Pygmalion supplies opposition to any claim that computation became exploratory only with prompting. It places example, manipulation, and interaction inside program construction itself.

SOURCE TERMS:
programming by demonstration
concrete
abstract description
icons
programming environment
demonstration

WHAT BECAME STRANGE:
The opposition between “formal program written first” and “meaning discovered after running” is historically weak. Programming environments have long allowed specification to emerge through interaction with partial behavior.

QUESTION:
What, if anything, is new when a language model generalizes from linguistic examples and corrections rather than a programming-by-demonstration system generalizing from concrete manipulations?

DEEPER QUESTION:
Does the important change lie in the medium of demonstration, the scope of inference, or the cost of constructing the interpreter?

MECHANISM:
Concrete example / manipulation
→ system records or interprets demonstrated relation
→ generalized reusable procedure
→ further examples expose missing distinctions
→ program revised.

FORMAL SHIFT:
<ABSTRACT PROGRAM DESCRIPTION>
→ <CONCRETE DEMONSTRATION>
→ [INFER / RECORD PROCEDURE]
→ <REUSABLE BEHAVIOR>

SOURCE FORMALISM:
Pygmalion is an implemented visual programming environment organized around icons and programming by demonstration; this zettel does not reconstruct its internal formalism beyond Smith’s retrospective description.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
SPECIFICATION may be distributed across EXAMPLE + SYSTEM INFERENCE + CORRECTION rather than exhausted by a prior textual program.

TENSION:
Pygmalion’s examples occur in a designed visual programming environment. Contemporary language models generalize through learned statistical representations over far broader domains. Similarity of interactive specification is not equivalence of mechanism.

MISSING:
A direct comparison between how Pygmalion and contemporary LLM systems infer generality from examples, including what prior ontology each requires.

BOUNDARY:
The 1993 chapter is a retrospective source for the 1975 system. It supports historical precedent for programming by demonstration, not a claim of direct influence on modern prompting.

CITATION TRAIL:
Smith 1975 thesis → Smith 1993 retrospective → programming by demonstration → example-based and end-user programming → in-context examples in language models.

TEST:
Give one task to a programming-by-demonstration environment and a language model using only examples plus corrections. Compare what generalization each makes without an explicit rule and what prior representational commitments make the inference possible.

PLATFORM:
[[INTERACTIVE SPECIFICATION]]

LINKS:
[[PF-FAILURE-005]]
[[PF-SEMANTICS-004]]
[[LIT-SUCHMAN-004]]
[[RESTRICTION MIGRATION]]

BIBTEX:
@incollection{smith1993pygmalion,
  author = {David Canfield Smith},
  title = {Pygmalion: An Executable Electronic Blackboard},
  booktitle = {Watch What I Do: Programming by Demonstration},
  editor = {Allen Cypher},
  publisher = {MIT Press},
  year = {1993},
  url = {https://acypher.com/wwid/Chapters/01Pygmalion.html}
}