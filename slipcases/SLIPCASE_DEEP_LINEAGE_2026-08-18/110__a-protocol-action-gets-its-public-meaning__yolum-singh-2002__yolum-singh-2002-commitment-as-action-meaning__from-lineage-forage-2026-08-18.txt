ZETTEL

ID:
yolum-singh-2002-commitment-as-action-meaning

TITLE:
A protocol action gets its public meaning from the social commitment it creates or changes.

SOURCE:
Pınar Yolum and Munindar P. Singh — “Flexible Protocol Specification and Execution: Applying Event Calculus Planning Using Commitments” — 2002 — AAMAS

SOURCE URL:
https://www.csc2.ncsu.edu/faculty/mpsingh/papers/mas/aamas-02-protocols.pdf

PASSAGE:
[SOURCE SUMMARY] The paper represents interaction meaning through social commitments—obligations from one party to another—rather than through fixed message order alone.

RESEARCH OBJECT:
PUBLIC COMMITMENT AS PROTOCOL SEMANTICS

LOCAL MOVE:
Follow the lineage from promise/commitment language into an explicit public normative state machine.

SOURCE TERMS:
social commitment; debtor; creditor; obligation; protocol; action meaning

WHAT BECAME STRANGE:
The semantic primitive is neither message text nor private mental state but a publicly attributable relation between parties.

QUESTION:
Is a commitment ledger sufficient to represent the institutional meaning of communication?

DEEPER QUESTION:
How should commitment semantics represent disputed creation, contested authority, or incompatible interpretations of what was promised?

MECHANISM:
<social action> → [CREATE/MODIFY COMMITMENT] → <public normative state> → constrains/plans future actions

FORMAL SHIFT:
message sequence → public deontic relation

SOURCE FORMALISM:
Commitments C(debtor, creditor, condition) are represented as fluents and manipulated by event-calculus operations.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
NormativeState = {Commitment(d,c,p)}; Sem(action)=Δ(NormativeState).

TENSION:
Public commitment removes dependence on private intent but can still institutionalize one authoritative interpretation of the relation.

MISSING:
Contestability and evidence semantics around commitment creation and discharge.

BOUNDARY:
Commitment semantics does not by itself represent hermeneutic understanding or material performance.

CITATION TRAIL:
promise/obligation → public social semantics → commitment protocol execution

TEST:
Represent the same interaction using mentalistic FP/RE and public commitments; compare black-box testability.

PLATFORM:
[[commitment-as-public-state]]

LINKS:
[[austin-1962-promise-orders-future-conduct]]
[[singh-1998-public-perspective-testability]]
[[coordinator-1993-incompletion-token-a]]

BIBTEX:
@inproceedings{yolumsingh2002flexible, author={Yolum, Pınar and Singh, Munindar P.}, title={Flexible Protocol Specification and Execution: Applying Event Calculus Planning Using Commitments}, booktitle={Proceedings of the First International Joint Conference on Autonomous Agents and Multiagent Systems}, year={2002}, pages={527--534}, publisher={ACM}, doi={10.1145/544862.544867}}
