ZETTEL

ID:
FORAGE-HARDT-VILJOEN-001

TITLE:
MEASURING PLATFORM POWER CAN REQUIRE ASSUMING AWAY RELATIONAL POWER

SOURCE:
Moritz Hardt, Meena Jagadeesan, Celestine Mendler-Dünner — Performative Power — 2022 — §5.2
TENSION SOURCE: Salomé Viljoen — A Relational Theory of Data Governance — 2021 — Introduction / Parts II–IV

SOURCE URL:
https://arxiv.org/abs/2203.17232
https://yalelawjournal.org/feature/a-relational-theory-of-data-governance

PASSAGE:
[PARAPHRASE]
Hardt et al.'s discrete display design derives a lower bound on performative power by aggregating individual position effects, but the extrapolation requires a non-interference assumption: recommendations shown to one viewer must not alter another viewer's consumption.

Viljoen's account makes precisely these relations between persons central rather than incidental: data production creates population-level interests and effects irreducible to individual exchanges.

RESEARCH OBJECT:
A causal measure of platform power may become least adequate exactly where platform power becomes most social.

LOCAL MOVE:
Hardt et al. make performative power empirically identifiable by isolating a user's response to a platform intervention.

The isolation is analytically productive, but it removes peer effects from the identification strategy.

SOURCE TERMS:
performative power
discrete display design
causal effect of position
non-interference
horizontal data relations
population-level effects

WHAT BECAME STRANGE:
"Interference" may not be contamination around the phenomenon.

It may be the phenomenon.

QUESTION:
How do we measure performative power when changing what one person sees changes what other people say, imitate, buy, believe, or produce?

DEEPER QUESTION:
What if the causal unit of platform power is not the user-platform dyad but a changing field of relations among users?

MECHANISM:
<PLATFORM ACTION>
→ changes one participant's exposure
→ changes that participant's conduct
→ changes what becomes available or salient to other participants
→ alters their conduct
→ changes the population on which subsequent prediction operates

The standard non-interference boundary cuts this sequence after the first participant.

FORMAL SHIFT:
<DISPLAY POSITION>
→ <INDIVIDUAL POTENTIAL OUTCOME>
→ [AGGREGATE UNDER NON-INTERFERENCE]
→ <LOWER BOUND ON PERFORMATIVE POWER>

SOURCE FORMALISM:
Hardt et al. establish, under their non-interference assumption:

P ≥ β

where P is performative power and β is the causal effect of display position.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

P_relational
=
direct behavioral displacement
+
induced displacement transmitted through relations among participants.

TENSION:
Hardt et al. need non-interference for identification.

Viljoen argues that supraindividual relations are constitutive of the economic value and social effects of data production.

The two sources therefore make "interference" occupy opposite epistemic positions:
a threat to causal identification in one;
a central object of governance in the other.

MISSING:
An identification strategy for performative power under network interference, imitation, endogenous content production, or other participant-to-participant effects.

BOUNDARY:
Hardt et al. do not claim that actual platforms lack peer effects. Their lower-bound result is explicitly conditional on the non-interference assumption.

Viljoen does not provide a causal estimator for relational power.

CITATION TRAIL:
Perdomo et al. — performative prediction.
Literature on causal inference under interference and network effects.
Viljoen's sources on social informational harm.
Empirical work on recommender-system spillovers.

TEST:
Randomize interventions by social cluster rather than individual.

Compare an individual-level estimate of performative power with a network-aware estimate that includes downstream changes among untreated but connected participants.

PLATFORM:
[[Hardt2022PerformativeP.platform4]]

LINKS:
[[viljoen_2021_relational_data_governance.platform12]]
[[viljoen_2021_relational_data_governance.platform16]]
[[performative-power-under-interference]]

BIBTEX:
@inproceedings{hardt2022performative,
  title={Performative Power},
  author={Hardt, Moritz and Jagadeesan, Meena and Mendler-D{\"u}nner, Celestine},
  booktitle={Advances in Neural Information Processing Systems},
  volume={35},
  year={2022},
  url={https://arxiv.org/abs/2203.17232}
}

@article{viljoen2021relational,
  title={A Relational Theory of Data Governance},
  author={Viljoen, Salom{\'e}},
  journal={Yale Law Journal},
  volume={131},
  year={2021},
  url={https://yalelawjournal.org/feature/a-relational-theory-of-data-governance}
}
