ZETTEL

ID: PF-009

TITLE:
Prompt robustness belongs to a prompt–model relation, not to the prompt alone.

SOURCE:
Chatterjee et al. — POSIX: A Prompt Sensitivity Index For Large Language Models — 2024.

PASSAGE:
[PARAPHRASE] POSIX measures changes in model behavior under intent-preserving prompt variations and finds substantial sensitivity to surface form.

RESEARCH OBJECT:
A supposedly “battle-hardened prompt” can change robustness when the model changes.

LOCAL MOVE:
The paper treats prompt sensitivity as a measurable property of model behavior under perturbation.

SOURCE TERMS:
prompt sensitivity; intent-preserving perturbation; relative log-likelihood.

WHAT BECAME STRANGE:
Testing a prompt many times on one model may harden a local coupling rather than the prompt itself.

QUESTION:
What does it mean for a prompt to “work elsewhere” when robustness is relational?

DEEPER QUESTION:
Should a scholarly prompt artifact include the tested model distribution as part of its identity?

MECHANISM:
<prompt meaning>
→ <surface variants>
→ [run model]
→ <behavioral divergence>

FORMAL SHIFT:
<intended instruction>
→ <variant prompt set>
→ [evaluate model responses]
→ <sensitivity index>

SOURCE FORMALISM:
POSIX sensitivity measure.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
ROBUSTNESS(P) is incomplete; use ROBUSTNESS(P,M,C).

TENSION:
The aphorism treats battle-hardening as accumulated testing, but portability may remain model- and context-specific.

MISSING:
Cross-model, cross-version, cross-context durability studies for prompts claimed as research instruments.

BOUNDARY:
POSIX measures sensitivity, not scholarly reproducibility.

CITATION TRAIL:
PromptBench; adversarial prompting; software portability.

TEST:
Run one “battle-hardened” prompt across ten models, three model versions, and five context conditions.

PLATFORM:
[[Prompt Robustness as Relational]]

LINKS:
[[POSIX]]
[[Battle-Hardened Prompt]]
[[Model Drift]]

BIBTEX:
@inproceedings{chatterjee2024posix,
  author={Anwoy Chatterjee and H. S. V. N. S. Kowndinya Renduchintala and Sumit Bhatia and Tanmoy Chakraborty},
  title={POSIX: A Prompt Sensitivity Index For Large Language Models},
  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2024},
  year={2024},
  pages={14550--14565}
}