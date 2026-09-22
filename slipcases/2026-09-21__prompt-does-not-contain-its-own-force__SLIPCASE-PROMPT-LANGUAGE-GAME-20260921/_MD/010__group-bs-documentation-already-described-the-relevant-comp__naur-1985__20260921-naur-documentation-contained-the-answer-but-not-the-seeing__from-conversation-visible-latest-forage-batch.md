ZETTEL

ID:
20260921-naur-documentation-contained-the-answer-but-not-the-seeing

TITLE:
Group B’s Documentation Already Described the Relevant Compiler Facilities, Yet Group B Still Reached for Patches

SOURCE:
Peter Naur — “Programming as Theory Building” — 1985 — Microprocessing and Microprogramming 15:253–261. ([gwern.net](https://gwern.net/doc/cs/algorithm/1985-naur.pdf?utm_source=chatgpt.com))

PASSAGE:
[PARAPHRASE] Naur states that the facilities Group B failed to use were not merely hidden in the compiler: they were discussed at length in the documentation Group B possessed. Group A nevertheless recognized immediately how the extension fit the existing structure, while Group B proposed additional patches.

RESEARCH OBJECT:
Explicitly available information failing to produce the discriminating perception required to use it.

LOCAL MOVE:
The case eliminates a simple explanation of knowledge loss: the relevant facts were not merely omitted from the documents.

SOURCE TERMS:
full documentation
annotated program texts
design discussion
facilities
discussed at length
patches
instantly

WHAT BECAME STRANGE:
The missing knowledge is not equivalent to a missing sentence. Group B could possess the proposition “facility F exists” without seeing that the new problem was a case for F.

QUESTION:
What does a prompt-system maintainer need beyond documentation in order to recognize that a new failure is structurally the same as an earlier one?

DEEPER QUESTION:
Can a harness preserve not only solutions and explanations but the similarity judgments that caused builders to treat two superficially different failures as instances of one mechanism?

MECHANISM:
documentation contains facility
→ maintainer encounters new requirement
→ requirement not recognized as instance of existing abstraction
→ local patch proposed
→ theory-holder recognizes structural similarity
→ existing abstraction reused.

FORMAL SHIFT:
<KNOW FACTS ABOUT SYSTEM>
→ <RECOGNIZE RELEVANT SIMILARITY>
→ [MAP NOVEL CASE TO EXISTING STRUCTURE]
→ <THEORY-GUIDED MODIFICATION>

SOURCE FORMALISM:
Naur’s theory-building account says possession of the program theory includes being able to explain how the program relates to the world and how modifications fit its structure. ([gwern.net](https://gwern.net/doc/cs/algorithm/1985-naur.pdf?utm_source=chatgpt.com))

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
theory_transfer requires:
stored_fact
+
retrieval_trigger
+
similarity_judgment
+
counterfactual understanding.

TENSION:
A sufficiently good retrieval or case-based system might recover relevant past abstractions even when maintainers do not initially possess the builders’ theory.

MISSING:
Evidence distinguishing genuinely internalized theory from excellent retrieval over a structured case archive.

BOUNDARY:
Naur’s evidence is anecdotal and does not establish that tacit theory cannot be partially externalized through better representations.

CITATION TRAIL:
[[20260921-naur-compiler-patches-preserved-output-and-destroyed-design]]
→ Group B had the relevant facility documented
→ documentation failure becomes a retrieval-and-recognition failure.

TEST:
Give maintainers a novel failure whose mechanism is documented under very different surface symptoms. Compare plain documentation, semantic retrieval of analogous cases, and direct apprenticeship from an experienced builder.

PLATFORM:
[[prompt-knowledge]]

LINKS:
[[20260921-naur-compiler-patches-preserved-output-and-destroyed-design]]
[[theory-building]]
[[similarity-judgment]]
[[case-retrieval]]

BIBTEX:
@article{naur1985programming,
  author = {Naur, Peter},
  title = {Programming as Theory Building},
  journal = {Microprocessing and Microprogramming},
  year = {1985},
  volume = {15},
  pages = {253--261}
}
