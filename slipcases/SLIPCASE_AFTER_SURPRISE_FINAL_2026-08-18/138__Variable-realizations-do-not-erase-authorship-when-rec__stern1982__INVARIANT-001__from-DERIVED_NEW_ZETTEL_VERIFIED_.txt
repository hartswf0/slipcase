ZETTEL

ID:
INVARIANT-001

TITLE:
Variable realizations do not erase authorship when recurring expressive invariants remain attributable upstream.

SOURCE:
Stern Electronics, Inc. v. Kaufman — 669 F.2d 852 — U.S. Court of Appeals for the Second Circuit — 1982 — especially 669 F.2d at 856–57.

SOURCE URL:
https://law.justia.com/cases/federal/appellate-courts/F2/669/852/149312/

PASSAGE:
[PARAPHRASE]
Stern accepts that each play produces a different sequence because of player action but holds that substantial recurring visual and aural elements remain fixed and original. The underlying program and the audiovisual work can also exist as distinct copyright objects.

RESEARCH OBJECT:
AUTHORSHIP OF INVARIANTS ACROSS VARIABLE REALIZATIONS.

LOCAL MOVE:
Instead of asking whether a user determines every token, ask which stable expressive relations recur across variation and who introduced them.

SOURCE TERMS:
player participation
repetitive sequence
constant
originality
program
audiovisual work

WHAT BECAME STRANGE:
A variable process can have a stable authored skeleton even when no single realization is fully predetermined.

QUESTION:
Can human-authored constraints in a generative system be identified as cross-realization invariants rather than exact token-level determinations?

DEEPER QUESTION:
How can one distinguish an invariant introduced by the user from an invariant already supplied by the model’s learned defaults?

MECHANISM:
Generate family Y under human constraint c. Extract recurring relations Inv(Y|c). Compare to baseline Inv(Y|c_0). Attribute only differences causally tied to c.

FORMAL SHIFT:
<EXACT OUTPUT CONTROL> → <ATTRIBUTABLE CROSS-REALIZATION INVARIANTS>

SOURCE FORMALISM:
Stern’s legal reasoning distinguishes variable player-controlled sequences from recurring audiovisual elements fixed in memory devices.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
HInv(c)=Inv(Y|do(c))−Inv(Y|baseline), evaluated over artistically relevant features rather than raw pixels.

TENSION:
Statistical recurrence is not the same as statutory fixation, and an invariant can be too abstract to constitute protectable expression.

MISSING:
A feature representation and fixation theory suitable for probabilistic constraint systems.

BOUNDARY:
This does not establish “distributional authorship.” It identifies a narrower evidentiary object: stable expression attributable to a human constraint.

CITATION TRAIL:
[[RETENTION-005-S-B]] → Stern → recurring structure across variable play → attributable invariants.

TEST:
Generate matched output populations with and without a human constraint. Identify properties whose stability changes materially. Then verify that the maker actually originated and intended those properties rather than inheriting them from model defaults.

PLATFORM:
[[class-is-not-a-path]]

LINKS:
[[RETENTION-005-S-B]]
[[RETENTION-005-S-C]]
[[expressive-invariants]]

BIBTEX:
@misc{stern1982,
  title        = {Stern Electronics, Inc. v. Kaufman},
  howpublished = {669 F.2d 852 (2d Cir. 1982)},
  year         = {1982}
}
