ZETTEL

ID:
FORAGE-HUDGENS-HALLORAN-002

TITLE:
THE INDIRECT EFFECT CAN BE LARGER THAN THE DIRECT EFFECT AND STILL NOT BE CAUSALLY IDENTIFIED

SOURCE:
Michael G. Hudgens and M. Elizabeth Halloran — Toward Causal Inference With Interference — 2008 — §§1.2, 5.2

PASSAGE:
[PARAPHRASE]
Using published cholera-vaccine data as motivation, Hudgens and Halloran calculate an apparent indirect effect among unvaccinated people of 5.54 fewer cases per 1,000 under high rather than low vaccine coverage.

That difference is larger than either within-group direct-effect estimate.

Later, however, they explicitly warn that their causal methodology cannot be directly applied to those data because communities were not randomly assigned to vaccine-coverage levels. They replace the observational comparison with a hypothetical two-stage randomized experiment.

RESEARCH OBJECT:
A dataset can make a relational effect spectacularly visible while remaining unable to establish that the relation caused it.

LOCAL MOVE:
The source uses the observational contrast to expose why indirect effects matter, then withdraws causal identification from that same example and specifies the experiment that would be required.

SOURCE TERMS:
direct effect
indirect effect
total effect
overall effect
coverage
two-stage randomization
interference

WHAT BECAME STRANGE:
The most persuasive-looking evidence for relational power may be the evidence whose causal interpretation requires the greatest restraint.

QUESTION:
How much platform research mistakes differences between high-exposure and low-exposure ecologies for causal evidence of indirect platform effects?

DEEPER QUESTION:
What experiment corresponds to the claim that a platform changes not merely treated users but the environment in which untreated people act?

MECHANISM:
Observed case:

<HIGH-COVERAGE ECOLOGY>
versus
<LOW-COVERAGE ECOLOGY>
→ large outcome difference among untreated individuals

But:

coverage not randomized
→ ecology may differ for other reasons
→ indirect causal effect not identified

Required design:

randomize groups to allocation regimes
→ randomize individuals within groups
→ compare potential outcomes across regimes

FORMAL SHIFT:
<OBSERVED ECOLOGICAL DIFFERENCE>
→ <CANDIDATE INDIRECT EFFECT>
→ [RANDOMIZE EXPOSURE REGIME]
→ <CAUSALLY IDENTIFIABLE INDIRECT EFFECT>

SOURCE FORMALISM:
The motivating example computes:

7.01 - 1.47 = 5.54

fewer cholera cases per 1,000 as an estimated indirect effect among unvaccinated individuals in the observational coverage comparison.

The authors subsequently state that direct application of their proposed method is inappropriate because the groups were not randomized to coverage levels.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

VISIBLE RELATIONAL DIFFERENCE
≠
IDENTIFIED RELATIONAL CAUSE

Identification requires intervention on the distribution of treatment itself:

do(ALLOCATION REGIME = A)
versus
do(ALLOCATION REGIME = B)

not merely comparison of populations that happen to occupy A and B.

TENSION:
[[FORAGE-HARDT-VILJOEN-001]] asks how relational platform effects can be measured once interference is admitted.

The present source adds a second trap:

even after the correct relational outcome becomes visible, observational variation in population exposure may not identify its cause.

MISSING:
Platform experiments that randomize allocation regimes rather than only individual recommendations.

The missing intervention may be:
percentage of a community exposed,
ranking regime applied to a creator ecosystem,
distribution of generated content,
moderation prevalence,
or availability of a behavioral affordance.

BOUNDARY:
The numerical cholera comparison is an illustration, not a valid causal estimate under Hudgens and Halloran's proposed design.

Nothing in the source licenses transferring the reported magnitude to platform systems.

CITATION TRAIL:
[[FORAGE-HARDT-VILJOEN-001]]
→ Hudgens and Halloran
→ two-stage randomized designs
→ saturation and allocation experiments
→ platform experiments where the treatment is a population-level exposure regime rather than an individual item

TEST:
Instead of randomizing recommendation R to isolated users, randomly assign comparable communities to different saturation levels of R.

Within each community, randomize which members directly receive R.

Estimate separately:

direct effect on recipients,
indirect effect on nonrecipients,
total effect,
overall community effect.

Then compare these with the conventional individual-level A/B estimate.

PLATFORM:
[[relational-power-under-interference]]

LINKS:
[[FORAGE-HARDT-VILJOEN-001]]
[[population-exposure-is-an-intervention]]
[[observed-relational-difference-is-not-relational-causation]]

BIBTEX:
@article{hudgens2008interference,
  title={Toward Causal Inference With Interference},
  author={Hudgens, Michael G. and Halloran, M. Elizabeth},
  journal={Journal of the American Statistical Association},
  volume={103},
  number={482},
  pages={832--842},
  year={2008},
  doi={10.1198/016214508000000292}
}
