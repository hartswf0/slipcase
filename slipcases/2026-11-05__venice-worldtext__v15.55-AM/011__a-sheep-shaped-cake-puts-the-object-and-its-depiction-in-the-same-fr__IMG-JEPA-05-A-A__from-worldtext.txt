ZETTEL

ID:
IMG-JEPA-05-A-A

TITLE:
A sheep-shaped cake puts the object and its depiction in the same frame

SOURCE:
Randall Balestriero and Yann LeCun — Proving and Improving the Platonic Representation Hypothesis with JEPAs — 2026 — appendix passage “Scaling the captioner”
W. J. T. Mitchell — Ekphrasis and the Other — 1994 — §21

PASSAGE:
[QUOTE — Balestriero and LeCun] “a cake shaped like a sheep”
[QUOTE — Mitchell] “utilitarian objects that happen to have ornamental or symbolic visual representations attached to them”

RESEARCH OBJECT:
An artifact that resembles one thing while being another, photographed for captioning.

LOCAL MOVE:
The JEPA authors mention the sheep-shaped cake in a qualitative report about additional decoder pretraining. Mitchell uses artifacts such as cups and shields to locate early ekphrastic objects within practices of making and use.

SOURCE TERMS:
Recaptions, decoder, ornamental or symbolic visual representations, ekphrastic objects.

WHAT BECAME STRANGE:
[OUR INFERENCE] A caption for the cake may need to distinguish three things: the photograph, the object photographed, and the figure the object presents. A caption can name both cake and sheep while still getting their relation wrong.

QUESTION:
Can the captioner distinguish resemblance, depiction, and physical presence when the same nouns fit all three?

DEEPER QUESTION:
When a model calls something a sheep, is it describing what is present in the photographed space or what an artifact in that space represents?

MECHANISM:
The vision encoder supplies features to a mapped embedding. The decoder turns those features into a sentence. An object-level description must assign different roles to the visible material and to the figure it resembles or depicts.

FORMAL SHIFT:
<Photograph of a representational artifact> → <visual embedding and mapped text embedding> → [caption decoding] → <a sentence that may preserve or collapse representational levels>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
Use separate labels for the physical bearer, the represented figure, and the relation between them. For example, cake / sheep / shaped like differs from cake / sheep / printed on and cake / sheep / next to.

TENSION:
The paper reports that extra pretraining helps some unusual examples without improving Flickr or COCO transfer. The reported example could indicate better recognition of an uncommon artifact or better description of its representational structure.

MISSING:
The specific candidate captions and a controlled comparison that keeps the named objects fixed while changing their relation.

BOUNDARY:
The authors’ phrase identifies an example. It is not a transcript of the model’s caption or a quantified result about representational nesting.

CITATION TRAIL:
[[IMG-JEPA-05-A]] → the JEPA appendix’s qualitative example → Mitchell §21 on the objects of ekphrasis → the Shield as an artifact bearing scenes.

TEST:
Compare a sheep-shaped cake, a cake with a printed sheep, and a plain cake beside a toy sheep. Score noun recognition and relation recognition separately. Repeat with the same Shield scene embossed on metal, printed on a poster, and staged by actors. Ask whether each caption tells the reader where the depicted figures exist.

PLATFORM:
[[Imagetext and Representational Nesting]]

LINKS:
[[IMG-JEPA-05-A]]
[[Shield of Achilles]]
[[Bearer and Depicted Figure]]
[[Description of a Representation]]

BIBTEX:
@misc{balestriero2026platonic,
  author = {Balestriero, Randall and LeCun, Yann},
  title = {Proving and Improving the Platonic Representation Hypothesis with {JEPAs}},
  year = {2026},
  eprint = {2610.39302},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/html/2610.39302v1}
}
@incollection{mitchell1994ekphrasis,
  author = {Mitchell, W. J. T.},
  title = {Ekphrasis and the Other},
  booktitle = {Picture Theory: Essays on Verbal and Visual Representation},
  publisher = {University of Chicago Press},
  year = {1994},
  url = {https://complit.utoronto.ca/wp-content/uploads/COL1000-Week11-Nov25_WJT_Mitchell.pdf}
}