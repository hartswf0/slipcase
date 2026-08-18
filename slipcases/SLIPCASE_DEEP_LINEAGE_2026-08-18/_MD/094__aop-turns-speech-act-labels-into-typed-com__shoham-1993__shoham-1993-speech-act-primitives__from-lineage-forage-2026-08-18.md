ZETTEL

ID:
shoham-1993-speech-act-primitives

TITLE:
AOP turns speech-act labels into typed communication primitives.

SOURCE:
Yoav Shoham — “Agent-oriented programming” — 1993 — Artificial Intelligence 60(1):51–92

SOURCE URL:
https://www.sciencedirect.com/science/article/pii/0004370293900349

PASSAGE:
[SOURCE SUMMARY] Shoham contrasts unconstrained object messages with agent messages whose types include acts such as informing, requesting, offering, promising, and declining, explicitly invoking the spirit of speech-act theory.

RESEARCH OBJECT:
SPEECH ACT AS PROGRAMMING PRIMITIVE

LOCAL MOVE:
Locate the moment where an illocutionary category becomes an instruction accepted by an interpreter.

SOURCE TERMS:
inform; request; offer; promise; decline; message type; speech act

WHAT BECAME STRANGE:
The act label is no longer only an analyst’s description: it participates in computation.

QUESTION:
Does executable typing preserve the social semantics of the source speech act or merely reuse its name?

DEEPER QUESTION:
What conditions must an interpreter enforce before INFORM or PROMISE deserves its ordinary-language name?

MECHANISM:
<typed message> → [agent interpreter] → <state/action consequence>

FORMAL SHIFT:
illocutionary taxonomy → communication instruction set

SOURCE FORMALISM:
AGENT0 provides syntactic forms and an interpreter for agent programs and communication.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
MESSAGE.type ∈ {INFORM,REQUEST,OFFER,PROMISE,DECLINE}; semantics requires more than enumeration.

TENSION:
Typing enables rigorous execution while encouraging semantic equivalence between a software message and a human communicative act.

MISSING:
Source-level mapping from each AGENT0 message type to its formal preconditions and effects.

BOUNDARY:
Shared labels do not prove semantic fidelity to Austin or Searle.

CITATION TRAIL:
speech-act theory → Shoham AOP → FIPA communicative acts

TEST:
For each primitive, list source-attested preconditions/effects and compare them with Austinian felicity conditions.

PLATFORM:
[[speech-act-to-instruction]]

LINKS:
[[austin-1962-explicitness-force]]
[[fipa-2002-catalogue-performatives]]
[[graph-2026-transfer-depth]]

BIBTEX:
@article{shoham1993aop, author={Shoham, Yoav}, title={Agent-oriented programming}, journal={Artificial Intelligence}, year={1993}, volume={60}, number={1}, pages={51--92}, doi={10.1016/0004-3702(93)90034-9}}
