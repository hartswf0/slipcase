ZETTEL

ID:
winograd-flores-1986-speech-act-synthesis

TITLE:
Speech-act theory is explicitly a starting point that Winograd and Flores transform rather than simply implement.

SOURCE:
Terry Winograd and Fernando Flores — Understanding Computers and Cognition — 1986 — Chapter 5

SOURCE URL:
https://archive.org/details/understandingcom00wino

PASSAGE:
[SOURCE SUMMARY] The authors call speech-act theory a starting point and present their own synthesis, emphasizing commitment, interpretation, social interaction, and background rather than treating formal illocutionary categories as sufficient.

RESEARCH OBJECT:
TRANSFORMATION RATHER THAN DIRECT IMPORT

LOCAL MOVE:
Replace the genealogy “speech-act theory → software” with a documented transformation step.

SOURCE TERMS:
speech act theory; starting point; synthesis; commitment; conversation; background

WHAT BECAME STRANGE:
The theoretical ancestor most often credited for the software is explicitly declared insufficient by the designers before implementation begins.

QUESTION:
Which elements of Austin/Searle are retained, altered, or rejected in the language/action synthesis?

DEEPER QUESTION:
Which later implementation choices restore the very categorical rigidity the book’s synthesis was designed to avoid?

MECHANISM:
<speech-act distinctions> + <background/interpretation> + <commitment> → [SYNTHESIZE] → <conversation for action>

FORMAL SHIFT:
taxonomy of acts → socially situated coordination dynamics

SOURCE FORMALISM:
Conceptual synthesis; no complete operational semantics in the book.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
TRANSFER(Austin/Searle→WF) = selected act distinctions + normative consequence, transformed by background and listening.

TENSION:
The book widens speech-act theory philosophically while its descendants narrow interaction operationally.

MISSING:
A precise source comparison of Searle’s felicity/illocution machinery with Winograd/Flores’s commitments and conversation states.

BOUNDARY:
The source does not license attributing all later Coordinator details directly to Austin or Searle.

CITATION TRAIL:
Austin/Searle → Winograd/Flores synthesis → Coordinator/ActionWorkflow

TEST:
Make a retention table for intention, uptake, felicity, authority, commitment, background, and conversational sequence across the lineage.

PLATFORM:
[[genealogy-of-formalization]]

LINKS:
[[austin-1962-felicity-procedure-context]]
[[winograd-flores-1986-lineage-heidegger-gadamer]]
[[medina-mora-1992-executable-workflow]]

BIBTEX:
@book{winogradflores1986understanding, author={Winograd, Terry and Flores, Fernando}, title={Understanding Computers and Cognition: A New Foundation for Design}, year={1986}, publisher={Ablex}, address={Norwood, NJ}}
