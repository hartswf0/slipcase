ZETTEL

ID:
SOURCE-COLLISION-001

TITLE:
Schön’s 1992 “Designing as Reflective Conversation” exists in two journal publications and should not be silently normalized.

SOURCE:
Donald A. Schön — same-title publications in Research in Engineering Design 3 (1992) and Knowledge-Based Systems 5(1) (1992).

SOURCE URL:
https://doi.org/10.1007/BF01580516

PASSAGE:
[VERIFIED BIBLIOGRAPHIC COLLISION]
Publisher and bibliographic records identify a 1992 Research in Engineering Design version (3:131–147, DOI 10.1007/BF01580516) and a 1992 Knowledge-Based Systems version (5(1):3–14, DOI 10.1016/0950-7051(92)90020-G) with the same title.

RESEARCH OBJECT:
SOURCE EDITION COLLISION.

LOCAL MOVE:
Preserve earlier cards exactly while making the edition used by the current paper explicit.

SOURCE TERMS:
Donald Schön
1992
Research in Engineering Design
Knowledge-Based Systems
DOI
bibliography conflict

WHAT BECAME STRANGE:
A source can be correctly remembered by title and year yet still be bibliographically ambiguous enough to corrupt page references, DOI resolution, or claims of exact verification.

QUESTION:
Are the two 1992 versions textually identical, abridged, revised, or separately typeset versions of the same essay?

DEEPER QUESTION:
What level of source identity should a research archive require before merging citations that share author, year, and title?

MECHANISM:
same author/title/year → two journal/DOI records → preserve both receipts → current paper binds its citation to the Research in Engineering Design edition actually inspected.

FORMAL SHIFT:
<SAME TITLE = SAME SOURCE> → <EDITION-SPECIFIC SOURCE IDENTITY>

SOURCE FORMALISM:
Bibliographic fact only; textual identity between editions was not exhaustively compared during this build.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
SourceIdentity should include venue/DOI/version when available, not author-title-year alone.

TENSION:
Splitting editions too aggressively can create false multiplicity when publishers legitimately reproduce the same text.

MISSING:
A page-by-page textual comparison of both complete editions.

BOUNDARY:
Do not rewrite prior immutable zettels to “correct” the venue. Add this collision card and cite the inspected edition in the current paper.

CITATION TRAIL:
[[DISCOVERY-002]] → Schön source verification → duplicate-title journal records → preserve collision rather than silently merge.

TEST:
Acquire both full texts, normalize typography only, diff paragraph order and wording, and record whether they are substantively identical.

PLATFORM:
[[after-surprise]]

LINKS:
[[DISCOVERY-002]]
[[source-identity]]
[[bibliographic-collision]]

BIBTEX:
@article{Schon1992Reflective,
  author={Schön, Donald A.},
  title={Designing as Reflective Conversation with the Materials of a Design Situation},
  journal={Research in Engineering Design},
  volume={3},
  pages={131--147},
  year={1992},
  doi={10.1007/BF01580516}
}

@article{Schon1992KnowledgeBased,
  author={Schön, Donald A.},
  title={Designing as Reflective Conversation with the Materials of a Design Situation},
  journal={Knowledge-Based Systems},
  volume={5},
  number={1},
  pages={3--14},
  year={1992},
  doi={10.1016/0950-7051(92)90020-G}
}
