ZETTEL

ID:
winograd-flores-1986-doing-outside-speech-act

TITLE:
The action that satisfies a request is not itself reducible to the conversation that coordinates it.

SOURCE:
Terry Winograd and Fernando Flores — Understanding Computers and Cognition — 1986 — conversation-for-action discussion

SOURCE URL:
https://archive.org/details/understandingcom00wino

PASSAGE:
[SOURCE SUMMARY] The book distinguishes the speech acts coordinating a commitment from the practical work performed to satisfy it; the doing may occur outside the conversational sequence.

RESEARCH OBJECT:
NORMATIVE SHELL / MATERIAL PERFORMANCE DISTINCTION

LOCAL MOVE:
Separate protocol state from the world-changing labor the protocol coordinates.

SOURCE TERMS:
doing; performance; conditions of satisfaction; conversation; action

WHAT BECAME STRANGE:
An executable conversation can be internally correct while the material action it purports to coordinate is absent, defective, or differently understood.

QUESTION:
What binds a protocol ledger to the external world it claims has been changed?

DEEPER QUESTION:
Is an institutional runtime complete without evidence semantics connecting declared completion to material performance?

MECHANISM:
<commitment> → [MATERIAL/PRACTICAL WORK OUTSIDE PROTOCOL] → <world change> → [REPORT/ASSESS] → <normative update>

FORMAL SHIFT:
conversation trace → conversation-plus-world coupling

SOURCE FORMALISM:
The source distinguishes coordination from doing but does not formalize sensors, evidence, or verification.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
K = <normative_state, world_state>; communicative acts update normative_state, practical acts update world_state, assessments relate the two.

TENSION:
Keeping the worlds separate prevents declaration from magically causing material completion, but institutions often make declarations consequential regardless of physical facts.

MISSING:
A typed semantics for evidence connecting performance claims to external conditions.

BOUNDARY:
The distinction does not deny that some speech acts directly change institutional reality.

CITATION TRAIL:
conversation for action → ActionWorkflow → DEMO C-acts/P-acts → institutional execution

TEST:
Build a trace with a valid REPORT OF COMPLETION but failed material work; determine which state changes should occur.

PLATFORM:
[[event-normative-interpretive-semantics]]

LINKS:
[[dietz-1999-transaction-state]]
[[searle-2018-deontic-powers]]
[[yolum-singh-2002-commitment-as-action-meaning]]

BIBTEX:
@book{winogradflores1986understanding, author={Winograd, Terry and Flores, Fernando}, title={Understanding Computers and Cognition: A New Foundation for Design}, year={1986}, publisher={Ablex}, address={Norwood, NJ}}
