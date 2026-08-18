ZETTEL

ID:
singh-1998-social-context

TITLE:
Public communication semantics still depends on social context rather than message syntax alone.

SOURCE:
Munindar P. Singh — “Agent Communication Languages: Rethinking the Principles” — 1998 — Computer 31(12):40–47

SOURCE URL:
https://www.csc2.ncsu.edu/faculty/mpsingh/papers/mas/computer-acl-98.pdf

PASSAGE:
[SOURCE SUMMARY] Singh argues that communication is inherently public and depends on agents’ social context; pragmatics constrains how agents relate and how messages are used and interpreted.

RESEARCH OBJECT:
SOCIAL CONTEXT INSIDE PUBLIC SEMANTICS

LOCAL MOVE:
Prevent the public-semantics turn from being mistaken for context-free ledger semantics.

SOURCE TERMS:
social context; pragmatics; public; relation; interpretation; meaning

WHAT BECAME STRANGE:
Moving away from private minds does not eliminate context; it relocates context into publicly structured relations.

QUESTION:
Which contextual relations must be explicit for public semantics to remain testable?

DEEPER QUESTION:
Can roles, authority, conventions, histories, and institutional settings be represented without freezing them into universal categories?

MECHANISM:
<message> × <public social context> → [INTERPRET] → <social consequence>

FORMAL SHIFT:
mental context → relational/social context

SOURCE FORMALISM:
Singh’s design-space analysis distinguishes semantic/pragmatic basis, context flexibility, meaning type, and perspective.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
K_public = <roles, commitments, conventions, observable events, protocol>; semantics is indexed to K_public.

TENSION:
Context is necessary for meaning but the more context enters the model, the harder universal interoperability becomes.

MISSING:
Typed representation of role and authority changes over protocol execution.

BOUNDARY:
Social context is broader than an FSM state number.

CITATION TRAIL:
Austin circumstances → Winograd/Flores background → Singh social context → commitment protocols

TEST:
Hold a message constant and vary only public role/authority relations; a contextual semantics should alter consequences.

PLATFORM:
[[authority-as-runtime]]

LINKS:
[[austin-1962-authority-as-felicity-condition]]
[[winograd-flores-1986-listening-background]]
[[yolum-singh-2002-event-calculus-operations]]

BIBTEX:
@article{singh1998rethinking, author={Singh, Munindar P.}, title={Agent Communication Languages: Rethinking the Principles}, journal={Computer}, year={1998}, volume={31}, number={12}, pages={40--47}, doi={10.1109/2.735849}}
