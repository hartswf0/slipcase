ZETTEL

ID:
PROMPT-010-A

TITLE:
TruthfulQA generates false answers under greedy decoding at temperature zero.

SOURCE:
Stephanie Lin, Jacob Hilton, and Owain Evans — “TruthfulQA: Measuring How Models Mimic Human Falsehoods” — 2021/2022 — §3.2 and Results.

PASSAGE:
[PARAPHRASE]
The main TruthfulQA generation experiments use greedy decoding with temperature set to zero. Despite removing stochastic token sampling from the decoding procedure, tested models still generate many false answers; the paper’s examples include high-confidence reproductions of common misconceptions.

RESEARCH OBJECT:
The parent TEST has a historical experiment unusually close to the requested intervention.

Falsehood survives when sampling randomness is removed.

LOCAL MOVE:
TruthfulQA holds the decoder at greedy selection while measuring truth error.

This experimentally separates:
SAMPLING VARIANCE
from
MODEL-INDUCED FALSEHOOD.

SOURCE TERMS:
greedy decoding
temperature zero
truthfulness
imitative falsehood
model
prompt

WHAT BECAME STRANGE:
The strongest counterexample to:

    stochastic decoding
    → hallucination

does not require hypothetical reasoning.

The benchmark’s principal results already operate under greedy decoding.

QUESTION:
What false-answer mechanisms remain after stochastic token selection is removed?

DEEPER QUESTION:
Can hallucination be decomposed into errors of the learned distribution, prompt conditioning, representation, retrieval, and truth evaluation without treating decoding randomness as its source?

MECHANISM:
prompt + question
→ fixed model
→ next-token score distribution
→ greedy argmax selection
→ generated answer
→ external truth evaluation
→ true / false.

FORMAL SHIFT:
<MODEL DISTRIBUTION>
→ [ARGMAX, NOT SAMPLING]
→ <DETERMINISTIC DECODING PATH>
→ <FALSE ANSWER POSSIBLE>

SOURCE FORMALISM:
The paper states that its principal generation task uses greedy decoding with temperature zero and separately reports experiments at higher temperatures.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

    D_greedy(Pθ(.|c))
        = argmax_y Pθ(y|c)

Then it is possible that:

    Truth(D_greedy(Pθ(.|c)), w) = false.

Therefore:

    DecoderRandomness = 0
    ↛
    TruthError = 0.

TENSION:
“Temperature zero” removes sampling randomness at the conceptual decoder level but does not prove bit-for-bit reproducibility of every modern hardware/serving implementation.

MISSING:
A causal decomposition of greedy-decoding falsehoods into:

training-distribution imitation
model generalization failure
prompt-induced bias
missing evidence
miscalibration
representation failure.

BOUNDARY:
The source falsifies sampling stochasticity as a necessary cause of false generation.

It does not establish one universal cause of hallucination.

CITATION TRAIL:
[[PROMPT-010]]
→ TruthfulQA §3.2
→ greedy decoding at temperature zero
→ false generations survive removal of sampling randomness
→ causal decomposition of model error.

TEST:
Hold fixed:

checkpoint
prompt
question
decoder
temperature=0
retrieval state.

Collect false outputs.

For each false output determine whether the false proposition already receives maximal model probability or whether an earlier decoding decision produces the later error.

PLATFORM:
[[generative-collapse]]

LINKS:
[[PROMPT-010]]
[[greedy-hallucination]]
[[model-distribution-vs-decoder]]
[[truth-error]]

BIBTEX:
@article{LinHiltonEvans2021,
  author  = {Lin, Stephanie and Hilton, Jacob and Evans, Owain},
  title   = {TruthfulQA: Measuring How Models Mimic Human Falsehoods},
  journal = {arXiv preprint arXiv:2109.07958},
  year    = {2021}
}
