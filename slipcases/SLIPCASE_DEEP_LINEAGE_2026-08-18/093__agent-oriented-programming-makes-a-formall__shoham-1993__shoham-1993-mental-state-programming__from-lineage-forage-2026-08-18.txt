ZETTEL

ID:
shoham-1993-mental-state-programming

TITLE:
Agent-oriented programming makes a formally represented mental state part of program state.

SOURCE:
Yoav Shoham — “Agent-oriented programming” — 1993 — Artificial Intelligence 60(1):51–92

SOURCE URL:
https://www.sciencedirect.com/science/article/pii/0004370293900349

PASSAGE:
[SOURCE SUMMARY] Shoham defines agent state through mental categories such as beliefs, decisions/choices, capabilities, and obligations/commitments and proposes a programming framework in which these states constrain computation.

RESEARCH OBJECT:
MENTAL ATTITUDES AS PROGRAM STATE

LOCAL MOVE:
Follow speech-act concepts into a setting where their associated mental attitudes become machine-manipulated state.

SOURCE TERMS:
belief; choice; capability; commitment; obligation; mental state; agent-oriented programming

WHAT BECAME STRANGE:
A vocabulary developed to analyze human action is now part of an executable software abstraction.

QUESTION:
What is gained by making mental attitudes primitive computational state?

DEEPER QUESTION:
Can interoperability rely on states that other agents cannot publicly inspect?

MECHANISM:
<agent mental state> + <message/event> → [INTERPRET/EXECUTE] → <updated mental state + action>

FORMAL SHIFT:
philosophical intentional state → programming-language state

SOURCE FORMALISM:
Shoham presents modal machinery for mental state and the AGENT0 programming language/interpreter.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
K_agent = <beliefs, choices, capabilities, commitments>; δ(K_agent,event)→K_agent′.

TENSION:
The formal state is executable for the agent implementation but may be epistemically inaccessible to external participants.

MISSING:
A full comparison between Shoham’s commitment notion and later public social commitments.

BOUNDARY:
AOP does not prove that software literally possesses human mental states; the categories are a computational abstraction.

CITATION TRAIL:
BDI/intentional stance + speech-act theory → Shoham AOP → agent communication languages → FIPA

TEST:
Ask whether two heterogeneous implementations with different internal belief structures can satisfy the same externally testable protocol.

PLATFORM:
[[artificial-agent-speech-acts]]

LINKS:
[[shoham-1993-speech-act-primitives]]
[[singh-1998-private-intention-normative-limit]]
[[fipa-2002-mental-attitude-model]]

BIBTEX:
@article{shoham1993aop, author={Shoham, Yoav}, title={Agent-oriented programming}, journal={Artificial Intelligence}, year={1993}, volume={60}, number={1}, pages={51--92}, doi={10.1016/0004-3702(93)90034-9}}
