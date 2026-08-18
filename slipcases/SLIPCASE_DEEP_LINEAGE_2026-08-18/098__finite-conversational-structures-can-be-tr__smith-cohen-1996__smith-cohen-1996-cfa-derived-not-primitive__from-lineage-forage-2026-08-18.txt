ZETTEL

ID:
smith-cohen-1996-cfa-derived-not-primitive

TITLE:
Finite conversational structures can be treated as consequences of act semantics rather than primitive protocols.

SOURCE:
Ira A. Smith and Philip R. Cohen — “Toward a Semantics for an Agent Communications Language Based on Speech-Acts” — 1996 — AAAI-96

SOURCE URL:
https://cdn.aaai.org/AAAI/1996/AAAI96-004.pdf

PASSAGE:
[SOURCE SUMMARY] Smith and Cohen argue that much finite-state dialogue structure, including the Winograd/Flores conversation-for-action pattern, can be derived from the logical relationships created by communicative acts.

RESEARCH OBJECT:
PROTOCOL AS DERIVED STRUCTURE

LOCAL MOVE:
Reverse the usual causal story: the finite-state pattern need not define meaning; meaning can constrain which sequences emerge.

SOURCE TERMS:
finite state; conversation for action; logical relationship; communicative act; derivation

WHAT BECAME STRANGE:
The same visible state machine can be either the source of semantics or the trace-level consequence of a deeper semantics.

QUESTION:
Should a protocol language enumerate legal sequences or derive them from normative/intentional state?

DEEPER QUESTION:
What differences appear under exceptions when sequence-first and semantics-first models share the same happy path?

MECHANISM:
<act semantics> → [COMPOSE] → <admissible dialogue trajectories>

FORMAL SHIFT:
FSM as primitive → FSM as projection of deeper semantics

SOURCE FORMALISM:
Logical semantics of communicative acts used to constrain/derive dialogue structure.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
TRACE_SET = derive(SemanticsOfActs); FSM may be a compiled view rather than source ontology.

TENSION:
Derived protocols preserve flexibility but depend on the correctness and observability of the deeper semantic state.

MISSING:
Executable trace equivalence test between Coordinator FSM and semantics-derived conversations.

BOUNDARY:
Resemblance to Conversation for Action does not establish direct implementation lineage.

CITATION TRAIL:
Winograd/Flores CFA → Smith/Cohen derivation claim → commitment protocol alternatives

TEST:
Generate all legal traces from act semantics and compare with hand-authored FSM transitions under refusal, cancellation, and renegotiation.

PLATFORM:
[[protocol-as-derived-view]]

LINKS:
[[winograd-flores-1986-cfa-possibility-space]]
[[yolum-singh-2002-sequence-overconstraint]]

BIBTEX:
@inproceedings{smithcohen1996semantics, author={Smith, Ira A. and Cohen, Philip R.}, title={Toward a Semantics for an Agent Communications Language Based on Speech-Acts}, booktitle={Proceedings of AAAI-96}, year={1996}, pages={24--31}, publisher={AAAI Press}}
