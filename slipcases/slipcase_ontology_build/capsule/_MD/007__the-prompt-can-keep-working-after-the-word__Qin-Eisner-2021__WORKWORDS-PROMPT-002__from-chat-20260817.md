ZETTEL

ID:
WORKWORDS-PROMPT-002

TITLE:
The prompt can keep working after the words have been removed.

SOURCE:
Guanghui Qin and Jason Eisner — “Learning How to Ask: Querying LMs with Mixtures of Soft Prompts” — 2021 — arXiv:2104.06599

PASSAGE:
[PARAPHRASE] Qin and Eisner replace ordinary prompt words with trainable continuous vectors they call “soft words.” These vectors need not correspond to actual word embeddings. They optimize them by gradient descent and report that even prompts initialized from random vectors can become highly effective at eliciting relational knowledge.

[PARAPHRASE] Their experiments therefore relax the condition that the units controlling a language model must themselves be words from a human language.

RESEARCH OBJECT:
PROMPTING IS LARGER THAN PROMPT LANGUAGE.

There exists an operational descendant of prompting in which:

the function remains

but

the sentence disappears.

LOCAL MOVE:
This pressures the claim that prompt language itself is the new computational language.

Perhaps natural-language prompting is only the human-facing surface of a more general phenomenon:

CONDITIONING A MODEL THROUGH A CONTROL PREFIX.

SOURCE TERMS:
soft prompts
soft words
continuous vectors
gradient descent
prompt mixture
word embeddings
random initialization

WHAT BECAME STRANGE:
If a random collection of continuous vectors can be trained into a better question than an English sentence, then “asking” has become detached from saying.

The computer can be addressed effectively in something that no human can read, pronounce, paraphrase, or understand.

QUESTION:
Which properties of prompting actually require language?

DEEPER QUESTION:
Is natural language the computational medium of prompting, or merely the temporary human-readable encoding of a deeper control space?

MECHANISM:
Hard prompt
→ token embeddings

is relaxed to:

arbitrary vectors
→ gradient optimization
→ model conditioning.

The model receives vectors either way.

Human lexicality is therefore a constraint imposed on one class of prompts, not a necessary condition of model control.

FORMAL SHIFT:
FROM:

WORD
→ MEANING
→ MODEL RESPONSE

TO:

CONTROL VECTOR
→ MODEL STATE
→ RESPONSE.

SOURCE FORMALISM:
The authors permit each soft-prompt token to be an arbitrary vector in R^d rather than requiring it to equal an existing word embedding.

They optimize these vectors using a differentiable log-loss objective and gradient descent and also learn mixtures over multiple prompts.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Human-readable prompt:

p ∈ Vocabulary*

Soft prompt:

z ∈ R^(n×d).

Both can condition:

M(condition, x) → y.

Therefore:

PROMPT ≠ necessarily TEXT.

Text is one admissible coordinate system for controlling M.

TENSION:
This could kill the strongest version of “prompting is a new form of writing.”

But it could also sharpen it.

Writing may matter precisely because hard prompts preserve a peculiar double accessibility:

machine-operational
AND
human-readable.

Soft prompts reveal what is lost when those two properties separate.

MISSING:
Comparative work on what becomes possible or impossible when prompts move among:

natural language,
discrete optimized tokens,
soft vectors,
examples,
images,
structured constraints.

BOUNDARY:
Qin and Eisner study soft prompting of pretrained language models for relational knowledge extraction. Their results do not establish that contemporary conversational LLM interfaces secretly execute equivalent soft prompts.

CITATION TRAIL:
[[DEFAULT-IMAGES-CHI26-F-2]]
→ human non-word can still be model-significant
→ Qin and Eisner
→ even words themselves can disappear
→ prompt becomes model-relative conditioning rather than necessarily language
→ next edge: interface layer that translates human writing into nonlinguistic control.

TEST:
Construct one task in four forms:

ordinary prose prompt,
automatically optimized hard-token prompt,
soft prompt,
formal structured control.

Hold model and evaluation constant.

Compare not only performance but:

human inspectability,
editability,
transfer,
provenance,
semantic predictability,
and ability to explain why a modification worked.

PLATFORM:
Pretrained language models; soft-prompt optimization.

LINKS:
[[DEFAULT-IMAGES-CHI26-F-2]]

BIBTEX:
@article{QinEisner2021SoftPrompts,
  author = {Qin, Guanghui and Eisner, Jason},
  title = {Learning How to Ask: Querying LMs with Mixtures of Soft Prompts},
  year = {2021},
  url = {https://arxiv.org/abs/2104.06599}
}
