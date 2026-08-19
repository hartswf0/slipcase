ZETTEL

ID:
FORAGE-OD-010

TITLE:
THE MODEL ATTENDS TO THE CORRECT TOOL 80% OF THE TIME AND STILL PICKS THE WRONG ONE — SO THE ATTENTION-TAX FAILURE CONDITION IS THE WRONG FAILURE CONDITION

SOURCE:
Shiyang Chen — Looking Is Not Picking: An Attention-Segment Account of Tool-Selection Failures in LLM Agents — arXiv:2606.16364v2 — 2026

PASSAGE:
[QUOTE]
"the model attends most to the correct tool 80% of the time (vs. 21% chance); the gold tool is the under-attended segment on only 10%."

[PARAPHRASE]
The bottleneck is the late-layer readout mechanism, not the input harness.

RESEARCH OBJECT:
The archive's formal model says routing fails when the description's attention cost exceeds the operator's attention budget: Tax(D,O) > A(O).

On real failures, attention is allocated correctly and the route is still wrong. The failure is downstream of attention.

LOCAL MOVE:
Chen inverts the intuitive diagnosis. The obvious story — the model missed the right tool in a crowded list — is measured and rejected. Perception is fine; selection is broken.

SOURCE TERMS:
readout stage
Harness Attention Allocation
attention margin
gold tool
under-attended segment
looking is not picking

WHAT BECAME STRANGE:
"Attention tax" is the archive's most portable idea — it unifies interface design and prompt design under one law ("Interface Design = Prompting for human operators"). That unification depends on attention being the scarce resource whose exhaustion produces failure.

If failure happens with attention intact, the unification loses its mechanism and becomes a metaphor again.

QUESTION:
What is the operator-side analogue of a readout failure — a human who has attended to the label, understood it, and still routes wrongly?

DEEPER QUESTION:
Does the archive need a two-stage operator model — allocation and commitment — and does that split reopen the Rylean distinction between holding the thread and drawing the conclusion?

MECHANISM:
<DESCRIPTION SEGMENTS>
→ attention mass allocated (correctly, 80%)
→ representations available
→ [LATE-LAYER READOUT MAPS REPRESENTATION TO CHOICE]
→ readout mis-selects
→ <WRONG ROUTE DESPITE CORRECT ATTENTION>

FORMAL SHIFT:
<ATTENTION ALLOCATION>
→ <REPRESENTATION>
→ [READOUT / COMMITMENT]
→ <ACTION>

The archive's model stops at the first arrow. The failure lives at the third.

SOURCE FORMALISM:
Harness Attention Allocation (HAA) as per-segment attention mass; attention margin = gold minus distractor attention (Eq. 1). Reported: 80% correct-tool attention vs 21% chance; gold tool under-attended on 10% of failures.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Split the operator's Act into two maps:

  allocate : context → attention distribution α
  commit   : (representation, α) → action

Then two distinct failure modes:

  F1 (tax failure):     Tax(D,O) > A(O)  →  α misallocated
  F2 (readout failure): α correct        →  commit misfires

The archive currently has only F1. Chen's evidence says F2 dominates on the failure set.

This matters politically: F1 failures are the *operator's* overload; F2 failures are the *system's* commitment rule. Blame lands in different places.

TENSION:
READING A: the readout is itself an attention mechanism at a later layer, so F2 is F1 at a different depth and the archive's model survives with a depth index added.
READING B: readout is a distinct computation (a learned decision rule over representations), and collapsing it into attention is precisely the intellectualist error the archive's Ryle chapter attacks — mistaking the presentation of considerations for the drawing of a conclusion.

Reading B is the more interesting one for the archive, because it means Ryle's *own* distinction predicts Chen's finding.

MISSING:
A human-subject analogue. There is no study in the archive of moderators or maintainers who attended to a label, understood it, and routed against it. That study would be the archive's F2 case, and it is where contestation actually lives.

BOUNDARY:
Chen measures one model family on one benchmark's failure set. The claim licensed is: for these failures, attention allocation is not the binding constraint. Not: attention never matters.

CITATION TRAIL:
PAPERS/ryl-01.md §"Inference as an Achievement" — Ryle's separation of the search from the conclusion, which is structurally the allocate/commit split.
PAPERS/attention-tax-semiotics.md §11.4 (latent attention buffer) and §14 (the failure predicate).
Mechanistic work on late-layer decision circuits.
FORAGE-OD-012.

TEST:
For each failed selection, record both the attention margin and the readout logit margin. Classify failures as F1 (attention margin negative) or F2 (attention margin positive, logit margin negative).

Then re-run the archive's description manipulation and ask which class it repairs. If descriptions only repair F1 while most failures are F2, thick prompting is treating the wrong organ.

PLATFORM:
[[allocation-is-not-commitment]]

LINKS:
[[FORAGE-OD-006]]
[[FORAGE-OD-007]]
[[FORAGE-OD-011]]
[[FORAGE-OD-012]]

BIBTEX:
@article{chen2026lookingispicking,
  title={Looking Is Not Picking: An Attention-Segment Account of Tool-Selection Failures in LLM Agents},
  author={Chen, Shiyang},
  journal={arXiv preprint arXiv:2606.16364},
  year={2026},
  url={https://arxiv.org/abs/2606.16364}
}
