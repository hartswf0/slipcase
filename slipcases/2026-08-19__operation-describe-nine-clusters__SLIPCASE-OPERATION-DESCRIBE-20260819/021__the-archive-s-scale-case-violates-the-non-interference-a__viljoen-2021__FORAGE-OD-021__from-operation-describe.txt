ZETTEL

ID:
FORAGE-OD-021

TITLE:
THE ARCHIVE'S SCALE CASE VIOLATES THE NON-INTERFERENCE ASSUMPTION ITS COUNTERFACTUAL REQUIRES

SOURCE:
Watson Hartsoe — PAPERS/operation-describe-label-01.md §3 "Causality: Holding the Input Constant" and §17; read against Moritz Hardt, Meena Jagadeesan, Celestine Mendler-Dünner — Performative Power — arXiv:2203.17232 — 2022 — §5.2, and Salomé Viljoen — A Relational Theory of Data Governance — Yale Law Journal — 2021

PASSAGE:
[QUOTE]
label-01 §3:
"Causality is proven by holding the input constant and varying only the description. ... The counterfactual is the unlabeled or baseline state."

[QUOTE]
label-01 §17:
"if adding GitHub issue labels has no statistical effect on issue resolution times"

[PARAPHRASE]
Hardt et al.'s position-effect estimator requires non-interference: what is shown to one participant must not change another participant's behavior.

RESEARCH OBJECT:
A `good first issue` label does not add contributor attention. It reallocates a fixed pool of it. When one contributor takes the labeled issue, that issue leaves the pool for everyone else, and the unlabeled issues become relatively more available.

The counterfactual "the same issue without the label" is therefore not identified: the untreated issues are not untreated. They are affected by the treatment of others.

LOCAL MOVE:
The archive borrows the language of controlled comparison ("holding the input constant") from experimental design, and applies it to a setting where the outcome variable is a shared, rivalrous resource.

SOURCE TERMS:
holding the input constant
counterfactual
unlabeled baseline
statistical effect
resolution times
non-interference
horizontal data relations
population-level effects

WHAT BECAME STRANGE:
"Resolution time" is the archive's chosen outcome for the scale case, and it is one of the most interference-contaminated quantities available. It depends on queue depth, maintainer availability, release cadence, and every other label applied that week.

The archive picked the outcome that is easiest to scrape and hardest to identify.

QUESTION:
What is the correct estimand for a routing effect when routing reallocates a fixed pool of operator attention rather than creating new action?

DEEPER QUESTION:
If interference is not noise around the phenomenon but the phenomenon itself — as Viljoen's relational account implies — is the individual description/action pair the wrong unit of analysis for every case in the archive except the sandboxed one?

MECHANISM:
<LABEL APPLIED TO ISSUE i>
→ raises salience of i
→ contributor selects i
→ [i REMOVED FROM THE POOL]
→ relative salience of all j ≠ i changes
→ resolution times of unlabeled issues shift
→ <TREATMENT AND CONTROL ARE COUPLED>

FORMAL SHIFT:
<LABEL>
→ <REALLOCATION OF A FIXED ATTENTION POOL>
→ [SUTVA VIOLATION]
→ <UNIDENTIFIED COUNTERFACTUAL>

SOURCE FORMALISM:
Hardt et al. state non-interference explicitly as a condition on their lower bound. The archive states no assumptions at all for its GitHub design.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Under interference, the individual effect is not defined; only contrasts between *allocation policies* are.

  estimand = E[outcome | policy π₁] − E[outcome | policy π₂]

where a policy is a rule for which issues get labeled, applied at the repository-week level.

This changes the unit of analysis from the label to the labeling *regime*, and the design from issue-level comparison to cluster randomization or interrupted time series over repository-weeks.

It also reframes the political question productively. Under congestion, a label does not only route; it *deprives*. The unlabeled issue is not neutral, it is disadvantaged. That is a stronger political claim than the archive currently makes, and it is the one the mechanism supports.

TENSION:
READING A: with enough issues and contributors, interference is negligible and issue-level comparison is approximately valid.
READING B: interference is strongest exactly where the archive's interest lies — scarce maintainer attention, competition for `good first issue` work, credit allocation — so the approximation fails on the cases that matter.

Discriminating evidence: measure whether resolution times of *unlabeled* issues change when labeling rates change. If they do, interference is first-order.

MISSING:
Any assumption statement, cluster design, or spillover measurement in the archive's GitHub plan. Also missing: any use of the archive's own Bateson chapter, which is about circuits and cannot be reconciled with issue-level independence.

BOUNDARY:
This concerns identification, not existence. Labels almost certainly route labor. The claim licensed is that the archive's stated design cannot measure by how much.

CITATION TRAIL:
Viljoen — A Relational Theory of Data Governance — 2021.
SLIPCASE FORAGE-HARDT-VILJOEN-001 and -002 — the user's own corpus, where this exact tension is already recorded for platform power and never transferred to labels.
Spillover and interference in causal inference; cluster-randomized designs.
PAPERS/cyber-00.md §3 (Bateson: "mind is the circuit, not the skull").
FORAGE-OD-009, FORAGE-OD-022.

TEST:
On a public repository with a long history, regress resolution time of *unlabeled* issues on the contemporaneous rate of labeling of other issues, controlling for volume.

A non-zero coefficient is direct evidence of interference and forces the design change. This uses only public data and can be run in an afternoon.

PLATFORM:
[[routing-under-congestion]]

LINKS:
[[FORAGE-OD-009]]
[[FORAGE-OD-022]]
[[FORAGE-OD-015]]

BIBTEX:
@article{viljoen2021relational,
  title={A Relational Theory of Data Governance},
  author={Viljoen, Salom{\'e}},
  journal={Yale Law Journal},
  volume={131},
  pages={573--654},
  year={2021},
  url={https://yalelawjournal.org/feature/a-relational-theory-of-data-governance}
}
