ZETTEL

ID:
JOSHUA-DEEP-003

TITLE:
“PHOTOREALISTIC” CAN BE A WORSE CONTROL WORD THAN “FILM STILL”: PROMPTING MAY ADDRESS LEARNED VISUAL CONCEPTS BY CULTURAL PROXY.

SOURCE:
Joshua Larson interview with Watson Hartsoe, 2022-10-18. Original local source: _RESOURCES/BLUE_MJ_Interview 2_Joshua.pages; best-effort extracted text: _RESOURCES/_joshua_decompressed_strings.txt. SOURCE URL: LOCAL_FILE | Alec Radford et al., “Learning Transferable Visual Models From Natural Language Supervision,” ICML 2021, PMLR 139:8748-8763. SOURCE URL: https://proceedings.mlr.press/v139/radford21a.html

PASSAGE:
[QUOTE — JOSHUA, 39:29]
“photorealistic is often a word that you want to avoid.”

[QUOTE — JOSHUA, 39:29]
“what’s much better to use is some kind of term that references a set of data.”

[PARAPHRASE — RADFORD ET AL.]
CLIP shows a formal precedent in which natural language can reference learned visual concepts after large-scale image-text pretraining.

RESEARCH OBJECT:
A PROMPT TERM CAN OPERATE LESS LIKE A PROPERTY DESCRIPTION AND MORE LIKE AN INDEX INTO A LEARNED VISUAL NEIGHBORHOOD.

LOCAL MOVE:
Joshua’s strongest concrete prompt lesson is counter-semantic: if he wants photographic appearance, he may avoid the literal adjective “photorealistic” and instead write “film still,” “miniatures,” “museum display,” or another culturally specific phrase he believes is associated with high-quality photographs. CLIP does not establish Midjourney’s mechanism, but it supplies a technical precedent for language referencing learned visual concepts rather than simply denoting literal properties.

SOURCE TERMS:
“prompting source data” · “photorealistic” · “film still” · “miniatures” · “museum display” · “references a set of data” · learned visual concepts

WHAT BECAME STRANGE:
Ordinary semantic precision can become operational imprecision. The word that best describes the desired property may be worse than a phrase whose cultural history predicts a useful region of image-text association.

QUESTION:
Why can an indirect cultural phrase produce a desired visual property more reliably than the literal adjective naming that property?

DEEPER QUESTION:
Is expert prompting partly the craft of discovering indexical handles into learned representation space rather than improving natural-language description?

MECHANISM:
DESIRED VISUAL PROPERTY → CHOOSE CULTURAL / GENRE TERM WITH ASSOCIATED VISUAL REGULARITIES → MODEL ACTIVATES LEARNED CONCEPT NEIGHBORHOOD → OUTPUT INHERITS TARGET PROPERTY INDIRECTLY.

FORMAL SHIFT:
PROMPT AS DESCRIPTION OF OUTPUT → PROMPT AS ADDRESSING OPERATION OVER LEARNED ASSOCIATIONS.

SOURCE FORMALISM:
[PARAPHRASE]
Radford et al. train CLIP on 400 million image-text pairs and report that after pretraining natural language can reference learned visual concepts for zero-shot transfer.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
Desired feature F need not be maximized by token t_F that literally names F. A proxy term t_C may produce stronger F if its learned association neighborhood has higher P(F | t_C).

TENSION:
Joshua explains the effect in terms of “source data,” but successful proxy prompting does not by itself reveal whether the cause is training-data frequency, representation geometry, caption conventions, aesthetic tuning, or another mechanism.

MISSING:
Controlled comparisons of literal property words against culturally indexical proxies, plus model-specific evidence about which internal or training mechanisms explain the difference.

BOUNDARY:
CLIP is not evidence that Midjourney used the same architecture or that Joshua’s “source data” explanation is mechanistically correct. It only makes the addressing interpretation technically plausible in a related vision-language paradigm.

CITATION TRAIL:
[[CALLSHOT-FIELD-003]] → Joshua treats words as unequal controls → “prompting source data” at 39:29 → Radford et al. natural language references learned visual concepts → distinguish describing from addressing.

TEST:
Build matched prompt pairs: literal property term versus proxy cultural term while holding content constant. Sample broadly across seeds and models. Test effect size, transfer across models, and whether success survives paraphrasing the proxy.

PLATFORM:
Midjourney · vision-language learning · prompt semantics

LINKS:
[[CALLSHOT-FIELD-003]] [[JOSHUA-DEEP-004]] [[JOSHUA-DEEP-010]]

BIBTEX:
@inproceedings{RadfordEtAl2021,
 author={Radford, Alec and Kim, Jong Wook and Hallacy, Chris and Ramesh, Aditya and Goh, Gabriel and Agarwal, Sandhini and Sastry, Girish and Askell, Amanda and Mishkin, Pamela and Clark, Jack and Krueger, Gretchen and Sutskever, Ilya},
 title={Learning Transferable Visual Models From Natural Language Supervision},
 booktitle={Proceedings of the 38th International Conference on Machine Learning},
 series={Proceedings of Machine Learning Research}, volume={139}, pages={8748--8763}, year={2021},
 url={https://proceedings.mlr.press/v139/radford21a.html}
}
