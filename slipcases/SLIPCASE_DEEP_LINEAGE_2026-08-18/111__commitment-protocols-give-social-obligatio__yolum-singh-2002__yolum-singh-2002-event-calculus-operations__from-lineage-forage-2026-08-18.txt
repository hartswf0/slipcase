ZETTEL

ID:
yolum-singh-2002-event-calculus-operations

TITLE:
Commitment protocols give social obligations explicit state-change operations in event calculus.

SOURCE:
Pınar Yolum and Munindar P. Singh — “Flexible Protocol Specification and Execution: Applying Event Calculus Planning Using Commitments” — 2002 — AAMAS — pp. 529–531

SOURCE URL:
https://www.csc2.ncsu.edu/faculty/mpsingh/papers/mas/aamas-02-protocols.pdf

PASSAGE:
[SOURCE SUMMARY] The paper defines operations including Create, Discharge, Cancel, Release, Assign, and Delegate; events initiate or terminate commitment fluents in an event-calculus representation.

RESEARCH OBJECT:
EXECUTABLE NORMATIVE STATE TRANSITIONS

LOCAL MOVE:
Recover actual technical machinery rather than relying on metaphorical claims that institutions are “like code.”

SOURCE TERMS:
Create; Discharge; Cancel; Release; Assign; Delegate; event calculus; Initiates; Terminates; commitment

WHAT BECAME STRANGE:
Operations familiar from social obligation are given explicit transition semantics suitable for planning and execution.

QUESTION:
Which institutional relations can be represented with commitment-fluent operations and which require richer authority or interpretation models?

DEEPER QUESTION:
Can these operations become a general intermediate representation for institutional action without universalizing one theory of obligation?

MECHANISM:
<event> → [Initiates/Terminates] → <commitment fluent changes> → <new normative state>

FORMAL SHIFT:
social obligation → event-calculus fluent with operations

SOURCE FORMALISM:
Create, Discharge, Cancel, Release, Assign, Delegate are defined through Happens/Initiates/Terminates relations over commitment fluents.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
δ_norm(event,K) applies typed commitment operation and yields K′; this is genuine source-adjacent executable machinery, not only analogy.

TENSION:
Formal precision exposes operations but does not settle whether the social world recognizes the event as authorized or correctly interpreted.

MISSING:
Authority predicates, evidence rules, dispute states, and multi-party commitments beyond debtor-creditor relations.

BOUNDARY:
Do not infer that all institutional action reduces to these six operations.

CITATION TRAIL:
Singh social semantics → Yolum/Singh commitment operations → executable institutional protocol

TEST:
Implement the source operations and then attempt hard cases: unauthorized release, disputed discharge, delegated obligation without consent.

PLATFORM:
[[event-normative-interpretive-semantics]]

LINKS:
[[austin-1962-authority-as-felicity-condition]]
[[winograd-flores-1986-cos-not-objective]]
[[yolum-singh-2002-flexible-runtime-paths]]

BIBTEX:
@inproceedings{yolumsingh2002flexible, author={Yolum, Pınar and Singh, Munindar P.}, title={Flexible Protocol Specification and Execution: Applying Event Calculus Planning Using Commitments}, booktitle={Proceedings of the First International Joint Conference on Autonomous Agents and Multiagent Systems}, year={2002}, pages={527--534}, publisher={ACM}, doi={10.1145/544862.544867}}
