ZETTEL

ID:
CALLSHOT-FIELD-005

TITLE:
THE MODEL TRAINS THE USER’S DIALECT WHILE THE USER TRAINS THEIR PROMPT.

SOURCE:
Shachar Don-Yehiya, Leshem Choshen, and Omri Abend, “Human Learning by Model Feedback: The Dynamics of Iterative Prompting with Midjourney,” EMNLP 2023, 4146–4161. DOI 10.18653/v1/2023.emnlp-main.253. SOURCE URL: https://aclanthology.org/2023.emnlp-main.253/

PASSAGE:
[QUOTE]
“adaptation to the model’s ‘preferences’”

RESEARCH OBJECT:
ITERATIVE PROMPTING CAN ALIGN HUMAN LANGUAGE TO MODEL-SPECIFIC PREFERENCES, NOT ONLY MAKE INTENT MORE EXPLICIT.

LOCAL MOVE:
The authors analyze iterative Midjourney sessions and find prompt convergence consistent with both clarification of human intentions and adaptation toward model-preferred language.

SOURCE TERMS:
“iterative prompting” · “converge” · “model’s preferences” · “specific language style” · “human intentions”

WHAT BECAME STRANGE:
Prompt mastery can be a learned accommodation to a particular machine. The better a user gets, the less their language may resemble ordinary description.

QUESTION:
When improvement occurs, how much is clearer intention and how much is model accommodation?

DEEPER QUESTION:
If adapted prompts are later reused as training data, can model-induced language be mistaken for independent human preference?

MECHANISM:
INTENTION → P₀ → OUTPUT → HUMAN UPDATE → P₁; update may follow an intention gradient and/or a model-preference gradient.

FORMAL SHIFT:
USER TRAINS PROMPT → USER AND MODEL CO-ADAPT THROUGH FEEDBACK.

SOURCE FORMALISM:
[PARAPHRASE]
The paper compiles iterative Midjourney interactions and reports predictable convergence, with initial evidence for both intention clarification and adaptation to model preferences.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
ΔQUALITY = ΔINTENTION_EXPRESSION + ΔMODEL_ADAPTATION. These components need not point in the same linguistic direction.

TENSION:
Community transmission can make model-selected forms look like human conventions; social convention can also persist after model preference changes.

MISSING:
Feature-level account of which lexical or syntactic changes are model-specific and whether they transfer across systems.

BOUNDARY:
The study is aggregate evidence from Midjourney interactions, not Joshua’s individual trajectory.

CITATION TRAIL:
[[MJ-JOSHUA-001-A]] → empirical Midjourney study → model feedback shapes user language → [[CALLSHOT-FIELD-007]] current agent dialects.

TEST:
Test expert prompts across model families and versions while holding semantics constant. Forms that lose advantage outside one model are candidate model dialect rather than general descriptive skill.

PLATFORM:
Midjourney · EMNLP · human-model adaptation

LINKS:
[[MJ-JOSHUA-001-A]] [[CALLSHOT-FIELD-001]] [[CALLSHOT-FIELD-007]]

BIBTEX:
@inproceedings{DonYehiyaChoshenAbend2023,
  author={Don-Yehiya, Shachar and Choshen, Leshem and Abend, Omri},
  title={Human Learning by Model Feedback: The Dynamics of Iterative Prompting with Midjourney},
  booktitle={Proceedings of EMNLP 2023},
  year={2023},
  pages={4146--4161},
  doi={10.18653/v1/2023.emnlp-main.253},
  url={https://aclanthology.org/2023.emnlp-main.253/}
}
