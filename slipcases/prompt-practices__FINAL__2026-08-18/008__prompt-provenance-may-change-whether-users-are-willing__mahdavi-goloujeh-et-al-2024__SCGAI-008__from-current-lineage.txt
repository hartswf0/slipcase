ZETTEL

ID:
SCGAI-008

TITLE:
Prompt provenance may change whether users are willing to enter collaboration at all.

SOURCE:
Atefeh Mahdavi Goloujeh, Anne Sullivan, and Brian Magerko — “The Social Construction of Generative AI Prompts” — CHI EA ’24 — 2024 — https://doi.org/10.1145/3613905.3650947

PASSAGE:
[QUOTE] “Clear mechanisms for tracking and crediting contributions can encourage users to transition between orientations.”

RESEARCH OBJECT:
The authors propose provenance infrastructure not merely as record keeping but as a mechanism capable of changing participation.

LOCAL MOVE:
Treat PROVENANCE as an operational variable affecting social behavior rather than passive metadata.

SOURCE TERMS:
tracking; crediting; contributions; transition; orientations; confidence; assurance; sharing; collaboration

WHAT BECAME STRANGE:
A metadata system can alter the social topology of prompting. Recording who changed what may determine whether knowledge remains private or enters circulation.

QUESTION:
Can provenance infrastructure causally increase prompt sharing and reuse?

DEEPER QUESTION:
When provenance becomes machine-readable, does it protect authorship or create a programmable social layer governing forks, credit, reward, and recombination?

MECHANISM:
Fear of losing credit → withholding → provenance/credit mechanism → perceived risk decreases → sharing/reuse increases → more collaborative knowledge production.

FORMAL SHIFT:
PROVENANCE = DESCRIPTION OF PAST ACTION becomes PROVENANCE = CONDITION ON FUTURE ACTION.

SOURCE FORMALISM:
The authors explicitly suggest tracking/crediting contributions as a design intervention that may encourage transitions between engagement orientations.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
Test whether P(share | visible attribution + modification history) > P(share | no provenance).

TENSION:
Attribution could encourage sharing by protecting recognition but also intensify proprietary thinking by making every borrowed modifier look owned.

MISSING:
Experimental evidence testing whether provenance increases collaboration, ownership disputes, or both for different users.

BOUNDARY:
Tracking and crediting are proposed design implications; the study does not empirically demonstrate the behavioral transition.

CITATION TRAIL:
[[SCGAI-2024]] → tracking and crediting → copying/control concerns → provenance-system research → test circulation under attribution.

TEST:
Build interfaces with no provenance, author attribution, and complete fork/diff lineage; measure sharing, reuse, modification, ownership, and conflict.

PLATFORM:
Text-to-image generative AI platforms

LINKS:
[[SCGAI-2024]]

BIBTEX:
@inproceedings{mahdavigoloujeh2024social,
  author = {Mahdavi Goloujeh, Atefeh and Sullivan, Anne and Magerko, Brian},
  title = {The Social Construction of Generative AI Prompts},
  booktitle = {Extended Abstracts of the CHI Conference on Human Factors in Computing Systems},
  year = {2024},
  publisher = {Association for Computing Machinery},
  doi = {10.1145/3613905.3650947},
  url = {https://doi.org/10.1145/3613905.3650947}
}
