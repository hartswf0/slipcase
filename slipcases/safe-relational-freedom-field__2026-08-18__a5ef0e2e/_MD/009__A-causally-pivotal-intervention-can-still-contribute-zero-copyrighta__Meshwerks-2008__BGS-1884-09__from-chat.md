ZETTEL

ID:
BGS-1884-09

TITLE:
A causally pivotal intervention can still contribute zero copyrightable authorship

SOURCE:
U.S. Court of Appeals for the Tenth Circuit — Meshwerks, Inc. v. Toyota Motor Sales U.S.A., Inc. — 2008 — 528 F.3d 1258.

PASSAGE:
[PARAPHRASE]
Meshwerks performed extensive technical labor to translate Toyota vehicles into digital wire-frame models. The court nevertheless characterized its contribution as a “narrow, if pivotal, role”: expressive decisions such as backgrounds, lighting, angles, and colors were left to later creators.

RESEARCH OBJECT:
“Effective cause” cannot mean mere causal indispensability. A participant can be necessary to the production pipeline, technically skilled, labor-intensive, and even pivotal while contributing none of the expression copyright recognizes as its own.

LOCAL MOVE:
The court separates causal contribution from original expressive contribution.

SOURCE TERMS:
narrow
pivotal
original to the author
independently created
copying
expressively manipulated by others

WHAT BECAME STRANGE:
The strongest version of [[BGS-1884-05]] now breaks.

If authorship meant “the effective cause” in ordinary causal language, Meshwerks should look extraordinarily authorial: without its intervention, the later digital artifacts could not have been made in the same way.

Yet the court says precisely the opposite.

Causal necessity is therefore too weak.

QUESTION:
What kind of causation does copyright mean when it says a work “owes its origin” to an author?

DEEPER QUESTION:
Is authorship not causation of the artifact at all, but causation of the artifact’s protectable differences?

MECHANISM:
Meshwerks:
physical vehicle
→ highly skilled measurement
→ digital model
→ later expressive manipulation

The technically decisive transformation does not itself establish authorship because its governing purpose is faithful copying rather than the production of independently originated expressive difference.

FORMAL SHIFT:
<CAUSAL CONTRIBUTION>
→ <ASK WHAT DIFFERENCE THE CONTRIBUTOR ORIGINATED>
→ [FILTER COPIED / GIVEN FEATURES]
→ <AUTHORSHIP ONLY IN REMAINING ORIGINAL DIFFERENCE>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

BUT-FOR CAUSE ≠ AUTHORSHIP CAUSE

A stronger candidate:

AUTHORSHIP_CAUSE(x,w)
requires
CAUSE(x, Δexpressive(w))

not merely
CAUSE(x, existence(w))

TENSION:
Burrow-Giles describes the photographer as the “effective cause” of the photograph, while Meshwerks refuses copyright to an actor occupying a demonstrably pivotal causal position.

The two cases become compatible only if “effective” silently means effective with respect to original expression rather than effective with respect to production generally.

MISSING:
A doctrine-level account of what counts as an expressive difference caused by a participant rather than merely transmitted, measured, reproduced, or exposed by that participant.

BOUNDARY:
Meshwerks concerns digital models deliberately designed to reproduce preexisting vehicles. It does not establish that technologically mediated transformations are inherently uncreative.

CITATION TRAIL:
[[BGS-1884-05]]
→ Nottage / “effective cause”
→ Meshwerks / “narrow, if pivotal”
→ distinguish causal indispensability from expressive origination

TEST:
Construct cases in which the same human intervention is equally necessary to production but varies only in how much expressive difference it introduces.

Ask whether copyright tracks necessity or originated difference.

PLATFORM:
[[Expressive Causation]]

LINKS:
[[BGS-1884-05]]
[[BGS-1884-08]]
[[Effective Cause]]
[[Causal Traceability]]

BIBTEX:
@case{MeshwerksToyota2008,
  title = {Meshwerks, Inc. v. Toyota Motor Sales U.S.A., Inc.},
  year = {2008},
  note = {528 F.3d 1258 (10th Cir.)}
}
