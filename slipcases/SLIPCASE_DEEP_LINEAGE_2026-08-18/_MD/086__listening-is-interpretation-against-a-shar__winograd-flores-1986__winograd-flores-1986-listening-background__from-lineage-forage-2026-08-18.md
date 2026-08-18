ZETTEL

ID:
winograd-flores-1986-listening-background

TITLE:
Listening is interpretation against a shared but never fully explicit background.

SOURCE:
Terry Winograd and Fernando Flores — Understanding Computers and Cognition — 1986 — §5.1 “Listening in a background”

SOURCE URL:
https://archive.org/details/understandingcom00wino

PASSAGE:
[SOURCE SUMMARY] Section 5.1 argues that speech acts occur against a background of practices and understanding; what is heard as a request, promise, or other act depends on listening and interpretation in that background.

RESEARCH OBJECT:
BACKGROUND AS A CONDITION OF SPEECH-ACT UPTAKE

LOCAL MOVE:
Make the hearer’s interpretive situation part of the lineage rather than treating a speech act as fully typed at emission.

SOURCE TERMS:
listening; background; interpretation; language act; shared understanding

WHAT BECAME STRANGE:
The semantic burden is not all on the speaker or message. A listener helps constitute what act is socially available.

QUESTION:
Can a machine protocol represent an act whose type depends partly on how it is heard?

DEEPER QUESTION:
What would an executable semantics look like if act classification were provisional and revisable as background assumptions become visible?

MECHANISM:
<utterance> × <listener background> → [LISTEN/INTERPRET] → <socially operative act>

FORMAL SHIFT:
speaker-intention semantics → interactional uptake semantics

SOURCE FORMALISM:
NONE. The source supplies a hermeneutic account rather than a transition calculus.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
UPTAKE(u,listener,K) → provisional_act_type; later interaction may revise that type.

TENSION:
A fixed act menu needs classification before interaction, while the source makes interpretation part of what determines the act.

MISSING:
A computational model of revisable uptake that retains protocol accountability.

BOUNDARY:
Winograd/Flores still use recognizable speech-act categories; background dependence does not imply categorical chaos.

CITATION TRAIL:
Gadamerian interpretation → Winograd/Flores listening → Suchman interactional critique → deferred classification problem

TEST:
Present the same utterance under two backgrounds and test whether competent participants classify its force differently.

PLATFORM:
[[background-beneath-protocol]]

LINKS:
[[gadamer-1960-conversation-event]]
[[suchman-1993-interactional-intention]]
[[medina-mora-1992-background-runtime-a]]

BIBTEX:
@book{winogradflores1986understanding, author={Winograd, Terry and Flores, Fernando}, title={Understanding Computers and Cognition: A New Foundation for Design}, year={1986}, publisher={Ablex}, address={Norwood, NJ}}
