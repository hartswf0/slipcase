ZETTEL

ID:
yolum-singh-2002-sequence-overconstraint

TITLE:
Sequence-oriented protocols overconstrain autonomous agents by prescribing trajectories instead of interaction meaning.

SOURCE:
Pınar Yolum and Munindar P. Singh — “Flexible Protocol Specification and Execution: Applying Event Calculus Planning Using Commitments” — 2002 — AAMAS

SOURCE URL:
https://www.csc2.ncsu.edu/faculty/mpsingh/papers/mas/aamas-02-protocols.pdf

PASSAGE:
[SOURCE SUMMARY] Yolum and Singh criticize finite-state and Petri-net style protocol specifications for constraining agents to predetermined sequences and for failing to represent the meaning of actions.

RESEARCH OBJECT:
SEQUENCE OVERCONSTRAINT

LOCAL MOVE:
Make the distinction between legal trace and normative meaning explicit.

SOURCE TERMS:
finite state machine; Petri net; protocol; autonomous agent; sequence; meaning; flexibility

WHAT BECAME STRANGE:
A perfectly verified trace can still be semantically weak if the protocol cannot say what obligations the actions create.

QUESTION:
Should protocol correctness be defined by following an allowed path or by preserving public normative constraints?

DEEPER QUESTION:
Can sequence be compiled on demand from commitments rather than authored in advance?

MECHANISM:
<sequence-first protocol> → [ENUMERATE] → <allowed traces>; critique: traces constrain action without encoding why they are valid

FORMAL SHIFT:
trajectory specification → meaning/state specification

SOURCE FORMALISM:
The paper contrasts sequence-oriented protocols with commitment-based specifications and uses planning over event-calculus representations.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
Correct(trace) := satisfies(commitment_constraints(trace)), not trace ∈ preenumerated_paths.

TENSION:
Sequence constraints can simplify safety verification; flexibility increases planning and verification complexity.

MISSING:
Comparative complexity and safety analysis under open-ended commitment-preserving traces.

BOUNDARY:
The critique does not imply that all sequence constraints are unnecessary.

CITATION TRAIL:
FIPA/pre-enumerated plans → Yolum/Singh commitment protocol

TEST:
Insert a normatively harmless extra action into a valid protocol trace; sequence-first and commitment-first semantics should differ.

PLATFORM:
[[sequence-vs-semantics]]

LINKS:
[[fipa-2002-preenumerated-plans]]
[[smith-cohen-1996-cfa-derived-not-primitive]]
[[yolum-singh-2002-commitment-as-action-meaning]]

BIBTEX:
@inproceedings{yolumsingh2002flexible, author={Yolum, Pınar and Singh, Munindar P.}, title={Flexible Protocol Specification and Execution: Applying Event Calculus Planning Using Commitments}, booktitle={Proceedings of the First International Joint Conference on Autonomous Agents and Multiagent Systems}, year={2002}, pages={527--534}, publisher={ACM}, doi={10.1145/544862.544867}}
