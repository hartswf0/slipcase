ZETTEL

ID:
Z-SLIP-002

TITLE:
A ghost is not missing information but a declared future object

SOURCE:
Watson Hartsoe — SLIPCASE — 2026 — “The relations get compiled”

PASSAGE:
[PARAPHRASE]
An unresolved declared address becomes a ghost. Ghosts are published rather than hidden, and those receiving multiple inbound links become promising forage targets.

RESEARCH OBJECT:
An unresolved reference can become a positive research object when the system preserves its identity and inbound demand.

LOCAL MOVE:
SLIPCASE converts failed resolution from an error state into prospective structure.

SOURCE TERMS:
ghost
unresolved
address
inbound links
conceptual attractor
forage target
broken link

WHAT BECAME STRANGE:
The archive may know that an idea is important before anyone has written the note describing it.

QUESTION:
Can an archive discover a concept before it possesses content for that concept?

DEEPER QUESTION:
Is a sufficiently connected absence already a weak form of knowledge?

MECHANISM:
Independent cards emit the same unresolved address; relation compilation aggregates those references; repeated convergence produces a visible empty node; that node becomes a candidate for investigation.

FORMAL SHIFT:
<unwritten but repeatedly named concept>
→ <persistent unresolved address>
→ [INVERT LINKS + COUNT INBOUND REFERENCES]
→ <visible conceptual attractor>

SOURCE FORMALISM:
ghost = declared [[ADDRESS]] with no conservatively resolvable card

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

GHOST(g) :=
unresolved(g) ∧ indegree(g) ≥ 1

ATTRACTOR(g) :=
GHOST(g) ∧ independent_origins(g) ≥ 2

LIVE_EDGE(g) :=
ATTRACTOR(g) ∧ occurrence_in(g,
 {QUESTION, DEEPER_QUESTION, MISSING, CITATION_TRAIL, TEST})

TENSION:
High indegree can reflect repeated vocabulary, bad naming practice, or copied assumptions rather than genuine conceptual importance.

MISSING:
A notion of independent origin strong enough to distinguish genuine convergence from copying or template inheritance.

BOUNDARY:
Link frequency alone does not establish scholarly significance.

CITATION TRAIL:
Information retrieval work on query expansion and latent needs; graph-theoretic treatments of missing nodes; Luhmann on references to unwritten continuations; open-world knowledge representation.

TEST:
Compare the top ten high-indegree ghosts against expert-chosen future research questions across several mature checkpoints.

PLATFORM:
[[ghosts as positive research objects]]

LINKS:
[[conceptual attractor]]
[[negative space]]
[[forage target]]
[[open world archive]]

BIBTEX:
@misc{hartsoe2026slipcase,
  author = {Hartsoe, Watson},
  title = {SLIPCASE: A Research Checkpoint Compiler},
  year = {2026},
  note = {Working specification}
}
