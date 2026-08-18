ZETTEL

ID:
singh-1998-public-perspective-testability

TITLE:
A normative communication standard needs semantics whose compliance can be tested from a public perspective.

SOURCE:
Munindar P. Singh — “Agent Communication Languages: Rethinking the Principles” — 1998 — Computer 31(12):40–47

SOURCE URL:
https://www.csc2.ncsu.edu/faculty/mpsingh/papers/mas/computer-acl-98.pdf

PASSAGE:
[SOURCE SUMMARY] Singh argues that standards are useless without testable compliance and that testability requires a public perspective emphasizing social agency rather than inaccessible private mental states.

RESEARCH OBJECT:
PUBLIC TESTABILITY AS A SEMANTIC DESIGN REQUIREMENT

LOCAL MOVE:
Change the criterion for a good communication semantics from psychological plausibility to observable normative accountability.

SOURCE TERMS:
compliance; testable; public perspective; social agency; interoperability; autonomous; heterogeneous

WHAT BECAME STRANGE:
The semantics problem becomes institutional: not “what did the sender mean internally?” but “what public relation now holds and who complied?”

QUESTION:
What public facts are sufficient to determine whether a communicative act complied with a protocol?

DEEPER QUESTION:
Can public testability coexist with interpretive ambiguity and contested institutional facts?

MECHANISM:
<public message/event trace> → [EVALUATE AGAINST SOCIAL SEMANTICS] → <compliance/noncompliance/underdetermined>

FORMAL SHIFT:
private mental-state meaning → public social meaning

SOURCE FORMALISM:
Singh presents a conceptual design space contrasting private/public perspective, personal/conventional meaning, fixed/flexible context, and other dimensions.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
COMPLIANT(agent,protocol,trace) must be decidable from public protocol state plus publicly admissible evidence.

TENSION:
Public semantics improves accountability but can privilege what the institution can observe over what participants understand or intend.

MISSING:
A theory of contested evidence and partial observability inside public semantics.

BOUNDARY:
Singh does not argue that private mental states are irrelevant to agent design; he relocates them away from normative standard semantics.

CITATION TRAIL:
mentalistic ACLs → Singh 1998 public social semantics → commitment protocols

TEST:
Black-box test a protocol implementation without inspecting agent internals. Any semantic condition that cannot be checked is not public.

PLATFORM:
[[private-to-public-semantics]]

LINKS:
[[fipa-2002-mental-attitude-model]]
[[yolum-singh-2002-commitment-as-action-meaning]]
[[suchman-1993-category-discipline]]

BIBTEX:
@article{singh1998rethinking, author={Singh, Munindar P.}, title={Agent Communication Languages: Rethinking the Principles}, journal={Computer}, year={1998}, volume={31}, number={12}, pages={40--47}, doi={10.1109/2.735849}}
