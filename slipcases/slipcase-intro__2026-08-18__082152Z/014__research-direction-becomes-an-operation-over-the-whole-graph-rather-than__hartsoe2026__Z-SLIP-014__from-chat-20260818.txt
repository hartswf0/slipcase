ZETTEL

ID:
Z-SLIP-014

TITLE:
Research direction becomes an operation over the whole graph rather than inheritance from the latest note

SOURCE:
Watson Hartsoe — PRIME ZETTEL FORAGE — AUTONOMOUS GRAPH INQUIRY — 2026 — “loop_command”

PASSAGE:
[PARAPHRASE]
The daemon surveys the entire supplied graph, determines an active frontier, selects the unresolved edge most capable of changing understanding, forages it, adds the resulting children, and then reconsiders the entire graph rather than continuing automatically from the newest branch. Its objective is not zettel count but changes in what the graph knows to ask.

RESEARCH OBJECT:
Choosing what to investigate next is itself a first-class research operation.

LOCAL MOVE:
The daemon breaks the assumption that research genealogy should also determine research attention.

SOURCE TERMS:
ACTIVE FRONTIER
expected epistemic gain
entire graph
newest branch
most promising question
changes in what the graph knows to ask

WHAT BECAME STRANGE:
Parentage tells us where a question came from but not whether it deserves the next unit of attention.

QUESTION:
What should determine the allocation of research attention when lineage, novelty, uncertainty, and potential consequence point toward different edges?

DEEPER QUESTION:
Can “expected epistemic gain” be operationalized without forcing inquiry to optimize only what its current representation can already recognize as valuable?

MECHANISM:
Global survey detaches edge selection from generation order and reallocates attention toward unresolved relations expected to alter multiple interpretations.

FORMAL SHIFT:
<latest generated node>
→ <global unresolved frontier>
→ [STEER]
→ <highest-value next inquiry>

SOURCE FORMALISM:
Survey graph
→ determine ACTIVE_FRONTIER
→ choose edge
→ forage
→ oppose
→ emit
→ update graph
→ reassess

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

NEXT_EDGE =
argmax(e ∈ ACTIVE_FRONTIER)
EXPECTED_GRAPH_CHANGE(e)

TENSION:
A system can only estimate epistemic gain using features already represented in the graph. The most transformative question may therefore receive a low score precisely because the archive lacks vocabulary for its importance.

MISSING:
A novelty mechanism capable of surfacing edges that are low-connectivity, low-frequency, or poorly represented but potentially field-changing.

BOUNDARY:
The architecture defines a steering principle, not a validated measure of epistemic gain.

CITATION TRAIL:
[[epistemic gain]]
→ active learning
→ optimal experimental design
→ curiosity-driven search
→ value of information

TEST:
Compare global-frontier steering against depth-first lineage following and random edge selection on the same checkpoint. Measure how often each strategy changes multiple existing interpretations rather than merely adding leaves.

PLATFORM:
[[research attention allocation]]

LINKS:
[[Z-SLIP-003]]
[[active frontier]]
[[expected epistemic gain]]
[[representation blind spot]]

BIBTEX:
@misc{hartsoe2026graphdaemon,
  author = {Hartsoe, Watson},
  title = {Prime Zettel Forage: Autonomous Graph Inquiry},
  year = {2026},
  note = {Working prompt specification}
}
