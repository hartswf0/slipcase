ZETTEL

ID:
Z-SLIP-018

TITLE:
Autonomous inquiry requires a principled condition for surrendering priority back to a human

SOURCE:
Watson Hartsoe — PRIME ZETTEL FORAGE — AUTONOMOUS GRAPH INQUIRY — 2026 — “stopping”

PASSAGE:
[PARAPHRASE]
The research daemon should stop not only when budgets or evidence are exhausted, but when the graph reaches a state in which a human choice of research priority would be more valuable than automatic continuation. It must never manufacture findings merely to keep the loop running.

RESEARCH OBJECT:
A useful autonomous research system needs a deference criterion, not merely a stopping criterion.

LOCAL MOVE:
The daemon treats human intervention as epistemically valuable when the unresolved frontier becomes a question of priorities rather than information retrieval.

SOURCE TERMS:
stopping
human choice
research priority
automatic continuation
available evidence
duplicate
unavailable sources

WHAT BECAME STRANGE:
Automation may fail not because it cannot continue, but because continuing would require choosing what ought to matter.

QUESTION:
How can a research system detect the transition from an epistemic decision to a value-laden priority decision?

DEEPER QUESTION:
Is knowing when not to choose a research direction a necessary component of research autonomy?

MECHANISM:
The daemon evaluates whether remaining edges can be discriminated through evidence and whether automatic search is still likely to add informational value; when priority judgment dominates, control should leave the autonomous loop.

FORMAL SHIFT:
<open research frontier>
→ <classify remaining uncertainty>
→ [CONTINUE | DEFER]
→ <machine forage or human priority choice>

SOURCE FORMALISM:
Stop when:
budget exhausted;
evidence cannot discriminate;
work would duplicate;
sources unavailable;
or human research-priority choice is more valuable.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

CONTINUE iff
EXPECTED_EVIDENTIARY_GAIN >
EXPECTED_VALUE_OF_HUMAN_PRIORITY_JUDGMENT

TENSION:
The system itself must estimate when human judgment is more valuable, which seems to require the very normative competence it is supposed to defer.

MISSING:
Observable indicators that distinguish “hard research problem” from “human priority decision.”

BOUNDARY:
The prompt states the deference principle but does not provide an operational detector.

CITATION TRAIL:
[[deference boundary]]
→ mixed-initiative systems
→ selective prediction
→ abstention
→ human-in-the-loop decision theory

TEST:
Collect daemon stopping decisions across a large graph and ask independent researchers whether each frontier required more evidence or a substantive choice of values/priorities. Compare classifications.

PLATFORM:
[[bounded research autonomy]]

LINKS:
[[human deference]]
[[active frontier]]
[[research attention allocation]]
[[abstention]]

BIBTEX:
@misc{hartsoe2026graphdaemon,
  author = {Hartsoe, Watson},
  title = {Prime Zettel Forage: Autonomous Graph Inquiry},
  year = {2026},
  note = {Working prompt specification}
}
