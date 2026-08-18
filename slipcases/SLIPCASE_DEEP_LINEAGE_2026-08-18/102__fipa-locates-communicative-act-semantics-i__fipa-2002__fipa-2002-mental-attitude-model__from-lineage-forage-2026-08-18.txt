ZETTEL

ID:
fipa-2002-mental-attitude-model

TITLE:
FIPA locates communicative-act semantics in beliefs, intentions, uncertainty, and rational effects.

SOURCE:
Foundation for Intelligent Physical Agents — FIPA Communicative Act Library Specification — 2002 — SC00037J

SOURCE URL:
https://www.fipa.org/specs/fipa00037/SC00037J.html

PASSAGE:
[SOURCE SUMMARY] FIPA act definitions are mentalistic: formal clauses refer to what agents believe, intend, are uncertain about, or seek to bring about through communication.

RESEARCH OBJECT:
STANDARDIZED PRIVATE-STATE SEMANTICS

LOCAL MOVE:
Identify the precise target of Singh’s later/public-semantics critique.

SOURCE TERMS:
belief; intention; uncertainty; rational effect; semantic model; agent

WHAT BECAME STRANGE:
A public interoperability standard defines meaning through states that may be private to heterogeneous implementations.

QUESTION:
How can another agent or auditor determine whether a FIPA act satisfied a semantic condition about internal belief or intention?

DEEPER QUESTION:
Can mentalistic semantics be retained as internal reasoning guidance while a separate public semantics governs compliance?

MECHANISM:
<message> → [MENTALISTIC SEMANTIC INTERPRETATION] → <belief/intention effects>

FORMAL SHIFT:
public message token → private mental-attitude semantics

SOURCE FORMALISM:
Formal act semantics expressed through mental-attitude operators and action propositions.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
InternalSemantics(act)=Δ(mental_state); PublicCompliance(act) requires a distinct observable criterion.

TENSION:
The standard needs abstraction over implementation but refers to states whose realization may vary or be inaccessible.

MISSING:
A dual-semantics architecture connecting internal reasoning semantics to public normative semantics.

BOUNDARY:
Mentalistic semantics is not meaningless; the issue is external testability across autonomous heterogeneous agents.

CITATION TRAIL:
Shoham/Smith-Cohen mentalistic branch → FIPA → Singh public-perspective critique

TEST:
Attempt to build a black-box conformance test for INFORM using only messages and public events; record which FIPA clauses are untestable.

PLATFORM:
[[private-to-public-semantics]]

LINKS:
[[shoham-1993-mental-state-programming]]
[[smith-cohen-1996-joint-intention-semantics]]
[[singh-1998-public-perspective-testability]]

BIBTEX:
@techreport{fipa2002cal, author={{Foundation for Intelligent Physical Agents}}, title={FIPA Communicative Act Library Specification}, institution={FIPA}, year={2002}, number={SC00037J}, url={https://www.fipa.org/specs/fipa00037/SC00037J.html}}
