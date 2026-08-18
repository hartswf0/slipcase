ZETTEL

ID: PF-047

TITLE:
Workflow categories should be tested against process traces, not invented from intuition.

SOURCE:
Zhu et al. — Humanly — 2026.

PASSAGE:
[PARAPHRASE] Humanly captures human and AI actions because final text alone cannot reveal the production process.

RESEARCH OBJECT:
The proposed contrast between “five pasted pages” and “two thousand words of prompts with no retained output” is empirically representable.

LOCAL MOVE:
The system supplies trace data from which workflow classes could be derived.

SOURCE TERMS:
traceable environment; writing process; AI assistance.

WHAT BECAME STRANGE:
The obvious two-example contrast may conceal many intermediate workflow types.

QUESTION:
What workflow classes actually emerge from large corpora of human-AI writing traces?

DEEPER QUESTION:
Should governance categories be empirically induced from practice rather than stipulated from edge cases?

MECHANISM:
<interaction traces>
→ <features>
→ [cluster/classify]
→ <workflow types>

FORMAL SHIFT:
NONE

SOURCE FORMALISM:
Event capture and process certificate.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
WORKFLOW TYPE from behavior, not self-report label.

TENSION:
Data-driven categories can reproduce whatever behaviors the capture tool makes visible.

MISSING:
Large diverse trace corpora across scholarly disciplines.

BOUNDARY:
Humanly's environment is not a representative sample of all AI writing.

CITATION TRAIL:
CoAuthor; process mining; writing-process typologies.

TEST:
Cluster interaction traces without using preassigned “brainstorming/editing/generation” labels and inspect resulting categories.

PLATFORM:
[[Empirical Workflow Ontology]]

LINKS:
[[Humanly]]
[[Process Trace]]
[[Workflow Classification]]

BIBTEX:
@article{zhu2026humanly,
  author={Shenzhe Zhu and Haoqian Zhang and Xu Yang and Jingyu Tang and Yi Nian and Xiaoxue Du and Shu Yang and Alex Pentland and Joachim Baumann and Jiaxin Pei},
  title={Humanly: A Configurable and Traceable Environment for Human-AI Collaborative Writing},
  journal={arXiv preprint arXiv:2607.21758},
  year={2026}
}