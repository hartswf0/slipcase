ZETTEL

ID:
singh-1998-private-intention-normative-limit

TITLE:
Private intention is unsuitable as the normative ground of interoperability because autonomous agents cannot read one another’s minds.

SOURCE:
Munindar P. Singh — “Agent Communication Languages: Rethinking the Principles” — 1998 — Computer 31(12):40–47

SOURCE URL:
https://www.csc2.ncsu.edu/faculty/mpsingh/papers/mas/computer-acl-98.pdf

PASSAGE:
[SOURCE SUMMARY] Singh’s core critique is that semantics based on beliefs and intentions presupposes access to other agents’ private mental states, which fails for autonomous heterogeneous agents.

RESEARCH OBJECT:
EPISTEMIC LIMIT OF MENTALISTIC PROTOCOL SEMANTICS

LOCAL MOVE:
Turn an ontological criticism into a concrete verification criterion.

SOURCE TERMS:
mental agency; belief; intention; autonomous; heterogeneous; public; private

WHAT BECAME STRANGE:
The problem is not merely whether mental categories are philosophically correct; the semantics can be operationally unverifiable across independently controlled systems.

QUESTION:
What semantic commitments can be enforced without access to implementation-private state?

DEEPER QUESTION:
For human institutions, does the same public/private distinction explain why sincerity cannot be the sole basis of enforceable obligation?

MECHANISM:
<private-state semantic clause> → [CROSS-AGENT VERIFICATION ATTEMPT] → <unobservable condition> → <compliance gap>

FORMAL SHIFT:
mental-state criterion → public normative criterion

SOURCE FORMALISM:
Conceptual argument tied to interoperability and compliance requirements.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
If semantic predicate P requires inaccessible internal state, external CONFORMS(P) is generally undecidable by observation.

TENSION:
Public semantics may be enforceable while losing motives and meanings that remain important to participants.

MISSING:
A layered semantics that distinguishes public normative validity from private interpretive/intentional state.

BOUNDARY:
The argument concerns communication-standard semantics, not a claim that internal beliefs/intents are useless in agent reasoning.

CITATION TRAIL:
FIPA/private mental semantics → Singh critique → social commitments

TEST:
For every semantic predicate in an ACL, tag PUBLICLY OBSERVABLE, DECLARED, INFERRED, or PRIVATE; require normative compliance to avoid PRIVATE-only predicates.

PLATFORM:
[[private-to-public-semantics]]

LINKS:
[[fipa-2002-mental-attitude-model]]
[[yolum-singh-2002-commitment-as-action-meaning]]
[[austin-1962-promise-orders-future-conduct]]

BIBTEX:
@article{singh1998rethinking, author={Singh, Munindar P.}, title={Agent Communication Languages: Rethinking the Principles}, journal={Computer}, year={1998}, volume={31}, number={12}, pages={40--47}, doi={10.1109/2.735849}}
