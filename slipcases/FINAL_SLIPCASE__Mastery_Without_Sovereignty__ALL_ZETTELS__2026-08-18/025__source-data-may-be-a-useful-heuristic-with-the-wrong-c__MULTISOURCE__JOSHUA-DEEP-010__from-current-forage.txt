ZETTEL

ID:
JOSHUA-DEEP-010

TITLE:
“SOURCE DATA” MAY BE A USEFUL HEURISTIC WITH THE WRONG CAUSAL STORY.

SOURCE:
Joshua Larson interview with Watson Hartsoe, 2022-10-18. Original local source: _RESOURCES/BLUE_MJ_Interview 2_Joshua.pages; best-effort extracted text: _RESOURCES/_joshua_decompressed_strings.txt. SOURCE URL: LOCAL_FILE | Alec Radford et al., “Learning Transferable Visual Models From Natural Language Supervision,” ICML 2021. SOURCE URL: https://proceedings.mlr.press/v139/radford21a.html

PASSAGE:
[QUOTE — JOSHUA, 39:29]
“the things that have the most impact on like, kind of the visual result is, if your prompting source data”

[PARAPHRASE — RADFORD ET AL.]
Large-scale image-text pretraining can yield learned visual concepts that natural language later references, but this does not imply retrieval from a literal source-data bucket at generation time.

RESEARCH OBJECT:
PRACTITIONER EXPLANATION AND PRACTITIONER CONTROL SHOULD BE TESTED SEPARATELY: A RULE CAN WORK EVEN WHEN THE STORY ABOUT WHY IT WORKS IS WRONG.

LOCAL MOVE:
Joshua’s “source data” account is mechanistically specific: some phrases work because they reference photographic datasets. Related vision-language work makes association-based addressing plausible, but does not vindicate that exact causal story for Midjourney. The useful next move is not to accept or dismiss the heuristic; it is to separate predictive power from explanatory accuracy.

SOURCE TERMS:
“source data” · “most impact” · film still · miniatures · learned visual concepts · mechanism

WHAT BECAME STRANGE:
A folk theory can be operationally excellent and mechanistically false. The user may reliably steer the system with a vocabulary whose causal explanation points to the wrong layer.

QUESTION:
Which of Joshua’s prompt rules predict repeatable changes even when their stated mechanism cannot be verified?

DEEPER QUESTION:
What kind of expertise is it to possess reliable interventions without a correct causal model—and how should a community preserve the intervention while keeping the explanation provisional?

MECHANISM:
OBSERVE REPEATABLE EFFECT → INVENT CAUSAL STORY → USE STORY TO GENERATE NEW INTERVENTIONS. Predictive success of interventions and truth of story must be evaluated independently.

FORMAL SHIFT:
TECHNIQUE TRUE / SUPERSTITION FALSE → TWO AXES: INTERVENTION RELIABILITY × EXPLANATORY ACCURACY.

SOURCE FORMALISM:
[PARAPHRASE]
Radford et al. establish one image-text learning architecture where language references learned visual concepts. They do not establish Midjourney’s training or inference mechanism.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
Technique T has predictive validity V(T) and explanation E_T has mechanistic validity M(E_T). V(T)>0 does not imply M(E_T)>0.

TENSION:
Demanding mechanistic proof before using a heuristic would discard real craft knowledge; treating successful intervention as proof of mechanism produces confident folklore.

MISSING:
Model-specific internal evidence, controlled ablations, and alternative causal explanations for why Joshua’s cultural proxy terms work.

BOUNDARY:
This zettel deliberately refuses to infer Midjourney internals from CLIP or from practitioner success.

CITATION TRAIL:
[[JOSHUA-DEEP-003]] → proxy terms seem effective → Joshua explains via “source data” → related vision-language formalism supports learned associations but not exact mechanism → split intervention validity from explanation validity.

TEST:
For each prompt heuristic, first replicate the output effect without discussing mechanism. Then enumerate rival mechanisms that predict different transfer behavior across models, versions, paraphrases, and conditioning modes; run the smallest discriminating tests.

PLATFORM:
Midjourney · folk theory · causal inference

LINKS:
[[JOSHUA-DEEP-003]] [[JOSHUA-DEEP-007]] [[JOSHUA-DEEP-008]]

BIBTEX:
@inproceedings{RadfordEtAl2021,
 author={Radford, Alec and Kim, Jong Wook and Hallacy, Chris and Ramesh, Aditya and Goh, Gabriel and Agarwal, Sandhini and Sastry, Girish and Askell, Amanda and Mishkin, Pamela and Clark, Jack and Krueger, Gretchen and Sutskever, Ilya},
 title={Learning Transferable Visual Models From Natural Language Supervision},
 booktitle={Proceedings of the 38th International Conference on Machine Learning}, series={Proceedings of Machine Learning Research}, volume={139}, pages={8748--8763}, year={2021}, url={https://proceedings.mlr.press/v139/radford21a.html}
}
