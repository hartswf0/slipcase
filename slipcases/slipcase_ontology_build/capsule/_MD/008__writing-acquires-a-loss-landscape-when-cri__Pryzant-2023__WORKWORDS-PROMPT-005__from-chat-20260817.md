ZETTEL

ID:
WORKWORDS-PROMPT-005

TITLE:
Writing acquires a loss landscape when criticism is treated as a textual gradient.

SOURCE:
Reid Pryzant, Dan Iter, Jerry Li, Yin Tat Lee, Chenguang Zhu, and Michael Zeng — “Automatic Prompt Optimization with ‘Gradient Descent’ and Beam Search” — EMNLP 2023 — arXiv:2305.03495

PASSAGE:
[PARAPHRASE] Pryzant et al. propose Automatic Prompt Optimization. An LLM examines failures produced by a prompt and generates natural-language criticisms called textual “gradients.” Candidate prompts are then rewritten in the opposite semantic direction of those criticisms, with beam search and bandit selection used to choose promising revisions.

RESEARCH OBJECT:
PROSE BECOMES AN OPTIMIZATION VARIABLE.

The strange move is not simply automated editing.

It is importing the conceptual machinery of numerical optimization into semantic revision:

failure
→ criticism
→ direction
→ changed sentence.

LOCAL MOVE:
Prompt practice moves from:

WRITE / INTERPRET / REWRITE

toward:

OBJECTIVE / ERROR / SEMANTIC DIRECTION / UPDATE.

SOURCE TERMS:
Automatic Prompt Optimization
textual gradients
gradient descent
beam search
bandit selection
prompt editing

WHAT BECAME STRANGE:
Criticism stops being commentary outside the work.

It becomes an operation that changes the work.

A sentence such as:

“the instruction fails to distinguish X from Y”

can function as something analogous to directional information in an optimization procedure.

QUESTION:
What is lost when revision is reframed as optimization?

DEEPER QUESTION:
Can writing have a gradient without first reducing what counts as good writing to an evaluable objective?

MECHANISM:
Prompt
→ run on minibatch
→ inspect failures
→ LLM produces natural-language criticism
→ generate semantically opposed edits
→ evaluate candidates
→ retain better candidate
→ repeat.

FORMAL SHIFT:
FROM:

REVISION = authorial judgment

TO:

REVISION =
error assignment
+
direction proposal
+
candidate search
+
selection criterion.

SOURCE FORMALISM:
The authors explicitly describe natural-language criticisms as textual “gradients,” edit prompts in the opposite semantic direction, and combine these updates with beam search and a bandit-selection procedure.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let prompt be P and evaluator be E.

E(P) → failures F.

Critic:

C(F,P) → textual direction g_text.

Rewrite:

R(P,-g_text) → {P1,...,Pn}.

Selection:

P' = argmax score(Pi).

The “gradient” is therefore not numerical differentiation.

It is a language-produced proposal about how the instruction should move.

TENSION:
The gradient metaphor is technically useful but philosophically dangerous.

Numerical gradients have formally defined local meaning.

“Textual gradients” are model-generated interpretations of failure.

Their direction is itself another act of language.

So optimization has not escaped interpretation.

It has recursively inserted interpretation into the optimization loop.

MISSING:
Cases where a textual gradient improves the metric while destroying:

style,
openness,
surprise,
interpretive richness,
minority cases,
or values absent from the evaluator.

BOUNDARY:
The method requires evaluable tasks and training examples. Prompt practices whose success cannot be reduced to a stable metric may resist this optimization structure.

CITATION TRAIL:
[[DEFAULT-IMAGES-CHI26-A-1]]
→ meaning can be gained or lost during execution
→ ProTeGi makes failure generate instructions for rewriting instructions
→ prompt practice acquires semantic backpropagation
→ next edge: TextGrad, credit assignment, aesthetic optimization, and Goodhart effects.

TEST:
Select one creative prompt.

Define two evaluators:

narrow measurable success
and
human judgment of interestingness.

Optimize the prompt repeatedly against the narrow metric.

Preserve every generation.

Test whether objective improvement creates a measurable decline in outputs humans consider surprising, rich, or worth keeping.

PLATFORM:
LLM prompt optimization.

LINKS:
[[DEFAULT-IMAGES-CHI26-A-1]]

BIBTEX:
@article{Pryzant2023APO,
  author = {Pryzant, Reid and Iter, Dan and Li, Jerry and Lee, Yin Tat and Zhu, Chenguang and Zeng, Michael},
  title = {Automatic Prompt Optimization with "Gradient Descent" and Beam Search},
  year = {2023},
  url = {https://arxiv.org/abs/2305.03495}
}
