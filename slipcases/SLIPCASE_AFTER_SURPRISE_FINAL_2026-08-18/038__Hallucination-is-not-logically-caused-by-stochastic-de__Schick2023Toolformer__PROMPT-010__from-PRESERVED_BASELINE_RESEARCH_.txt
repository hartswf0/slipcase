ZETTEL

ID:
PROMPT-010

TITLE:
Hallucination is not logically caused by stochastic decoding.

SOURCE:
Timo Schick et al. — “Toolformer” — 2023 — §1 notes factual hallucination as an existing model limitation and studies external tools as a remedy. Hydari and Iqbal separately emphasize that deterministic decoding does not imply safe or correct behavior. 10

PASSAGE:
[PARAPHRASE]
Language models may generate false information because their learned predictive behavior does not guarantee factual truth. Sampling introduces one source of run-to-run variation, but removing sampling does not establish correctness.

RESEARCH OBJECT:
TRUTH ERROR and RANDOMNESS are orthogonal dimensions.

LOCAL MOVE:
The risk genealogy must separate inaccurate model distributions from stochastic selection within those distributions.

SOURCE TERMS:
hallucination
sampling
greedy decoding
knowledge
tool
factual lookup

WHAT BECAME STRANGE:
The INPUT derives:

probabilistic semantics
→ hallucination.

But a distribution may assign probability 1 to a false answer.

Conversely, a stochastic distribution may assign probability 1 across a set of equally correct paraphrases.

QUESTION:
Which failure modes arise from probability itself, and which arise from the learned conditional distribution being wrong?

DEEPER QUESTION:
Should hallucination be modeled as semantic unsoundness relative to an external truth relation rather than stochasticity?

MECHANISM:
context
→ model distribution P
→ decoder
→ output y
→ external factual observer
→ true / false / unsupported.

FORMAL SHIFT:
<MODEL OUTPUT DISTRIBUTION>
→ [DECODING]
→ <OUTPUT>
→ [TRUTH OBSERVER]
→ <FACTUAL STATUS>

SOURCE FORMALISM:
NONE that equates hallucination with stochasticity.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let Truth(y,w) evaluate output y against world w.

Hallucination risk:

    Pr_{y~Pθ(.|c)}[¬Truth(y,w)]

Stochasticity concerns whether:

    entropy(Pθ(.|c)) > 0.

Neither condition entails the other.

TENSION:
Sampling from low-probability tails can increase some kinds of factual error, so decoding strategy can modulate hallucination rate.

MISSING:
A causal decomposition of factual error into:
model distribution,
prompt,
decoder,
knowledge access,
retrieval,
and verification.

BOUNDARY:
“Probabilistic” is not a synonym for “unreliable.”

CITATION TRAIL:
factuality evaluation.
retrieval augmentation.
verification.
decoding strategy.

TEST:
Measure factual error under:
greedy,
temperature 0-like deterministic choice,
low-temperature sampling,
high-temperature sampling

with the same checkpoint and prompts.

Separate baseline model error from additional sampling variance.

PLATFORM:
[[generative-collapse]]

LINKS:
[[hallucination-vs-stochasticity]]
[[truth-observer]]
[[decoder-risk]]

BIBTEX:
@inproceedings{Schick2023Toolformer,
  author    = {Schick, Timo and others},
  title     = {Toolformer: Language Models Can Teach Themselves to Use Tools},
  booktitle = {Advances in Neural Information Processing Systems},
  volume    = {36},
  year      = {2023}
}

@article{HydariIqbal2026,
  author  = {Hydari, Muhammad Zia and Iqbal, Raja},
  title   = {The Token Not Taken: Sampling, State, and the Stochasticity of AI Agents},
  journal = {arXiv preprint arXiv:2606.08998},
  year    = {2026}
}
