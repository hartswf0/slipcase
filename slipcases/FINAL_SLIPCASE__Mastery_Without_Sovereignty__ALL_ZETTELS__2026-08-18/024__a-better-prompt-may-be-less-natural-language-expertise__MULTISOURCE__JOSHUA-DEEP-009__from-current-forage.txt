ZETTEL

ID:
JOSHUA-DEEP-009

TITLE:
A “BETTER” PROMPT MAY BE LESS NATURAL LANGUAGE: EXPERTISE CAN MEAN ADAPTATION TO A MODEL DIALECT.

SOURCE:
Joshua Larson interview with Watson Hartsoe, 2022-10-18. Original local source: _RESOURCES/BLUE_MJ_Interview 2_Joshua.pages; best-effort extracted text: _RESOURCES/_joshua_decompressed_strings.txt. SOURCE URL: LOCAL_FILE | Shachar Don-Yehiya, Leshem Choshen, and Omri Abend, “Human Learning by Model Feedback: The Dynamics of Iterative Prompting with Midjourney,” EMNLP 2023, 4146-4161. DOI: 10.18653/v1/2023.emnlp-main.253. SOURCE URL: https://aclanthology.org/2023.emnlp-main.253/

PASSAGE:
[QUOTE — JOSHUA, 03:02]
“trying to get a feel for, you know, the language of prompting.”

[QUOTE — JOSHUA, 1:13:32]
“what you’re interested in, is like some principle”

[PARAPHRASE — DON-YEHIYA ET AL.]
Iterative Midjourney prompts converge through both intention clarification and adaptation to model preferences; the authors warn that model-specific adaptation may diverge from natural human expression.

RESEARCH OBJECT:
PROMPT EXPERTISE HAS AT LEAST TWO POSSIBLE TARGETS: EXPRESSING THE HUMAN INTENTION MORE FAITHFULLY AND SPEAKING IN A FORM THE MODEL RESPONDS TO MORE FAVORABLY.

LOCAL MOVE:
Joshua calls prompting a “language,” then says advanced users care about principles rather than exact strings. Don-Yehiya et al. show that iterative improvement is not reducible to clearer human intent; users may also adapt to model preferences. The mature principle may therefore be a rule for speaking a machine dialect.

SOURCE TERMS:
“language of prompting” · principle · iterative prompting · convergence · “model’s preferences” · “natural manner of expression”

WHAT BECAME STRANGE:
Fluency can move away from ordinary communicative fluency. A phrase that sounds awkward or indirect to a human may be an expert utterance if it occupies a privileged region of the model’s learned interface.

QUESTION:
When an expert prompt improves output, which fraction of the gain comes from clarifying intention and which from model-specific accommodation?

DEEPER QUESTION:
Can a prompting community become more expert while its shared language becomes less portable across models and less transparent to ordinary speakers?

MECHANISM:
INTENTION I → PROMPT P0 → OUTPUT → USER UPDATE. Update follows both an INTENTION GRADIENT and a MODEL-PREFERENCE GRADIENT; observed success does not identify their relative contributions.

FORMAL SHIFT:
PROMPTING AS NATURAL-LANGUAGE INTERFACE → PROMPTING AS ACQUIRED MODEL DIALECT SUPERIMPOSED ON NATURAL LANGUAGE.

SOURCE FORMALISM:
[PARAPHRASE]
Don-Yehiya et al. compile iterative Midjourney interactions, observe predictable prompt convergence, and report initial evidence for both missing-detail realization and adaptation to model preferences.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
Δsuccess = α·Δintent_fidelity + β·Δmodel_compatibility. Portability tests estimate β by moving the same formulations across model families.

TENSION:
A model-specific dialect can be an efficient instrument skill rather than a pathology. The problem appears when accommodation is mistaken for universal semantics or “better human description.”

MISSING:
Cross-model transfer studies of expert prompt principles and measurements of human comprehensibility versus model effectiveness.

BOUNDARY:
Don-Yehiya et al. provide aggregate Midjourney evidence, not a direct analysis of Joshua’s prompts.

CITATION TRAIL:
[[CALLSHOT-FIELD-001]] → “language of prompting” → [[CALLSHOT-FIELD-005]] → Don-Yehiya et al. model adaptation → return to Joshua’s “principles” as candidate rules of dialect rather than universal semantics.

TEST:
Create semantically matched prompt sets ranging from ordinary descriptions to expert model-specific formulations. Test human interpretability and output performance across multiple model families and versions.

PLATFORM:
Midjourney · prompt dialect · human-model adaptation

LINKS:
[[CALLSHOT-FIELD-001]] [[CALLSHOT-FIELD-005]] [[JOSHUA-DEEP-003]] [[JOSHUA-DEEP-008]]

BIBTEX:
@inproceedings{DonYehiyaChoshenAbend2023,
 author={Don-Yehiya, Shachar and Choshen, Leshem and Abend, Omri},
 title={Human Learning by Model Feedback: The Dynamics of Iterative Prompting with Midjourney},
 booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
 year={2023}, pages={4146--4161}, doi={10.18653/v1/2023.emnlp-main.253},
 url={https://aclanthology.org/2023.emnlp-main.253/}
}
