ZETTEL

ID:
FORAGE-OD-009

TITLE:
THE POSITION EFFECT THAT THREATENS THE PRIMARY CASE IS THE EXACT QUANTITY ANOTHER LITERATURE USES TO MEASURE PLATFORM POWER

SOURCE:
Moritz Hardt, Meena Jagadeesan, Celestine Mendler-Dünner — Performative Power — arXiv:2203.17232 — 2022 — §5.2; read against Huang et al. — arXiv:2407.03007 — 2024 — §5.2; and against the SLIPCASE zettel FORAGE-HARDT-VILJOEN-001

PASSAGE:
[PARAPHRASE]
Hardt et al. derive a lower bound on a platform's performative power from a discrete display design: the causal effect of the *position* at which an item is shown, aggregated across viewers under a non-interference assumption.

[PARAPHRASE]
Huang et al. treat the same ordering sensitivity in an LLM's tool list as an instability to be minimized.

RESEARCH OBJECT:
One field's confound is another field's estimator. Display position is the cheapest available randomizable intervention on a routing system, which is why economists of platform power built their identification strategy on it — and why it contaminates the archive's semantic manipulation.

LOCAL MOVE:
The collision is not analogical. It is the same manipulation — randomize where an option appears — read once as noise and once as signal.

SOURCE TERMS:
performative power
discrete display design
causal effect of position
non-interference
positional bias of tools
lower bound

WHAT BECAME STRANGE:
The archive has been searching for a causal design that isolates routing (label-00 §3, label-01 §3) while an adjacent literature has had one since 2022 — and it isolates routing by *refusing* to touch the description at all.

Position randomization gives an unbiased estimate of how much the *presentation apparatus* routes action, independent of what anything says. That is the counterfactual baseline against which any semantic effect must be judged.

QUESTION:
What does the archive's ΔG look like when position-randomization is used as the *baseline* rather than treated as noise?

DEEPER QUESTION:
If a platform's power over routing can be lower-bounded without reference to meaning, does "operative description" measure a residual — the part of routing that survives after apparatus power is subtracted?

MECHANISM:
<RANDOMIZED POSITION>
→ exogenous variation in exposure
→ [MEASURE CHANGE IN SELECTION]
→ <LOWER BOUND ON APPARATUS ROUTING POWER>

then

<SEMANTIC VARIATION, LENGTH-MATCHED>
→ [MEASURE ADDITIONAL CHANGE]
→ <DESCRIPTIVE ROUTING POWER AS RESIDUAL ABOVE BASELINE>

FORMAL SHIFT:
<POSITION RANDOMIZATION>
→ <EXOGENOUS INSTRUMENT>
→ [CAUSAL LOWER BOUND]
→ <APPARATUS POWER>
→ <DESCRIPTION POWER AS RESIDUAL>

SOURCE FORMALISM:
Hardt et al.: aggregate individual position effects under non-interference to obtain a lower bound on performative power.

Huang et al.: report shuffled-vs-original success rates as a stability metric.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

  Routing power = P_apparatus + P_description + interaction

Estimate P_apparatus by position randomization with text held fixed.
Estimate P_description by length-matched semantic variation with position held fixed.

Report the ratio. The dissertation's contribution becomes a *share of variance* claim, which is defensible, quantitative, and comparative across all three cases.

TENSION:
Hardt et al.'s bound requires non-interference: what one viewer sees must not change another's behavior. For the archive's LLM case that holds trivially (independent API calls). For the GitHub case it fails by construction — labels route a shared, rivalrous pool of contributor attention.

So the design transfers cleanly to the case with no politics and fails on the case that carries the politics.

MISSING:
An interference-robust version of the estimator for congested routing. Viljoen's relational account (SLIPCASE FORAGE-HARDT-VILJOEN-001) says the relations *are* the phenomenon; no estimator in the archive respects that.

BOUNDARY:
Hardt et al. bound a platform's power in a recommendation setting. Transferring the *design* is warranted; transferring the *interpretation* ("performative power") to tool schemas is not, and would be exactly the formal-resemblance-as-genealogy error the archive warns against.

CITATION TRAIL:
Salomé Viljoen — A Relational Theory of Data Governance — 2021.
Performative prediction (Perdomo, Zrnic, Mendler-Dünner, Hardt).
SLIPCASE case "2026 08 17 — prompt semantics hidden machinery" — the user's own corpus already holds this collision in a different vocabulary.
FORAGE-OD-021.

TEST:
Run the archive's primary experiment with a 2×2: {position randomized, position fixed} × {description varied, description fixed}. Four cells, one task, one model.

The variance decomposition from those four cells is the single most informative table the dissertation could contain, and it does not currently exist anywhere in the archive.

PLATFORM:
[[the-typographic-residue]]

LINKS:
[[FORAGE-OD-008]]
[[FORAGE-OD-021]]
[[FORAGE-OD-014]]

BIBTEX:
@article{hardt2022performative,
  title={Performative Power},
  author={Hardt, Moritz and Jagadeesan, Meena and Mendler-D{\"u}nner, Celestine},
  journal={arXiv preprint arXiv:2203.17232},
  year={2022},
  url={https://arxiv.org/abs/2203.17232}
}
