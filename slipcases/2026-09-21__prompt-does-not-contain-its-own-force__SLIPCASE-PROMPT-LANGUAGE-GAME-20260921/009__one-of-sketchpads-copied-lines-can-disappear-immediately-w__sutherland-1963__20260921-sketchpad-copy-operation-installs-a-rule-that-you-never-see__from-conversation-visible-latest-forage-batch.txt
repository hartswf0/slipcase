ZETTEL

ID:
20260921-sketchpad-copy-operation-installs-a-rule-that-you-never-see

TITLE:
One of Sketchpad’s Copied Lines Can Disappear Immediately While Its Constraint Survives

SOURCE:
Ivan E. Sutherland — Sketchpad: A Man-Machine Graphical Communication System — 1963 — p. 106. ([studylib.net](https://studylib.net/doc/13354892/technical-report-sketchpad--a-man-machine-graphical-commu...?utm_source=chatgpt.com))

PASSAGE:
[PARAPHRASE] Sutherland describes a definition containing two lines constrained to equal length, both designated as attachers. When copied while aiming at an existing line, the first copied line merges into that target and is never seen as a separate object. The second remains attached to the light pen until it is merged with another target line. The copied equal-length constraint then governs the two pre-existing lines.

RESEARCH OBJECT:
Copying an invisible relational structure into existing objects without leaving a visible copied artifact corresponding to every copied part.

LOCAL MOVE:
The operation called “copy” functions partly as rule installation: graphical scaffolding is consumed during merge while the relation it carried persists.

SOURCE TERMS:
copy
merge
attacher
equal length
constraint
recursive
never actually being seen

WHAT BECAME STRANGE:
The user performs an apparently graphical operation, yet the most consequential copied thing is not a visible shape. What survives is a law over future geometry.

QUESTION:
How can a generative interface show that an operation installed a persistent rule when the immediate rendered world looks almost unchanged?

DEEPER QUESTION:
What visual grammar distinguishes “I changed this object once” from “I changed the future behavior of this object”?

MECHANISM:
definition contains geometry + constraint
→ copy invoked
→ copied attacher merges into target A
→ visible copy disappears into A
→ second attacher merges into target B
→ equality relation survives
→ future changes to A/B remain coupled.

FORMAL SHIFT:
<COPY OBJECT>
→ <COPY RELATION-BEARING STRUCTURE>
→ [MERGE SCAFFOLDING AWAY]
→ <PERSISTENT RULE OVER EXISTING OBJECTS>

SOURCE FORMALISM:
Sketchpad supports attachers, merge, recursive merging, explicit geometric constraints, copies, and instances. ([studylib.net](https://studylib.net/doc/13354892/technical-report-sketchpad--a-man-machine-graphical-commu...?utm_source=chatgpt.com))

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
operation_result =
visible_delta
+
persistent_rule_delta

where visible_delta may approach zero while rule_delta remains substantial.

TENSION:
A visible badge for every persistent rule can itself become clutter that obscures the geometry it is meant to explain.

MISSING:
Interaction forms for revealing latent rules on demand without permanently saturating the scene.

BOUNDARY:
Sketchpad’s rule is deterministic and explicit. A system-prompt or model-mediated instruction can have softer, conditional, or stochastic persistence.

CITATION TRAIL:
[[20260921-sketchpad-copies-a-relation-not-just-a-shape]]
→ exact equal-length copy/merge sequence
→ the copied artifact can vanish while copied causality persists.

TEST:
Create two visually identical pairs of beams: one manually made equal once, one constrained equal persistently. Hide all metadata, then ask users to predict effects of dragging one beam. Add progressively richer rule visualization and repeat.

PLATFORM:
[[inspectable-pipeline]]

LINKS:
[[20260921-sketchpad-copies-a-relation-not-just-a-shape]]
[[persistent-rule]]
[[constraint]]
[[Sketchpad]]

BIBTEX:
@phdthesis{sutherland1963sketchpad,
  author = {Sutherland, Ivan Edward},
  title = {Sketchpad: A Man-Machine Graphical Communication System},
  year = {1963},
  school = {Massachusetts Institute of Technology}
}
