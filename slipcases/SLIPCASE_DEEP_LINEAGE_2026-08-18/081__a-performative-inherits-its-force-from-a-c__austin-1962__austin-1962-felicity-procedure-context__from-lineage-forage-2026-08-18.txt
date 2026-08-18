ZETTEL

ID:
austin-1962-felicity-procedure-context

TITLE:
A performative inherits its force from a conventional procedure and its circumstances.

SOURCE:
J. L. Austin — How to Do Things with Words — 1962 — Lecture II

SOURCE URL:
https://web.english.upenn.edu/~cavitch/pdf-library/Austin_How_To_Do_Things_with_Words.pdf

PASSAGE:
[SOURCE SUMMARY] Austin’s A.1/A.2 felicity conditions require an accepted conventional procedure with a conventional effect and appropriate persons and circumstances.

RESEARCH OBJECT:
FELICITY CONDITIONS AS CONTEXTUAL SEMANTICS

LOCAL MOVE:
Move behind the utterance to the procedure that makes the utterance operative.

SOURCE TERMS:
conventional procedure; conventional effect; persons; circumstances; appropriate; infelicity

WHAT BECAME STRANGE:
Speech-act force is already distributed across an utterance, a convention, actors, and circumstances before later formal systems isolate a message type.

QUESTION:
What part of a performative’s meaning can be carried by an explicit act label, and what remains in the surrounding institution?

DEEPER QUESTION:
When a software protocol replaces contextual felicity with a state-transition guard, which social conditions have been compiled and which have disappeared?

MECHANISM:
<utterance> + <accepted procedure> + <appropriate persons/circumstances> → [PERFORM] → <conventional effect>

FORMAL SHIFT:
sentence meaning → situated conventional operation

SOURCE FORMALISM:
Austin’s enumerated felicity conditions A.1, A.2, B.1, B.2, Γ.1, Γ.2 are analytic conditions, not an executable transition system.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
FELICITOUS(act,K) := PROCEDURE_EXISTS(K) ∧ PERSONS_APPROPRIATE(K) ∧ EXECUTED_CORRECTLY(act) ∧ EXECUTED_COMPLETELY(act)

TENSION:
Formal guards can represent some felicity conditions, but treating them as exhaustive risks turning historically revisable conventions into fixed predicates.

MISSING:
A source-grounded lineage showing exactly which Austinian felicity conditions survive in later workflow and agent protocols.

BOUNDARY:
Austin does not provide software semantics or claim that contextual conditions are reducible to machine state.

CITATION TRAIL:
Austin 1962 felicity conditions → Searle constitutive rules → Winograd/Flores speech-act synthesis → executable protocols

TEST:
For one promise, vary only authority, procedure, and circumstance. A faithful executable account must distinguish successful from infelicitous performances.

PLATFORM:
[[felicity-to-protocol]]

LINKS:
[[austin-1962-authority-as-felicity-condition]]
[[winograd-flores-1986-speech-act-synthesis]]
[[fipa-2002-feasibility-rational-effect]]

BIBTEX:
@book{austin1962things, author={Austin, J. L.}, title={How to Do Things with Words}, year={1962}, publisher={Clarendon Press}, address={Oxford}}
