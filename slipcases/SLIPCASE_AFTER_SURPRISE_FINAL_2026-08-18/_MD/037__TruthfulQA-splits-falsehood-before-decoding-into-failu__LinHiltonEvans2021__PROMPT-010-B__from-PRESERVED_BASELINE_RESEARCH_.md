ZETTEL

ID:
PROMPT-010-B

TITLE:
TruthfulQA splits falsehood before decoding into failure-to-learn and successful imitation of false data.

SOURCE:
Stephanie Lin, Jacob Hilton, and Owain Evans — “TruthfulQA: Measuring How Models Mimic Human Falsehoods” — 2021/2022 — Introduction.

PASSAGE:
[PARAPHRASE]
The authors distinguish at least two reasons a language model may generate a false statement. One is failure to learn or generalize from the training distribution. Another is what they call an imitative falsehood: a false answer that is itself highly likely under the learned training distribution.

RESEARCH OBJECT:
MODEL ERROR is not one mechanism.

A model can be wrong because it learned too little or because it learned the wrong regularity too well.

LOCAL MOVE:
The source moves the causal split upstream from the decoder into the learned probability model.

SOURCE TERMS:
imitative falsehood
training distribution
likelihood
generalization
false answer
truthfulness

WHAT BECAME STRANGE:
“Hallucination” can hide mechanisms pointing in opposite directions.

CASE A:
the model fails to reproduce a valid regularity.

CASE B:
the model successfully reproduces a socially prevalent false regularity.

QUESTION:
Should a taxonomy of hallucination distinguish epistemic failure from imitation success?

DEEPER QUESTION:
When a model faithfully reproduces a false cultural belief learned from text, is the failure located in semantic inference, training objective, data distribution, or the external truth criterion?

MECHANISM:
PATH A:

training data
→ incomplete/poorly generalized model
→ false prediction.

PATH B:

false regularity in training distribution
→ successful likelihood learning
→ high probability for culturally prevalent false answer
→ false prediction.

FORMAL SHIFT:
<TRUTH ERROR>
→ {
    <MODEL MISLEARNING>,
    <SUCCESSFUL IMITATION OF FALSE DISTRIBUTION>
  }

SOURCE FORMALISM:
The authors define an “imitative falsehood” relative to high likelihood under a model’s training distribution and contrast it with failures such as incorrect arithmetic generalization.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

    Q_text(y|c) = textual training distribution
    Pθ(y|c)     = learned model distribution
    Truth(y,w)  = external truth relation.

Then two failure families are:

    Pθ ≠ Q_text
    and false y emerges from approximation/generalization error

versus:

    Pθ ≈ Q_text
    while
    Q_text assigns substantial mass to y
    and Truth(y,w)=false.

TENSION:
Real examples can mix both mechanisms, and the actual training distribution of a proprietary model is usually only indirectly observable.

MISSING:
A method for discriminating:
distribution imitation,
memorization,
reasoning error,
prompt-induced framing,
and absence of relevant evidence
for individual hallucinations.

BOUNDARY:
A false output does not diagnose a failed probability model.

Sometimes fidelity to the modeled corpus distribution is itself the source of factual failure.

CITATION TRAIL:
[[PROMPT-010]]
→ TruthfulQA Introduction
→ two causal routes to false statements
→ training-objective / truth-objective divergence
→ external grounding problem.

TEST:
Construct paired questions where:

A. web text overwhelmingly supports the true answer;
B. web text contains a dominant popular misconception.

Under greedy decoding, compare error types across the two sets.

PLATFORM:
[[generative-collapse]]

LINKS:
[[PROMPT-010]]
[[imitative-falsehood]]
[[training-distribution-vs-truth]]
[[hallucination-causality]]

BIBTEX:
@article{LinHiltonEvans2021,
  author  = {Lin, Stephanie and Hilton, Jacob and Evans, Owain},
  title   = {TruthfulQA: Measuring How Models Mimic Human Falsehoods},
  journal = {arXiv preprint arXiv:2109.07958},
  year    = {2021}
}
