ZETTEL

ID:
QUESTIONSPACE-001

TITLE:
A generative system can shape not only answers but which distinctions the maker learns to ask about.

SOURCE:
Shachar Don-Yehiya, Leshem Choshen, and Omri Abend — “Human Learning by Model Feedback: The Dynamics of Iterative Prompting with Midjourney” — EMNLP 2023.

SOURCE URL:
https://aclanthology.org/2023.emnlp-main.253/

PASSAGE:
[PARAPHRASE]
Don-Yehiya and colleagues find evidence that iterative users both add omitted details and adapt their language toward patterns the model appears to handle better. The study raises concern that model feedback can bias users’ expression.

RESEARCH OBJECT:
QUESTION-SPACE SHAPING.

LOCAL MOVE:
Extend co-adaptation from vocabulary change to a hypothesis about salience: systems may differentially reward some distinctions until those distinctions become easier to notice and ask about than others.

SOURCE TERMS:
model feedback
co-adaptation
salience
preference shaping
prompt convergence
question space

WHAT BECAME STRANGE:
A tool can increase local proficiency while narrowing the practical vocabulary of differences that receive useful feedback.

QUESTION:
Which distinctions stop being noticed because the system does not make them actionable or rewarding?

DEEPER QUESTION:
Can a creative interface increase the user’s control over a local region while shrinking the space of distinctions the user learns to value?

MECHANISM:
model affordance/default → differential feedback quality → user attention shifts toward responsive dimensions → vocabulary/preferences evolve → future prompts further concentrate there.

FORMAL SHIFT:
<SYSTEM ANSWERS QUESTIONS> → <SYSTEM SHAPES THE SPACE OF ASKABLE QUESTIONS>

SOURCE FORMALISM:
The source establishes adaptation toward model-preferred language, not the stronger claim that the full space of artistic questions is narrowed. That extension remains a hypothesis.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
Let Q_t be distinctions available to the maker as actionable questions. Feedback can alter salience weights over Q_t and may affect which new q enter Q_{t+1}.

TENSION:
All media shape attention. Medium formation is not automatically capture.

MISSING:
A task-independent baseline for user attention and preference that does not assume a pristine pre-medium intention.

BOUNDARY:
Question-space shaping is an open empirical claim, not evidence that model users lose agency.

CITATION TRAIL:
[[RETENTION-005-T-B]] → adaptation to model preferences → extend cautiously from prompt language to salience and question formation.

TEST:
Before interaction, elicit target distinctions through sketches/references/free description. After extended use, repeat with a novel model and compare which distinctions are spontaneously articulated and pursued.

PLATFORM:
[[after-surprise]]

LINKS:
[[RETENTION-005-T-B]]
[[RETENTION-005-R-A]]
[[question-space]]
[[co-adaptation]]

BIBTEX:
@inproceedings{DonYehiyaEtAl2023,
  author={Don-Yehiya, Shachar and Choshen, Leshem and Abend, Omri},
  title={Human Learning by Model Feedback: The Dynamics of Iterative Prompting with Midjourney},
  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
  pages={4146--4161},
  year={2023},
  doi={10.18653/v1/2023.emnlp-main.253}
}
