ZETTEL

ID:
Z-SLIP-011

TITLE:
Lineage addresses make intellectual descent visible but may confuse descent with identity

SOURCE:
Watson Hartsoe — SLIPCASE — 2026 — “Three ancestors”; “Status”

PASSAGE:
[PARAPHRASE]
SLIPCASE retains original IDs and extends them for descendants, so an identifier such as Z-CEPTR-002-K1-K2 records a chain of descent. The durability of this identity scheme under long-term merging remains unresolved.

RESEARCH OBJECT:
Encoding genealogy directly into identifiers makes derivation legible but creates tension when objects merge, split, migrate, or acquire multiple parents.

LOCAL MOVE:
Identity is made historically informative instead of opaque.

SOURCE TERMS:
original ID
address
descent
child
lineage
merge
derived identity

WHAT BECAME STRANGE:
An identifier that tells a story about where an object came from may become less stable precisely because intellectual objects can have more than one ancestry.

QUESTION:
Can a research object simultaneously have a stable identity and an identifier that encodes its evolving genealogy?

DEEPER QUESTION:
Should identity record descent, or should descent be a relation attached to identity?

MECHANISM:
Descendants inherit and extend parent identifiers, preserving a readable path through recursive forage.

FORMAL SHIFT:
<research object with parent>
→ <lineage-bearing identifier>
→ [EXTEND ID]
→ <human-readable descent>

SOURCE FORMALISM:
Example:
Z-CEPTR-002-K1-K2

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

If ID encodes lineage:

ID(child) = ID(parent) + derivation token

But for merge:
child = f(parent_A, parent_B)

No single linear identifier preserves both ancestries without becoming structurally complex.

TENSION:
Human-readable descent and permanent location-independent identity may be incompatible goals.

MISSING:
A merge semantics for cards with multiple intellectual ancestors.

BOUNDARY:
The lineage scheme works straightforwardly for trees but has not been shown to survive graph-shaped derivation.

CITATION TRAIL:
Content-addressable identifiers; Merkle DAGs; version control commit graphs; archival provenance; genealogical identifiers.

TEST:
Construct adversarial merge histories—two-parent merges, split/recombine, duplicate discovery, independent rediscovery—and attempt to preserve stable IDs without losing ancestry.

PLATFORM:
[[identity versus genealogy]]

LINKS:
[[derived identity]]
[[merge semantics]]
[[address by identity]]
[[research DAG]]

BIBTEX:
@misc{hartsoe2026slipcase,
  author = {Hartsoe, Watson},
  title = {SLIPCASE: A Research Checkpoint Compiler},
  year = {2026},
  note = {Working specification}
}
