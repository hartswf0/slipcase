ZETTEL

ID:
PROMPT-ONTOLOGY-004

TITLE:
The word “prompt” survives the disappearance of words.

SOURCE:
Brian Lester, Rami Al-Rfou, and Noah Constant — “The Power of Scale for Parameter-Efficient Prompt Tuning” — EMNLP 2021 — SOURCE URL: https://arxiv.org/abs/2104.08691

PASSAGE:
[PARAPHRASE] Lester et al. distinguish discrete text prompts from learned “soft prompts”: continuous parameters optimized through backpropagation to condition a frozen language model for downstream tasks.

RESEARCH OBJECT:
PROMPT AS FUNCTIONAL FAMILY RATHER THAN TEXTUAL KIND.

If soft prompts are genuine prompts, textuality cannot be an inherent property of all prompts. If they are excluded, a mature technical tradition called prompt tuning is using “prompt” for a different ontology.

LOCAL MOVE:
Force the vocabulary to choose what it is preserving: LANGUAGE or CONDITIONING FUNCTION.

SOURCE TERMS:
prompt tuning
soft prompts
continuous parameters
conditioning
frozen language models
backpropagation

WHAT BECAME STRANGE:
Prompt scholarship can describe prompts as texts written in a language while machine learning simultaneously calls nonlinguistic continuous vectors prompts. The noun crosses an ontological boundary without announcing the crossing.

QUESTION:
What property makes a soft prompt and a natural-language prompt instances of the same kind?

DEEPER QUESTION:
If the shared property is only “conditions a model,” what prevents retrieval, model state, tool schemas, or other conditioning variables from becoming prompts too?

MECHANISM:
Continuous learned vectors enter the model as conditioning without requiring a human-readable lexical realization.

FORMAL SHIFT:
FROM:
PROMPT = HUMAN-READABLE INSTRUCTION

TO:
PROMPT = MODEL-CONDITIONING OBJECT

which threatens to make PROMPT extensionally enormous.

SOURCE FORMALISM:
Soft prompts are learned through backpropagation while model parameters remain frozen.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Text prompt p ∈ V*.
Soft prompt z ∈ R^(n×d).
Both can condition M.

The common type cannot be “text” unless soft prompt is metaphorical nomenclature.

TENSION:
Human-readable prompting remains distinctive because it is simultaneously interpretable by people and operational for models. Soft prompting does not erase that difference; it makes the difference ontologically unavoidable.

MISSING:
A vocabulary that distinguishes human-operational language from nonlinguistic model conditioning without pretending they are either identical or unrelated.

BOUNDARY:
Soft prompts in prompt tuning are trained parameters, not evidence that ordinary chat systems secretly execute such vectors as replacements for user prompts.

CITATION TRAIL:
[[WORKWORDS-PROMPT-002]]
→ prompting larger than prompt language
→ Lester et al. canonical soft prompt tuning
→ textual ontology fractures
→ ask what common property keeps “prompt” coherent.

TEST:
Compare a task controlled by natural-language prompts and learned soft prompts. Test which notions survive across both: syntax, semantics, authorship, versioning, portability, interpretability, causal intervention, and transfer. The intersection is a candidate minimum ontology; its thinness is itself evidence.

PLATFORM:
T5; frozen language models; prompt tuning.

LINKS:
[[WORKWORDS-PROMPT-002]]

BIBTEX:
@inproceedings{Lester2021PromptTuning,
  title={The Power of Scale for Parameter-Efficient Prompt Tuning},
  author={Lester, Brian and Al-Rfou, Rami and Constant, Noah},
  booktitle={Proceedings of EMNLP},
  year={2021},
  url={https://arxiv.org/abs/2104.08691}
}
