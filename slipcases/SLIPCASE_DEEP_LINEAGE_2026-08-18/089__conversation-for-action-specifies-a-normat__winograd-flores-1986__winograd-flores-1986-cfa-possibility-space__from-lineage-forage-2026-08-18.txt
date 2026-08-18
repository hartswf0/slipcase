ZETTEL

ID:
winograd-flores-1986-cfa-possibility-space

TITLE:
Conversation for action specifies a normative possibility space, not merely a four-step script.

SOURCE:
Terry Winograd and Fernando Flores — Understanding Computers and Cognition — 1986 — discussion of the basic conversation for action

SOURCE URL:
https://archive.org/details/understandingcom00wino

PASSAGE:
[SOURCE SUMMARY] The basic conversation for action distinguishes requests, promises, counter-moves, reports, declarations of satisfaction, and breakdown-related continuations. The diagram organizes legitimate continuations rather than describing every naturally occurring utterance.

RESEARCH OBJECT:
CONVERSATIONAL POSSIBILITY SPACE

LOCAL MOVE:
Read the diagram as a partial grammar of coordination rather than a deterministic linear workflow.

SOURCE TERMS:
conversation for action; request; promise; counteroffer; decline; report; satisfaction

WHAT BECAME STRANGE:
The theoretical diagram already has a syntax-like character: after some social states, some continuations make sense and others do not.

QUESTION:
At what point does a normative conversation diagram become an executable protocol?

DEEPER QUESTION:
What is gained and lost when “possible continuation” becomes “permitted machine transition”?

MECHANISM:
<conversation state> → [SOCIAL CONTINUATION] → <new commitment state>

FORMAL SHIFT:
descriptive/normative conversational distinctions → transition-oriented representation

SOURCE FORMALISM:
A conversation diagram with recognizable phases and alternative continuations; not a fully specified finite-state semantics.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
NEXT(K) = socially intelligible continuations; later software approximates NEXT(K) as an enumerable permitted-move set.

TENSION:
A possibility-space reading leaves room for repair and interpretation; an FSM reading encourages closure over a finite act vocabulary.

MISSING:
Exact comparison between book diagram, Coordinator patent tables, and ActionWorkflow runtime.

BOUNDARY:
The source diagram should not be retrospectively called a rigid FSM without implementation evidence.

CITATION TRAIL:
Winograd/Flores 1986 conversation diagram → Coordinator patent → ActionWorkflow architecture

TEST:
Reconstruct all branches visible in the book diagram and compare them to patent-permitted move tables.

PLATFORM:
[[conversation-becomes-program]]

LINKS:
[[coordinator-1993-fsm-permitted-moves]]
[[medina-mora-1992-executable-workflow]]
[[suchman-1993-category-discipline]]

BIBTEX:
@book{winogradflores1986understanding, author={Winograd, Terry and Flores, Fernando}, title={Understanding Computers and Cognition: A New Foundation for Design}, year={1986}, publisher={Ablex}, address={Norwood, NJ}}
