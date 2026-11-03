ZETTEL

ID:
IMG-JEPA-02-B-A

TITLE:
A detail that crosses scenes can belong to the composite work

SOURCE:
Randall Balestriero and Yann LeCun — Proving and Improving the Platonic Representation Hypothesis with JEPAs — 2026 — §2.3 and Appendix B, Table 7
W. J. T. Mitchell — Beyond Comparison: Picture, Text, and Method — 1994 — Picture Theory, p. 89 n. 9, as reprinted in his introduction to The Future of Text and Image

PASSAGE:
[QUOTE — Balestriero and LeCun] “alt-texts sharing a brand name”
[QUOTE — Mitchell] “composite, synthetic works (or concepts) that combine image and text”

RESEARCH OBJECT:
A brand name that connects photographs of different scenes and also connects each photograph to the page on which it appears.

LOCAL MOVE:
The JEPA paper uses a repeated brand name to illustrate how overlapping text corruptions can create links across scenes. Mitchell’s imagetext shifts the unit of analysis to the work made by combining the verbal and visual materials.

SOURCE TERMS:
Alt-text, nuisance, induced world kernel, imagetext.

WHAT BECAME STRANGE:
[OUR INFERENCE] The same word can be a shortcut for matching photographs and an indispensable part of understanding how a photograph is published. Removing it could make the text a better view of the pictured scene while making it a poorer account of the page.

QUESTION:
When does a recaption describe the photographed thing more accurately while describing the published imagetext less adequately?

DEEPER QUESTION:
Should a visible logo, a merchant name supplied by the page, and a merchant name hallucinated by the captioner count as three different kinds of evidence?

MECHANISM:
In the paper’s example, shared wording can cause corruptions of texts from distinct scenes to overlap. In a published composite, wording can intentionally connect distinct scenes through sponsorship, authorship, or a series title. The visible pixels can remain identical across those contexts.

FORMAL SHIFT:
<Photograph embedded in a page> → <image ID and associated text strings> → [caption replacement or positive pairing] → <different relations become available to the encoder>

SOURCE FORMALISM:
The induced world kernel gives the probability that a positive pair joins observations of two specified states.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
Give each phrase separate provenance labels for pixel evidence and page evidence. Keep unsupported claims distinct from supported claims that require the page.

TENSION:
Table 7 favors different caption mixtures on Flickr retrieval and WIT alignment. That difference makes the target worth specifying. It does not explain whether the difference comes from literalness, caption genre, or another property of the data.

MISSING:
The original page as evidence alongside the isolated image and its text fields.

BOUNDARY:
The brand example illustrates an alignment mechanism. It cannot establish that a given brand term is irrelevant to the artifact or that alt-text ordinarily functions as a public caption.

CITATION TRAIL:
[[IMG-JEPA-02-B]] → JEPA §2.3 on the brand-name example → Mitchell’s distinction among imagetext, image-text, and image/text.

TEST:
Take one identical photograph published on two pages under different, verifiable sponsorships. Compare literal recaptions with page-aware descriptions. Test scene retrieval and publication attribution separately. Include a case where the sponsor is visible in the image to test whether the two tasks can coincide.

PLATFORM:
[[The Published Imagetext]]

LINKS:
[[IMG-JEPA-02-B]]
[[IMG-JEPA-01]]
[[Scene Versus Page]]
[[Description Provenance]]

BIBTEX:
@article{mitchell1994beyond,
  author = {Mitchell, W. J. T.},
  title = {Beyond Comparison: Picture, Text and Method},
  journal = {Interfaces},
  volume = {5},
  pages = {13--38},
  year = {1994},
  doi = {10.3406/inter.1994.932},
  note = {The quoted Picture Theory note is reproduced in Mitchell's introduction to The Future of Text and Image},
  url = {https://www.cambridgescholars.com/resources/pdfs/978-1-4438-3640-1-sample.pdf}
}
@misc{balestriero2026platonic,
  author = {Balestriero, Randall and LeCun, Yann},
  title = {Proving and Improving the Platonic Representation Hypothesis with {JEPAs}},
  year = {2026},
  eprint = {2610.39302},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/html/2610.39302v1}
}