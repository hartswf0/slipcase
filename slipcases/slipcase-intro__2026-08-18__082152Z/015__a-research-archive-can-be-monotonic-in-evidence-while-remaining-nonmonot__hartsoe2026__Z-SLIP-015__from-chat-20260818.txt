ZETTEL

ID:
Z-SLIP-015

TITLE:
A research archive can be monotonic in evidence while remaining nonmonotonic in interpretation

SOURCE:
Watson Hartsoe — SLIPCASE — PORTABLE RESEARCH FIELD — 2026 — “model”; “laws”

PASSAGE:
[PARAPHRASE]
SLIPCASE separates EVIDENCE, FIELD, and INTERPRETATION. Evidence is preserved, field structure is compiled, and interpretation remains revisable. Existing zettel payloads are immutable rather than rewritten.

RESEARCH OBJECT:
The architecture permits knowledge revision without evidence mutation by making accumulation and interpretation obey different temporal rules.

LOCAL MOVE:
What appears to be a preservation convention becomes an epistemic architecture: evidence accumulates while theses, maps, MOCs, and arrangements may be abandoned.

SOURCE TERMS:
EVIDENCE
FIELD
INTERPRETATION
immutable payload
compiled
revisable

WHAT BECAME STRANGE:
Changing one's mind does not require changing one's notes.

QUESTION:
Could a research system support radical theoretical revision while maintaining an append-only evidentiary substrate?

DEEPER QUESTION:
What kinds of scholarly disagreement become easier when competing interpretations share an immutable evidentiary history?

MECHANISM:
New evidence enters as new immutable objects; relations are recompiled; interpretations can be discarded and regenerated without deleting earlier receipts.

FORMAL SHIFT:
<mutable notebook>
→ <append-only evidence + recomputable relations>
→ [REINTERPRET]
→ <revisable scholarly state>

SOURCE FORMALISM:
EVIDENCE:
ZETTEL · SOURCE · RESOURCE · PROMPT · APPEARANCE

FIELD:
PLATFORM · LINK · CONCEPT · GHOST · BACKLINK · LINEAGE

INTERPRETATION:
MOC · ARRANGEMENT · TRAIL · PAPER

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

E_(t+1) ⊇ E_t

I_(t+1) need not contain I_t

Therefore:

EVIDENCE HISTORY = monotonic

INTERPRETATION HISTORY = nonmonotonic

TENSION:
Evidence is never interpretation-free: admitting something as a zettel, selecting its boundaries, assigning identity, and deciding what counts as a source already contain judgment.

MISSING:
A distinction between immutable source payload and the revisable admission decision that made it a research object.

BOUNDARY:
Immutability protects history but cannot make the archive epistemically neutral.

CITATION TRAIL:
[[monotonic evidence nonmonotonic interpretation]]
→ truth-maintenance systems
→ append-only event sourcing
→ nonmonotonic logic
→ versioned scientific knowledge

TEST:
Take a checkpoint whose central thesis has been defeated. Recompile a contradictory interpretation without modifying or deleting any admitted evidence and record exactly where the old architecture obstructs the new reading.

PLATFORM:
[[evidence architecture]]

LINKS:
[[paper as compiled view]]
[[immutable evidence]]
[[revisable interpretation]]
[[append-only scholarship]]

BIBTEX:
@misc{hartsoe2026slipcasearchitecture,
  author = {Hartsoe, Watson},
  title = {SLIPCASE: Portable Research Field},
  year = {2026},
  note = {Working system specification}
}
