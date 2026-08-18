ZETTEL

ID:
fipa-2002-refusal-executable-semantics

TITLE:
Refusal becomes a formally typed communicative operation with specified semantic structure.

SOURCE:
Foundation for Intelligent Physical Agents — FIPA Communicative Act Library Specification — 2002 — “refuse” communicative act

SOURCE URL:
https://www.fipa.org/specs/fipa00037/SC00037J.html

PASSAGE:
[SOURCE SUMMARY] REFUSE is a standardized act whose content identifies an action and an explanatory proposition/reason; the specification supplies formal feasibility and effect conditions.

RESEARCH OBJECT:
REFUSAL AS EXECUTABLE SOCIAL OPERATION

LOCAL MOVE:
Use refusal as a hard case for comparing protocol freedom, autonomy, and semantic typing.

SOURCE TERMS:
refuse; action; reason; feasibility; rational effect; autonomy

WHAT BECAME STRANGE:
The ability to say no—often treated as the mark of agent autonomy—is itself formalized as a permitted semantic operation.

QUESTION:
Is formal refusal genuine autonomy if the protocol determines the form and consequences of refusal?

DEEPER QUESTION:
How should a protocol represent refusal that also rejects the legitimacy of the request or the protocol itself?

MECHANISM:
<requested action> → [REFUSE(action,reason)] → <public conversational consequence>

FORMAL SHIFT:
social refusal → typed protocol act

SOURCE FORMALISM:
FIPA REFUSE includes structured content and FP/RE clauses.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
REFUSE may target ACTION while META_REFUSE could target the authority/protocol that made ACTION requestable.

TENSION:
A refusal primitive expands agency within the protocol but can leave refusal of the protocol unrepresentable.

MISSING:
Meta-level refusal semantics and exit rights in institutional protocols.

BOUNDARY:
The standard’s refusal act is not itself evidence of coercion or freedom in deployed systems.

CITATION TRAIL:
AOP autonomy/refusal → FIPA REFUSE → public commitment protocols

TEST:
Model three refusals: cannot do, will not do, contest request authority. Test whether one REFUSE type preserves all distinctions.

PLATFORM:
[[protocol-contestability]]

LINKS:
[[shoham-1993-speech-act-primitives]]
[[suchman-1993-category-discipline]]
[[yolum-singh-2002-flexible-runtime-paths]]

BIBTEX:
@techreport{fipa2002cal, author={{Foundation for Intelligent Physical Agents}}, title={FIPA Communicative Act Library Specification}, institution={FIPA}, year={2002}, number={SC00037J}, url={https://www.fipa.org/specs/fipa00037/SC00037J.html}}
