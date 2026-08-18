ZETTEL

ID:
Z-SLIP-013

TITLE:
Recursive research objects require a second state that must never become part of the object

SOURCE:
Watson Hartsoe — Combined FORAGE / RESEARCH DAEMON / SLIPCASE prompt architecture — 2026 — “Recursive Inquiry”; “Autonomous Graph Inquiry”

PASSAGE:
[PARAPHRASE]
The recursive forager requires every child to preserve exactly the same ZETTEL type so that any output can immediately become another input. The graph daemon simultaneously maintains ZETTEL_SET, EDGE_SET, ACTIVE_FRONTIER, VISITED_EDGES, OPEN_CONTRADICTIONS, and SOURCE_HUBS, but explicitly forbids this orchestration state from entering the ZETTEL syntax.

RESEARCH OBJECT:
Recursive research requires a separation between the invariant research object and the changing state of inquiry over those objects.

LOCAL MOVE:
The combined architecture discovers that recursion alone is insufficient. Something outside the recursive type must remember which possibilities have been explored, which contradictions remain open, and which edge should be pursued next.

SOURCE TERMS:
ZETTEL
recursive type
ACTIVE_FRONTIER
VISITED_EDGES
OPEN_CONTRADICTIONS
SOURCE_HUBS
orchestration state

WHAT BECAME STRANGE:
A self-forageable card is not a self-directing research system.

QUESTION:
What is the minimum external state required to turn recursively forageable research objects into sustained inquiry?

DEEPER QUESTION:
Can orchestration state remain disposable if losing it changes what the system would investigate next?

MECHANISM:
ZETTELS preserve local intellectual state while an external controller maintains global search state and chooses subsequent operations.

FORMAL SHIFT:
<recursive research object>
→ <invariant ZETTEL + external inquiry state>
→ [SELECT FRONTIER EDGE]
→ <continued graph inquiry>

SOURCE FORMALISM:
FORAGE : ZETTEL → ZETTEL[]

Internal daemon state:
ZETTEL_SET
EDGE_SET
ACTIVE_FRONTIER
VISITED_EDGES
OPEN_CONTRADICTIONS
SOURCE_HUBS

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

RESEARCH_SYSTEM =
  IMMUTABLE_OBJECTS
  +
  MUTABLE_ORCHESTRATION_STATE

where:

OBJECT_STATE is portable

ORCHESTRATION_STATE determines attention

TENSION:
SLIPCASE privileges preserved evidence and regenerable derived structures, but orchestration history may itself contain irrecoverable information about abandoned paths, skipped edges, and why one branch was chosen over another.

MISSING:
A classification of which orchestration state is mechanically reconstructible and which constitutes consequential research history.

BOUNDARY:
The prompts establish the separation but do not prove that the external state can safely disappear.

CITATION TRAIL:
[[research orchestration as provenance]]
→ workflow systems
→ search-state persistence
→ scientific workflow provenance

TEST:
Run the same ZETTEL graph twice, once with preserved daemon state and once after reconstructing state only from the cards. Compare the next ten selected research edges.

PLATFORM:
[[recursive research architecture]]

LINKS:
[[Z-SLIP-003]]
[[research orchestration as provenance]]
[[active frontier]]
[[recursive type]]

BIBTEX:
@misc{hartsoe2026combinedforage,
  author = {Hartsoe, Watson},
  title = {Combined FORAGE, Research Daemon, and SLIPCASE Prompt Architecture},
  year = {2026},
  note = {Working research-system specification}
}
