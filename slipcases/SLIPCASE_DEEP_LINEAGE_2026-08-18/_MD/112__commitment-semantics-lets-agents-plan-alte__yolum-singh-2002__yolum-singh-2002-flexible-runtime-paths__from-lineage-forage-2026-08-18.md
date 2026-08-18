ZETTEL

ID:
yolum-singh-2002-flexible-runtime-paths

TITLE:
Commitment semantics lets agents plan alternative runtime paths while preserving social obligations.

SOURCE:
Pınar Yolum and Munindar P. Singh — “Flexible Protocol Specification and Execution: Applying Event Calculus Planning Using Commitments” — 2002 — AAMAS

SOURCE URL:
https://www.csc2.ncsu.edu/faculty/mpsingh/papers/mas/aamas-02-protocols.pdf

PASSAGE:
[SOURCE SUMMARY] Agents can reason and plan over commitment states, exploiting opportunities and handling exceptions without being bound to a single pre-enumerated message sequence.

RESEARCH OBJECT:
SEMANTIC CONSTRAINT WITH TRAJECTORY FREEDOM

LOCAL MOVE:
Find a computational answer to Suchman’s sequence-rigidity problem that does not simply abandon formal semantics.

SOURCE TERMS:
planning; commitments; flexible protocol; exception; opportunity; execution

WHAT BECAME STRANGE:
Formalization need not mean a rigid path: the invariant can be a normative state relation while concrete sequences remain open.

QUESTION:
Could human workflow systems use public commitments as constraints while leaving conversational realization open?

DEEPER QUESTION:
Would that solve category politics, or merely move power from transition tables into commitment definitions?

MECHANISM:
<current commitments + goals + available actions> → [PLAN] → <one of multiple normatively valid traces>

FORMAL SHIFT:
fixed finite-state path → constraint-based runtime planning

SOURCE FORMALISM:
Event-calculus commitment model combined with planning to generate protocol behavior.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
VALID_PATHS(K) = {trace | trace preserves/discharges normative commitments}; choose trace at runtime.

TENSION:
Trajectory freedom increases autonomy but leaves the ontology of commitments, authority, and evidence politically consequential.

MISSING:
Human-centered protocol design that combines trajectory freedom with interpretive contestability and explicit power analysis.

BOUNDARY:
Commitment flexibility addresses sequence rigidity, not every problem Suchman identifies about categorization and situated meaning.

CITATION TRAIL:
Suchman critique || commitment-protocol research → possible contestable institutional runtime

TEST:
Replace a human workflow FSM with commitment constraints and compare freedom of action, auditability, and dispute handling.

PLATFORM:
[[protocol-contestability]]

LINKS:
[[suchman-1993-category-discipline]]
[[winograd-flores-1986-background-free-language-limit]]
[[yolum-singh-2002-sequence-overconstraint]]

BIBTEX:
@inproceedings{yolumsingh2002flexible, author={Yolum, Pınar and Singh, Munindar P.}, title={Flexible Protocol Specification and Execution: Applying Event Calculus Planning Using Commitments}, booktitle={Proceedings of the First International Joint Conference on Autonomous Agents and Multiagent Systems}, year={2002}, pages={527--534}, publisher={ACM}, doi={10.1145/544862.544867}}
