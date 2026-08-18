ZETTEL

ID: PF-012

TITLE:
Discarded model text can still leave a measurable writing-process contribution.

SOURCE:
Lee, Liang, and Yang — CoAuthor — 2022.

PASSAGE:
[PARAPHRASE] CoAuthor records fine-grained interactions between writers and GPT-3 across more than a thousand writing sessions so that collaboration can be studied through process rather than final text alone.

RESEARCH OBJECT:
An AI interaction can alter writing without contributing retained sentences.

LOCAL MOVE:
The dataset makes requests, suggestions, acceptance, and revision analyzable as interaction traces.

SOURCE TERMS:
human-AI collaborative writing; interaction dataset; writing process; language model capabilities.

WHAT BECAME STRANGE:
Zero retained AI prose does not imply zero AI-mediated change.

QUESTION:
How can a distinction or conceptual redirection caused by discarded generations be represented as contribution?

DEEPER QUESTION:
Does contribution require traceable textual inheritance, or can counterfactual influence be enough?

MECHANISM:
<writer request>
→ <model suggestion>
→ [accept/reject/react]
→ <changed subsequent writing>

FORMAL SHIFT:
NONE

SOURCE FORMALISM:
Recorded interaction sessions and replayable writing histories.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
DISCARDED OUTPUT → altered next human move → downstream contribution.

TENSION:
Counterfactual influence is difficult to establish from logs alone.

MISSING:
A method for proving that a rejected generation caused a later conceptual move.

BOUNDARY:
CoAuthor records process but does not provide a general authorship test.

CITATION TRAIL:
Writing-process research; causal inference from interaction logs; stimulated recall.

TEST:
Ask writers to annotate moments where rejected generations changed their subsequent argument, then compare against interaction traces.

PLATFORM:
[[Influence Without Textual Retention]]

LINKS:
[[CoAuthor]]
[[Discarded Output]]
[[Interaction Trace]]

BIBTEX:
@inproceedings{lee2022coauthor,
  author={Mina Lee and Percy Liang and Qian Yang},
  title={CoAuthor: Designing a Human-AI Collaborative Writing Dataset for Exploring Language Model Capabilities},
  booktitle={Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems},
  year={2022},
  doi={10.1145/3491102.3502030}
}