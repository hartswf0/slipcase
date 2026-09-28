ZETTEL

ID:
ENCOUNTER-OP-033

TITLE:
Linguistic convergence is measurable but does not prove encounter.

SOURCE:
Holly P. Branigan, Martin J. Pickering, Jamie Pearson, and Janet F. McLean — “Linguistic alignment between people and computers” — 2010 — Journal of Pragmatics 42(9), 2355–2368. ([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0378216609003282))

PASSAGE:
[PARAPHRASE] Human speakers align linguistically with computers; the reviewed evidence suggests such alignment can be stronger than human-human alignment and may be substantially driven by attempts to improve communicative success. ([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0378216609003282))

RESEARCH OBJECT:
Behavioral coupling must be distinguished from relational reciprocity because humans can adapt strongly to a machine precisely because they believe adaptation is necessary.

LOCAL MOVE:
The authors distinguish alignment arising from relatively automatic language-processing mechanisms from alignment mediated by beliefs about the interlocutor, communicative success, or social affect.

SOURCE TERMS:
linguistic alignment
syntax
lexicon
beliefs
communicative success
social affect
mediated
unmediated

WHAT BECAME STRANGE:
More convergence can indicate greater asymmetry. The human may converge on machine-preferred forms because the machine is perceived as inflexible.

QUESTION:
When linguistic alignment increases in an AI conversation, who is adapting to whom?

DEEPER QUESTION:
Could high surface synchrony coexist with low bidirectional coupling?

MECHANISM:
interlocutor behavior
→ expectation about successful communication
→ adaptation of lexical/syntactic choices
→ observable convergence.

FORMAL SHIFT:
<SURFACE SIMILARITY>
→ <DIRECTIONAL ADAPTATION>
→ [CAUSAL MANIPULATION]
→ <COUPLING OR ACCOMMODATION?>

SOURCE FORMALISM:
The paper distinguishes:
UNMEDIATED alignment mechanisms
from
MEDIATED mechanisms involving beliefs about the interlocutor, communicative success, or social affect. ([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0378216609003282))

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

ALIGNMENT MATRIX:

H→AI = change in human language conditional on AI language
AI→H = change in AI language conditional on human language

SYMMETRIC COUPLING requires estimating both directions separately.

High(H→AI) + Low(AI→H)
should not be reported simply as “high relational alignment.”

TENSION:
Encounter theory may treat synchrony, resonance, or convergence as relational evidence. Alignment research shows that the same traces can arise from unilateral accommodation.

MISSING:
Experiments that perturb human and AI linguistic styles independently enough to estimate both directional effects.

BOUNDARY:
Linguistic alignment concerns observable language form. It cannot by itself determine shared meaning, agency, relationship, or epistemic transformation.

CITATION TRAIL:
[[ENCOUNTER-AI-016]]
[[ENCOUNTER-006]]
→ Branigan et al. 2010
→ entrainment
→ accommodation
→ directional coupling estimates.

TEST:
Randomly vary AI lexical and syntactic style across otherwise equivalent interactions while separately manipulating how strongly the model mirrors user language. Estimate H→AI and AI→H adaptation independently and relate each to repair success and artifact development.

PLATFORM:
[[Operational Encounter Model]]

LINKS:
[[ENCOUNTER-AI-016]]
[[ENCOUNTER-006]]
[[Linguistic Alignment]]
[[Directional Coupling]]

BIBTEX:
@article{BraniganEtAl2010Alignment,
  author = {Holly P. Branigan and Martin J. Pickering and Jamie Pearson and Janet F. McLean},
  title = {Linguistic alignment between people and computers},
  journal = {Journal of Pragmatics},
  year = {2010},
  volume = {42},
  number = {9},
  pages = {2355--2368},
  doi = {10.1016/j.pragma.2009.12.012}
}