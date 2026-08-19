ZETTEL

ID:
FORAGE-OD-007

TITLE:
BOOSTING DESCRIPTION TOKENS ALONE, WITH THE NAME EXCLUDED, RECOVERS 43.9% OF FAILED TOOL SELECTIONS

SOURCE:
Shiyang Chen — Looking Is Not Picking: An Attention-Segment Account of Tool-Selection Failures in LLM Agents — arXiv:2606.16364v2 — 27 June 2026

PASSAGE:
[QUOTE]
"boosting only the description tokens (excluding the name)" — the intervention "still recovers 43.9% (at high 38.7% damage)"

RESEARCH OBJECT:
The rival reading to the name-suffices result, obtained by a different method (attention-segment intervention rather than activation steering) on real benchmark failures rather than synthetic pairs.

Description tokens are causally load-bearing on the cases that actually fail.

LOCAL MOVE:
Chen does not ablate descriptions to show they are unnecessary. Chen intervenes on them to show they can rescue a failure. Opposite experimental posture, opposite conclusion.

SOURCE TERMS:
Harness Attention Allocation
attention margin
gold tool
distractor
readout stage
boosting
description tokens
damage

WHAT BECAME STRANGE:
The two strongest available results on the archive's primary case disagree, and they disagree because of *sampling*: Wu et al. measure average-case discriminations, Chen measures the failure set.

Operativity may be a tail phenomenon. Descriptions do nothing on the easy 90% and everything on the hard 10% — which means average-case experiments will always understate them, and the archive's whole falsification strategy is aimed at the average.

QUESTION:
Is operative description a tail phenomenon, and if so what experimental design can detect an effect that only exists conditional on failure?

DEEPER QUESTION:
Does a theory whose effects appear only in the failure set thereby become a theory of *repair* rather than a theory of *routing*?

MECHANISM:
<HARD DISCRIMINATION>
→ name-based margin insufficient
→ readout selects distractor
→ [AMPLIFY ATTENTION TO DESCRIPTION SEGMENT]
→ margin recovered on 43.9% of failures
→ <CORRECT TOOL>
with collateral: 38.7% damage, i.e. previously-correct selections broken

FORMAL SHIFT:
<FAILURE SET>
→ <SEGMENT ATTENTION MASS>
→ [BOOST DESCRIPTION SEGMENT]
→ <PARTIAL RECOVERY WITH COLLATERAL DAMAGE>

SOURCE FORMALISM:
Harness Attention Allocation (HAA): per-segment attention mass routed to each segment. Attention margin = gold-tool attention minus distractor attention (the paper's Eq. 1). Interventions reported as recovery % against damage %.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Stratify by outcome:
  ΔG_easy(desc) ≈ 0
  ΔG_hard(desc) > 0

Then the honest headline claim is conditional:
  E[ΔG | route already determined] ≈ 0
  E[ΔG | route contested] ≫ 0

And the archive's own "38.7% damage" figure names a category it lacks: **iatrogenic description** — description that repairs one route by breaking another.

TENSION:
READING A (Wu et al., arXiv:2605.07990): descriptions add at most a few points; names suffice.
READING B (Chen, arXiv:2606.16364): description tokens independently recover 43.9% of failures.

Smallest discriminating evidence: run both interventions on the *same* stratified split — easy vs hard discriminations — and report ΔG per stratum. If Reading A holds on easy and Reading B on hard, both papers are right and the disagreement was about sampling all along.

MISSING:
Neither paper reports whether the recovered failures are the *semantically* hard ones (near-synonym tools) or the *positionally* disadvantaged ones. Without that, description and position remain confounded.

BOUNDARY:
Chen's intervention is a mechanistic manipulation of attention mass, not a manipulation of description *text*. It shows description tokens are causally sufficient when amplified. It does not show that rewriting a description achieves the same effect through normal inference.

That gap matters: the archive wants to claim authors route action by writing. Chen shows an experimenter can route action by boosting attention. These are different powers.

CITATION TRAIL:
Berkeley Function-Calling Leaderboard failure cases.
Wu et al. — arXiv:2605.07990 (the rival).
Attention-attribution and causal tracing methods.
PAPERS/attention-tax-semiotics.md §11.4 (the archive's "latent attention buffer" — the same object under a literary name).

TEST:
Stratify BFCL discriminations into near-synonym pairs and distinct pairs. For each stratum, vary description text only. Report ΔG per stratum, plus iatrogenic damage.

Prediction: ΔG_near-synonym ≫ ΔG_distinct, and damage rises with description length.

PLATFORM:
[[names-route-descriptions-repair]]

LINKS:
[[FORAGE-OD-004]]
[[FORAGE-OD-010]]
[[FORAGE-OD-008]]

BIBTEX:
@article{chen2026lookingispicking,
  title={Looking Is Not Picking: An Attention-Segment Account of Tool-Selection Failures in LLM Agents},
  author={Chen, Shiyang},
  journal={arXiv preprint arXiv:2606.16364},
  year={2026},
  url={https://arxiv.org/abs/2606.16364}
}
