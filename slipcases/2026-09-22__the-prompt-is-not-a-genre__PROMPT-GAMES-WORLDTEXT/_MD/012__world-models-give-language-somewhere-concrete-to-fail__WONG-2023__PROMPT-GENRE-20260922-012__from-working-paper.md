ZETTEL

ID:
PROMPT-GENRE-20260922-012

TITLE:
World models give language somewhere concrete to fail

SOURCE:
Lionel Wong et al., "From Word Models to World Models: Translating from Natural Language to the Probabilistic Language of Thought," 2023.

SOURCE URL:
https://arxiv.org/abs/2306.12672

PASSAGE:
[PARAPHRASE]\nWong and colleagues map natural-language utterances into probabilistic programs and explore how language can construct generative world models that support inference.

RESEARCH OBJECT:
[OUR INFERENCE]\nA WORLD MODEL ADDS RESISTANCE: THE RESULT CAN VIOLATE GEOMETRY, CAUSAL STRUCTURE, OR OTHER EXPLICIT RELATIONS.

LOCAL MOVE:
Shift evaluation from discourse plausibility toward consequences in an executable model.

SOURCE TERMS:
word model; world model; probabilistic language of thought; simulation

WHAT BECAME STRANGE:
When downstream reasoning happens in an explicit world representation, language can be wrong in ways that fluent prose alone may not expose.

QUESTION:
What new failure modes become visible when text is grounded in an executable model?

DEEPER QUESTION:
How much of prompting's apparent unreliability is actually the absence of a substrate that can veto language?

MECHANISM:
Natural language populates or modifies variables and relations in a generative model whose consequences are then computed.

FORMAL SHIFT:
WORD -> MODEL -> CONSEQUENCE -> TEST.

SOURCE FORMALISM:
[PARAPHRASE]\nRational meaning construction translates natural language into probabilistic programs supporting generative modeling and inference.

OUR FORMALIZATION:
World resistance is epistemically valuable because it localizes failure.

TENSION:
Explicit models can be wrong, incomplete, or over-closed just as microworlds can.

MISSING:
Methods for comparing world-model error with language-model error across the same task.

BOUNDARY:
The paper does not claim that this architecture proves human-like understanding.

CITATION TRAIL:
Wong/Tenenbaum -> probabilistic program -> world model -> veto.

TEST:
Compare text-only answers with answers forced through an explicit simulator on tasks with checkable physical or causal consequences.

PLATFORM:
World models; probabilistic programming; grounding

LINKS:
[[PROMPT-GENRE-20260922-004]]
[[PROMPT-GENRE-20260922-011]]
[[PROMPT-GENRE-20260922-013]]

BIBTEX:
@article{wong2023wordworld,
  author={Wong, Lionel and Grand, Gabriel and Lew, Alexander K. and Goodman, Noah D. and Mansinghka, Vikash K. and Andreas, Jacob and Tenenbaum, Joshua B.},
  title={From Word Models to World Models: Translating from Natural Language to the Probabilistic Language of Thought},
  journal={arXiv preprint arXiv:2306.12672},
  year={2023},
  url={https://arxiv.org/abs/2306.12672}
}
