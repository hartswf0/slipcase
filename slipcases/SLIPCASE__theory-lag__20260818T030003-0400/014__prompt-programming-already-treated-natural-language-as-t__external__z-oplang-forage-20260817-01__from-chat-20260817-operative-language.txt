ZETTEL

ID:
Z-OPLANG-FORAGE-20260817-01

TITLE:
Prompt programming already treated natural language as task location, so “prompt as specification” is too narrow.

SOURCE:
Laria Reynolds and Kyle McDonell — Prompt Programming for Large Language Models: Beyond the Few-Shot Paradigm — 2021 — abstract.

SOURCE URL:
https://arxiv.org/abs/2102.07350

PASSAGE:
[QUOTE]
“locating an already learned task rather than meta-learning.”

RESEARCH OBJECT:
<task location> as a rival mechanism to <task specification>.

A prompt may work not by encoding the operation to be performed but by steering a pretrained model toward a capability already latent in its learned distribution.

LOCAL MOVE:
Reynolds and McDonell explicitly widen “prompt programming” beyond few-shot examples and emphasize natural language, narratives, and cultural anchors as means of expressing nuanced intention.

SOURCE TERMS:
“prompt programming”
“natural language”
“narratives”
“cultural anchors”
“nuanced intentions”
“locating an already learned task”
“metaprompt”

WHAT BECAME STRANGE:
The specification metaphor may over-credit the prompt with containing the task.

If a prompt partly locates a competence acquired during training, then missing information may not be completed only at inference time. Some of the operative structure predates the prompt entirely.

QUESTION:
When does a prompt specify a task, and when does it merely locate or activate a task already represented by the model?

DEEPER QUESTION:
How should semantic slack be measured when the missing structure is not improvised during interpretation but recovered from learned priors?

MECHANISM:
<pretrained model>
[contains] <learned capability distribution>.

<prompt>
[locates / evokes / constrains] <candidate capability>.

<model>
[realizes] <task behavior>.

FORMAL SHIFT:
<PROMPT AS COMPLETE TASK DESCRIPTION>
→ <PROMPT AS INDEX INTO LEARNED CAPABILITY>
→ [LOCATE]
→ <TASK BEHAVIOR>

SOURCE FORMALISM:
The abstract distinguishes 0-shot and few-shot prompting and proposes task location as an interpretation of few-shot examples. No general mathematical semantics of task location is supplied in the abstract.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Behavior B may depend on:

B = f(P, M)

where P is the prompt and M contains learned task structure.

A high-slack prompt may succeed because P supplies little while M supplies much.

TENSION:
“Task location” can become another metaphor unless the located representation or behavioral basin can be operationally identified.

The model may also synthesize behavior rather than retrieve a stable pre-existing task.

MISSING:
An experiment distinguishing:
- task retrieval,
- task composition,
- specification completion,
- imitation from examples.

BOUNDARY:
The paper does not establish that all prompts merely locate learned tasks.

Its evidence concerns GPT-3 prompt programming and motivates a broader account of prompt control.

CITATION TRAIL:
Prompt-based learning surveys.
In-context learning mechanisms.
Representation steering.
Task vectors.
Prompt sensitivity studies.

TEST:
Hold the target task fixed and compare semantically minimal labels, demonstrations, detailed instructions, and unrelated paraphrases. Test whether successful prompts cluster around a stable learned capability or require incremental specification.

PLATFORM:
[[Operative Language]]

LINKS:
[[Task Location]]
[[Specification Completion]]
[[Learned Semantics]]

BIBTEX:
@article{reynolds2021promptprogramming,
  author = {Reynolds, Laria and McDonell, Kyle},
  title = {Prompt Programming for Large Language Models: Beyond the Few-Shot Paradigm},
  year = {2021},
  journal = {Extended Abstracts of the 2021 CHI Conference on Human Factors in Computing Systems},
  doi = {10.1145/3411763.3451760}
}
