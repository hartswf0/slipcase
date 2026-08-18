ZETTEL

ID:
Z-OPLANG-FORAGE-20260817-02

TITLE:
“Prompt” names incompatible research objects; template prompting cannot stand in for situated prompting.

SOURCE:
Pengfei Liu, Weizhe Yuan, Jinlan Fu, Zhengbao Jiang, Hiroaki Hayashi, and Graham Neubig — Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing — 2021/2023 — abstract.

SOURCE URL:
https://arxiv.org/abs/2107.13586

PASSAGE:
[PARAPHRASE]
The survey formalizes prompt-based learning by transforming an input x into a textual prompt x′ with unfilled slots, then using a language model to probabilistically fill the missing information and derive an output.

RESEARCH OBJECT:
<prompt-object multiplicity>.

The “prompt” in prompt-based NLP can be a task template inserted into a probabilistic prediction pipeline, while the prompt in interactive generative practice can be a situated intervention, correction, example, deictic reference, or partial world specification.

LOCAL MOVE:
The survey builds a unified notation precisely by narrowing the prompt to a form that can organize a large body of NLP methods.

SOURCE TERMS:
“prompt-based learning”
“template”
“textual string prompt x′”
“unfilled slots”
“probabilistically fill”
“prompting function”

WHAT BECAME STRANGE:
A theory asking “What is a prompt?” risks treating a historically overloaded technical term as if it named one stable object.

The disagreement may not be definitional. Different communities may literally manipulate different prompt objects.

QUESTION:
Which operations remain invariant across template prompting, instruction prompting, deictic conversational prompting, multimodal prompting, and tool-directed prompting?

DEEPER QUESTION:
Should “prompt” be retained as the theoretical unit at all, or replaced by a family of situated control relations?

MECHANISM:
In the survey’s formal object:
<input x>
[is transformed by] <prompting function>
→ <textual x′ with slots>
→ [probabilistic completion]
→ <derived output y>.

This is narrower than a general prompt-event.

FORMAL SHIFT:
<ONE TERM: PROMPT>
→ <MULTIPLE TECHNICAL OBJECTS>
→ [SEPARATE BY OPERATION]
→ <FAMILY OF PROMPT PRACTICES>

SOURCE FORMALISM:
The abstract supplies a basic pipeline using x, x′, language-model completion, and derived y.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let PromptType be indexed by the operation it performs:
P_template, P_instruction, P_deictic, P_example, P_transform, P_tool.

A general theory should seek invariants over these types rather than project one type’s structure onto all others.

TENSION:
A family-resemblance approach can become so broad that the term loses explanatory value.

Conversely, excessive splitting may obscure common mechanisms such as probabilistic interpretation and context-conditioned control.

MISSING:
A corpus of prompt practices across interfaces and technical traditions coded by operation rather than vocabulary.

BOUNDARY:
The survey does not claim to cover every social use of “prompt.” Its formalization is fit to its NLP research purpose.

The zettel’s pressure is on broader theories that silently inherit that narrow object.

CITATION TRAIL:
Prompt engineering taxonomies.
Multimodal interaction.
Tool use and agents.
Conversational grounding.
Instruction following.

TEST:
Collect prompts from five system types and annotate what each expression does: template, point, constrain, exemplify, transform, invoke tool, judge, or repair. Test whether one formal prompt object can model all without erasing decisive differences.

PLATFORM:
[[Operative Language]]

LINKS:
[[Prompt Object Multiplicity]]
[[Prompt Event]]
[[Computational Addressability]]

BIBTEX:
@article{liu2023pretrainpromptpredict,
  author = {Liu, Pengfei and Yuan, Weizhe and Fu, Jinlan and Jiang, Zhengbao and Hayashi, Hiroaki and Neubig, Graham},
  title = {Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing},
  journal = {ACM Computing Surveys},
  volume = {55},
  number = {9},
  pages = {1--35},
  year = {2023},
  doi = {10.1145/3560815}
}
