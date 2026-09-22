ZETTEL

ID:
20260921-sketchpad-arrowhead-has-fixed-identity-and-flexible-tail

TITLE:
Sketchpad Could Make One Visible “Object” Half Instance and Half Copy

SOURCE:
Ivan E. Sutherland — Sketchpad: A Man-Machine Graphical Communication System — 1963 — chapter 7, “The Mechanics of Copying.” ([cs.virginia.edu](https://www.cs.virginia.edu/~evans/cs6501-s13/sketchpad.pdf?utm_source=chatgpt.com))

PASSAGE:
[PARAPHRASE] Sutherland explicitly describes intermediate ground between rigid instances and fully loose copies. His example copies an instance into a definition so that a diamond arrowhead retains fixed internal structure while its tail remains flexible like an ordinary line. ([cs.virginia.edu](https://www.cs.virginia.edu/~evans/cs6501-s13/sketchpad.pdf?utm_source=chatgpt.com))

RESEARCH OBJECT:
Identity and editability assigned at sub-object granularity rather than to the whole rendered object.

LOCAL MOVE:
The source constructs hybrid objects whose components obey different persistence rules.

SOURCE TERMS:
instance
copy
fixed internal structure
loose internal structure
diamond arrowhead
flexible tail

WHAT BECAME STRANGE:
The question “is this the same object?” becomes too coarse even inside one arrow. The head can preserve instance identity while the tail remains structurally open to modification.

QUESTION:
Should worldtext identity attach independently to components, relations, materials, roles, and histories rather than to whole scene objects?

DEEPER QUESTION:
Can a user say “keep the character the same but change the costume” only if the system represents identity at multiple nested scopes?

MECHANISM:
definition includes rigid instance component
+
flexible copied component
→ composite object drawn
→ edits apply under different rules to different regions
→ one visible whole contains multiple identity regimes.

FORMAL SHIFT:
<OBJECT HAS ONE IDENTITY MODE>
→ <OBJECT CONTAINS NESTED IDENTITY MODES>
→ [EDIT SELECTIVELY]
→ <PARTIAL PERSISTENCE>

SOURCE FORMALISM:
Sutherland distinguishes fixed-internal-structure instances, loose copies, and intermediate constructions made by copying instances. ([cs.virginia.edu](https://www.cs.virginia.edu/~evans/cs6501-s13/sketchpad.pdf?utm_source=chatgpt.com))

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
IdentityScope(entity) =
{
  whole,
  component,
  relation,
  role,
  provenance
}

each may carry distinct persistence semantics.

TENSION:
Fine-grained identity controls can impose excessive representational complexity on users who simply want perceptual continuity.

MISSING:
Methods for inferring likely identity scope from ordinary language without forcing users to manipulate an ontology manually.

BOUNDARY:
Sketchpad’s internal structures are deliberately authored and deterministic. Generative visual systems may not expose stable sub-object decomposition.

CITATION TRAIL:
[[20260921-sketchpad-instance-and-copy-look-alike-but-have-different-futures]]
→ Sutherland’s diamond-arrowhead example
→ identity ceases to be binary even within one displayed object.

TEST:
Create a character object with separately persistent face, body, clothing, pose, and scene role. Test instructions such as “same person, different clothes,” “same outfit, different person,” and “copy the pose only.”

PLATFORM:
[[worldtext]]

LINKS:
[[20260921-sketchpad-instance-and-copy-look-alike-but-have-different-futures]]
[[partial-identity]]
[[instance]]
[[Sketchpad]]

BIBTEX:
@phdthesis{sutherland1963sketchpad,
  author = {Sutherland, Ivan Edward},
  title = {Sketchpad: A Man-Machine Graphical Communication System},
  year = {1963},
  school = {Massachusetts Institute of Technology}
}
