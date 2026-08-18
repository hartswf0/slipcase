ZETTEL

ID:
CBX-009-CONVINCINGNESS-HAS-NO-PERSON

TITLE:
Evidence that wins a comparison is not evidence that changes a particular person.

SOURCE:
Gleize et al. — Are You Convinced? Choosing the More Convincing Evidence with a Siamese Network — 2019.

PASSAGE:
[PARAPHRASE]
EviConv constructs a task in which pairs of evidence are labeled according to which is more convincing and trains a model to predict that comparative judgment.

RESEARCH OBJECT:
Convincingness ranking and personalized persuasion optimize different objects.

LOCAL MOVE:
The source turns convincingness into a pairwise prediction problem over evidence.

SOURCE TERMS:
convincingness
evidence
pairwise comparison
Siamese network
argumentation

WHAT BECAME STRANGE:
The Centaur paper groups EviConv with evidence for increasingly sophisticated persuasive AI, but EviConv does not require a psychographic representation of the individual being persuaded.

QUESTION:
What transformation licenses movement from “this evidence is generally judged more convincing” to “this evidence will change this gatekeeper”?

DEEPER QUESTION:
Is personalized persuasion being assembled by silently joining models whose target variables are fundamentally different?

MECHANISM:
evidence A + evidence B
→ comparative representation
→ convincingness prediction
→ ranked evidence.

FORMAL SHIFT:
<EVIDENCE PAIR>
→ <PAIR REPRESENTATION>
→ [COMPARE CONVINCINGNESS]
→ <A > B OR B > A>

SOURCE FORMALISM:
A Siamese-network architecture is used to learn comparative convincingness. Exact source equations are not reproduced here.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

EviConv-like target:
rank(E_a, E_b)

Centaur-required target:
Δbelief(person_i | E_a)

These are not interchangeable functions.

TENSION:
A universally high-ranking argument could have no causal effect on a particular gatekeeper; a generally weak argument could matter greatly given a specific belief or institutional state.

MISSING:
The bridge from pairwise convincingness labels to individual-level causal response.

BOUNDARY:
EviConv remains relevant to argument selection. The evidence does not by itself establish psychographic personalization.

CITATION TRAIL:
Gleize et al. 2019.
Persuasion for Good.
Strategic argumentation models that explicitly represent persuadee beliefs and concerns.
Causal studies of message heterogeneity.

TEST:
Compare three selectors on held-out individuals:
(1) general convincingness rank,
(2) psychographic profile,
(3) belief/state-conditioned treatment prediction.
Measure actual belief or action change rather than judged convincingness.

PLATFORM:
[[Centaur Box — Source Translation]]

LINKS:
[[Convincingness Is Not Persuasion]]
[[The Target Variable Changed]]
[[Source Migration Without Equivalence]]

BIBTEX:
@inproceedings{gleize2019convinced,
  title={Are You Convinced? Choosing the More Convincing Evidence with a Siamese Network},
  author={Gleize, Martin and Shnarch, Eyal and Choshen, Leshem and Dankin, Lena and Moshkowich, Guy and Aharonov, Ranit and Slonim, Noam},
  booktitle={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
  pages={967--976},
  year={2019},
  doi={10.18653/v1/P19-1093}
}
